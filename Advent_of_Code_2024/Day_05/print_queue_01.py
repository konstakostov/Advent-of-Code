def check_page_order(curr_page, pages_data, rule_type):
    # Initialize rules to None
    rules = None

    # Determine the rule type and set the appropriate rules
    if rule_type == "before":
        rules = number_after_rules
    elif rule_type == "after":
        rules = number_before_rules

    # If the current page is not in the rules, return False
    if not curr_page in rules:
        return False

    # Check if all data in pages_data follow the rules for the current page
    for data in pages_data:
        if not data in rules[curr_page]:
            return False

    return True

# Initialize pages list and middle_pages_sum
pages = []
middle_pages_sum = 0

# Initialize dictionaries to store before and after rules
number_before_rules = {}
number_after_rules = {}

# Read the input file and populate the rules and pages
with open("print_queue_input.txt", "r") as file:
    for line in file:
        if "|" in line:
            # Split the line into before and after numbers
            before_num, after_num = list((map(int, line.strip().split("|"))))

            # Update number_before_rules dictionary
            if before_num not in number_before_rules:
                number_before_rules[before_num] = []
            if after_num not in number_before_rules[before_num]:
                number_before_rules[before_num].append(after_num)

            # Update number_after_rules dictionary
            if after_num not in number_after_rules:
                number_after_rules[after_num] = []
            if before_num not in number_after_rules[after_num]:
                number_after_rules[after_num].append(before_num)

        if "," in line:
            # Split the line into a list of page numbers and add to pages
            line_update = list((map(int, line.strip().split(","))))
            pages.append(line_update)

# Process each page in pages
for page in pages:
    before_pages = []
    after_pages = []
    correct_order = True

    # Check the order of each page
    for i in range(len(page)):
        if i - 1 >= 0:
            before_pages = page[:i]
        if i + 1 >= len(page):
            after_pages = page[i + 1:]

        current_page = page[i]

        # Check the order of pages before and after the current page
        if not before_pages and after_pages:
            after_page_status = check_page_order(current_page, after_pages, "after")
            if not after_page_status:
                correct_order = False
                break
        elif before_pages and not after_pages:
            before_page_status = check_page_order(current_page, before_pages, "before")
            if not before_page_status:
                correct_order = False
                break
        else:
            after_page_status = check_page_order(current_page, after_pages, "after")
            before_page_status = check_page_order(current_page, before_pages, "before")
            if not after_page_status or not before_page_status:
                correct_order = False
                break

    # If the order is correct, add the middle page to the sum
    if correct_order:
        middle_index = len(page) // 2
        middle_page = page[middle_index]
        middle_pages_sum += middle_page

# Print the sum of the middle pages
print(middle_pages_sum)