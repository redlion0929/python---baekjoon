a = input().split()
a = [int(i) for i in a]
sum = 0
for i in a:
    sum+=i**2
print(sum%10)