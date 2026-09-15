class  products:
    count =0 
    def __init__(self,name,price):
        self.name = name
        self.price = price
        products.count += 1
    def get_info(self):
         print(f"the name of product is {self.name} and the price is Rs. {self.price}")
    @classmethod
    def total_count(cls):
        print(f"the total no of products is {cls.count}")
    
    @staticmethod
    def discout_price(price,discount):
        print(f"the discounted price is ={price - (price*discount/100)}")
        
p1=products("mobile",10000)
p2=products("watch",1000)
p3=products("laptopp",70000)

# p1.get_info()
# products.total_count()
# p1.discout_price(10_000,10)
p1.discout_price(p3.price,10)