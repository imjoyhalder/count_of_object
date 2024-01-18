class person:
    def __init__(self,name,age,hight):
        self.name = name
        self.age = age
        self.hight  = hight
    
    def __str__(self) -> str:
        return "Name: {} \nAge: {} \nHight: {}".format(self.name,self.age,self.hight)
    
class worker(person):
    def __init__(self,name,age,hight,salary):
        super(worker,self).__init__(name,age,hight)
        self.salary = salary

    def __str__(self) -> str:
        txt =  super(worker,self).__str__()
        return txt + "\nSalary: {}".format(self.salary)

    def calculate_salray(self):
        return self.salary*12


person1 = worker("Joy Halder",12,"5.4 fit",120000)
person1.calculate_salray()
print(person1)
    
    