def add(a, b):
    return a + b

def menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("5. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        menu()
        choice = input("Select an option (1, 5): ").strip()
        
        if choice == '5':
            print("Exiting Calculator Master, Goodbye!")
            break
        elif choice == '1':
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        else:
            print("Invalid choice! Please select 1 or 5.")

if __name__ == "__main__":
    main()
