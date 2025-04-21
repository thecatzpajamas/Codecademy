# Scrabble letters and their associated values
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letters_to_points = {key:value for key, value in zip(letters, points)}

# Game scores to calculate
player_to_words = {}
player_to_points = {}
turns_per_round = 0

# Turn tracker
while True:
    turns_per_round = input("Please enter the number of players:  ")
    try:
        turns_per_round = int(turns_per_round)
        turns_per_round -= 1
        break
    except ValueError:
        print("Please use an integer instead")

# Get player names
player_count = 0
while True:
    if player_count <= turns_per_round:
        name = input("Enter Player Name:  ")
        player_to_words[name] = []
        player_count += 1
    else:
        break

# Calculate word value and correct for letter case
def score_word(word):
    points = 0
    for letter in word:
        letter = str.upper(letter)
        points += letters_to_points.get(letter, 0)
    return points


# Playing the game
current_turn = 0
current_round = 0
while True:
    if current_turn <= turns_per_round:

        while True:
            player = input("Whose turn is it?  ")

            if player in list(player_to_words) and current_turn <= turns_per_round:
                word = input("What word did they play?  ")
                player_to_words[player].append(word)
                break
            elif player not in list(player_to_words):
                print("Hmm, I don't recognize that name. Did you mean to say one of these:  ")
                print(list(player_to_words))

        # Calculate each player's total score
        for player, words in player_to_words.items():
          player_points = 0
          for word in words:
            player_points += score_word(word)
          player_to_points[player] = player_points

        # Increment turn
        current_turn += 1
    else:
        still_playing = input("Play another round? (y/n):  ")
        if still_playing == "y":
            current_turn = 0
            current_round += 1
            pass
        if still_playing == "n":
            break
        elif still_playing != "y" and still_playing != "n":
            print("Sorry, please answer with either y or n.")

# Print game results
for player in player_to_words:
    print(player + " played these words:  " + str(player_to_words[player]) + " for a total of " + str(player_to_points[player]) + " points!")
