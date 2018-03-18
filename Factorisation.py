# Stack OverFlow: 'Python Finding Prime Factors'

def prime_factors(x):
    x=2520
    '''x=232792560  # lcm of the first 10 natural numbers'''
    A=[]
    for i in range (2, x):
        while x%i==0:
            x=x/i

            A.append(i)

    if sum(A)==0:

        A.append(x)

    return A


print(prime_factors(2520)) # Able to print the factorisation of 2520-from line 5


def primes(y):

    if y==1:
        return False

    for a in range (2,y):
        if y% a == 0:
            return False
        return True

    for n in range(11,21):
        print (n,primes(y))