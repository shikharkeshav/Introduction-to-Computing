x= int(input('How many numbers do you need in the sequence '))
fibbonaci=[1]
a=0
b=1
for i in range(x):
    c=a+b
    fibbonaci.append(c)
    a=b
    b=c
print(fibbonaci)
print('Average: ',sum(fibbonaci)/len(fibbonaci))


