# Allowed adjacent levels
ADJACENT_LEVELS_ALLOWED = [1, 2, 3]

# Safe Reports Counter
safe_reports = 0

# Read input file
with open("red_nosed_reports_input.txt", "r") as unusual_data:
    for report in unusual_data:
        levels = [int(x.strip()) for x in report.split()]

        # Is the current level safe
        is_safe = True

        # Check if the current has to be increasing or decreasing
        if levels[0] < levels[1]:
            is_increasing = True
        elif levels[0] > levels[1]:
            is_increasing = False
        else:
            is_safe = False

        # Skip to next level if the level is unsafe
        if not is_safe:
            continue

        # Check if the levels are safe
        for i in range(1, len(levels)):
            if (levels[i - 1] < levels[i]) != is_increasing:
                is_safe = False
                break

            if not abs(levels[i - 1] - levels[i]) in ADJACENT_LEVELS_ALLOWED:
                is_safe = False
                break

        # Increase safe reports if the levels are safe
        if is_safe:
            safe_reports += 1

# Print the result
print(safe_reports)
