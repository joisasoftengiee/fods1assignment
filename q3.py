number = int(input("enter a number:"))
if number > 0: #using if/else statements
    rem = number % 2 
    if rem == 0 :
        print("The number is positive even")
    else :
        print("the number is positive odd")
elif number < 0 :
    rem = number % 2 
    if rem == 0 :
        print("The number is negative even")
    else:
        print("The number is negative odd")
else:
    print("The number is zero")
