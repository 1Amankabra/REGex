


lst = []
while True:
    p = input()
    p = p.split()
    if p[0] == 'stop':
        break
    elif p[0] == 'push':
        lst.append(p[1])
    elif p[0] == 'pop':
        index_of_value = lst.index(p[1])
        lst.pop(index_of_value)
    else:
        print('invalid')
print(lst)        
