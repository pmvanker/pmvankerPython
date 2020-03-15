class Animal:
    legs = 4
    
    @classmethod
    def walk(cls,name):
        print('{} can walk with {} legs'.format(name,cls.legs))

Animal.walk('dog')