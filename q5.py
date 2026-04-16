m1 = float(input("enter  marks of subject 1 : "))
m2 = float(input("enter  marks of subject 2 : "))
m3 = float(input("enter  marks of subject 3 : "))
m4 = float(input("enter  marks of subject 4 : "))
m5 = float(input("enter  marks of subject 5 : "))
m6 = float(input("enter  marks of subject 6 : "))

#total 

total = m1 + m2 + m3 + m4 + m5 + m6 

#average 

avg = total / 6 

#percentage 

p = (total / 600) * 100 

#grade

if p >= 85:
    grade = "Distinction" 
elif p >= 70:
    grade = "First Division"
elif p>= 55:
    grade ="Second Division"
elif p>= 45:
    grade ="Third Division"
else:
    grade ="Fail"

print("Total = ",total)
print("Average = ",avg)
print("Percentage = ",p)
print("Grade = ",grade)