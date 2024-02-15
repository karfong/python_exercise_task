#Exercise 1
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('labs/cars.csv')

# Print out cars
print(cars)

#Exercise 2
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('labs/cars.csv', index_col=0)

# Print out cars
print(cars)


#Exercise 3
# Import cars data
import pandas as pd
cars = pd.read_csv('labs/cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])  

# Print out country column as Pandas DataFrame
print(cars[['country']])

#Exercise 4
# Import cars data
import pandas as pd
cars = pd.read_csv('labs/cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc[['JAP']])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])


#Exercise 5
# Import cars data
import pandas as pd
cars = pd.read_csv('labs/cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc[['MOR'], ['drives_right']])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])