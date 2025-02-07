# Variable for storing the sum eligible game ID's
cubes_power_sum = 0

# Opening file with puzzle input
with open('cube_conundrum_input.txt', 'r') as file:
    # Looping through each line
    for line in file:
        eligible_game = True

        # Max of values of each cube
        # Each value is set to 1 so no error occurs
        # When the power is calculated
        max_red = 1
        max_green = 1
        max_blue = 1

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
            # If the current colour's max value is bigger the colour's max value is overwritten
            if line[i + 1].startswith("r"):
                if int(line[i]) > max_red:
                    max_red = int(line[i])

            elif line[i + 1].startswith("g"):
                if int(line[i]) > max_green:
                    max_green = int(line[i])

            elif line[i + 1].startswith("b"):
                if int(line[i]) > max_blue:
                    max_blue = int(line[i])

        # Here the value of the power of the cubes is found by multiplying each cube
        power_cubes = max_red * max_green * max_blue

        # The value of the power of the cube is added to the total power sum
        cubes_power_sum += power_cubes

# The 'cubes_power_sum' is printed to show the result
print(cubes_power_sum)
