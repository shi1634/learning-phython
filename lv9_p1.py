 # name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

# Print 
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
# Ask for two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

#  integers
num1 = int(num1)
num2 = int(num2)

# Compare and print
if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print("Both numbers are equal")