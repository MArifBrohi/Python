def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n*factorial(n-1)
    # 5*4*3*2*1=120
print(factorial(5))
#factorial(5)