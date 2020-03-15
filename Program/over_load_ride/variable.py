class Test:
    def sum(self,*a):
        total = 0
        for x in a:
            total = total + x
        return total
t = Test()
print(t.sum(10,20))
print(t.sum(10,20,30))
print(t.sum())

