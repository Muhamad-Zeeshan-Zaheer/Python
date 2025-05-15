a=float(input("Enter the marks of student"))
if a>=90:
    print("Grade A")
elif a>=85 or a<90:
    print("Grade A-")
elif a>=80 or a<85:
    print("Grade B+")
elif a>=75 or a<80:
    print("Grade B")
elif a>=70 or a<75:
    print("Grade B-")
elif a>=65 or a<70:
    print("Grade C+")
elif a>=60 or a<65:
    print("Grade C")
elif a>=55 or a<60:
    print("Grade C-")
elif a>=50 or a<55:
    print("Grade D")
else:
    print("Grade F")
