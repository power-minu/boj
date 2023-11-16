totalscore = 0
totalgrade = 0

for i in range(0, 20, 1) :
    subject, score, grade = input().split()
    if grade == "A+" : totalgrade += 4.5*float(score)
    elif grade == "A0" : totalgrade += 4.0*float(score)
    elif grade == "B+" : totalgrade += 3.5*float(score)
    elif grade == "B0" : totalgrade += 3.0*float(score)
    elif grade == "C+" : totalgrade += 2.5*float(score)
    elif grade == "C0" : totalgrade += 2.0*float(score)
    elif grade == "D+" : totalgrade += 1.5*float(score)
    elif grade == "D0" : totalgrade += 1.0*float(score)

    if grade != "P" : totalscore += float(score)

print(totalgrade/totalscore)