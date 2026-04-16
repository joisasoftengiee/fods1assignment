start = int(input("Enter start number : "))
stop = int(input("Enter end number : "))

count = 0 
total = 0 

print("Number divisible by 9 but not by 6 : ")

for num in range(start,stop + 1): #using loop 
    if num % 9 == 0 and num % 6 != 0:
        print(num)
        count = count + 1 
        total = total + num

print("count : ",count)
print("Sum   : ",total)