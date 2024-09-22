# File: multiplication_table.py

# Prompt the user for a number to generate its multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to generate the multiplication table from 1 to 10
for i in range(1, 11):
    # Calculate the product and print the multiplication table
    print(f"{number} * {i} = {number * i}")
