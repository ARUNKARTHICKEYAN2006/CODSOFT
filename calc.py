

# 1. Ask the user what they want to do.
print("What do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# 2. Get the user's choice.
choice = input("Enter your choice (1/2/3/4): ")

# 3. Get the numbers from the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 4. Do the calculation based on the choice .
if choice == "1":
    result = num1 + num2
    print("Result:", result)
elif choice == "2":
    result = num1 - num2
    print("Result:", result)
elif choice == "3":
    result = num1 * num2
    print("Result:", result)
elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid choice.")

# 5. Say thankyou .
print("Thank you for using the calculator!")