players_and_scores = {}

while True:
    print("Enter 1 to add a new player and his score in the match")
    print("Enter 2 to exit entering players and scores")

    response = int(input())

    if response == 1:
        print("Enter the name of the player")
        name = input()
        print("Enter the score of the player")
        score = int(input())
        players_and_scores[name] = score

    else:
        break

max_name = ""
min_name = ""

for key in players_and_scores:
    minimum = players_and_scores[key]
    maximum = players_and_scores[key]

for key in players_and_scores:

    if players_and_scores[key] > maximum:
        maximum = players_and_scores[key]
        max_name = key

    if players_and_scores[key] < minimum:
        minimum = players_and_scores[key]
        min_name = key

print("The person to score maximum is: {} and his score is: {}".format(max_name, maximum))
print("The person to score minimum is: {} and his score is: {}".format(min_name, minimum))
