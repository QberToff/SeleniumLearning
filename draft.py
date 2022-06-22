class MyClass:
    message = ""

    def Foo(self):
        for i in range(3):
            self.message += str(i)
            print(self.message)

myclass = MyClass()
myclass.Foo()