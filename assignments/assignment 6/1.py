def factors(a):
    factors_list=[]
    for i in range(1,a):
        if a%i==0:
            factors_list.append(i)
    return factors_list

x= int(input('Enter no.: '))
if sum(factors(x))==x:
    print('It is a perfect number')
else:
    print('It is not a perfect number')