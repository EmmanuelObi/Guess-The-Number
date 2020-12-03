from random import randint

secret_num = randint(0, 20)
guess = ""
guess_limit = 5
guess_count = 0
out_of_guesses = False

print('HELLO')
User_Name = input("What is your name? :")
print('Welcome,' + User_Name)

print("Let the Game Begin......haq haq haq")

while guess != secret_num and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = float(input("Guess a number: "))
        if guess < secret_num:
            print(" Your Guess is lower than secret_number, try again ")
            guess_count += 1
        elif guess > secret_num:
            print(" Your Guess is higher than secret_number, try again ")
            guess_count += 1
        else:
            print(" BRAVO!, You Guessed Right.")
        
    else:
        out_of_guesses = True

if out_of_guesses == True:
    print(" You are out of Guesses, Game over!. ")



print("Thanks for Playing..")




