"""
For this problem, you will be creating three sets. 

You will use the hash function that has been built in. 

You will also create a union and intersection of two sets. 
"""

"""
This is the solution for the setProblem.
Only look at this solution after you have attempted to do it on your own. 
"""

"""
Problem 1
Create a set that contains strings and floats.
You will need to use the hash method that python has built in. 
"""
# Creating my Yset. 
mixedSet = {2, 4, 6}

# Starting to get input from user. 
addToSet = input("Would you like to add an item to the set? Y or N: ")

# Creating the conditional statement for my loop.
while addToSet == "Y":
    # Getting input for item
    item = input("Enter in item: ")
    # Hashing the item
    hashedItem = hash(item)
    # Getting the item index
    remainder = hashedItem % len(mixedSet)
    # Showing index value
    print(remainder)
    # Adding item to the set. 
    mixedSet.add(item)

    # Continue the loop
    addToSet = input("Would you like to add an item to the set? Y or N: ")

print(mixedSet)

"""
Problem 2
Create two sets that contains a list of numbers.
TIP: Do regular integers instead of floats. It will make your life easier.
They need to have a little overlap so that some integers are listed twice. 
One in each set. 
"""
# Creating my first set.
set1 = {0, 2, 4, 6, 8}

# Creating my second set. 
set2 = {0, 1, 3, 5, 7, 9}

"""
Problem 3
Create a union of the two sets. 
If done correctly, it will show the numbers from both sets in one set. 
"""
# Python has a built function that can be used or this alternate way. 
unionSet = set1 | set2
# Showing my union set. 
print(unionSet)

"""
Problem 4
Create an intersection of the two sets. 
If done correctly, it will show what numbers both sets have in common. 
"""
# Python has a built function that can be used or this alternate way.
intersectionSet = set1 & set2
# Showing the intersection set. 
print(intersectionSet)