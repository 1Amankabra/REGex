def table(file_path):
 file = open('tab.txt','r')
 data = file.readlines()
 for i in range(1,len(data)):   
    if (int(data[i])-int(data[i-1])==2):
        con = 1
    else:
        con = 0
        break
 if con == 1:
    print('true')
 else:
    print('false')

