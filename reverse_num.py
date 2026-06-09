
n=12345
original=n
sum=0
while n>0:
    digit=n%10
    sum=sum*10+digit
    n=n/n

print(sum)
