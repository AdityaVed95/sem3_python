def match(d):
    players_and_scores = d
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


def main():
    players = {}

    while True:
        print("Enter 1 to make a player and 2 to exit making players in the dictionary")
        response = int(input())

        if response == 2:
            break

        if response == 1:
            print("Enter the name of the player: ")
            name = input()
            print("Enter the score of the player: ")
            score = int(input())

            players.update({name: score})

    match(players)


if __name__ == "__main__":
    main()
