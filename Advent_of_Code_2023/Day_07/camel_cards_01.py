# Every card value
CARDS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

# Every type of hand and the hands that belong to it
HANDS = {
    'High Card': [],
    'One Pair': [],
    'Two Pair': [],
    'Three of a Kind': [],
    'Full House': [],
    'Four of a Kind': [],
    'Five of a Kind': [],
}


# Function to determine the type of the current hand
# by its length and length of each card type in the hand
# Every hand length is 5 characters
def find_type_of_hand(hand_length, current_hand_data):
    type_of_hand = ''

    # One type of cards in the hand
    if hand_length == 1:
        type_of_hand = 'Five of a Kind'

    # Two types of cards in the hand
    elif hand_length == 2:
        if 4 in current_hand_data.values():
            type_of_hand = 'Four of a Kind'
        elif 3 in current_hand_data.values():
            type_of_hand = 'Full House'

    # Three types of cards in the hand
    elif hand_length == 3:
        if 3 in current_hand_data.values():
            type_of_hand = 'Three of a Kind'
        elif 2 in current_hand_data.values():
            type_of_hand = 'Two Pair'

    # Fur types of cards in the hand
    elif hand_length == 4:
        type_of_hand = 'One Pair'

    # Five types of cards in the hand
    elif hand_length == 5:
        type_of_hand = 'High Card'

    # Returns as string the type of card
    return type_of_hand


# Reading the input data file
with open('camel_cards_input.txt', 'r') as hands_list:
    # Reading the input file line by line
    for line in hands_list:
        # First part of the line is the current hand
        # Second part of the line is bid for it
        hand, bid = line.strip().split()

        # Variable to hold the different types of cards in the current hand
        current_hand = {}

        # Iterating through every card in the current hand
        for card in hand:
            # Adding the current card to the 'current_hand'
            # and how many times it repeats in it
            if card not in current_hand:
                current_hand[card] = 0

            current_hand[card] += 1

        # Finding the current hand type based on its length
        # and how many a card type repeats in the same hands
        hand_type = find_type_of_hand(len(current_hand), current_hand)

        # Adding the current card to the correct hand type it belongs to
        # as tuple with its bid
        HANDS[hand_type].append((hand, bid))

# Variable to keep the total winnings for every hand
total_winnings = 0

# The current rank counter
rank = 1


# Function to sort the all the hands in every hand type
# Each hand is represented by a string and each string is converted
# into the corresponding int values from 'CARDS' dictionary.
# After that all hands are sorted in ASC order based on
# their int values (their converted values)
def sort_hand_data(hands):
    return sorted(hands, key=lambda hand_list: [CARDS[c] for c in hand_list[0]])


# Iterating through the keys, values of the 'HANDS dictionary
for hand_, hand_data in HANDS.items():
    # Variable to keep the current hand  type winnings
    current_hand_winnings = 0

    # Sorting the current hand type's hands
    hand_data_sorted = sort_hand_data(hand_data)

    # Iterating through all the sorted hands
    for h in hand_data_sorted:
        # Calculating the current hand winnings
        current_hand_winnings += int(h[-1]) * rank

        # Increasing the rank counter by 1
        rank += 1

    # Adding the current hand type winnings to 'total_winnings'
    total_winnings += current_hand_winnings

# Printing the total winnings
print(total_winnings)
