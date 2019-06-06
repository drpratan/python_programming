class Raja():
    def __init__(self):
        print('I am Raja')
    def swim(self):
        print('I cannot swim')

class Dinesh():
    def __init__(self):
        print('I am Dinesh')
    def swim(self):
        print('I can swin')


def swim_test(candidate):
    print (candidate.swim())


raja = Raja()
swim_test(raja)

dinesh = Dinesh()
swim_test(dinesh)

