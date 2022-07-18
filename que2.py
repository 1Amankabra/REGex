


n = int(input('enter value'))
for i in range(n):

    dt = input("enter data type")
    value1 = int(input("enter first value")) 
    value2 = int(input("enter second value "))

    if dt == 'add':
        print(value1 + value2)
    elif dt == 'mul':
        print(value1 * value2 )
    elif dt == 'sub':
        print( value1 - value2 ) 
    elif dt == 'div':
        print(value1 / value2 )    
    else:
        print('please enter some thing')



# n = input('how many test case')
# n = int(n)

# for i in range(n):
#     op = input('please enter operation')
#     op_list = op.split()
#     print(op_list)
#     if op_list[0] == 'add':
#         fno = int(op_list[1])
#         sno = int(op_list[2])
#         print(fno + sno)
#     elif op_list[0] == 'sub':
#         fno = int(op_list[1])
#         sno = int(op_list[2]) 
#         print(fno - sno) 
#     elif op_list[0] == 'mul':
#         fno = int(op_list[1])
#         sno = int(op_list[2]) 
#         print(fno * sno)
#     elif op_list[0] == 'div':
#         fno = int(op_list[1])
#         sno = int(op_list[2]) 
#         print(fno / sno) 
#     else:
#         print('enter some opperation')               