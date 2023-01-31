'''
Dynamic programming(DP): DP is an algorithm 'design' technique.
                         It has recurrences with overlapping sub-instances.

Memoization: Memoization is one of the optimization techniques for DP.
             Simply storing the results of previouis function calls to reuse it later.

We can solve the Fibonacci problem again while using DP's memoization.
'''
def FibonacciDP(n):
    dicFibonacci = {} #using a dictionary collection variable type for memoization.
    dicFibonacci[0] = 0
    dicFibonacci[1] = 1

    for itr in range(2, n+1): #building up a bigger solutions
        dicFibonacci[itr] = dicFibonacci[itr-1] + dicFibonacci[itr-2]
    return dicFibonacci[n]


for itr in range(0, 10):
    print(FibonacciDP(itr), end=" ")

'''
compare with the recursion's Fibonacci solution in big-O,
    recursion spends O(2^n)
    DP spends O(N)
'''