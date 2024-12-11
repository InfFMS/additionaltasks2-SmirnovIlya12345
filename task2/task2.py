a=int(input())
b=int(input())
c=int(input())
for i in range(min(a, b)//2+1):
    if 2*a*i+2*b*i-4*i*i>c:
        print(i-1)
        break




