#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

import math
x = int(input("give me a whole number please"))
N = x/2
n = str(N)
if ".5" in n:
    print("the number is odd")
else:
    print("the number is even")