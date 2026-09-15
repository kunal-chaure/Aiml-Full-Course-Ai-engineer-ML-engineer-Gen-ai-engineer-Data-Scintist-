# def avg(a,b,c):
#     sum = a+b+c
#     return sum/3
# print(avg(2,2,2))

## default values in function

def sum(a,b=1):
    return a+b
# print(sum(10)) result will 11 as 1 will be from b
# print(sum(10,10)) result is 20

# lambda function

sum= lambda a,b : a+b
print(sum(2,2))