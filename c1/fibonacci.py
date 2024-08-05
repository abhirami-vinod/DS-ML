a=0
b=1
fib=[]
n=int(input("Enter the limit"))
for _ in range(n):
   fib.append(a)
   a,b=b,a+b
print(fib)
