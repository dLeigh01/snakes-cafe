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
Meal = {}

# Loop through ordering until user enters 'quit'

# Create a variable to store user's order
order = input("> ")
while order != "quit":
    # print user's current order
    num_items = 1 # TODO: tally items
    report = f"** {num_items} order of {order} have been added to your meal **"

    print(report)
    order = input("> ")
# end loop