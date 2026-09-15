class student:
    college_name = "zeal college"   #this is class
    
    def __init__(self,name,cgpa):
                self.name = name  #this is instance
                self.cgpa = cgpa

student1 = student("kunal",10)
print(student1.cgpa)