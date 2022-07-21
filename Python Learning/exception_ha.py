# try:
#     print(5/0)
# except:
#     print("You can't divide by 0")


try:
    print(5/'a')
except ZeroDivisionError:
    print("you can't divide")
except         