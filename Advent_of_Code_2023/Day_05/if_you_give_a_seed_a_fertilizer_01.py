# Variable to save all the values from seed to location
seeds_data = []
# Variable to save the current map information
current_map = []

# Index of the current seed
index = 0

# Opening file containing all maps in the almanac
with open('if_you_give_a_seed_a_fertilizer.txt', "r") as almanac:
    # Getting all the seeds from the first row
    seeds = almanac.readline().strip().split()

    # Checking if the current element is a seed (is variable)
    # and adding it to 'seeds_data' list
    for seed in seeds:
        if seed.isnumeric():
            seeds_data.append([int(seed)])

    # Reading the second line which is always empty
    first_empty_page = almanac.readline()

    # Reading all the remaining pages of the almanac
    for page in almanac:
        # Removing '\n' from the end of each line and splitting the line into elements
        page = page.strip().split()

        # If the current page is blank that means that all
        # the needed data from the current map has been extracted
        if not page:
            # Looking through each seed and its data from the 'seeds_data' list
            for data in seeds_data:
                # Taking the current seed, and it's last found map value
                current = data[-1]

                # Variable to store the next destination value
                destination = None

                # Iterating through the available data from the current map
                for item in current_map:
                    # The first element is the destination start range
                    destination_start = int(item[0])

                    # The second element is the source start range
                    source_start = int(item[1])

                    # The third element is the source length,
                    # So we get the source end range by adding it to the source start range
                    source_end = int(item[1]) + int(item[2])

                    # Checking if the current element is in the source range
                    # If the current element is in the source range
                    # the destination value can be calculated
                    # The destination value can be found by:
                    # 1. Subtracting the current element value from the source start range
                    # 2. To the result of the subtraction the destination start range is added
                    if source_start <= current < source_end:
                        destination = (current - source_start) + destination_start

                # If the current element is not in the source range
                # The 'destination' variable stays None
                # So the destination value is equal to the current value
                if not destination:
                    destination = current

                # The found value is appended to the current seed data
                seeds_data[index].append(destination)

                # The index is increased by 1
                index += 1

            # Resetting 'current_map' list
            current_map = []

            # Resetting 'index' variable
            index = 0

            continue

        # If the first element of the current page is not number
        # this signifies the start of a new map
        if not page[0].isnumeric():
            continue

        # If the current page is with numbers (data)
        # The data is added to the 'current_map' list
        current_map.append(page)

    # Iterating through the final available data from the current map
    for data in seeds_data:
        # Taking the current seed, and it's last found map value
        current = data[-1]

        # Variable to store the next destination value
        destination = None

        # Iterating through the available data from the current map
        for item in current_map:
            # The first element is the destination start range
            destination_start = int(item[0])

            # The second element is the source start range
            source_start = int(item[1])

            # The third element is the source length,
            # So we get the source end range by adding it to the source start range
            source_end = int(item[1]) + int(item[2])

            # Checking if the current element is in the source range
            # If the current element is in the source range
            # the destination value can be calculated
            # The destination value can be found by:
            # 1. Subtracting the current element value from the source start range
            # 2. To the result of the subtraction the destination start range is added
            if source_start <= current < source_end:
                destination = (current - source_start) + destination_start

        # If the current element is not in the source range
        # The 'destination' variable stays None
        # So the destination value is equal to the current value
        if not destination:
            destination = current

        # The found value is appended to the current seed data
        seeds_data[index].append(destination)

        # The index is increased by 1
        index += 1

    # Resetting 'current_map' list
    current_map = []

    # Resetting 'index' variable
    index = 0


# Iterating through every seed and taking every
# location data from it (last element of every seed data)
locations = [(seed[-1]) for seed in seeds_data]

# Variable to hold the lowest location value from 'locations' list
lowest_location = min(locations)

# Printing the final result
print(lowest_location)
