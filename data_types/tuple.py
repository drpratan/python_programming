tup = (1,2,3,4)
tup1 = ([1,2,3,4],'a','b','c')

print('before changing val : {}'.format(tup1))
for index,val in enumerate(tup1):
    if index == 0:
        #print (tup1[0][0])
        #print (tup1[0][1])
        tup1[0][1] = tup1[0][3]
    print (val)
print('After changing val : {}'.format(tup1))
