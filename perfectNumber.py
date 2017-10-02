#Gary Li
#9/29/17
#perfectNumber.py

number = int(input('Enter a number: '))

total = 0
for i in range(1,number):
    if number%i==0:
        total = total+i
    if total = number:
        print('Perfect')
    else:
        print('Not perfect')
