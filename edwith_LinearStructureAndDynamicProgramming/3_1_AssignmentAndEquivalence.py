'''
assignment operator(=): check the equivalence of two referenced values

equivalence operator(is): check the equivalence of two referenced object's IDs
'''

x = [1, 2, 3]
y = [100, x, 120]
z = [x, 'a', 'b']

x[1]=2

x2 = [1, 2, 3]

if x == x2:
    print("equivalent") #True
else:
    print("not equivalent")

if x is x2:
    print("is same ID")
else:
    print("is not same") #True

if x[1] is y[1][1]:
    print("is same ID") #True
else:
    print("is not same")