list1= input('enter string ').split()
i=0
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
for i in list2:
    print(i,':',list1.count(i))
