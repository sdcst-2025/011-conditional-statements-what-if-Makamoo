#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""

X = input("Choose a number, any number")
x = int(X)
if x > 100:
    print("The number is larger than 100")
elif x < 100:
    print("The number is smaller than 100")
elif x == 100:
    print("The number is 100")