import sys
N, M = map(int, sys.stdin.readline().split())
h = list(map(int,sys.stdin.readline().split()))
print(N, M, h)
h.sort()
i = 0

while ((M>=h[i]) & (i<N)):
    i+=1
    M+=1
print(M)