# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":
# Ask the user how many numbers to loop through
    user_number = input("How many numbers? ")

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range(int(1,user_number+1)):

        # Print each number in the range
        print(i)    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")