
# Step 1: Take input from the user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

# Step 2: Use the find() method to check for the substring
position = main_string.find(substring)

# Step 3: Print the result
if position != -1:
    print(f"The substring '{substring}' is present in the main string at index {position}.")
else:
    print(f"The substring '{substring}' is not present in the main string.")

# Step 4: Exit
