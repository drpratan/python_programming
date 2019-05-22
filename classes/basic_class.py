class A():
    pass
class B():
    i =10
    pass

class C(A,B):
    pass

c_obj = C()

print(c_obj.i)


