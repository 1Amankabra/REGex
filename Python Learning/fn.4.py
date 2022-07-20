# def add_ascii(n):
#     a = 0
#     for i in n:
#         s=ord(i)
#         print(s)
#         a=s+a
#     return a

# n = input()
# print(add_ascii(n))


def sum(input_string):
    return sum(map(ord,input_string))
print(sum('aman'))
