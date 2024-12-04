# Input data
LEFT_LIST = []
RIGHT_LIST = []

# Read the input file
with open("tasks_input", "r") as file:
    for line in file:
        LEFT_LIST.append(int(line.split()[0].strip()))
        RIGHT_LIST.append(int(line.split()[1].strip()))

# Similarity score
similarity_score = 0

# Calculate the similarity score
for i in range(len(LEFT_LIST)):
    num_to_search = LEFT_LIST[i]
    current_similarity = RIGHT_LIST.count(num_to_search)

    similarity_score += num_to_search * current_similarity

# Print the result
print(similarity_score)
