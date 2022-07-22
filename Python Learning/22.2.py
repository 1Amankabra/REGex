from inspect import classify_class_attrs
from unicodedata import name


class School:
    def __init__ (self,name,pers_det):
        self.name = name
        self.pers_det = pers_det

    def get_name(self):
        return f'this is {self.name}'    

    def get_pers_det(self):
        return f'details {self.pers_det}'

class st(School):
    def __init__(self,name,pers_det,class_,roll_no):
        super().__init__(name,pers_det)
        self.class_ = class_ 
        self.roll_no = roll_no

    def get_class_(self):
        return f'st class {self.class_}'

    def get_roll_no(self):
        return f'st roll no {self.roll_no}'

xyz = st('aman','20 years','2nd year',222) 
print(xyz.get_name())
print(xyz.get_pers_det())
print(xyz.get_class_())
print(xyz.get_roll_no())                

