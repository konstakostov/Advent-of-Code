import re

mul_sum = 0

# Read input file
data_text = open("mull_it_over_input.txt").read()

# Find all matches
matches = re.findall(r"mul\(\d+,\d+\)", data_text)

for match in matches:
    numbers = list(map(int, re.findall(r"(\d+)", match)))

    mul_sum += numbers[0] * numbers[1]

print(mul_sum)