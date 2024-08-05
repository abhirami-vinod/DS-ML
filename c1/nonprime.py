a=int(input("Enter the lower bound"))
b=int(input("Enter the upper bound"))
non_prime=[]
print(" non prime numbers are")
for num in range(a,b+1):
    if num<2:
        non_prime.append(num)
    else:
        for i in range (2,int(num**0.5)+1):
            if num % i ==0:
                non_prime.append(num)
                break
print(non_prime)

