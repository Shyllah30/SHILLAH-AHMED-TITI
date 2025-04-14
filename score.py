students = []
while True:
    student_name = input("Enter student name or Q to stop: ")

    if student_name.upper()== "Q":
        break
    student_course = input("Enter students course: ")
    reg_no = int(input("Enter Reg no: "))
    gender = input("Enter Gender: ")
    age = int(input("Enter your age: "))
    
    scores= []
    for i in range(4):
        scores = int(input("Enter score: "))
    
    student = {
        "student_name": student_name,
        "student_course": student_course,
        "reg.no": reg_no,
        "gender": gender,
        "age": age,
        "scores": scores,
    }
    students.append(student)

def Display_student():
    for student in students:
         print(f'name{student.get("student_name")}')
def students_list_by_course(course):
    for student in students:
        if student("course") == course:
            print(student.get("name"))

    
   
Display_student()


    
