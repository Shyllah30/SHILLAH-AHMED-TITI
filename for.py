students = ["shifra", "shillah","jane","Ahmed"]
subject = 4
for student in students:
    print(student)
    maths_score = int(input("Enter Math Score: "))
    English_score = int(input("Enter English Score: "))
    Science_score = int(input("Enter science score: "))
    SST_score = int(input("Enter SST score: "))

    total_score = maths_score + English_score + Science_score + SST_score
    Average = total_score/subject
    print(f"total Score :{total_score}\n Average : {Average}")