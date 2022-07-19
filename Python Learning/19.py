n = input('enter string')
# map_ = {}
# # s = len.n
# for i in n:
#  count = int(0)
#  if i in n:
#     print(count+1)
#  else:
#     print('no repa')
# print(map_ )    


# for i in n:
#     if i in map_:
#         map_[i]+=1
#     else:
#         map_[i] =1
# print(map_)      

       
n = n.lower()
map_={}
for i in n:
    if i in map_:
        map_[i]+=1
    else:
        map_[i]=1
print(map_)            
