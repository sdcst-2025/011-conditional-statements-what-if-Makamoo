#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math
charmander = int(input("side 1:"))
bulbasaur = int(input("side 2:"))
squirtle = int(input("side 3:"))
if charmander > bulbasaur:
    if charmander > squirtle:
        pikachu = charmander
    elif squirtle > charmander:
        pikachu = squirtle
elif bulbasaur > charmander:
    if bulbasaur > squirtle:
        pikachu = bulbasaur
    elif squirtle > bulbasaur:
        pikachu = squirtle
else:
    print("that is an acute triangle")

if pikachu == charmander:
    if pikachu == math.sqrt(bulbasaur**2 + squirtle**2):
        print("that is a right triangle")
    elif pikachu**2 > bulbasaur**2 + squirtle**2:
        print("that is an obtuse triangle")
    elif pikachu**2 < bulbasaur**2 + squirtle**2:
        print("that is an acute triangle")
elif pikachu == bulbasaur:
    if pikachu == math.sqrt(charmander**2 + squirtle**2):
        print("that is a right triangle")
    elif pikachu**2 > charmander**2 + squirtle**2:
        print("that is an obtuse triangle")
    elif pikachu**2 < charmander**2 + squirtle**2:
        print("that is an acute triangle")
elif pikachu == squirtle:
    if pikachu == math.sqrt(bulbasaur**2 + charmander**2):
        print("that is a right triangle")
    elif pikachu**2 > bulbasaur**2 + charmander**2:
        print("that is an obtuse triangle")
    elif pikachu**2 < bulbasaur**2 + charmander**2:
        print("that is an acute triangle")
elif charmander == bulbasaur:
    if squirtle**2 > charmander**2 + bulbasaur**2:
        print("that is an obtuse triangle")
    if squirtle**2 < charmander**2 + bulbasaur**2:
        print("that is an acute triangle")
    if squirtle**2 == charmander**2 + bulbasaur**2:
        print("that is a right triangle")
elif squirtle == bulbasaur:
    if charmander**2 > squirtle**2 + bulbasaur**2:
        print("that is an obtuse triangle")
    if charmander**2 < squirtle**2 + bulbasaur**2:
        print("that is an acute triangle")
    if charmander**2 == squirtle**2 + bulbasaur**2:
        print("that is a right triangle")
elif charmander == squirtle:
    if bulbasaur**2 > charmander**2 + squirtle**2:
        print("that is an obtuse triangle")
    if bulbasaur**2 < charmander**2 + squirtle**2:
        print("that is an acute triangle")
    if bulbasaur**2 == charmander**2 + squirtle**2:
        print("that is a right triangle")