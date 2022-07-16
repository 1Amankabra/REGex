
# map_ = {
#     'key': 'value',
# }
map_ = {
    'first_name': 'Aman',
    'last_name': 'kabra',
    'company': 'regex'

}

print(map_['first_name'])
print(map_['last_name'])
# print(map_['company'])
print(map_.get('company'))
print(map_.get('company','not found'))
map_.update({'company':'starks'})
print(map_)
print(map_['company'])
company = map_.pop('company')
print('company')
print(map_)