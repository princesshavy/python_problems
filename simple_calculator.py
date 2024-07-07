def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def Area_of_a_Triangle(x,y):
    return (1*x*y)/2

def Area_of_a_Ellipse(x,y):
    return π*x*y
π = 22/7

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Area of a Triangle")
print("6. Area of a Ellipse")

choice = input("Enter choice (1/2/3/4/5/6): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", Area_of_a_Triangle(num1, num2))
elif choice == '6':
    print("Result:", Area_of_a_Ellipse(num1, num2))

else:
    print("Invalid input")

