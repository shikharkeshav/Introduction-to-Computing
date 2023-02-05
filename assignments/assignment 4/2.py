x=int(input('Enter year '))
if x%4==0 and x%100!=0 or x%400==0:
    print("It is a leap year")
else:
    print('It is not a leap year')