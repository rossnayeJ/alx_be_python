# File: pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print each asterisk in the row
    for col in range(size):
        print("*", end="")  # Print without a newline
    print()  # Print a newline after completing a row
    row += 1  # Move to the next row
