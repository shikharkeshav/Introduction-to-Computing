list1=[]
list2=[]
while(len(list1)<10):
    x=int(input('enter value '))
    list1.append(x)

for i in list1 :
    if i>0:
        list2.append(i)
print('positive numbers:',list2)
list2=[]

for i in list1 :
    if i<0:
        list2.append(i)
print('negative numbers:',list2)
list2=[]

for i in list1 :
    if i%2==0:
        list2.append(i)
print('even numbers:',list2)
list2=[]

for i in list1 :
    if i%2!=0:
        list2.append(i)
print('odd numbers:',list2)
list2=[]

list3=[]
for i in list1:
    if i not in list3:
        list3.append(i)
for i in list3:
    print(i,':',list1.count(i),'times')