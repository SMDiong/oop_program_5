# Diong, Shan Marc C.
# BSCPE 1-2

# Greet and enter username
while True:
    user_name = input("Please enter your name: ")

    # Input Validation and Display Error
    if not user_name.isalpha() or " " in user_name:
        print("\nInvalid input! Please enter a valid name without symbols, spaces, or numbers.\n")
    else:
        print(f"\nHello {user_name}! Welcome to my Simple App Calculator!")
        break

# The loop for Try Again function
while True:
    numbers = []

    # The user will input as many numbers as they want instead of just two
    while True:
        print("\nThe maximum number count is 20.")
        for i in range(20):
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

            # Input Validation and Display Error
            while True:
                try:
                    number = float(user_number)
                    numbers.append(number)
                    break
                except ValueError:
                    user_number = input("\nInvalid input! Please enter a valid number: ")
                    if user_number == "":
                        break

        # Error if there are not enough numbers
        if len(numbers) < 2:
            print("\nInvalid input! At least two numbers are required.")
            numbers = []
        else:
            break

    # Ask the user what of the four operations will be used
    while True:
        print("\nChoose one of the four math operations by their corresponding initials.")
        print("(A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision.")
        math_operation = input("\nPlease enter your operation (A/S/M/D): ")

        # Input Validation and Display Error
        if math_operation.upper() not in ['A', 'S', 'M', 'D']:
            print("\nInvalid math operation choice!")
            continue

        # Calculations
        # Addition
        if math_operation.upper() == 'A':
            operation_name = "Addition"
            user_result = sum(numbers)

        # Subtraction
        elif math_operation.upper() == 'S':
            operation_name = "Subtraction"
            user_result = numbers[0] - sum(numbers[1:])

        # Multiplication
        elif math_operation.upper() == 'M':
            operation_name = "Multiplication"
            user_result = 1
            for num in numbers:
                user_result *= num

        # Division
        elif math_operation.upper() == 'D':
            operation_name = "Division"
            if 0 not in numbers[1:]:
                user_result = numbers[0]
                for num in numbers[1:]:
                    user_result /= num
            # Zero Division Error
            else:
                print("\nDivision by zero is invalid.")
                continue

        # Display results
        print(f"\nThe result of the {operation_name} operation is: {user_result}")

        # Ask the user whether to try again or not. If not, display grateful message
        try_again = input("\nDo you want to try the calculator again? (Yes/No): ")
        if try_again.lower() == "yes":
            break
        elif try_again.lower() == "no":
            print(f"\nThe program ended. Thank you for your participation, {user_name}!")
            exit()
        else:
            print("\nInvalid input! Please enter 'Yes' or 'No'.")
