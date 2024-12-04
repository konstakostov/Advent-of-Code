# NB! WORK IN PROGRESS. ORIGINAL VERSION WAS WAY TOO MEMORY HEAVY
#  TO BRUTE FORCE THE ANSWER OF THIS TASK.

# Variable to save all the values from seed to location
seeds_data = []

# Variable to save the all map information
all_maps_data = {}

# Opening file containing all maps in the almanac
with open('if_you_give_a_seed_a_fertilizer.txt', "r") as almanac:
    # Getting all the seeds from the first row
    seeds = almanac.readline().strip().split()

    # Adding the seed [i] and it's range [i+1] as a tuple
    # to the 'seeds_data' list
    for i in range(1, len(seeds), 2):
        seeds_data.append((int(seeds[i]), int(seeds[i + 1])))

    # Reading the second line which is always empty
    first_empty_page = almanac.readline()

    # Current page index
    page_index = 1

    # Iterating through all the almanac pages
    for page in almanac:
        # Removing '\n' from the end of each line and splitting the line into elements
        page = page.strip().split()

        # If the current page is empty the last ma
        if not page:
            page_index += 1
            continue

        # If the first element of the current page is not number
        # this signifies the start of a new map
        # A new map id is generated in the 'all_maps_data' dictionary
        if not page[0].isnumeric():
            all_maps_data[page_index] = []
            continue

        # Variables to store the data from the current page
        destination_range = int(page[0])
        source_range = int(page[1])
        range_length = int(page[2])

        # Appending all the map data to the corresponding map as a tuple
        all_maps_data[page_index].append((destination_range, source_range, range_length))







