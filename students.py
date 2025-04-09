scores = []
total = 0
def add_score(score):
    if score > 0 :
        scores.append(score)
    else:
        print("Score should be Above Zero(0)")

    return None

def list_scores(scores):
    for score in scores:
        print(score)
    return None

def compute_total(scores):
    total = 0
    for score in scores:
        total += score
    print (f"total = {total}")
    
    return total

def get_maximum(scores):
    maximum = 0
    for score in scores:
        if score > maximum :
            maximum = score
    print(maximum)
    return maximum

while True:
    score = input("Enter score or Q to Quit: ")

    if score.upper()== "Q":
        break

    add_score(int(score))

list_scores (scores)
compute_total(scores)
get_maximum(scores)