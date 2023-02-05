import random
for i in range(10):
    a= random.randrange(1,10)
    b= random.randrange(1,10)
    c=int(input(f'{a}x{b}= '))
    if c==a*b:
        print('right')
    else:
        print('wrong')
        print('correct ans is',a*b)