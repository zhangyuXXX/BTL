import sys
import getopt

# 第一个参数：传入的参数
# 第二个参数：短参数
# 第三个参数：长参数列表
# 短参数后面的冒号：表示有参数
# 长参数后面的等号：表示有参数
opts, args = getopt.getopt(sys.argv[1:], "h:o:", ["help", "output="])
print(opts)
# print(args)

for o, a in opts:
    # print(o)
    # if o in ("-h", "--help"):
        # usage()
        # sys.exit()
    if o in ("-o", "--output"):
        output = a
        print(output)
