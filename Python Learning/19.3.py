# while True:
#     p = input()
#     p = p.split()
#     lst1 = []
#     lst2 = []
#     if p[0] == 'stop':
#         break
#     else:
#         for i in p:
#          map_ = {}
#          map_[1] = set()
#          map_[0] = lst1[]
#          map_[i]=1
#          map_[0] = 'lst2'
# print(map_)

map_={}
while True:
    stud = input()
    stud = stud.split()
    if stud[0] == 'stop':
        break
    else:
        if stud[0] in map_:
            map_[stud[0]].add(stud[1])
        else:
            map_[stud[0]]={stud[1]}
            map_[stud[0]].add(stud[1])
print(map_)            

