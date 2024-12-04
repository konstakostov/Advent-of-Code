# Variable for storing all owned scratchcards
scratchcards_pile = {}

# Current scratchcard ID
scratchcard_id = 1

# Opening file containing all scratchcards
with open('scratchcards_input.txt', 'r') as file:
    # Reading each scratchcard individually
    for cards in file:
        if scratchcard_id not in scratchcards_pile:
            scratchcards_pile[scratchcard_id] = 0

        scratchcards_pile[scratchcard_id] += 1

        cards_won = 0

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
            # If the current number is a winning number additional card is won
            if num in winning_numbers:
                cards_won += 1

        # Check to see if there are any winning cards
        if cards_won > 0:

            # Variables to store the range in which add copies of scratchcards
            start_range = scratchcard_id + 1
            end_range = scratchcard_id + cards_won + 1

            # Iterating though the elements in the dictionary in the specified range
            for i in range(start_range, end_range):
                # If the current scratchcard ID does not exist we create it and set value 0
                if i not in scratchcards_pile:
                    scratchcards_pile[i] = 0

                # Adding the required number of copies to the specified card
                scratchcards_pile[i] += scratchcards_pile[scratchcard_id]

        # Setting next scratchcard ID
        scratchcard_id += 1

# Variable to store the total scratchcards in the pile
total_scratchcards = 0

# Iterating through every item in the scratchcards pile
# to calculate the total amounts of cards in the pile
for key, value in scratchcards_pile.items():
    total_scratchcards += value

# Printing the total amount of scratchcards in the pile
print(total_scratchcards)
