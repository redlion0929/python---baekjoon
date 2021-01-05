a = input().split()
a = [int(i) for i in a]
b = [i for i in range(1,9)]
c = [i for i in range(8,0,-1)]
if a ==b:
    print("ascending")
elif a==c:
    print("descending")
else:
    print("mixed")