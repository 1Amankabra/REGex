def generate_password(username , password):
    username=username[:4]
    password=password[-4:]
    a = username+password
    return a
username = input()
password = input()
print(generate_password(username,password))    

