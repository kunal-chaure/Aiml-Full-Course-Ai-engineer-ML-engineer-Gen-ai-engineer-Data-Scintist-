class Student:
    def __init__(self,name,cgpa):
        # print("hello kunal ")
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self):  
        return self.cgpa  
stud1 = Student("KUNAL",9.0)
stud2 = Student("anil",10)
stud3 = Student("suraj",7)

print(stud1.name)
print(stud1.get_cgpa())
print(stud2.get_cgpa())
print(stud3.get_cgpa())

# stud1.get_cgpa()