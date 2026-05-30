def get_number(prompt):
    """Safely gets a float number from the user, handling invalid inputs."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid numerical value.")

def calculate():
    """Main calculator logic."""
    print("\n--- Modern Python Calculator ---")
    
    # 1. Safe Input Gathering
    num1 = get_number("Enter the first number: ")
    
    # Normalize input by converting to lowercase and stripping extra whitespace
    operation = input("Select operation (+, -, *, / or word): ").strip().lower()
    
    num2 = get_number("Enter the second number: ")

    # 2. Conditional Execution (Calculates ONLY what is needed)
    if operation in ["+", "add", "addition"]:
        print(f"✅ The sum of the numbers is: {num1 + num2}")
        
    elif operation in ["-", "subtract", "subtraction"]:
        print(f"✅ The difference of the numbers is: {num1 - num2}")
        
    elif operation in ["*", "product", "multiply"]:
        print(f"✅ The product of the numbers is: {num1 * num2}")
        
    elif operation in ["/", "divide", "division"]:
        # Inline Exception Handling for Division by Zero
        try:
            result = num1 / num2
            print(f"✅ The result after division is: {result}")
        except ZeroDivisionError:
            print("❌ Error: Math Domain Error. Division by zero is not allowed.")
            
    else:
        print("❌ Invalid operation selected. Please try again.")

def main():
    """Controls the program flow and allows repeating calculations."""
    while True:
        calculate()
        
        # Ask the user if they want to continue
        choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if choice not in ["yes", "y"]:
            print("Goodbye! Thanks for using the calculator.")
            break

# This ensures the script only runs if executed directly
if __name__ == "__main__":
    main()

