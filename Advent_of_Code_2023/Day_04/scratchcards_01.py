# Variable for storing the sum of all the scratchcards points
scratchcard_points_sum = 0

# Opening file containing all scratchcards
with open('scratchcards_input.txt', 'r') as file:
    # Reading each scratchcard individually
    for cards in file:
        points = 0

        # Removing '\n' from the end of each line
        cards = cards.strip()

        winning_numbers, random_numbers = cards.split(" | ")

        # Splitting the winning numbers on individual numbers
        winning_numbers = winning_numbers.split()

        # Removing "Card" string
        winning_numbers.pop(0)

        # Removing "Card ID" string
        winning_numbers.pop(0)

        # Splitting the random numbers on individual numbers
        random_numbers = random_numbers.split()

        # Iterating through every number in the 'random_numbers'
        for num in random_numbers:
            # If the current number is a winning number we calculate the points
            if num in winning_numbers:
                # If the current points are 0 we add 1 (+1) to them
                if points == 0:
                    points += 1
                # If the current points are above 0 we multiply them by 2 (*2)
                else:
                    points *= 2

        # Adding the total points for the current card to the total scratchcards points
        scratchcard_points_sum += points

# Printing the total scratchcards points
print(scratchcard_points_sum)
