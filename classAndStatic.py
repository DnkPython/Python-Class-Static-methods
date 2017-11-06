class A:
    @classmethod
    def classMethod(cls):
        print "this is class method"
    @staticmethod
    def staticMethod():
        print "this is static method"
if __name__=="__main__":
    obj = A()
    print (obj.classMethod())
    print (obj.staticMethod)

