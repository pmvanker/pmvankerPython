class Test:
    x = 10;
    def m1(self):
        self.x = 100
        self.y = 200

t1 = Test()
t2 = Test()
t3 = Test()
t1.x = 1000
t1.y = 2000
t3.m1()
print(t1.x,t1.y)
print(t3.x,t3.y)
print(t2.x,t2.y)


