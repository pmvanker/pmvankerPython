import time
from threading import *
def duble(number):
    for n in number:
        time.sleep(1)
        print('duble :',n*2)
def squre(number):
    for n in number:
        time.sleep(1)
        print('squre :',n*n)

n = [1,2,3]
begin = time.time()
duble(n)
squre(n)
end = time.time()
print('time taken by single thread :',end - begin)
t1 = Thread(target=duble,args=(n,))
t2 = Thread(target=squre,args=(n,))
begin = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('time taken by multi thread :',end - begin)

