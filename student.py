# A program to ask the user o enter the student name and enter the scores of english, math, science and art

student_name = input("What's your name: ")


score_in_english = int(input("English marks: "))

score_in_math = int(input("Math marks: "))

score_in_science= int(input("Science marks: "))

score_in_art =int(input("art marks : "))

total_score = score_in_english + score_in_math + score_in_science + score_in_art


#print(total_score)

average_score = total_score / 4

percentage_score = (total_score / 400) *100

print(f"student_name{student_name.upper()[:10]}\nTotal: {total_score} \nAverage: {average_score} \nPercentage: {percentage_score}")
