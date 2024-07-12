nm=input("Enter Your Name:")
rn=input("Enter Your Roll Number:")
a=int(input("Enter The python Mark:"))
b=int(input("Enter The CS Mark:"))
c=int(input("Enter The J2EE Mark:"))
total = a+b+c
per = round((a+b+c)/3,2)

print()
print("Name      :",nm)
print("Roll No   :",rn)
print()
print("Python    :",a)
print("CS        :",b)
print("J2EE      :",c)
print("Total     :",total)
print()
print("Percentage:",per)


if per>=40 and per<=50:
    print("C Grade...")
elif per>=50 and per<=60:
    print("B Grade...")
elif per>=60 and per<=100:
    print("A Grade...")
else:
    print("You Are Fail...")
    
if a>33 and b>33 and c>33:
    print("Pass")
else:
    print("Fail")