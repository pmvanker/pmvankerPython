from threading import *
class MyClass:
    def normal_method(self):
        for i in range(5):
            print('thread:',current_thread().getName());
obj = MyClass()
t1 = Thread(target=obj.normal_method)
t1.start()
for i in range(5):
    print('thread:',current_thread().getName());

