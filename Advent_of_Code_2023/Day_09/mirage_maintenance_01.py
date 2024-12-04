# Variable to store every history log from the oasis
oasis = []

# Opening, reading and formatting the input file
with open('mirage_maintenance_input.txt', 'r') as oasis_data:
    for data in oasis_data:
        data = [int(h) for h in data.strip().split()]

        oasis.append([data])

# The sum of all extrapolated values
extrapolated_values_sum = 0

# Iterating through every history log from the oasis
for history in oasis:
    # Current row index
    current_row = 0
    # Next row index ('current_row' + 1)
    next_row = 1

    # Creating sequences for each history log
    while True:
        # Creating a blank list for the new sequence
        history.append(list())

        # Calculating the next sequence
        for i in range(0, len(history[current_row]) - 1):
            # The next number to be added to the new sequence
            # is created by subtracting the current element from the next element
            next_num = history[current_row][i + 1] - history[current_row][i]

            # Adding the new number to the new sequence
            history[next_row].append(next_num)

        # Checking if every element in the new sequence is 0
        # If they are the while cycle is broken
        if all(n == 0 for n in history[next_row]):
            break

        # Increasing the current and next rows index by 1
        current_row += 1
        next_row += 1

    # Iterating through every row in the history sequence in reverse (from last to first)
    for row in range(len(history) - 1, -1, -1):
        # If this is the last row to it is added a 0
        if row == len(history) - 1:
            history[row].append(0)

        # For other row the new element added to the end of each row is calculated
        else:
            # The new element is equal to the next row's last element +
            # the current row's last element
            new_element = history[row + 1][-1] + history[row][-1]
            history[row].append(new_element)

    # Adding the extrapolated value to 'extrapolated_values_sum'
    # The extrapolated value is the last value from the first row
    # of the current history sequence
    extrapolated_values_sum += (history[0][-1])

# Printing the result
print(extrapolated_values_sum)
