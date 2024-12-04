# Variable to hold every node and next tow possible locations
map_network = {}

# Reading the input data file
with open('haunted_wasteland_input.txt', 'r') as wasteland:
    # First line hold the directions
    directions = list(wasteland.readline().strip())

    # Second line is empty so we skip it
    empty_line = wasteland.readline()

    # The consecutive lines hold the nodes and the next possible locations
    for line in wasteland:
        # The line is split, the node is the key
        # The directions are saved as a tuple and are values of the key
        node, left_right = line.strip().split(" = ")
        left_right = left_right.strip('()').split(', ')

        map_network[node] = tuple(left_right)

# Starting location
location = "AAA"

# Step Counter
counter = 0

# Bool to signify the end of the wasteland
end_of_wasteland = False

# Iterating until the wasteland's end is reached
while not end_of_wasteland:
    # Iterating through every direction command
    for direction in directions:
        # If the current location is 'ZZZ' we have reached the
        # end of the wasteland and the cycles are broken
        if location == "ZZZ":
            end_of_wasteland = True
            break

        # Resetting the next location
        next_location = ""

        # The next location is determined based on the direction L or R
        if direction == "L":
            next_location = map_network[location][0]

        elif direction == "R":
            next_location = map_network[location][1]

        # Increasing the step counter by 1
        counter += 1

        # The current location is changed
        location = next_location

# The result is printed
print(counter)
