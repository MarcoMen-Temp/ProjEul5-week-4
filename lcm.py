"""Marco Men
Adapted from:https://blog.dreamshire.com/project-euler-5-solution/
https://code.mikeyaworski.com/python/project_euler/problem_5"""

def factorial(n):
  if n==0:#Base case
     return 1
  else:
    return n*factorial(n-1)#Recursive call



def is_multiple(a,n):#checks if a is a multiple of every number from 1 to n
    for i in range (1,n):
      if a % i !=0:
        return False
    return True 

def findSmallestMultiple(n):
    for i in range(n, factorial(n) + 1, n):
        if is_multiple(i, n):
            return i
    return -1 # finishes the function



print (findSmallestMultiple(10))
print(findSmallestMultiple(20))