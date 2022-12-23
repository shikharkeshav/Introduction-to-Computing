x=int(input('Enter first side '))
y=int(input('Enter second side '))
z=int(input('Enter third side '))
lst=[x,y,z]
lst.remove(max(x,y,z))
if(max(x,y,z)<sum(lst)):
    print('yes')
else:
    print('no')
