number = float(input("enter a number :"))
cube = number * number * number 
print("Cube : ",cube )

cubeRoot = number ** (1/3) #for cube root 
print("Cube Root : " , cubeRoot)

x = number - 1 
ln = 0 
term = x 
i = 1 
while i <= 1000:
    ln = ln + term / i 
    i = i + 1 
    term = term * (-x)
print ("Natural Log  : ", ln)

log2 = ln / 0.6931471805599453
print("Base-2 Log: ", log2)

power = number ** 6
print("Power of 6 : ", power)