def add_positive(posSum , num):
    return posSum+num 

def add_negative(negSum , num):
    return negSum+num 

def menu():
    posSum = 0 
    negSum = 0

    while True: #using while loop 
        print("\n --- Menu --- ")
        print("1. Enter a number : ")
        print("2. Show sums ")
        print("3. Exit ")
        choice = input(" Enter your choice : ")

        if choice == "1":
            num = int(input("Enter a number : "))
            if num > 0 : 
                posSum = add_positive(posSum , num )
                print("Added to positive Sum !")
            elif num < 0 : 
                negSum = add_negative(negSum , num )
                print(" Added to negative sum ! ")
            else : 
                print("Zero is neither positive nor negative!")
            
        elif choice == "2":
            print("Positive Sum : ", posSum)
            print("Negative Sum  : " , negSum)

        elif choice == "3":
            print(" Bye Bye ")
            break 

        else: 
            print("Invalid choice ! Try again ")


menu()

