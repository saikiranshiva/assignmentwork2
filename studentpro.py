rollno=int(input("Enter your roll number"))
name=input("Enter your name")
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
sub6=int(input("Enter marks of the sixth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)//6
totalmarks=(sub1+sub2+sub3+sub4+sub5+sub6)
print(rollno)
print(name)
print(totalmarks)
print(avg)
if(avg>=80):
    print("Grade: A")
elif(avg>=60&avg<79):
    print("Grade: B")
elif(avg>=50&avg<59):
    print("Grade: C")
elif(avg>=40&avg<49):
    print("Grade: D")
elif(avg<40):
    print("promoted")
else:
    print("Grade: F")
