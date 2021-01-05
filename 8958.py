a = int(input())
b=[]
for i in range(a):
    s = input().strip()
    score = 0
    sum = 0
    for i in s:
        if i == 'O':
            score+=1
            sum+=score
        elif i == 'X':
            score=0
        else:
            exit()
    b.append(sum)
for i in b:
    print(i)
    