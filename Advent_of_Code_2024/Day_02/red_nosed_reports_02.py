# Allowed adjacent levels
ADJACENT_LEVELS_ALLOWED = [1, 2, 3]

# Safe Reports Counter
safe_reports = 0

# Read input file
with open("test_input.txt", "r") as unusual_data:
    for report in unusual_data:
        levels = [int(x.strip()) for x in report.split()]

        # Tolerance
        tolerance = 0

        is_increasing = False
        is_decreasing = False

        valid_levels = levels.copy()

        # Check if the levels are safe
        for i in range(len(levels) - 1):
            difference = levels[i] - levels[i + 1]

            if difference < 0:
                is_increasing = True
            if difference > 0:
                is_decreasing = True

            if not (abs(difference) in ADJACENT_LEVELS_ALLOWED) or (is_increasing and is_decreasing) or (difference == 0):
                tolerance += 1

                continue
            else:
                valid_levels.append(levels[i])

            if tolerance >= 1:
                break


            i += 1

            if i == len(levels) - 1:
                valid_levels.append(levels[i])

        if tolerance <= 1 and len(valid_levels) == len(levels):
            print(levels)
            safe_reports += 1

# Print the result
print(safe_reports)
