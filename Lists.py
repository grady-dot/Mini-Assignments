# Step 1: Create a list called 'foods' that stores 5 of your favourite foods.
# Example: foods = ["pizza", "tacos", "pasta", "ice cream", "sushi"]

foods = ["Pizza", "Burgers", "Chicken", "Tacos", "Fries"]

# Step 2: Print the entire list.

print(" ")
print("List of Foods")
print(" ")
print(foods)

# Step 3: Print the FIRST and LAST food using their index numbers.
# Hint: The first item is index 0, and the last one is index 4 (if you have 5 items).

print(" ")
print("First and Last")
print(" ")
print(foods[0])
print(foods[4])

# Step 4: Use len() to find how many foods are in your list.

print(" ")
print("Len Printing")
print(" ")
print(len(foods))

# Step 5: Use a for loop to print each food on its own line.
# Example:
# for food in foods:
#     print(food)

print(" ")
print("Seperate Foods")
print(" ")
for food in foods:
    print(food)

#Bonus Challenge:
# - Add one more food to your list using append()
# - Print your list again to see the change.

print(" ")
print("Bonus")
print(" ")
foods.append("Pasta")
print(foods)
print(" ")