# Diong, Shan Marc C.
# BSCPE 1-2

# Word Format
green = "\033[1;32m"
blue = "\033[1;34m"
red = "\033[1;31m"
yellow = "\033[1;33m"

# Greet and enter username
while True:
    user_name = input(green + "Please enter your name: ")

    # Input Validation and Display Error
    if not user_name.isalpha() or " " in user_name:
        print(red + "\nInvalid input! Please enter a valid name without symbols, spaces, or numbers.\n" + green)
    else:
        print(green + f"\nHello {blue + user_name + green}! Welcome to my Simple App Calculator!")
        break

# The loop for Try Again function
while True:
    numbers = []

    # The user will input as many numbers as they want instead of just two
    while True:
        print(yellow + "\nThe maximum number count is 20." + green)
        for i in range(20):
            if i == 0:
                prompt = f"Please enter your 1st number: "
            elif i == 1:
                prompt = f"\nPlease enter your 2nd number: "
            elif i == 2:
                prompt = f"\nPlease enter your 3rd number or press {yellow}ENTER{green} to finish: "
            else:
                prompt = f"\nPlease enter your {i + 1}th number or press {yellow}ENTER{green} to finish: "

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
                    user_number = input(red + "\nInvalid input! Please enter a valid number: " + green)
                    if user_number == "":
                        break

        # Error if there are not enough numbers
        if len(numbers) < 2:
            print(red + "\nInvalid input! At least two numbers are required." + green)
            numbers = []
        else:
            break

    # Ask the user what of the four operations will be used
    while True:
        print("\nChoose one of the four math operations by their corresponding initials.")
        print(yellow + "\t\t(A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision." + green)
        math_operation = input(f"\nPlease enter your operation {yellow}(A/S/M/D){green}: ")

        # Input Validation and Display Error
        if math_operation.upper() not in ['A', 'S', 'M', 'D']:
            print(red + "\nInvalid math operation choice!" + green)
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
                print(red + "\nDivision by zero is invalid." + green)
                continue

        # Display results
        print(f"\nThe result of the {yellow}{operation_name}{green} operation is: {blue}{user_result}{green}")

        # Ask the user whether to try again or not. If not, display grateful message
        while True:
            try_again = input(f"\nDo you want to try the calculator again? {yellow}(Yes/No){green}: ")
            if try_again.lower() == "yes":
                break
            elif try_again.lower() == "no":
                print(f"\nThe program ended. Thank you for your participation, {blue}{user_name}{green}!")
                exit()
            else:
                print(red + "\nInvalid input! Please enter 'Yes' or 'No' only." + green)
                continue
        break

# End