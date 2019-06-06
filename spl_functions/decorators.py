#!usr/bin/python

#from math import prod

@log_dec
def add(*args):
  return sum(args)

def mul(*args):
  return prod(args)



def log_dec(func):
    def ret_fun(*args):
        print ('func name : {}'.format(func.__name__))
        if args:
            print("args passed : {}".format(args))
        ret_value = func(*args)
        print (ret_value)
        return ret_value
    return ret_fun



if __name__ =='__main__':
  #add_dec = log_dec(add)
  #mul_dec = log_dec(mul)
  #print(add(1,2,3,4))
  add(1,2,3)
  #mul_dec(1,2,3)
  #print(add_dec.__name__)
  #print(mul_dec.__name__)
  #print(add_dec.__dir__)
