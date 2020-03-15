from threading import *
def thread1():
    print('in thread1 id',current_thread().ident)

t1 = Thread(target=thread1)
t1.start()
print('in main thread id',current_thread().ident)
print('in main thread t1 id',t1.ident)
