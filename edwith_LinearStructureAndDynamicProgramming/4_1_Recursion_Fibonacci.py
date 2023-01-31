'''
Recursion: A programming method to handle the repeating items in a 'self-similar' way.
           often calling the function again within the function.
'''

def Fibonacci(n):
    if n == 0: #escape when it's not for recursion
        return 0
    if n == 1: #escape when it's not for recursion
        return 1
    intRet = Fibonacci(n-1) + Fibonacci(n-2) #calling the function again within the function
    return intRet

for itr in range(0, 10):
    print(Fibonacci(itr), end=" ") #0 1 1 2 3 5 8 13 21 34