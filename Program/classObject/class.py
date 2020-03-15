class Student:
    ''' this is just a demo of class '''
    cname = "vvdn_training"
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
    def talk(self):
        print("my name is ",self.name)
        print("my roll no is ",self.rollno)
        print("cname = ",Student.cname)
s1 = Student(10,'praful')
s1.talk()
