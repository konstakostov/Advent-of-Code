# Input data
LEFT_LIST = []
RIGHT_LIST = []

# Read the input file
with open("tasks_input", "r") as file:
    for line in file:
        LEFT_LIST.append(int(line.split()[0].strip()))
        RIGHT_LIST.append(int(line.split()[1].strip()))

# Distances between numbers
distances = 0

# Calculate the distances
while len(LEFT_LIST) == len(RIGHT_LIST) > 0:
    left_num = min(LEFT_LIST)
    right_num = min(RIGHT_LIST)

    distances += abs(left_num - right_num)

    LEFT_LIST.remove(left_num)
    RIGHT_LIST.remove(right_num)

# Print the result
print(distances)

