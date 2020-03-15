class Outer:
    def __init__(self):
        print('Outer Constructor')
    class inner:
        def __init__(self):
            print('inner constructor')

o = Outer()
i = o.inner()
