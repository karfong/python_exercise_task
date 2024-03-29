# Exercise 1
# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5 * 12 != 75)

# Comparison of strings
print("pyscript" == "PyScript")

# Compare a boolean with an integer
print(True == 1)

# Exercise 2
# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print(y <= "test")

# Comparison of booleans
print(True > False)


#Exercise 3
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)

#Exercise 4
# verify the answer you guessed
x = 8
y = 9
print(not(not(x < 3) and not(y > 14 or y > 10)))


#Exercise 5
# run following code and verify your answer
area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")
    
#Exercise 6
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15 :
    print("big place!")
    
    
#Exercise 7
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit":
    False
else:
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    False
else:
    print("pretty small")
    
    
#Exercise 8
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 20:
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else:
    print("pretty small.")
