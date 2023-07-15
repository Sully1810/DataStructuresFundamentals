'''
For your stack problem, you will be creating a grocery list.
There are going to be several items you will have to add. 
You have to remove a few items. 

You will also have to make some conditional statements.

Here is the solution for the stack problem.
There are many ways that this could have been done. 
Here is how I choose to do mine. 

'''

# Problem 1
# Create your grocery list. 
# Your code will go here. 

# Creating a list for my 
groceryList = []

#Problem 2
# Add milk, eggs, butter, and bread to your grocery list. 
# Print your list when you are done.
# Your code will go here. 

# Creating a function to call. 
def addItem():

    # Getting input from the user. 
    addQuestion = input("Would you like to add items to your grocery list? (Y or N) ")

    # Creating a conditional statement to keep adding items to list. 
    while addQuestion == 'Y':
        item = input("Enter in name of the item. ")
        groceryList.append(item)
        addQuestion = input("Would you like to add items to your grocery list? (Y or N) ")

    # When finished, printing out grocery list. 
    print(groceryList)

# Problem 3
# Remove bread from the list.
# Print your list when you are done. 
# Your code will go here.

# Creating a function to call. 
def removeItem():
    # Pop removes the last item on a list. 
    groceryList.pop()

# Problem 4
# Your grocery list cannot have more than 5 items at a time. 
# Create a function that will only allow 5 items on the list at a time. 
# If more than 5 items exists, print your list is already full. 
# Your code will go here. 

# Creating a conditional for what should happen with the list
if len(groceryList) > 5:
    print("List too full!")
    removeItem()
else:
    # Calling add item function
    addItem()