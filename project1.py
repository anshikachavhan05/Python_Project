#Random password generator
import random
import string

length = int(input("Enter password length: "))

print("Choose character types:")
print("1. Digits")
print("2. Letters")
print("3. Special Characters")
print("4. Done")

characters = ""

while True:
    choice = input("Enter option: ")

    if choice == "1":
        characters = characters + string.digits
    elif choice == "2":
        characters = characters + string.ascii_letters
    elif choice == "3":
        characters = characters + string.punctuation
    elif choice == "4":
        break
    else:
        print("Invalid choice")

if characters == "":
    print("No characters selected, cannot generate password.")
else:
    password = ""
    for i in range(length):
        password = password + random.choice(characters)
    print("Your password is:", password)