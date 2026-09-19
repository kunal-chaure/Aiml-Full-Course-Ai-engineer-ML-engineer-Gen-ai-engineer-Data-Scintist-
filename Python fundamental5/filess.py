# f = open("info.txt","r")
# data = f.read()   #this will give all data


# data =f.readline()
# print(data)

# data =f.readline()
# print(data)
# data =f.readline()
# print(data)

# print(type(data))
# f.close()


# f = open("info.txt","a")
# f.write ("\n this is data is inserted using apend")


# f = open("info.txt","r+")
# f.write ("123")

f = open("info.txt","a+")
f.write (" 123")

import os
os.remove("kunal.java")