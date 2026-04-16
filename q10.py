
def generateRandom():
    import time 
    seed = int(time.time()) % 1000
    random = (seed * 1103515245 + 12345) % 50 + 1
    return random 

def checkGuess (secret , guess):
    if guess < secret:
        return "Too Low!"
    elif guess > secret:
        return "Too High!"
    else:
        return "Correct!"
    

def game(): #function 
    secret = generateRandom()
    attempts = 7 
    tries = 0 

    print("Welcome to Number Guessing Game! ")
    print("I have picked a number between 1 and 50!")
    print("You have 7 attempts!")

    while tries < attempts:
        remaining = attempts - tries 
        print("\n Attempts remaining:",remaining)
        guess = int(input("Enter Your Guess: "))
        tries += 1 

        result = checkGuess(secret , guess )

        if result == "Correct!" :
            print("Correct! You guessed it in", tries , "attempts!")
            return 
        
        else: 
            print(result)


    print("Better Luck Next Time! The Number Was : ", secret)

game()