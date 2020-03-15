from threading import *
def thread1():  # thread 
    for i in range(5):
        print('thread 1')

t1 = Thread(target=thread1)# creating thread object 
t1.start()  # starting thread
for i in range(5):
    print('Main Thread')
