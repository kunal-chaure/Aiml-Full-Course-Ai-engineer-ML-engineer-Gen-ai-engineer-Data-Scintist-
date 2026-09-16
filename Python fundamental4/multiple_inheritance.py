class student:
    def __init__(self,name):
        self.name = name
        
class teacher:
    def __init__(self,role):
        self.role = role

class TA(student,teacher):
    def __init__(self, name,role,salary):
        super().__init__(name)
        self.salary = salary
        self.role = role
      
ta1 = TA("kunal","aiml engineer","2cr")
print(ta1.name,ta1.salary,ta1.role)