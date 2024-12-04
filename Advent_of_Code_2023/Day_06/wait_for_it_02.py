# NB! Current solution is not optimized.
#  It does not run as fast as the solution in Task 01.
#  Improvement of the algorithm may be applied in the future.

# Opening file containing all races data
with open('wait_for_it.txt.', 'r') as file:
    # First line contains all the times for all the races
    time_data = file.readline().strip().split()
    # Removing the 0 element, which is text
    time_data.pop(0)

    # First line contains all the record distances for all the races
    distance_data = file.readline().strip().split()
    # Removing the 0 element, which is text
    distance_data.pop(0)

# Variables to store the available time and distance for the only race
time, distance = '', ''

# Iterating though every element in the 'time_data' and 'distance_data' lists
# so that the current value can be added to the 'time'/'distance' variable.
for td in range(len(time_data)):
    time += time_data[td]
    distance += distance_data[td]

# Turning the variables into integers
time, distance = int(time), int(distance)

# Counter of all the possible ways to win this wace
ways_to_win = 0

# Iterating through every possible race time
for j in range(0, time + 1):
    # Speed is equal the current time
    speed = j
    # Time left to travel
    travel_time = time - j

    # Distance passed in the current race
    travel_distance = travel_time * speed

    # If the current distance is greater than the record distance
    # the 'ways_to_win is increased by 1
    if travel_distance > distance:
        ways_to_win += 1

# Printing the final result
print(ways_to_win)
