#Gary Li
#9/29/17
#perfectNumber.py

number = int(input('Enter a number: '))

for i in range(1,number+1):
    if number%i==0:
        print(i)
