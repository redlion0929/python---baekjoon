a = int(input())
b = input().split()
b = [int(i) for i in b]
max = max(b)
sum = 0
for i in b:
    sum+=i/max*100

print(sum/len(b))