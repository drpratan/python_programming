#!usr/bin/python


def my_gen():
    for i in range (0,4):
      yield (i)

for item in my_gen():
  print(item)



gen_obj = my_gen()


