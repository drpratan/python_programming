def my_gen():
    yield 'r'
    yield 'a'
    yield 'j'
    yield 'a'


gen = my_gen()

for item in gen:
    print (item)


