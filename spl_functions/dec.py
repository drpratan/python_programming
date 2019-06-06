def logged_func(func):
    def logged(*args, **kwargs):
        print ("Function %r called" % func.__name__)
        if args:
            print ("\twith args: {}".format(args))
        if kwargs:
            print ("\twith kwargs: {}".format(kwargs))
        result = func(*args)
        print ("\t Result --> %r" % result)
        return result
    return logged


@logged_func
def add(*args):
    print ("Function 'add' called with args: %r" % locals())
    result = sum(args)
    print ("\tResult --> %r" % result)
    return result


add(1,2,3,4)
#logging_add = logged_func(add)
#logging_add(1,2)
#logging_add(1,23,4,5)
