# Diong, Shan Marc C.
# BSCPE 1-2

# Greet the user
user_name = input("Please enter your name: ")
print(f"\nHello {user_name}! Welcome to my Simple App Calculator!")
numbers = []

# The user will input as many numbers as they want instead of just two
while True:
    print("\nThe maximum number count is 10.")
    for i in range(10):
        if i == 0:
            prompt = "Please enter your 1st number or press ENTER to finish: "
        elif i == 1:
            prompt = "\nPlease enter your 2nd number or press ENTER to finish: "
        elif i == 2:
            prompt = "\nPlease enter your 3rd number or press ENTER to finish: "
        else:
            prompt = f"\nPlease enter your {i + 1}th number or press ENTER to finish: "

        user_number = input(prompt)
        if user_number == "":
            break

        # Input Validation
        try:
            number = float(user_number)
            numbers.append(number)
        except ValueError:
            print("\nInvalid input! Please enter a number.")
            break

    # Error if there are not enough numbers
    if len(numbers) < 2:
        print("\nInvalid input! At least two numbers are required.")
        continue
    break

# Ask what of the four operations will be used
while True:
    print("\nChoose one of the four math operations by their corresponding initials.")
    print("(A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision.")
    math_operation = input("\nPlease enter your choice (A/S/M/D): ")

    # Input Validation
    if math_operation.upper() not in ['A', 'S', 'M', 'D']:
        print("\nInvalid math operation choice!")
        continue

# Calculations
    # Addition
    if math_operation.upper() == 'A':
        user_result = sum(numbers)

    # Subtraction
    elif math_operation.upper() == 'S':
        user_result = numbers[0] - sum(numbers[1:])

    # Multiplication
    elif math_operation.upper() == 'M':
        user_result = 1
        for num in numbers:
            user_result *= num

    # Division
    elif math_operation.upper() == 'D':
        user_result = numbers[0]
        for num in numbers[1:]:
            user_result /= num
    break

# Display results
print(f"\nThe result of the operation is: {user_result}")

# Ask the user whether to try again or not, if not display grateful message

# Input Validations

# Display errors