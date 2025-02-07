# Opening file with puzzle input
with open('trebuchet_input.txt', 'r') as f:
    calibration_document = f.read().split('\n')

# The total sum of the calibration documents
calibration_values_sum = 0

# Iterating through every line in the document
for data in calibration_document:
    # Empty string is created to store the found calibration values
    calibration_value = ""
    # Empty list is created to store all found numbers in the documents
    found_numbers = []

    # Iterating through every character in the line
    for char in data:
        # If the character is a number us added to the 'found_numbers' list
        if char.isnumeric():
            found_numbers.append(char)

    # The first and last values in the 'found_numbers'
    # are used to create the 'calibration_value'
    calibration_value = found_numbers[0] + found_numbers[-1]

    # The 'calibration_value' is added to the 'calibration_values_sum'
    calibration_values_sum += int(calibration_value)

# The 'calibration_values_sum' is printed to show the result
print(calibration_values_sum)
