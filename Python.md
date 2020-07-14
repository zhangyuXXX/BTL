#Python 学习
## 一

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
    > 以上分别时sys.argv，argparse，tf.app.run
   
- sys.argv
    >sys模块是很常用的模块，它封装了与python解释器相关的数据，例如sys.module里面有已经
     加载了所有模块的信息，sys.path里面是PYTHONPATH的内容，而sys.argv则封装了传入的参数
    >> 第一个参数是 `脚本名`    
    import sys 
    
                                                                                                                                    
                                                                                                                                    