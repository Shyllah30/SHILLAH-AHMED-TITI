students = ["Shillah", "Ahmed", "Titi", "Aisha","Isa"]
student = []

subjects = ["Eng", "SST","SCI","Math"]
class_total = 0
for student in students :
    print(student)
    total = 0

    for subject in subjects:
        score = int(input(f"\t{subject}: "))

        total += score
        average = total/len(subjects)
    print(f"total = {total}\naverage = {average}")
class_total += total
class_average = class_total/len(subjects)
print(f"class total = {class_total}\nclass average = {class_average}")







