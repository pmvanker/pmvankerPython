from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print('thread name: ',current_thread().getName())
t1 = MyThread()
t1.start()
for i in range(5):
    print("thread name:",current_thread().getName())
