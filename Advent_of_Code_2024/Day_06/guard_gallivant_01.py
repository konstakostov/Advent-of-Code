# Initialize an empty matrix to store the grid
matrix = []

# Initialize a list to store the guard's coordinates
guard_coordinates = []

# Define the possible movement directions (Up, Right, Down, Left)
DIRECTIONS = [
    [-1, 0],    # Up
    [0, 1],     # Right
    [1, 0],     # Down
    [0, -1],    # Left
]

# Define the symbols corresponding to each direction
DIRECTIONS_SYMBOL = [
    "^",        # Up
    ">",        # Right
    "V",        # Down
    "<",        # Left
]

# Open the input file and read its contents
with open("guard_gallivant_input.txt", "r") as file:
    guard_symbol = "^"  # Symbol representing the guard
    line_index = 0  # Initialize line index

    # Read each line from the file
    for line in file:
        curr_line = []  # Initialize current line list

        # Process each character in the line
        for item in line.strip():
            curr_line.append(item)  # Add character to current line list

            # Check if the character is the guard symbol
            if guard_symbol in item:
                guard_coordinates = [line_index, line.index(item)]  # Store guard coordinates

        line_index += 1  # Increment line index

        matrix.append(curr_line)  # Add current line to the matrix

# Initialize unique guard positions counter
unique_guard_positions = 0

# Initialize direction index
direction_index = 0

# Start a loop to move the guard
while True:
    # Get the current direction's row and column changes
    row_direction = DIRECTIONS[direction_index][0]
    col_direction = DIRECTIONS[direction_index][1]

    # Get the current guard's row and column
    row = guard_coordinates[0]
    col = guard_coordinates[1]

    # Calculate the new position of the guard
    new_row = row + row_direction
    new_col = col + col_direction

    # Check if the new position is out of bounds
    if not (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0])):
        unique_guard_positions += 1

        break

    # Check if the new position is an obstacle
    if matrix[new_row][new_col] == "#":
        direction_index += 1
        # Reset direction index if it exceeds the number of directions

        if direction_index > 3:
            direction_index = 0

        continue

    # Check if the new position is an empty space
    if matrix[new_row][new_col] == ".":
        matrix[new_row][new_col] = DIRECTIONS_SYMBOL[direction_index]
        unique_guard_positions += 1
    else:
        # Mark the new position with the direction symbol
        matrix[new_row][new_col] = DIRECTIONS_SYMBOL[direction_index]

    # Mark the current position as visited
    matrix[row][col] = "X"
    # Update the guard's coordinates
    guard_coordinates = [new_row, new_col]

# Print the number of unique positions visited by the guard
print(unique_guard_positions)
