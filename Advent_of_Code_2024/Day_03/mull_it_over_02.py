import re
from gc import enable

mul_sum = 0

# Read input file
with open("mull_it_over_input.txt", "r") as data:
    for memory in data:
        matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory)
        # print(matches)

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

            # if match.startswith("mul"):
            numbers = list(map(int, re.findall(r"(\d+)", match)))
            mul_sum += numbers[0] * numbers[1]

print(mul_sum)