
import os
class opened(object):
    def __init__(self,filename):
        self.handle = open(filename,encoding='utf-8')
        print("Resorce:%s"%filename)

    def __enter__(self):
        print("[enter%s Allocate resource.]"%self.handle)
        return self.handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[exit%s]: Free Resource"%self.handle)
        if exc_tb is None:
            print("[exit %s]:exit without exception"%self.handle)
            self.handle.close()
        else:
            print("[exit %s]:exit with exception raise."%self.handle)
            return False

d = os.path.dirname(os.path.dirname(__file__))
print(d)
with opened('%s/README.md'%d) as fp:
    print(fp.read())