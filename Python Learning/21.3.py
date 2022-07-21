
# y = lambda n: [i for i in range(n)]
# z=y(5)
# print(z)


power = lambda n: [i*2 for i in range(n)]
z=power(6)
print(z)

def is_even(n):
    return n%2==0
a= filter(is_even, [1,33,4,67,89,55,45,42,8,4])
a = list(a)
print(a)