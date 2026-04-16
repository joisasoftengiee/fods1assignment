num = int(input("Enter a number : ")) # taking input 

if num < 0 : 
    print("Invalid input! Please enter a positive intger. ")
    
elif num == 0:
    print("Factorial of 0 is : 1")

else:
    fact = 1 
    i = 1 
    while i <= num:
        fact = fact * i 
        i = i + 1
    print(f"Factorial of {num}! is ",fact)