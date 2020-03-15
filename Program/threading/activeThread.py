import time
from threading import *
def mythread():
    print(current_thread().getName())
    time.sleep(3)
    print(current_thread().getName())

t1 = Thread(target=mythread,name='th1')
t2 = Thread(target=mythread,name='th2')
t3 = Thread(target=mythread,name='th3')
print('actvie threads :',active_count())
t1.start()
print('t1 start now actvie threads :',active_count())
t2.start()
print('t2 start now actvie threads :',active_count())
t3.start()
print('t3 start now actvie threads :',active_count())
t1.join()
t2.join()
t3.join()
print('all threads join now actvie threads :',active_count())
