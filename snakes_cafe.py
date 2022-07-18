print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
# Initialize empty dictionary
meal = {}
menu = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"] # all possible orders

# Loop through ordering until user enters 'quit'
# Create a variable to store user's order
order = input("> ")

while order != "quit":
    while order not in menu:
        print("""
        ** I'm sorry, I didn't recognize that item... **
        ** please check that it was spelled correctly **
        """)
        order = input("> ")
    if order in meal:
        meal[order] += 1
    else:
        meal[order] = 1

    # Create order report
    for item in meal:
        if meal[item] == 1:
            print(f"** {meal[item]} order of {item} has been added to your meal **")
        else:
            print(f"** {meal[item]} orders of {item} have been added to your meal **")

    order = input("> ")
# end loop