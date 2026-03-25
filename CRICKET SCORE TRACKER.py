total_runs = 0
balls = 0
fours = 0
sixes = 0
wickets = 0

batsman_score={} #Dictionary to store batsman name and their runs

print("______Cricket Score Tracker______")
print("Enter the batsman name  for each ball")
print("Enter runs for each ball (0-6), Enter -1 if batsman gets out\n")
print("Type 'exit' after innings ends\n")
i=1
while True:
    batsman = input("Enter batsman name: ").upper()
    run = input(f"Enter runs for {i}th ball: ")
    i=i+1
    if run == "exit":
        break
    run = int(run)

    if run < -1 or run > 6:
        print("Invalid run! Enter between -1 and 6")
        continue

    if run ==-1:
        wickets +=1
    else:
        total_runs += run
        if batsman in batsman_score:
            batsman_score[batsman] += run
        else:
            batsman_score[batsman] = run
    balls += 1

    if run == 4:
        fours += 1
    elif run == 6:
        sixes += 1

overs = balls // 6
remaining_balls = balls % 6
strike_rate = (total_runs / balls) * 100

print("\n____Innings Summary___")
print(f"Total Runs scored by the team in {overs}.{remaining_balls} overs: {total_runs}/{wickets}")
print("Total Wickets Lost:", wickets)
print("Overs:", str(overs) + "." + str(remaining_balls))
print("Fours:", fours)
print("Sixes:", sixes)
print("Team Strike Rate:", round(strike_rate, 2))
print("\n____Batsman Scorecard____:")
for batsman, runs in batsman_score.items():
    print(f"{batsman}: {runs} runs")