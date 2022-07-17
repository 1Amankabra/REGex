


# s = input("enter a string")
# for i in s:
#     if(ord(i)%2==0):
#        print(i , ' at even ascii')
#        print(ord(i))


# n = int(input('enter'))
# lst = []
# for i in range(0,n):
#    k = input('enter value')
#    lst.append(k)
# print(lst)


n= int(input('enter'))
map_ ={
    'lst1': [],
    'lst2': []
}
for i in range(0,n):
   k = int(input('enter value int'))
   map_['lst1'].append(k)
   m = str(input('some_value str'))
   map_['lst2'].append(m)
print(map_)


# no_of = int(input())
# map_ = {
#     'str': [],
#     'int': [],
#     'float': []
# }

# for i in range(no_of):
#     dt = input("enter data type")
#     value = input("enter value acc. to dt")
#     if dt == 'str':
#         map_['str'].append(value)
#     elif dt == 'int':
#         map_['int'].append(int(value))
#     elif dt == 'float':
#         map_['float'].append(float(value))   
#     else:
#         print('please enter intialize a empty for {dt}'.format(dt))     
# print(map_)        