# NB! This task was completed by looking for hints in the AoC Reddit
#  Most of the participants mentioned LCM (Least Common Multiple) and how it worked
#  After a quick research I tried to apply this method to this task.
#  The original solution was pure brute-force and it took way too much time
#  and it was anything but practical.


import math


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

# Variable to hold all nodes, whose key ends with 'A'
location = []

# Iterating through all the nodes to find every node ending with 'A'
for node, paths in map_network.items():
    if node[-1] == "A":
        location.append(node)

# Step Counter
counter_list = []

# Iterating through every node, whose key starts with 'A'
for start_location in location:
    current_location = [start_location]

    # Counter for steps taken from current starting location
    counter = 0

    # Bool to signify the end of the wasteland
    end_of_wasteland = False

    # Index to show current direction from the 'directions' list
    index = 0

    # Iterating until the wasteland's end is reached
    while not end_of_wasteland:
        # Variable to store the next location
        next_location_list = []

        # Depending on the location we either take a step to the left or to the right
        # Because 'current_location' is one-element list, the [0] element is taken as a string
        if directions[index] == "L":
            next_location_list.append(map_network[current_location[0]][0])
        elif directions[index] == "R":
            next_location_list.append(map_network[current_location[0]][1])

        # Increasing the step counter by 1
        counter += 1

        # Checking if all elements in the 'next_location_list' list finish with char 'Z'
        # If they do -> 'end_of_wasteland' is set as True and the cycle is broken
        if all(i[-1] == "Z" for i in next_location_list):
            end_of_wasteland = True
            break

        # Direction index is increased by 1
        index += 1

        # If the direction index is >= than the length of the 'directions' list
        # The index is reset to 0
        if index >= len(directions):
            index = 0

        # Current location takes the value of the next_location
        current_location = next_location_list

    # The current steps counter is added to a list
    counter_list.append(counter)

# All values from the 'counter_list' are used to find the
# LCM (Least Common Multiple), using the function math.lcm()
# Doing this allows for much faster run time and not brute-forcing
# the task's solution
lcm_counter_list = math.lcm(*counter_list)

# The result is printed
print(lcm_counter_list)
