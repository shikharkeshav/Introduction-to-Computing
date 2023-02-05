for i in range(200):
    if i%5==2 and i%6==3 and i%7==2:
        print('ans is:',i)
        break
    elif i==199:
        print('no such number exist')
    