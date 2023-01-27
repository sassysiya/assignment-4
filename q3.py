import random

for i in range(10):
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    x= int(input(f'{num1} x {num2} = '))

    if x==num1*num2:
        print('correct')
    else:
        print('wrong')
        print('the correct answer is ',num1*num2)
    
