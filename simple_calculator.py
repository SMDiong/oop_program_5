# Diong, Shan Marc C.
# BSCPE 1-2

# Greet the user
user_name = input("Please enter your name: ")
print(f"\nHello {user_name}! Welcome to my Simple App Calculator!")

# The user will input as many numbers as they want instead of just two
while True:
    for i in range(10):
        if i == 0:
            prompt = "Please enter your 1st number or press ENTER to finish: "
            print("\nThe maximum number count is 10.")
        elif i == 1:
            prompt = "\nPlease enter your 2nd number or press ENTER to finish: "
        elif i == 2:
            prompt = "\nPlease enter your 3rd number or press ENTER to finish: "
        else:
            prompt = f"\nPlease enter your {i + 1}th number or press ENTER to finish: "

        user_number = input(prompt)
        if user_number == "":
            break

# Ask what of the four operations will be used
    print("\nChoose one of the four math operations by their corresponding initials.")
    print("(A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision.")
    math_operation = input("\nPlease enter your choice (A/S/M/D): ")


# Display results

# Ask the user whether to try again or not, if not display grateful message

# Input Validations

# Display errors