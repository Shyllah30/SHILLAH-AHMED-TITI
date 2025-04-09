# Aprogram to prepare tuition bill

student_name = input("Enter students name: ")

Social_security_no = int(input("Enter Social security No: "))

total_credits = int(input("Enter total credits: "))

if total_credits >= 10 :
    print(f"student is full-time\nflat rate = $1000")

else :
    tuition = total_credits * 100

    print(f"student is part-time\nTuition\t =\t{tuition}")


