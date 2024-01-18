class person:
    person_amount = 0

    def __init__(self,name,age,hight):
        self.name = name 
        self. age = age
        self.hight = hight
        
        # This is conutn of our object
        person.person_amount += 1
    
    def __del__(self):
        person.person_amount -=1
    
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nHight: {self.hight}"
    

person1 = person("Joy Halder",19,"5.4 fit")
del person1
person2 = person("Joy Halder",19,"5.4 fit")
person3 = person("Joy Halder",19,"5.4 fit")
person4 = person("Joy Halder",19,"5.4 fit")
del person2
print(person.person_amount)
