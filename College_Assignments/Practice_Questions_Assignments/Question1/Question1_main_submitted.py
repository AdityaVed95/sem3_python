players_and_scores = {}

# for key in players_and_scores:
#     if players_and_scores[key] == lowest:
#         print(key)

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

max_name = []  # people who scored the maximum score
min_name = []  # # people who scored the minimum score

for key in players_and_scores:
    maximum_score = players_and_scores[key]
    minimum_score = players_and_scores[key]

for key in players_and_scores:

    if players_and_scores[key] > maximum_score:
        maximum_score = players_and_scores[key]

    if players_and_scores[key] < minimum_score:
        minimum_score = players_and_scores[key]

for key in players_and_scores:
    if players_and_scores[key] == maximum_score:
        max_name.append(key)
    if players_and_scores[key] == minimum_score:
        min_name.append(key)

print("Maximum score found is : ", maximum_score)
print("Maximum score is achieved by: ", max_name)

print("Minimum score found is : ", minimum_score)
print("Minimum score is achieved by: ", min_name)
