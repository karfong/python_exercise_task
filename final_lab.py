#Section 1
#Exercise 1
# Import pandas library
import pandas as pd

# Use pandas to read in recent_grads.csv
recent_grads = pd.read_csv('labs/recent_grads.csv')

# Print the shape
print(recent_grads.shape)

#Exercise 2
# Print .dtypes
print(recent_grads.dtypes)

# Output summary statistics
print(recent_grads.describe())

# Exclude data of type object
print(recent_grads.select_dtypes(exclude=['object']))


#Exercise 3
import numpy as np

# Names of the columns we're searching for missing values 
columns = ['median', 'p25th', 'p75th']

# Take a look at the dtypes
print(recent_grads[columns].dtypes)

# Find how missing values are represented
print(recent_grads["median"].unique())

# Replace missing values with NaN
for column in columns:
    recent_grads.loc[recent_grads[column] == 'UN', column] = np.nan
    
#Exercise 4
# Select sharewomen column
sw_col = recent_grads['sharewomen']

# Output first five rows
print(sw_col.head())


#Exercise 5
# Import numpy
import numpy as np

# Use max to output maximum values
max_sw = np.max(recent_grads['sharewomen'])

# Print column max
print(max_sw)

# Output the row containing the maximum percentage of women
print(recent_grads.loc[recent_grads['sharewomen'].idxmax()])


#Exercise 6
# Convert to numpy array
recent_grads_np = recent_grads.to_numpy()

# Print the type of recent_grads_np
print(type(recent_grads_np))


#Exercise 7
# Exclude non-numeric columns from recent_grads_np
numeric_columns = recent_grads.select_dtypes(include=[np.number]).columns
recent_grads_np_numeric = recent_grads[numeric_columns].to_numpy()

# Calculate correlation matrix
correlation_matrix = np.corrcoef(recent_grads_np_numeric, rowvar=False)

# Print the correlation matrix
print(correlation_matrix)


#Section 2
#Exercise 1
recent_grads['sharemen'] = 100 - recent_grads['sharewomen']

#Exercise 2
import numpy as np

# Find the maximum percentage value of men
max_men = np.max(recent_grads['sharemen'])

# Output the row with the highest percentage of men
# print(recent_grads[recent_grads['sharemen'] == max_men])

#Exercie 3
recent_grads['gender_diff'] = recent_grads['sharewomen'] - recent_grads['sharemen']

#Exercise 4
# Make all gender difference values positive
recent_grads['gender_diff'] = np.abs(recent_grads['gender_diff'])

# Find the 5 rows with lowest gender rate difference
lowest_gender_diff = recent_grads.nsmallest(5, 'gender_diff')

#Exercise 5
# Rows where gender rate difference is greater than .30
diff_30 = recent_grads['gender_diff'] > 0.30

# Rows with more men
more_men = recent_grads['sharemen'] > recent_grads['sharewomen']

# Combine more_men and diff_30
more_men_and_diff_30 = np.logical_and(more_men, diff_30)

# Find rows with more men and gender rate difference greater than .30
fewer_women = recent_grads[more_men_and_diff_30]

#Exercise 6
print(recent_grads.groupby('major_category').major_category.count())


#Exercise 7
# Filter departments skewed towards women (sharewomen > 0.5), group by major category, and count
departments_skewed_women = recent_grads[recent_grads['sharewomen'] > 0.5].groupby('major_category').count()

# Display the result
print(departments_skewed_women)

#Exercise 8
# Group by major category and calculate the mean of gender difference
average_gender_difference = recent_grads.groupby('major_category')['gender_diff'].mean()

# Display the result
print(average_gender_difference)

#Exercise 9
# Group by major category and calculate the average of 'low_wage_jobs' and 'unemployment_rate'
dept_stats = recent_grads.groupby('major_category')[['low_wage_jobs', 'unemployment_rate']].mean()

# Display the result
print(dept_stats)


#Section 3
#Exercise 1
# Import matplotlib
import matplotlib.pyplot as plt

# Get data
low_wage_jobs = recent_grads['low_wage_jobs']
unemployment_rate = recent_grads['unemployment_rate']

# Create scatter plot
plt.scatter(unemployment_rate, low_wage_jobs)

# Label x axis
plt.xlabel('Unemployment Rate')

# Label y axis
plt.ylabel('Low Wage Jobs')

# Display the graph 
plt.show()


#Exercise 2
# Plot the red and triangle shaped scatter plot  
plt.scatter(dept_stats['unemployment_rate'], dept_stats['low_wage_jobs'], color='r', marker='^')

# Label x axis
plt.xlabel('Unemployment Rate')

# Label y axis
plt.ylabel('Low Wage Jobs')

# Display the plot
plt.show()


#Exercise 3
sharewomen = recent_grads['sharewomen']

# Plot a histogram of sharewomen
plt.hist(sharewomen)

# Show the plot
plt.show()

#Exercise 4
# Create scatter plot
dept_stats.plot(kind='scatter', x='unemployment_rate', y='low_wage_jobs')
plt.show()

# Create histogram
recent_grads['sharewomen'].plot(kind='hist')
plt.show()


