while(True):
    y=int(input("enter year: "))
    if(y%4==0 and y%100!=0 or y%400==0):
        print('leap year')
    else:
        print('not leap year')

"""
if(y%4==0):
    if(y%100==0 and y%400==0):
        print(y,"is a leap year")
    elif(y%100==0 and y%400!=0):
        print(y,"is not a leap year")
    else:
        print(y,"is a leap year")
else:
    print(y,"is not a leap year")

"""
  
