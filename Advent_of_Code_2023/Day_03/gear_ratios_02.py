# All possible directions to search for adjacent numbers
DIRECTIONS = [
    (-1, 0),  # Up
    (1, 0),  # Down
    (0, -1),  # Left
    (0, 1),  # Right
    (-1, -1),  # Up-Left
    (-1, 1),  # Up-Right
    (1, -1),  # Down-Left
    (1, 1),  # Down-Right
]

# Iterating to the left [0] or right [1] on the row
LEFT_RIGHT = (-1, 1)

# Opening the input data file and creating a matrix with its data
with open('gear_ratios_input.txt', 'r') as file:
    engine = file.read().split('\n')
    engine = [list(block) for block in engine]

# Determining the length of the matrix, by getting the length of the first row
ROW_LENGTH = len(engine[0])
COL_LENGTH = len(engine)

# Variable to store the sum of all the found gear ratios
gear_ratios_sum = 0

# Variable to store the coordinates of all the numbers
# used to form a gear (2 adjacent numbers to '*' symbol)
gear_numbers_coordinates = []

# Variables to store the first and second number values as string
first_num_value = ''
second_num_value = ''

for row in range(len(engine)):
    for col in range(len(engine[row])):
        # Variable to store the current element's coordinates
        coordinates = [row, col]

        # List to store found numbers, next to gears
        found_numbers = []

        # List to store found numbers coordinates
        found_numbers_coordinates = []

        # Checking if current element coordinates
        # are already in 'gear_numbers'
        if [row, col] in gear_numbers_coordinates:
            continue

        # Checking if current element is possible gear
        if engine[row][col] == "*":
            for direction in DIRECTIONS:
                # Variables to store coordinates of element after it moved
                new_row = row + direction[0]
                new_col = col + direction[1]

                # Checking if 'element' is in the range of matrix
                if 0 <= new_row < ROW_LENGTH and 0 <= new_col < COL_LENGTH:
                    # Location of the element after movement
                    element = engine[new_row][new_col]
                else:
                    continue

                # Checking if 'element' is in the range of matrix and
                # it's coordinates are not already part of existing gear
                if element.isdigit() and [new_row, new_col] not in found_numbers_coordinates:
                    # Storing the found number digits
                    found_num_as_list = [element]

                    # Variable to store all the columns the current number is
                    columns_range = [new_col]

                    # Variables to store the start/left and end/right of a number
                    col_left = new_col
                    col_right = new_col

                    # Iterating to the left of the row
                    for i in range(col_left, -1, -1):
                        # The next element to the left to the last checked column
                        col_left += LEFT_RIGHT[0]

                        # If the current column is out of range the cycle is broken
                        # or the current column is not digit the cycle is broken
                        if col_left < 0 or not engine[new_row][col_left].isdigit():
                            break

                        # The found number is inserted to the beginning of the list
                        # That is storing all the digits of the current number
                        found_num_as_list.insert(0, engine[new_row][col_left])

                        # The found columns are added to the beginning of the list,
                        # storing all the columns in which the number takes
                        columns_range.insert(0, col_left)

                    # Iterating to the right of the row
                    for i in range(col_right, ROW_LENGTH):
                        # The next element to the right to the last checked column
                        col_right += LEFT_RIGHT[1]

                        # If the current column is out of range the cycle is broken
                        # or the current column is not digit the cycle is broken
                        if col_right >= ROW_LENGTH or not engine[new_row][col_right].isdigit():
                            break

                        found_num_as_list.append(engine[new_row][col_right])
                        columns_range.append(col_right)

                    # The found number is turned into a string
                    found_num = ''.join(found_num_as_list)

                    # The found number is added to the 'found_numbers' list
                    found_numbers.append(int(found_num))

                    # Adding all found number coordinates to the 'found_numbers_coordinates' list
                    for c in columns_range:
                        found_numbers_coordinates.append([new_row, int(c)])

                    # Checking if the 'found_numbers' list has 2 found numbers
                    if len(found_numbers) == 2:
                        # Calculating the gear ration
                        gear_ratio = found_numbers[0] * found_numbers[1]

                        # Adding the gear ratio to the total 'gear_ratios_sum'
                        gear_ratios_sum += gear_ratio

                        # Adding all found legible number coordinates to the 'gear_numbers_coordinates' list
                        gear_numbers_coordinates.append(c for c in found_numbers_coordinates)

                        break

# Printing the final result
print(gear_ratios_sum)
