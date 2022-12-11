with open("data.txt", "r") as i:
    lines = i.read().split("\n")


def round_score(game: tuple[str, str]) -> int:
    # What i played
    my_play = game[1]
    
    if game in (("A", "X"), ("B", "Y"), ("C", "Z")):
        outcome = "draw"
    elif game in (('A', 'Y'), ('B', 'Z'), ('C', 'X')):
        outcome = "win"
    else:
        outcome = "loss"
    
    # Summarize points
    points_for_item = dictionary_points_for_item[my_play]
    points_for_outcome = dictionary_points_for_outcome[outcome]
    return(points_for_item + points_for_outcome)


def second_round_score(game: tuple[str, str]) -> int:
    # Translate score
    translation_for_outcomes = {"X": "loss", "Y": "draw", "Z": "win"}
    outcome = translation_for_outcomes[game[1]]

    if outcome == "draw":
        my_play = game[0]
    elif outcome == "loss":
        # Get the index of the elf play in list_of_plays and move one to the left
            my_play = list_of_plays[list_of_plays.index(game[0]) - 1]
    elif outcome == "win":
        # Get the index of the elf play in list_of_plays and move one to the right
        try:
            my_play = list_of_plays[list_of_plays.index(game[0]) + 1]
        except IndexError:
            my_play = list_of_plays[0]

    # Translate play
    translation_for_plays = {"A": "X", "B": "Y", "C": "Z"}
    my_play = translation_for_plays[my_play]

    # Summarize points
    points_for_item = dictionary_points_for_item[my_play]
    points_for_outcome = dictionary_points_for_outcome[outcome]
    return(points_for_item + points_for_outcome)

# Dictionaries and lists
dictionary_points_for_item = {"X": 1, "Y": 2, "Z": 3}
dictionary_points_for_outcome = {"loss": 0, "draw": 3, "win": 6}
list_of_plays = ["A", "B", "C"]


# Assign game points to 0
game_points = 0

# First round
for line in lines:
    line = tuple(line.split(' '))
    game_points += round_score(line)
    
<<<<<<< HEAD
print(f"First game points {game_points}")

# Reset game points
game_points = 0

# Second round
for line in lines:
    line = tuple(line.split(' '))
    game_points += second_round_score(line)


print(f"Second game points {game_points}")
=======
print(game_points)

# Add 3rd element to line un 
>>>>>>> b906e7c (test)
