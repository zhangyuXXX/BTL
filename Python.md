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