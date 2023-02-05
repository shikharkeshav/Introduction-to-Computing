x=int(input('enter number of rows '))
p=0
for i in range(1,x+1):
    for j in range(i):
        if p>25:
            p=0
        print(chr(p+65),end='')
        p=p+1
    print('')