#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""
John = int(input("choose a number, you can even choose negative if you want!"))

if John > 0:
    print("positive")
elif John < 0:
    print("negative")
elif John == 0:
    print("zero")
