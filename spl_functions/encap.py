#!/usr/bin/python


class TV():
    
    def __init__(self):
        self.__maxprice = 10000
    def selling_price(self):
        print('Max selling price : {}'.format(self.__maxprice))
    def set_maxprice(self,price):
        self.__maxprice = price


mi = TV()
mi.selling_price()

mi.__maxprice = 9000

mi.selling_price()

mi.set_maxprice(9000)

mi.selling_price()
