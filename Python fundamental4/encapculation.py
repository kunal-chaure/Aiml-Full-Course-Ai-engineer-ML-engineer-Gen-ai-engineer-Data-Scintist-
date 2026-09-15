class data:
    def __init__(self,name,balance):
        self.name = name #this is public
        self.__balance = balance # only one _ this is protected and __ double underscor is private
    
acc1 = data("kunal",970000000)
print(acc1.name)
print(acc1.balance)