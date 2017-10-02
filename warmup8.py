#Gary Li
#10/2/17
#warmup8.py

total = 0
for i in range(1,100001):
    if i%3 ==0 and i%10==0 and i%17==0:
        total = total +i
print(total)
