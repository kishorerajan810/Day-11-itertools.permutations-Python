from itertools import permutations

s,n=map(str,input().split())
x,y=[],[]
for i in (list(permutations(list(s),int(n)))):
    i=list(i)
    x.append(i)
for j in x:
    l=""
    for k in j:
        l=l+str(k)
    y.append(l)
y.sort()
for m in y:
    print(m)
