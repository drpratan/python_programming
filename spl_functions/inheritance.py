#!/urs/bin/python

class Humans:
    def __init__(self):
        print('Human is ready')
        Power = 'Extra'
    def whoami(self):
        print('I am Human')
    def Func(self):
        print('I am Func in Human class.')

class Man(Humans):
    def __init__(self):
        super().__init__()
        print('Man is ready')
    def whoami(self):
        print('I am a Man')
    def Func(self):
        print('I am Func in Man class.')

class Women(Humans):
    def __init__(self):
        print('Women is ready')
    def whoami(self):
        print('I am a Women')
    def Func(self):
        print('I am Func in Womien class.')


raja = Man()
roja = Women()

raja.whoami()
roja.whoami()
print(raja.Power)
#roja.power
