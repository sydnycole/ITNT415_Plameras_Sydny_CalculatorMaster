def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """Returns the quotient or an error message if dividing by zero."""
    if y == 0:
        return "Error: Division-by-zero handling triggered!"
    return x / y

def menu():
    """Displays the interactive command selection menu."""
    print("\n=== Calculator Master ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_number(prompt):
    """Validates user entry to ensure only valid numeric formats are accepted."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input handling: Please enter a numeric value only.")

def main():
    """Core logic runner keeping the terminal open until option 5 is selected."""
    while True:
        menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '5':
            print("Exiting Calculator Master. Goodbye!")
            break
            
        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
             
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid input handling: Selection must be between 1 and 5.")

if __name__ == "__main__":
    main()
