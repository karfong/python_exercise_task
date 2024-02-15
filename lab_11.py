#Exercise 1
# Import numpy
import numpy as np
# np_baseball is available
np_baseball = np.array([[180, 78.4, 22.99],
            [215, 102.7, 34],
            [210, 98.5, 30],
            [188, 75.2, 35]])
# Create np_height from np_baseball
np_height = np_baseball[:,0]

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))

#Exercise 2 
#np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = None
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = None
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = None
print("Correlation: " + str(corr))


#Exercise 3
# heights and positions are available as lists
positions = ['GK', 'M', 'A', 'D', 'M', 'D', 'M', 'M', 'M', 'A', 'M', 'M', 'A', 'A', 'A']
heights = [191, 184, 185, 180, 181, 187, 170, 179, 183, 186, 185, 170, 187, 183, 173]
# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']


# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(None))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(None))
