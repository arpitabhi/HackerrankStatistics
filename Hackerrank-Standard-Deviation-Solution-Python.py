# Enter your code here. Read input from STDIN. Print output to STDOUT

#Author : Arpit Shukla
#Date : 28th May, 2020

#Hackerrank Standard Deviation Solution Python

import math
n=int(input())
ls=list(map(int,input().split()))

mean=sum(ls)/len(ls)
sum1=0

for i in ls:
    sum1+=(i-mean)**2

sd=math.sqrt(sum1/n)
print("%.1f" % sd)