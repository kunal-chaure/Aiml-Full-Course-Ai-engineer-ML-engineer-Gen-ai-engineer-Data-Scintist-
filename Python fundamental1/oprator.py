a= 10 
b= 10

print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a%b)
print (a**b)


#relational operator
print("\n")
print (a==b)
print (a!=b)
print (a>b)
print (a<b)
print (a>=b)
print (a<=b)
    
#logical operator
print("this is false", not True)

g = 19
h=20
print (  g> 20 and h<20)

# oprator presedence 
# we can alos say it bodmas rule
#  ()
# **
# *,/,%
# +,-
# == ,!= ,>,<,>=,<=
# not
# and 
# or

ans = 10/ 3
print(type(ans)) #this is called implicit type conversion as it converts int to float  automatically

ans =int  (10/ 3)
print( type(ans))
print (ans)