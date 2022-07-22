


from webbrowser import get


def max_freq_of_a_word(file_path):
 file = open(file_path,'r')
 data = file.read()
 data = data.split()

 map_={}     
 for ele in data:
    if ele in map_:
        map_[ele]+=1
    else:
        map_[ele]=1
 return map_ 

map_ = max_freq_of_a_word('demo.txt')
# print(map_)  

data = max_freq_of_a_word('demo.txt')
file = open('collect.txt','w')
for k,v in data.items():
    file.write(k+' '+str(v)+'\n')


     
     