questions =[
    "which year Prakash Kakad is bron?","2013","2023","1900","2003",4
],
["which year Prakash Kakad is bron?","2013","2023","1900","2003",4],
["which year Prakash Kakad is bron?","2013","2023","1900","2003",4],
["which year Prakash Kakad is bron?","2013","2023","1900","2003",4],
["which year Prakash Kakad is bron?","2013","2023","1900","2003",4],
["which year Prakash Kakad is bron?","2013","2023","1900","2003",4],


levels = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

for i in range(0,len(questions)):
    question = questions[i]
    print(f" Question for Rupees. {levels[i]}")
    print(f"a.{question[1]}               b.{question[2]}")
    print(f"c.{question[3]}               d.{question[4]}")
    reply = int(input("Enter your Answer (1-4) " ))
    if (reply == question[-1]):
        print(f"Correct answer ,you have won {levels[i]}")
        if (i ==4):
            money = 50000
        elif (i ==9):
            money = 100000
    else:
        print("Worng Answer!")
        break