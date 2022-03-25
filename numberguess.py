import random

while True:

    mode = input("Who is going to guess? (type either c for computer, or h for human) ")

    if mode == "h":
        while True:
            try:
                rang = abs(int(input("What is the range of the guess? (enter positive number) ")))
                break
            except:
                print("Range has to be a number, try again.")
        print(f"I'm thinking of a random number between 0 and {rang}...")
        num = random.randint(0, rang+1)
        while True:
            try:
                guess = int(input("Enter your guess: "))
                break
            except:
                print("Guess has to be a number, try again.")
        tries = 0
        while guess != num:
            if guess > rang or guess < 0:
                guess = int(input("Guess out of range, enter another number: "))
                tries += 1
            elif guess > num + rang/5:
                guess = int(input("Too high, enter another number: "))
                tries += 1
            elif guess < num - rang/5:
                guess = int(input("Too low, enter another number: ")) 
                tries += 1
            elif guess > num:
                guess = int(input("A bit high, enter another number: "))
                tries += 1
            else:
                guess = int(input("A bit low, enter another number: "))
                tries += 1
        print(f"You guessed it! The number was {num}! It took you {tries+1} tries!")
        while True:
            answer = input("Play again? (y/n) ")
            if answer.lower() == "n":
                print("Ok, program shutting down...")
                raise SystemExit
            elif answer.lower() != "y":
                print("Enter either y (yes) or n (no)")
            else:
                break
        continue

    elif mode == "c":
        while True:
            try:
                rang = abs(int(input("What is the range of the guess? (enter positive number) ")))
                break
            except:
                print("Range has to be a number, try again.")
        print("Please enter either h (high), l (low) or c (correct)")
        rangSmall = 0
        guess = random.randint(rangSmall, rang)
        check = input(f"My guess is {str(guess)}, how close is it? ")
        tries = 1
        while check != "c":
            if check == "h":
                while True:
                    if guess == rangSmall:
                        print("But this is the smallest number possible in current range.")
                    else:
                        break
                rang = guess-1
                guess = random.randint(rangSmall, rang)
                check = input(f"My guess is {str(guess)}, how close is it? ")
                tries += 1
            elif check == "l":
                while True:
                    if guess == rang:
                        print("But this is the biggest number possible in current range.")
                    else:
                        break
                rangSmall = guess+1
                guess = random.randint(rangSmall+1, rang)
                check = input(f"My guess is {str(guess)}, how close is it? ")
                tries += 1
            else:
                print("Please enter either h (high) or l (low)")
        print(f"GG, it took me {tries} tries.")
        while True:
            answer = input("Play again? (y/n) ")
            if answer.lower() == "n":
                print("Ok, program shutting down...")
                raise SystemExit
            elif answer.lower() != "y":
                print("Enter either y (yes) or n (no)")
            else:
                break
        continue

    else:
        print("Invalid option, try again.")