a=int(input())
b=int(input())
n=int(input())
m=int(input())
min1=n+a*(n-1)
min2=m+b*(m-1)
max1=n+a*(n+1)
max2=m+b*(m+1)
minimum=max(min1, min2)
maximum=min(max1, max2)
if minimum>maximum:
    print(-1)
else:
    print(minimum, maximum)
