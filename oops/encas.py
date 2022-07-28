class vehcile:
    _year=1000  #notation for protected modifier
    __price=100000 #denote private variable

class tatamoters(vehcile):
    car_name='harrier'


v1=vehcile()
# print(v1.__price)

# print(dir(v1))

t1 = tatamoters()        
print(t1._year,t1._vehcile__price)