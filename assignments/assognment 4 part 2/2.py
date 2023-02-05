x=int(input('minimum no. in range '))
y=int(input('maximum no. in range '))+1
z=int(input('no. to check for divisibility '))
for i in range(x,y):
    if i%z==0:
        print(i)
