


# file = open('hw.txt', 'r')
# # data = file.read()
# data = file.readlines()
# file.close()
# print(data)

file = open('hw.txt','w')
file.write('this is aman')
file.writelines(['hello','good'])
file.close()