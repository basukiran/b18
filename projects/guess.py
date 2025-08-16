import random

guessing_number = random.randint(1, 100)

while True:
    user_input = int(input("Guess the number: "))
    
    if user_input > guessing_number:
        print("Number is too big")
    elif user_input < guessing_number:
        print("Number is too small")
    else:
        print("🎉 You guessed the number!")
        break   # exit the loop when guessed correctly
