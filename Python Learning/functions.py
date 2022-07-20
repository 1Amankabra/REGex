# def greet():
#     print("hello")
#     return 'hii'
# var = greet()
# print(var)    


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

fact_of_5 = factorial(5)
fact_of_10 = factorial(10)

print(fact_of_5)
print(fact_of_10)
