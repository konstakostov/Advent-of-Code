import re

mul_sum = 0

# Read input file
data_text = open("mull_it_over_input.txt").read()

# Find all matches
matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data_text)

# Is the current mul to be read
enable_mul = True

for match in matches:
    if match == "do()":
        enable_mul = True
        continue
    if match == "don't()":
        enable_mul = False
        continue

    if not enable_mul:
        continue

    numbers = list(map(int, re.findall(r"(\d+)", match)))
    mul_sum += numbers[0] * numbers[1]

print(mul_sum)
