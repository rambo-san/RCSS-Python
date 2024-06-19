n=int(input("Enter the number of Students : "))
student_dict={}
for i in range(n):
    name=input("Enter the name of the student: ")
    roll_no=int(input("Enter the roll number of the student: "))
    marks=int(input("Enter the marks of the student: "))
    student_dict[name] = {
            "Roll Number": roll_no,
            "Marks": marks
        }
max=0
for i in student_dict:
    if(student_dict[i]["Marks"]>max):
        max=student_dict[i]["Marks"]
        name=i
print("The student with the highest marks is: ",name)
print("The details of the student are: ")
print("Name: ",name)
print("Roll Number: ",student_dict[name]["Roll Number"])
print("Marks: ",student_dict[name]["Marks"])
    