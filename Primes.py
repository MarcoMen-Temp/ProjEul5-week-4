""" Marco Men
Adapted from StackOverFlow : ' https://stackoverflow.com/questions/30543106/how-to-calculate-least-common-multiple-of-1-2-3-n ' """
import math
from itertools import compress

Prime=[]

def is_primes(n) :
    """return 'True' if 'n' is a prime number. False otherwise"""
    b =[]
    if n==1:
       return False # 1 is not a prime

    if n==2:
       return True
       
    
    if n > 2 and n % 2 ==0:
       return False
    
    max_divisor = math.floor(math.sqrt(n))
    for i in range (3, 1+max_divisor,2):
        if n % i == 0 :
            return False
    return True

    
for n in range (10,21):
    print (n, is_primes(n))