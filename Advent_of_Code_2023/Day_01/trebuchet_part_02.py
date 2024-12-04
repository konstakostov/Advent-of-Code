import re
#
# # Max length of the numbers 1-9, spelled
# max_length = 5

NUMBERS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open('trebuchet_input.txt', 'r') as file:
    document = file.read().split('\n')

# The total sum of the calibration documents
calibration_values_sum = 0

# Opening file with puzzle input
for line in document:
    # Empty string is created to store the found calibration values
    calibration_value = ""

    # Empty list is created to store all found numbers in the documents
    found_numbers = []

    # Empty dictionary to store the index of each found spelled number
    found_numbers_positions = {}

    # Iterating through the 'NUMBERS' dictionary to find matches in the current line
    for num in NUMBERS:
        # Checking for match for each 'num' in 'NUMBERS
        match = re.finditer(num, line)

        # If a match is found the starting index of the match will be stored
        # as integer in a list, corresponding the spelled number
        # in the 'found_numbers_positions' dictionary. If there is no match
        # the value will be empty
        found_numbers_positions[num] = [m.start() for m in match]

    # Iterating through the items in 'found_numbers_positions' dictionary
    for number, positions_list in found_numbers_positions.items():
        # Getting the corresponding digit
        num_value = str(NUMBERS.get(number))

        # If there were found matches we are going to iterate through
        # the list of their indexes
        if positions_list:
            for position in positions_list:
                # Replacing the first character of the found spelled number
                line = line[:position] + num_value + line[position + 1:]

    # Iterating through every character in the list
    for char in line:
        # If the current 'char is a digit it is added to the 'found_numbers' list
        if char.isdigit():
            found_numbers.append(char)

    # The first and last values in the 'found_numbers'
    # are used to create the 'calibration_value'
    calibration_value = found_numbers[0] + found_numbers[-1]

    # The 'calibration_value' is added to the 'calibration_values_sum'
    calibration_values_sum += int(calibration_value)

# The 'calibration_values_sum' is printed to show the result
print(calibration_values_sum)
