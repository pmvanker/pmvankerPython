import time
import gc
class Test:
    def __init__(self):#constructor
        print('constructor')
    def __del__(self):#destructor
        print('distructor')

print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

t = Test()
print('sleep.. 2sec before')
time.sleep(2)
t = None
print('end of programe')

print("checking garbage availablity")
t1= Test()
t2=t1;
t3=t1;
t4=t1;
t1 = None
print('first object is none')
t2 = None
print('first object is none')
t3 = None
print('first object is none')
t4 = None
print('all object is none')



