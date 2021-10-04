secret_animal = "rat"

#while guess != secret_animal:
#    guess = input("input guess :")

#while guess != secret_animal:
 #   guess = input("sorry try again, hint the animal has whiskers: ")

#while guess != secret_animal:
  #  guess = input("sorry try again, hint the animal has a long tail: ")

#print("you win!")

#checking answer

yes = 1

while (yes == 1):
    win = 2
    numberOfGuesses = 0
    guess = ""
    while (win == 2):
        guess = input("Input guess:")
        if (guess == secret_animal):
            print("You win!")
            win = 1;
        else:
            numberOfGuesses = numberOfGuesses + 1
            if (numberOfGuesses == 1):
                print("Sorry try again, hint the animal has whiskers: ")
            elif (numberOfGuesses == 2):
                print("Sorry try again, hint the animal has a long tail: ")
            elif (numberOfGuesses == 3):
                print("You Lose it was, " + secret_animal)
                win = 0
    yes = int(input("Do you want to try again?: "))
