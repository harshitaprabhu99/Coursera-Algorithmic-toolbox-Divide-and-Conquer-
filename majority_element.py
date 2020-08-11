import collections
def sol(n,e,l):
    seq=0
    count=collections.Counter(l)
    for i in count:
        if count[i]>e:
            seq+=1
    return seq

n=int(input())
l=list(map(int,input().split(' ',n)))
e=n/2
print(sol(n,e,l))
