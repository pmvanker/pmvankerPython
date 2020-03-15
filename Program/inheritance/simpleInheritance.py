class Parent:
    def house(self):
        print("house money 40000$")
    def land(self):
        print("land money 10000$")

class Child(Parent):
    def bike(self):
        print("bike money 5000$")
    def myallproperty(self):
        super().house()
        super().land()
        self.bike()

c = Child()
c.house()
c.land()
c.bike()
c.myallproperty()