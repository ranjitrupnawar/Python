#function is group of statement perfofrming a specific task 

#when a program gets bigger in size and its complexity grows , it gets difficult for a programm to keep track on which piece of code DeprecationWarning

#when your programme is repetable 

#give me to one piece of logic
 
#build in function ie inbuld function in python
len
range
print

#userdefined  function 

#fucntion with argument ie that value is parameter 


# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# Function Definition
# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))
    
#     average = (a + b + c)/3
#     print(average)


# avg() # Function Call
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# avg()


# def goodDay(name, ending):
#     print("Good Day, " + name)
#     print(ending)
#     return "ok"

# a = goodDay("Harry", "Thank you") 
# print(a)

########################################################################
# default value --> here print ending value if not providing 

def greet(name, ending="thank you"):
    print(f"Good day, {name}")
    print(ending)

greet("Harry", "thanks")
greet("Ranjit")
