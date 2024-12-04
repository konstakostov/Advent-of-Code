# Variable for storing the sum eligible game ID's
valid_games_sum = 0

# Variable for storing current game ID
game_id = 1

# Opening file with puzzle input
with open('cube_conundrum_input.txt', 'r') as file:
    # Looping through each line
    for line in file:
        eligible_game = True

        # Removing '\n' from the end of each line
        line = line.strip()

        # Splitting the line on multiple strings when ' ' occurs
        line = line.split(' ')

        # Removing "Game" string
        line.pop(0)

        # Removing "Game ID" string
        line.pop(0)

        # Iterating though every even value, which is a number
        for i in range(0, len(line), 2):
            # Every odd value of the line represents colour
            # If the color starts with 'r' is red, 'g' is green and 'b' is blue
            # If the current colour's value is bigger than the specified the game
            # is not eligible, the 'eligible_game' is set to True and the cycle is broken
            if line[i + 1].startswith("r") and int(line[i]) > 12:
                eligible_game = False
                break
            elif line[i + 1].startswith("g") and int(line[i]) > 13:
                eligible_game = False
                break
            elif line[i + 1].startswith("b") and int(line[i]) > 14:
                eligible_game = False
                break

        # If the game is eligible the 'game_id' is added to the 'valid_games_sum'
        if eligible_game:
            valid_games_sum += game_id

        # The game ID is increased by on to keep track of the current game
        game_id += 1

# The 'valid_games_sum' is printed to show the result
print(valid_games_sum)
