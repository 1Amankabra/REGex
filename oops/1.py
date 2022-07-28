class Student:
    def __init__(self,fname,id):
        #print("hello")
        self.fname=fname
        self.id=id
    def studentinfo(self):
        print(self.fname,self.id)
# constructor l=: function(allocate memory => object)
#object = classname()

#Student_john

s1=Student("john",1)
s1.studentinfo()

s2=Student("killer",2)
# print(s2.fname,s2.id)
s2.studentinfo()
