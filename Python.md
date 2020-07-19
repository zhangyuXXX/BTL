#Python 学习
## 第一章 基础学习

### 1. moudle、package和__init__.py
  - python是通过moudle组织代码的，每一个moudle就是一个python文件,但是moudle是通过
  package组织的
    > package定义很简单，在当前目录下有有__init__.py文件的目录即为一个package
    >> __init__.py文件可以为空，也可以写代码 (可以写 变量、导包操作)
    >>> package的初始化过程：
    >>>>      __init__.py文件内变量
    >>>>      是不是package内的subpackage 
    >>>>      是不是package中的moudle 

### 2. Python脚本传入参数
  - 运行python脚本时可以有传入参数的形式
  
        python demo.py 1,2,3,4 
        python demo.py -gpus=0,1,2 --batch-size=10
        python demo.py -gpus=0,1,2 --batch_size=10
    > 以上分别是sys.argv，argparse，tf.app.run
   
- sys.argv
    >sys模块是很常用的模块，它封装了与python解释器相关的数据，例如sys.module里面有已经
     加载了所有模块的信息，sys.path里面是PYTHONPATH的内容，而sys.argv则封装了传入的参数
    >> 第一个参数是 `脚本名`    
    import sys （sys.argv[1] 除了脚本名的第一个参数）
   
- argparse

        import argparse
        parser = argparse.ArgumentParser(description='manual to this script')
        parser.add_argument('--gpus', type=str, default=None)
        parser.add_argument('--batch-size', type=int, default=32)
        args = parser.parse_args()
        print(args.gpus)
        print(args.batch_size)
        调用脚本：python Params_argparse.py --gpus='hello' --batch-size=13

- getopt()函数
    > 在运行程序时，可能需要根据不同的条件，输入不同的命令选项来实现不同的功能。目前有短选项和长选项两种格式。短选项为'-'加上单个字母选项；长选项为'--'加上单词
    - 所有的参数都存储在sys.args中  
        > 对于短格式：'-'后面要紧跟一个字母。如果还有附加参数，可以用空格分开，也可以不用分开，长度任意，也可以用引号
        >> -0  
        -ob  
        -obbb  
        -o bbb  
        -o "a" "b"
    - 对于长格式：'--'后面要紧跟一个单词，如果这些选项还有附加参数，后面要紧跟=，再加上参数。=后面不能有空格
        > --help=file (其他形式都不对)
    >getopt()的使用
     - import getopt import sys
     - 分析命令行参数
     - 处理结果
          
           第一个参数：传入的参数
           第二个参数：短参数
           第三个参数：长参数列表
           短参数后面的冒号：表示有参数
           长参数后面的等号：表示有参数
           opts, args = getopt.getopt(sys.argv[1:], "h:o:", ["help", "output="])                                                                                                                          
           for o, a in opts:
                if o in ("-o", "--output"):
                output = a
                print(output)
           调用脚本：python Parmars_getopt.py -ha -o file --help --output=hello    
### 3. if \_\_name__ == "\_\_main__"  的作用

   - 一个python文件通常有两种用法，第一种是作为脚本直接执行，第二种是import到其他脚本中被执行。这句话的作用是，这句话下的语句只有在第一种情况下会被执行，import到其他脚本中不会被执行。
   - 每一个python模块(python文件)都包含内置变量__name__，当该模块被执行时，__name__等于该文件名(包含后缀.py)。如果该模块import到其他模块中，则该模块的__name__等于该模块名称(不包含后缀.py)
   - __main__  始终指向当前执行模块的名称(包含.py)  
   
### 4. os.popen()方法  
- os.popen() 是从一个命令打开一个***管道***
- 语法格式：os.popen(command[,mode[,buffersize]])
   - command -使用的命令
   - mode - 模式权限仅可以是 'r' 或 'w'
   - buffersize - 指明文件需要缓冲的大小：0意味着无缓冲，1意味着 行缓冲；其他参数表示使用参数的大小缓冲     
   - 返回一个文件描述符号为fd的打开的文件对象  
- python调用shell有两种方法：os.system() 和 os.popen()方法
    - 前者返回值是脚本运行的状态码 后者返回值是脚本执行过程中输出内容   
- 知识点
    - 返回值是文件对象，因此使用完需要进行关闭，显示关闭调用.close()方法
    - 也可以使用with os.popen() as p:  r = p.read() 这样就不用显示的关闭
    - 还有popen2()等方法； 返回值是可以输入、输入然后进行相应的操作（先不写了）
### 5. with语法
- 定义
    - with是python2.5引入的语法，它是一种上下文管理协议，目的在于从流程中把try except finally关键字和资源分配释放相关的代码统统去掉，
简化try...except...finally处理流程
    - with通过__enter__方法初始化，然后在__exit__中做善后以及异常处理
    - 所以使用with处理的对象必须有__enter__()和__exit__()这两个方法
    - 其中__enter__()在语句体(with包裹起来的代码块)执行之前进行，__exit__方法在语句体执行完毕后退出运行
    - with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。
- 基本语法格式
    -     with expression [as target]:
                with_body
    - expression:是一个需要执行的表达式
    - target是一个变量或者元组，存储的是expression表发式执行返回的结果
### 6. curl命令
- curl是常用的命令行工具，用来请求web服务器，就是client url工具的意思。
    - 不带参数的curl请求默认是get请求
    - -A(--user-agent)： 指定客户端的用户代理标头，即User-Agent  
    - -b : 用来向服务器发送cookie 
      - curl -b 'foo=bar' https://google.com 
      - $ curl -b cookies.txt https://www.google.com
    - -c : 将http回应所设置的cookie写入一个文件
    - C ： switch是恢复我们文件传输的设备，但是要注意，它后面紧跟一个 - 。这告诉crul继续文件传输，但是实现这一步，首先要查看已经下载的部分，找到下载后的最后一个字节才可以确定从何处恢复
      - curl -C - example.com/some-file.zip --output MyFile.zip
    - -d(--data-urlencode 区别在于会自动将发送的数据进行 URL 编码): 用于发送POST请求的数据体
      - $ curl -d'login=emma＆password=123'-X POST https://google.com/login
      - $ curl -d 'login=emma' -d 'password=123' -X POST  https://google.com/login
      - 使用-d参数后，HTTP请求会自动加上Content-Type:application/x-www-form-urlencode。并且自动将请求转为post请求，因为可以省略- X
      - -d 参数可以读取本地文件向服务器发送 curl -d '@data.txt' https://google.com/login
    - -e : 用来设置HTTP的标头Referer，表示请求的来源 curl -e 'https://google.com?q=example' https://www.example.com
    - -H : 与-e的作用相同，请求方式有些不同 curl -H 'Referer: https://google.com?q=example' https://www.example.com
    - -F : 用来向服务器上传二级制文件 curl -F 'file=@photo.png' https://google.com/profile
        - 上面命令会给 HTTP 请求加上标头Content-Type: multipart/form-data，然后将文件photo.png作为file字段上传。
        - F参数也可以指定文件名。$ curl -F 'file=@photo.png;filename=me.png' https://google.com/profile。上面命令中，原始文件名为photo.png，但是服务器接收到的文件名为me.png。
    - -G参数用来构造 URL 的查询字符串。
        - curl -G -d 'q=kitties' -d 'count=20' https://google.com/search
        - 上面会发出一个GET请求，实际请求的URL为https://google.com/search?q=kitties&count=20，如果省略-G会发出POST请求
        - 如果数据需要 URL 编码，可以结合--data--urlencode参数。
    - -H：添加http请求的标头：
        -  curl -d '{"login": "emma", "pass": "123"}' -H 'Content-Type: application/json' https://google.com/login
        - 上面命令添加 HTTP 请求的标头是Content-Type: application/json，然后用-d参数发送 JSON 数据。
        - 可以有多个http标头
    - -o : 将服务器的回应保存为文件，相当于wget
        - $ curl -o example.html https://www.example.com
    - -O：将服务器回应保存为文件，并将url的最后部分当做文件名
        - $ curl -O https://www.example.com/foo/bar.html 名字为：bar.html
    - -u:用来设定服务器认证的用户名和密码
        - curl -u 'bob:12345' https://google.com/login
        - curl 能够识别 URL 里面的用户名和密码。$ curl https://bob:12345@google.com/login
    - -x：指定http请求的代理
        - curl -x socks5://james:cats@myproxy.com:8080 https://www.example.com
        - 上面命令指定http请求通过myproxy.com:8080的 socks5 代理发出
        - 如果没有指定，默认为http
    - -X： 参数指定http的请求方法
        - curl -X POST https://www.example.com
### 6. http request的使用
- 特性：
    - python标准库中的urllib2模块已经包含了我们平常使用的大多数功能，但是api的使用不太友好，而request自称"HTTP For Humans"使用起来更方便
    - request唯一一个"非转基因的Python Http库"，可以放心使用   
    - request继承了urllib2的所有特性
        - request支持http连接保持和连接池
        - 支持使用cookie保持会话
        - 支持文件上传              
        - 支持自动确认响应内容的编码
        - 支持国际化的URL和POST数据自动编码
    - request的底层实现就是urllib3
- 基本GET使用 
    - response = request.get("http://www.baidu.com") 或 request.request("get", http://www.baidu.com")
        - print(response.text) 返回的是unicode格式的数据
        - print(response.content) 返回的是字节流数据
        - print(response.url) 返回完整的url
        - print(response.encoding) 查看响应头部字符编码
        - print(response.status_code) 查看响应编码
        - print(response.json()) 如果返回的json字符串，可以只返回json对象
        - 使用text时，会根据http响应的文本编码自动解码响应内容，大多数unicode字符集都能无缝的被解码
        - 使用content时，返回的是服务器响应数据的原始二进制流，可以用来保存图片等二进制文件
    - 添加参数 & header  
          
          kw = {'wd':'你好'} 
          header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
          response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)
- 基本POST使用:对于post请求来说，我们一本需要为它增加一些参数，最基本的方法就是利用data这个参数
    
      data = {
        "type":"AUTO",
        "i":"i love python",
        "doctype":"json",
        "xmlVersion":"1.8",
        "keyfrom":"fanyi.web",
        "ue":"UTF-8",
        "action":"FY_BY_ENTER",
        "typoResult":"true"
      } 
      url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
      headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
      response = requests.post(url, data = data, headers = headers)
- session
    - 在requests中，session对象是一个常用的对象，这个对象代表一次会话：从客户端浏览器连接服务器开始，到客户端浏览器断开连接
    - 会话能让我们在请求的时候保持某些参数，比如在同一个session实例发出的所有的请求之间保持cookie                                       
    
          from requests import sessions as s
          ss = s.session()
          headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
          data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
          ss.post("https://mail.163.com/", data = data)
          response = ss.get("http://www.renren.com/410043129/profile")
          print(response.text)
### 7. URL定义
- URL统一资源定位符，实际上就是一个网址。URL可以包含单词(www.baidu.com)或IP地址(127.0.0.1)，大多都是文字的形式
- URL由三部分组成：资源类型、存放资源的主机域名、资源文件名
- URL一般语法：protocol://prefix.domain:port/path/filename
    - protocol:用于指定使用的传输协议（http、https、file、ftp等）
    - prefix：用于定义域名前缀（http默认为www）
    - domain：用于定义internet域名（如baidu.com）
    - port:用于定义主机上的端口号（大部分默认为80，不会显式地写出来）
    - path：由另个或多个/符号隔开的字符串，一般用于表示服务器上的一个文件目录或地址
    - filename：用于定义文档或资源的名称
- URL编码一种将URL中的非ASCII字符的特殊字符转换为可以为web浏览器和服务器普遍接受的、有明确的表示形式的格式
- 因为URL只能通过使用ASCII字符集(十六进制)将特殊字符在web浏览器和服务器上显示。如果URL包含ASCII字符集之外的字符，则必须转为ASCII字符才可显示
 
          
          
