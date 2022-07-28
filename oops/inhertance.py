class driver:
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email

    def infoprint(self):
        print(self.id,self.name,self.email) 


class customer(driver):
    def __init__(self, id, name, email,wallet):
        super().__init__(id, name, email)
        self.wallet=wallet


c1=customer(1,'jack','jack@gmail.com',100)
print(c1.id,c1.name,c1.email,c1.wallet)                    