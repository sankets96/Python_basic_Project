#sanket suryavanshi
#calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number:"))
        
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                result = add(num1, num2)
                print("Result: ", result)
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result: ", result)
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result: ", result)
            elif choice == '4':
                result = divide(num1, num2)
                print("Result: ", result)
        else:
            print("Invalid choice. Please choose a valid operation (1/2/3/4).")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break