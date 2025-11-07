# Alex Harriman
#11/6/25
#requests the first and last name as inputs to output a custom user ID

import random
import math

# makeID takes first and last name 
# and returns the first initial of the first name and last five initials of the lastname ending with a random number between 10 and 99
def makeID( firstName, lastName ):
    # Extract the first inital of their first name
    firstInit = firstName[0].upper()
    # Extract the first five letters of last name
    lastFirstFive = lastName[0:5].upper()
    # Get a random number between 10 and 99
    myNumber = random.randint(10,99)

    # Put it all together (concatenate)
    ID = firstInit + lastFirstFive + str(myNumber)
    return ID


# main prompts the user ....
def main():
    # Ask for their first name
    firstName = input("What is your first name? ")

    # Ask for their last name
    lastName = input("What is your last name? ")

    # Call makeID
    newID = makeID(firstName, lastName)

    # Print out the newID
    print (newID)


# Function definitions above
############################
# Test code below
main()
