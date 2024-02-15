#Exercise 1
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

#Exercise 2
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [hall, kit, liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)    


#Exercise 3 (List A is a valid list)
# List A
a = [1, 3, 4, 2]
print(a)

# List B
b = [[1, 2, 3], [4, 5, 7]]
print(b)

# List C
c = [1 + 2, "a" * 5, 3]
print(c)



#Exercise 4
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
