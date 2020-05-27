# Enter your code here. Read input from STDIN. Print output to STDOUT

#Author : Arpit Shukla
#Date : 28th May, 2020

#Hackerrank Quartiles Solution Python

n=int(input())
ls=list(map(int,input().split()))

ls.sort()
def qart(ls):
    if len(ls)%2!=0:
        q=ls[(len(ls)-1)//2]
    else:
        q=(ls[len(ls)//2]+ls[(len(ls)//2)-1])//2
    return q

q2=qart(ls)
if n%2!=0:
    q1=qart(ls[:ls.index(q2)])
    q3=qart(ls[ls.index(q2)+1:])
else:
    q1=qart(ls[:len(ls)//2])
    q3=qart(ls[len(ls)//2:])

print(q1)
print(q2)
print(q3)
