#!/user/bin/env python
# -*- coding:utf-8 -*-
# 作者：xiaoxiaoyu
# 创建时间：2020-07-18 23:34
# 用意：练习使用request批量拉取网站图片，存储在当前文件夹下名为images的文件夹下

import requests
import re
import urllib.request
import os
from lxml import html
etree = html.etree


def check_save_path(save_path):
    try:
        os.mkdir(save_path)
    except FileExistsError as ex:
        print(ex.filename)


def get_image_name(image_link):
    file_name = os.path.basename(image_link)
    return file_name


def save_image(image_link, save_path):
    file_name = get_image_name(image_link)
    file_path = save_path + "\\" + file_name
    print("准备下载%s" % image_link)
    try:
        file_hander = open(file_path, "wb")
        image_hander = urllib.request.urlopen(image_link, timeout=5).read()
        file_hander.write(image_hander)
        file_hander.close()
    except Exception as ex:
        print(ex.message)


def get_image_link_from_web_page(web_page_link):
    image_link_list = []
    print(web_page_link)
    try:
        html_content  = urllib.request.urlopen(url=web_page_link, timeout=5).read()
        html_tree = etree.HTML(html_content)
        print(str(html_tree))
        link_list = html_tree.xpath('//p/image/@src')
        for link in link_list:
            if(str(link).find("uploadfile")):
                image_link_list.append("http://www.xgyw.cc/") + link
    except Exception as ex:
        pass
    return image_link_list


def get_page_link_list_from_index_page(base_page_link):
    try:
        html_content = urllib.request.urlopen(base_page_link, timeout=5).read()
        html_tree = etree.HTML(html_content)
        print(str(html_tree))
        link_tmp_list = html_tree.xpath('//div[@class="page"]/a/@href')
        page_link_list = []
        for link_tmp in link_tmp_list:
            page_link_list.append("http://www.xgyw.cc" + link_tmp)
        return page_link_list
    except Exception as ex:
        print(ex.message)
        return []


def get_page_title_from_index_page(base_page_link):
    try:
        html_content = urllib.request.urlopen(url=base_page_link, timeout=5).read()
        html_tree = etree.HTML(html_content)
        print(str(html_tree))
        page_tile_list = html_tree.xpath('//div[@class="photo v-pic"]')
        page_tile_tmp = page_tile_list[0].text
        print(page_tile_tmp)
        return page_tile_tmp
    except Exception as ex:
        print(ex)
        return ""


def get_image_from_web(base_page_link, save_path):
    check_save_path(save_path)
    base_page_list = get_page_link_list_from_index_page(base_page_link)
    for page_link in base_page_list:
        image_link_list = get_image_link_from_web_page(page_link)
        for image_link in image_link_list:
            save_image(image_link, save_path)


base_page_link = "https://gallery.vphotos.cn/vphotosgallery/index.html?vphotowechatid=963188CC24CED1998B80F3F339C847D8#/gallerypc"
page_title = get_page_title_from_index_page(base_page_link)
# print(page_title)
if page_title != "":
    save_path = "N:\\PIC\\" + page_title
else:
    save_path = "N:\\PIC\\other\\"
