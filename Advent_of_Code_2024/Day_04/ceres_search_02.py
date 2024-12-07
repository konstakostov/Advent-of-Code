def search_diagonals(matrix_, diagonals, r, c):
    # Initialize an empty string to store the found word
    word = ""

    # Iterate through each diagonal direction
    for diagonal in diagonals:
        new_row = r
        new_col = c

        # Move to the new position based on the current diagonal direction
        new_row += diagonal[0]
        new_col += diagonal[1]

        # Check if the new position is within the matrix boundaries
        if 0 <= new_row < len(matrix_) and 0 <= new_col < len(matrix_[0]):
            char = matrix_[new_row][new_col]

            # Check if the character matches the first or last letter of the word
            if char == WORD[0] or char == WORD[-1]:
                word += char

    # If two characters are found, construct the word by inserting the middle character
    if len(word) == 2:
        word = word[0] + WORD[1] + word[1]

    # Check if the constructed word matches the target word or its reverse
    if word == WORD or word == WORD[::-1]:
        return word

    # Return an empty string if the word is not found
    return ""


# Matrix to store all elements
matrix = []

# CONSTANTS
# Search directions
FIRST_DIAGONAL = [
    [-1, -1],   # Up Left
    [1, 1],     # Down Right
]
SECOND_DIAGONAL = [
    [-1, 1],    # Up Right
    [1, -1],    # Down Left
]
# Word to find
WORD = "MAS"


# Read input file
with open("ceres_search_input.txt", "r") as file:
    for file_line in file:
        elements = [str(el) for el in file_line.strip()]

        matrix.append(elements)


# Found words counter
words_found_count = 0


# Iterate through each row in the matrix
for row in range(len(matrix)):
    # Iterate through each column in the current row
    for col in range(len(matrix[row])):
        current_element = matrix[row][col]

        # Check if the current element matches the second letter of the word
        if current_element == WORD[1]:
            # Search for the word in the first set of diagonal directions
            first_word = search_diagonals(matrix, FIRST_DIAGONAL, row, col)
            # Search for the word in the second set of diagonal directions
            second_word = search_diagonals(matrix, SECOND_DIAGONAL, row, col)

            # If the word is found in both diagonal searches, increment the counter
            if first_word and second_word:
                words_found_count += 1

# Print the total count of found words
print(words_found_count)
