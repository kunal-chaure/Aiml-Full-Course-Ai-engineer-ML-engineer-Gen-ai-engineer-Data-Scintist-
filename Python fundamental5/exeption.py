try:
    no = int(input("Please enter the number "))
    ans = 100/no
except ZeroDivisionError:
    print("hey why are you trying to divide by zero?")   
except ValueError:
    print("don't enter the value")
else:
 print(ans)

finally:
    print("thank you sir have a great day")
    