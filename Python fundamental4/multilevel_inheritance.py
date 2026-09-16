class employee:
    start_time = "10am"
    end_time="5pm"
    
class teacher(employee):
    def __init__(self , role):
        self.role =role
        
class accounts(teacher):
    def __init__(self, salary,role):
       
        super().__init__(role)
        self.salary = salary
    
act1 = accounts("Aiml engineer",25000000)
print(act1.role,act1.salary,act1.start_time)