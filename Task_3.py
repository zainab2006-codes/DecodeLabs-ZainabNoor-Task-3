import random
import string

try:
    while True:
        length = int(input("\nEnter password length (minimum 8): "))

        if length >= 8:
            break
        else:
            print("\nPassword length should be at least 8 characters. Try again.")

    choice = input("\nInclude special characters? (Y/N): ").upper()

    if choice == "Y":
        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )
    else:
        characters = (
            string.ascii_letters +
            string.digits
        )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

except ValueError:
    print("\nPlease enter a valid number.")