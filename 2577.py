b =1
for i in range(3):
    b*=int(input())
    
b = str(b)

for i in range(10):
    print(b.count(str(i)))