def sum(n):
    if n==0:
        return n
    else:
        return n+sum(n-1)
    # 4+3+2+1+0

n=4   
print(f'sum of number {n} is: ', sum(4))


def fabnacci(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return fabnacci(n-1)+fabnacci(n-2)
n=6    
print(f'{n}th Fabonacci number is: ',fabnacci(n))