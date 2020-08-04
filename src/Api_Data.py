# encoding:utf-8 #
"""
RD: zhangyu93
icafe:
PM: zhangweixiao
创建日期： 20200803
项目简介：超休闲游戏接入广点通API数据
"""

"""import mode"""

import sys
import time
import uuid
import os
import json

reload(sys)
sys.setdefaultencoding('utf8')

# sys.path.append('../../utils')
# from local_to_afs import load_file_to_mart_460

# script_name = sys.argv[0]

# run_date = sys.argv[1][0:10].replace('-','')


# file_name =  script_name[:-3] + '_' + run_date


printlog = False


def http_get():
    datalist = []
    campaign_list = []
    """
    公共参数
    account_id：腾讯广告主的UID,广点通账户可登录投放端，点击右上角头像登录投放管理平台，然后可以看到右上角账号ID，即为account_id
    access_token:具体获取流程咨询数据PM
    timestamp：接口访问时间戳，最大误差600s(时区：GMT+8)
    """
    account_id = 16930239
    access_token = '5066780cc927b46ca1a8912cd805f23e'
    timestamp = str(int(time.time()))

    """
    以下获取推广计划id、推广计划名称
    :return: 
    """
    page = 1
    while (True):

        nonce = str(uuid.uuid4())[0:32]
        base_cmd = "curl -G 'https://api.e.qq.com/v1.1/campaigns/get?access_token=%s&timestamp=%s&nonce=%s' -d 'account_id=%s'" % (
        access_token, timestamp, nonce, account_id)
        filds = '["campaign_id","campaign_name"]'
        cmd = base_cmd + " -d 'fields=%s'" % filds + " -d 'page_size=30'"

        if printlog:
            print cmd

        stdin, stdout = os.popen2(cmd + " -d 'page=%s'" % page)
        res = stdout.read()

        resStr = json.loads(res)

        if len(resStr["data"]["list"]) == 0:
            break
        elif 'Access token is malformed.' in res:
            return "error"
        else:
            campaign_listtmp = resStr["data"]["list"]
        page = page + 1
        campaign_list += campaign_listtmp

    if printlog:
        print json.dumps(campaign_list, ensure_ascii=False)
    """
    以下获取天级数据
    每次最多获取500百条数据
    一直获取数据，直到获取到的list为空
    :return:
    """

    page = 1
    while (True):

        nonce = str(uuid.uuid4())[0:32]
        base_cmd = "curl -G 'https://api.e.qq.com/v1.1/daily_reports/get?access_token=%s&timestamp=%s&nonce=%s' -d 'account_id=%s'" % (
            access_token, timestamp, nonce, account_id)

        level = 'REPORT_LEVEL_AD'
        daterange = '{"start_date":"2020-06-23","end_date":"2020-06-23"}'
        group = '["site_set","campaign_id","adgroup_id","ad_id"]'
        filds = '["date","site_set","campaign_id","adgroup_id",' \
                '"ad_id","view_count","valid_click_count","ctr",' \
                '"cpc","cost","conversions_count","conversions_rate",' \
                '"conversions_cost","video_outer_play_rate","download_count",' \
                '"download_rate","download_cost","activated_count","activated_rate",' \
                '"install_count","install_rate","install_cost","activated_cost",' \
                '"click_activated_rate","app_register_count","app_register_cost",' \
                '"retention_count","retention_rate","retention_cost","thousand_display_price",' \
                '"no_interest_count","video_outer_play_count","video_outer_play100_count"]'

        cmd = base_cmd + " -d 'level=%s'" % level \
              + " -d 'date_range=%s'" % (daterange) \
              + " -d 'group_by=%s'" % group \
              + " -d 'fields=%s'" % filds \
              + " -d 'page_size=50'"

        if printlog:
            print cmd

        stdin, stdout = os.popen2(cmd + " -d 'page=%s'" % page)
        res = stdout.read()

        resStr = json.loads(res)

        if len(resStr["data"]["list"]) == 0:
            break
        elif 'Access token is malformed.' in res:
            return "error"
        else:
            datalisttmp = resStr["data"]["list"]
            for i in range(len(datalisttmp)):
                datalisttmp[i]["date"] = '2020-06-23'
                datalisttmp[i]["campaign_name"] = getListValue(datalisttmp[i]["campaign_id"], campaign_list)
        page = page + 1
        datalist = datalist + datalisttmp

    if printlog:
        print json.dumps(datalist, ensure_ascii=False)

    return datalist


def getListValue(key, list):
    for i in range(len(list)):
        if list[i]["campaign_id"] == key:
            return list[i]["campaign_name"]
    return ""


print http_get()