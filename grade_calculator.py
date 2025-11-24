print(".......students Grade calculator.....")
#input marks

sub1=float(input("enter marks of subject 1:"))
sub2=float(input("enter marks of subject 2:"))
sub3=float(input("enter marks of subject 3:"))
sub4=float(input("enter marks of subject 4:"))
sub5=float(input("enter marks of subject 5:"))

#calculate total and percentage

total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100

#determine grade
if percentage>=80:
    grade="A"
elif percentage>=60:
    grade="B"
elif percentage>=45:
    grade="C"
elif percentage>=35:
    grade="D"
else:
    grade="F"

    #print result
    print("\n....Result.....")
    print("Total Marks:", total)
    print("percentage:", percentage,"%")
    print("Grade:", grade)
