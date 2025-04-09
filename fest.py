games = ["Network","coding","repair","Quiz"]

groups = ["CYBER","SYNTAX","CODERS"]

group_scores =[]

for group in groups:
    games_score = []
    print(f"\n\t{group}")
    for game in games:
        score = int(input(f"\t\t{game} score: "))
        games_score.append(score)
    group_scores.append(games_score)
for group_score in group_scores:
    total = 0
    for score in group_score:
        total += score
print(f"total = {total}")
    



        

 