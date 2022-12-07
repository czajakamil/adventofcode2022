with open("day2\data.txt", "r") as i:
    lines = [line.rstrip('\n') for line in i]

dictionary_points_for_item = {"X": 1, "Y": 2, "Z": 3}
disctionary_points_for_score = {"loss": 0, "draw": 3, "win": 6}

def round_score(game: tuple[str, str]) -> int:
    # Co zagrałem
    my_play = game[2]
    
    if game in (("A", "X"), ("B", "Y"), ("C", "Z")):
        outcome = "draw"
    elif game in (("A", "Y"), ("B", "Z"), ("C", "X")):
        outcome = "win"
    else:
        outcome = "loss"

    points_for_item = dictionary_points_for_item[my_play]
    points_for_outcome = disctionary_points_for_score[outcome]
    points_for_game = points_for_item + points_for_outcome
    return(points_for_game)

game_points = 0

for line in lines:
    line.replace('\n', '')
    game_points = game_points + round_score(line)
    

print(game_points)