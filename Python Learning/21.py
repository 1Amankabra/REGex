


def read_file_and_return_map(file_path):
  file = open(file_path,'r')
      #data = file.read()
  data = file.readlines()
  map_={}

  for elem in data:
    sub, name = elem.split()
    if sub in map_:
     map_[sub].add(name)
    else:
     map_[sub]= {name}
  file.close()
  return map_

map_ = read_file_and_return_map('hw.txt')
print(map_)




# def check():
#  map_={}
#  while True:
#         if [0] in map_:
#             map_[stud[0]].add(stud[1])
#         else:
#             map_[stud[0]]={stud[1]}
#             # map_[stud[0]].add(stud[1])
# print(map_)            
# print(data)