# A program to capture the student name and the course work mark out 40 and the exam score outof 100 ,the program should compute the final course mark out of 30 and fianal exam mark out 70 and the final mark the program should then dertermine the students grade basing on the 

student_name = input("Enter Student name: ")

course_workmark = int(input("Enter course work mark :"))

final_course_work = (course_workmark/40)* 30

exam_mark = int(input("Enter exam mark :"))

final_exam_mark = (exam_mark/100)*70

print(f"final mark :{final_course_work}\nfinal exam : {final_exam_mark}")

final_score = final_course_work + final_exam_mark

if final_score >=80:
    print("GRADE A")
 
elif final_score >=70:
    print("GRADE B")

elif final_score >=60:
    print("GRADE C")

elif final_score >= 50:
    print("GRADE D")

else:
    print("F")