#Exercise 1 
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[9] = 10.50  

# Change "living room" to "chill zone"
areas[4] = "chill zone"

#Exercise 2 
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = list(areas)
areas_1.extend(["poolhouse", 24.5])

# Add garage data to areas_1, new list is areas_2s
areas_2 = list(areas_1)
areas_2.extend(["garage", 15.45])

print(areas_1)
print(areas_2)


#Exercise 3 (Option B,C,D)
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

del(areas[10]); del(areas[11])
print("Option A:", areas)
del(areas[10:11])
print("Option B:", areas)
del(areas[-4:-2])
print("Option C:", areas)
del(areas[-3]); del(areas[-4])
print("Option D:", areas)


#Exercise 4
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy --- modify following line
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)