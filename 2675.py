num = int(input())
a =[]
for i in range(num):
    R, S =input().split()
    R = int(R)
    T=""
    for i in range(len(S)):
        T+=(S[i]*R)
    a.append(T)
for i in a:
    print(i)