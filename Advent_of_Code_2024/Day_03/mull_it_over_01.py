import re

mul_sum = 0

# Read input file
with open("mull_it_over_input.txt", "r") as data:
    for memory in data:
        matches = re.findall(r"mul\(\d+,\d+\)", memory)

        for match in matches:
            numbers = list(map(int, re.findall(r"(\d+)", match)))

            mul_sum += numbers[0] * numbers[1]

print(mul_sum)