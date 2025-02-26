#Take a number and use the += operator to increase its value by 10
a=1
a+=10
print(a)

#Write a Python program to check if a given year is a leap year or not.
a=int(input("enter year:"))
if a%4==0:
    print("This is a Leap Year")
else:
    print("This is not a leap year")
    

# Write a program that asks the user to enter their marks and displays 
# their grade:
# • 90-100: A
# • 80-89: B
# • 70-79: C
# • 60-69: D
# • Below 60: F

marks=int(input("Enter Your Marks:"))
if 90<= marks <=100:
    print("Grade A")
elif 80<= marks <=89:
    print("Grade B")
elif 70<= marks <=79:
    print("Grade C")
elif 60<= marks <=69:
    print("Grade D")
else:
    print("Grade F")