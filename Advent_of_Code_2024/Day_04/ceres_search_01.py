# Matrix to store all elements
matrix = []

# Read input file
with open("ceres_search_input.txt", "r") as file:
    for file_line in file:
        elements = [str(el) for el in file_line.strip()]

        matrix.append(elements)

# Search directions
directions = [
    [-1, 0],    # Up
    [1, 0],     # Down
    [0, -1],    # Left
    [0, 1],     # Right
    [-1, -1],   # Up Left
    [-1, 1],    # Up Right
    [1, -1],    # Down Left
    [1, 1],     # Down Right
]

# Word to find
WORD = "XMAS"

# Found words
words_found_count = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current_element = matrix[row][col]

        # Check if the first letter matches
        if current_element == WORD[0]:
            for direction in directions:
                word = WORD[0]

                # Initialize search position
                new_row = row
                new_col = col

                # Traverse the word in the current direction
                for i in range(1, len(WORD)):
                    new_row += direction[0]
                    new_col += direction[1]

                    # Check boundaries and character match
                    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == WORD[i]:
                        word += matrix[new_row][new_col]
                    else:
                        break

                # If the word is found, count it
                if word == WORD:
                    words_found_count += 1

print(words_found_count)
