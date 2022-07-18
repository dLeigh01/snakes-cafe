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

# Loop through ordering until user enters 'quit'
# Create a variable to store user's order
order = input("> ")
while order != "quit":
    if order in meal:
        meal[order] += 1
    else:
        meal[order] = 1

    # Create order report

    if meal[order] == 1:
        report = f"** {meal[order]} order of {order} has been added to your meal **"
    else:
        report = f"** {meal[order]} orders of {order} have been added to your meal **"

    # print user's current order
    print(report)
    order = input("> ")
# end loop