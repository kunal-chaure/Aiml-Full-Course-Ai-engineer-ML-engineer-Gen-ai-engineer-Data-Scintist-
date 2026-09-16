class employee:
    start_time = "10am"
    end_time="5pm"
    
    def change_time(self,new_end_time):
        self.end_time = new_end_time

class teacher(employee):
    def __init__(self , subject):
        self.subject = subject
        
t1= teacher("DSA")
t1.change_time("4pm")
# print(t1.subject,t1.start_time,t1.end_time)
print(f"this is your subject {t1.subject} and your start time is {t1.start_time} and end time is {t1.end_time} ")
