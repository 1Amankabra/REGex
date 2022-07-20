def count_alp(n):
    total = 0
    for i in range(len(n)-1):
        # if n[i] == n[i+1]:
        if (ord(n[i])+1 == ord(n[i+1])):
            total +=1
    return total
n=input()
print(count_alp(n))            