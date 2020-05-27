# Enter your code here. Read input from STDIN. Print output to STDOUT

#Author : Arpit Shukla
#Date : 28th May, 2020

#Hackerrank Interquartile Range Solution Python

n=int(input())
elements=list(map(int,input().split()))
frequency=list(map(int,input().split()))

l=[]
for i in range(n):
    for j in range(frequency[i]):
        l.append(elements[i])
l.sort()
#Generating Median from a list
def qart(ls):
    if len(ls)%2!=0:
        q=ls[(len(ls)-1)//2]
    else:
        q=(ls[len(ls)//2]+ls[len(ls)//2-1])/2
    return q
def inter_qart(l):
    
    if len(l)%2!=0:
        q1=qart(l[:(len(l)-1)//2])
        q3=qart(l[((len(l)-1)//2)+1:])
    else:
        q1=qart(l[:(len(l))//2])
        q3=qart(l[((len(l))//2):])
    iqr=q3-q1
    return iqr
print("%.1f" %inter_qart(l))

