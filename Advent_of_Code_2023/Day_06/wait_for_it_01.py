# Opening file containing all races data
with open('wait_for_it.txt', 'r') as file:
    # First line contains all the times for all the races
    time = file.readline().strip().split()
    # Removing the 0 element, which is text
    time.pop(0)

    # First line contains all the record distances for all the races
    distance = file.readline().strip().split()
    # Removing the 0 element, which is text
    distance.pop(0)

# Error margin counter
# Value is 1 so no error occurs when multiplying later
error_margin = 1

# Iterating through every race
for i in range(0, len(time)):
    # Time to finish the current race
    time_available = int(time[i])
    # Record distance to beat
    record_distance = int(distance[i])

    # Time to finish the current race
    current_time = time_available

    # Variable to store all the current race distances
    # For every possible time
    all_distances = []

    # Iterating through every possible time for the current race
    for j in range(0, time_available + 1):
        # Speed is equal the current time
        speed = j
        # Time left to travel
        travel_time = time_available - j

        # Distance passed in the current race
        travel_distance = travel_time * speed

        # Adding the current distance to the 'all_distances' list
        all_distances.append(travel_distance)

    # Variable to count the current race error margin
    race_error = 0

    # Iterating through every distance in the 'all_distances' list
    for d in all_distances:
        # If current distance is bigger than the record distance
        # the error margin is increased by 1
        if record_distance < d:
            race_error += 1

    # Adding the current race error margin to the total error margin
    error_margin *= race_error

# Printing the final result
print(error_margin)
