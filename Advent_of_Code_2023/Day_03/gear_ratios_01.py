# All possible directions to search for adjacent numbers
DIRECTIONS = [
    (-1, 0),    # Up
    (1, 0),     # Down
    (0, -1),    # Left
    (0, 1),     # Right
    (-1, -1),   # Up-Left
    (-1, 1),    # Up-Right
    (1, -1),    # Down-Left
    (1, 1),     # Down-Right
]

# Opening the input data file and creating a matrix with its data
with open('gear_ratios_input.txt', 'r') as file:
    engine = file.read().split('\n')
    engine = [list(block) for block in engine]

# Determining the length of the matrix, by getting the length of the first row
SIZE = len(engine[0])

# Bool to store if a digit is part of the last found number
valid_number = False
# Variable to store if the current column is still part of the last found number
next_col = None

# Variable to store the sum of all the adjacent numbers in the engine
engine_numbers_sum = 0

# Iterating through every row of the matrix
for row in range(len(engine)):
    # When the next row comes the Variable 'next_col' is reset
    next_col = None

    # Iterating through every column of the current row
    for col in range(len(engine[row])):
        # Checking if the current element is digit
        if engine[row][col].isdigit():
            # If the current element is digit and part of the last found number
            # we skip it and go the next element in the matrix (next column)
            if valid_number:
                continue

        # If the current element is not part of the last found number
        # the bool 'valid_number' is reset
        valid_number = False

        # Checking if the current element is digit
        # If the current element is NOT digit we skip to the next element
        if engine[row][col].isdigit():
            # Variables to start first and last digit of a found number
            first_col = col
            last_col = col

            # Bool to store if last column of number is found
            last_col_found = False

            # While 'last_col_found is not found and the 'last_col' is in the matrix
            # the 'last_col' is increased by 1
            # If the 'last_col' is not a digit, it's value is decreased by 1
            # and this is last digit of the current number
            while not last_col_found and last_col + 1 < SIZE:
                last_col += 1
                current = engine[row][last_col]
                if not current.isdigit():
                    last_col -= 1
                    last_col_found = True
                    break

            # Iterating through every direction in 'DIRECTIONS'
            for direction in DIRECTIONS:
                # Variables to hold the position of the first row and first column
                first_digit_row = row + direction[0]
                first_digit_col = first_col + direction[1]

                # Variables to hold the position of the last row and last column
                last_digit_row = row + direction[0]
                last_digit_col = last_col + direction[1]

                # Checking if the first row and first digit are in the range of the matrix
                if 0 <= first_digit_row < SIZE and 0 <= first_digit_col < SIZE:
                    # Getting the current element value
                    current_block = engine[first_digit_row][first_digit_col]

                    # Checking if the current element is not '.' and is not digit
                    if current_block != '.' and not current_block.isnumeric():
                        # If it is true a valid number is found and 'valid_number'
                        # is set to True before breaking
                        valid_number = True
                        break

                # Checking if the last row and last digit are in the range of the matrix
                if 0 <= last_digit_row < SIZE and 0 <= last_digit_col < SIZE:
                    # Getting the current element value
                    current_block = engine[last_digit_row][last_digit_col]

                    # Checking if the current element is not '.' and is not digit
                    if current_block != '.' and not current_block.isnumeric():
                        # If it is true a valid number is found and 'valid_number'
                        # is set to True before breaking
                        valid_number = True
                        break

            # Checking if there is a valid number
            if valid_number:
                # Variable to hold the numbers if there is valid numbers
                valid_num = ''

                # Iterating through the valid number
                for i in range(first_col, last_col + 1):
                    # Adding every digit of the number to 'valid_num'
                    valid_num += engine[row][i]

                # Adding the valid number to the sum of all the adjacent numbers in the engine
                engine_numbers_sum += int(valid_num)

                # Setting 'next_col' value as the value of last digit in the found valid number
                next_col = last_col

# Printing the final result
print(engine_numbers_sum)

