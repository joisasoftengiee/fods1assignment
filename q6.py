begin = int(input("Enter start number : "))
end = int(input("Enter end number : "))


count = 0 
sum = 0 

print("prime numbers are : ")

for num in range (begin ,end  + 1): #using for loop 
    if num <= 1 :
        continue 
    is_prime = True 
    i = 2 
    while i < num:
      if num % i == 0 :
        is_prime = False
        break 
      i = i + 1 
    if is_prime:
      print(num)
      count = count + 1 
      sum = sum + num 

print("Count of a prime num is : ",count)
print("The sum of prime num is : ", sum)

