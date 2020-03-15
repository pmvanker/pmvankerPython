class Student:
    a = 10
    def __init__(self):
        self.rollno=0
        self.name='abc'
        print('inside constructor')
        print(self.a)
        print(Student.a)
    def setRollno(self,rollno):
        self.rollno = rollno
    def getRollno(self):
        return self.rollno
    def m1(self):
        print('inside instance method')
        print(self.a)
        print(Student.a)
    @classmethod
    def m2(cls):
        print('inside class method')
        print(cls.a)
        print(Student.a)
    @staticmethod
    def m3():
        print('inside static method')
        print(Student.a)

s1 = Student()
s1.setRollno(10)
print(s1.getRollno())
# s1.m1()
# s1.m2()
# Student.m3()
# print('outside class')
# print(Student.a)
# print(s1.a)