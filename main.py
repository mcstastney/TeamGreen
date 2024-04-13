# Before running program, install via terminal:
# pip install requests
# pip install jsonify

import requests
import json

basket = []


# Show homepage
def get_welcome_page():
    result = requests.get(
        'http://127.0.0.1:5000/',
        headers= {'content-type': 'application/json'}
    )
    return result.json()


# Get products
def get_products():
    result = requests.get(
        'http://127.0.0.1:5000/products',
        headers= {'content-type': 'application/json'}
    )
    return result.json()

# Get categories
def get_categories():
    result = requests.get(
        'http://127.0.0.1:5000/categories',
        headers= {'content-type': 'application/json'}
    )
    return result.json()

# Retrieving products from a particular category
def get_products_by_category(category):
    result = requests.get(
        'http://127.0.0.1:5000/products/{}'.format(category),
        headers= {'content-type': 'application/json'}
    )
    return result.json()


# display the products in a user friendly way
def display_products(items):
    while True:
        # Print the names of the columns with spacing.
        print("\n{:<4} {:<40} {:<25} {:<10} {:<10}".format(
            'CODE', 'NAME', 'CATEGORY', 'PRICE', 'STOCK'))
        print('-' * 90)
        # print each data item.
        for item in items:
            print("{:<4} {:<40} {:<25} £{:<10} {:<10}".format(
                item[0], item[1], item[2], item[3], item[4]
            ))
        print("\n0   Back to main menu\n"
            "\nEnter the code to add a product to your shopping basket: ", end="")
        selection = is_number()
        if selection == 0:
            # break out of loop and go back to main menu
            break
        else:
            print("Enter quantity required: ", end="")
            quantity = is_number()
            # if the product code matches the input, the item is added to the basket
            for item in items:
                if item[0] == selection:
                    # add the quantity selected by the user by using a loop
                    for i in range(quantity):
                        basket.append(item)
                    break
            print(basket)
            print()
    # returns user to main menu
    run()


# display the categories on the screen in rows
def display_categories(items):
    # loops until user goes back to main menu
    while True:
        # output headings
        print("{:<4} {:<40}".format('CODE', 'CATEGORY'))
        print('-' * 44)
        # output categories
        for item in items:
            print("{:<4} {:<40}".format(item[0], item[1]))
        print("\n0   Back to main menu\n"
        # input selection
            "\nEnter the code to select a category: ", end="")
        selection = is_number()
        if selection == 0:
            break
        else:
            # may need to add a selection statement to check if user has entered a valid number to avoid program crashing
            for item in items:
                if item[0] == selection:
                    category = item[1]
                    break
            products = get_products_by_category(category)
            display_products(products)
    # once user returns to main menu
    run()

    # def make_purchase():
        # check if items in basket and if not tell user basket is empty
        # display basket
        # edit basket (select code to edit item)
        # delete item or change quantity
        # book delivery slot (could give options pick up in store or deliver)
        # make purchase (add basket details to order table PUT, update the stock quantity in the products table PUT)



# a function to check if string input is a number and convert to integer data type
def is_number(msg=""):
    while True:
        print(msg, end="")
        selection = input()
        # checks it is a numerical character
        if selection.isnumeric():
            selection = int(selection)
            return selection
        else:
            print("Invalid selection.\n")


# get_welcome_page not working for me. Is it working for anyone else?
# Wondering if it is because the data is not in json format?


# a function to display the main menu and take user selection
def main_menu():
    msg = ("1: View all products\n"
           "2: View products by category\n"
           "3: Find a specific product\n"
           "4: Make purchase\n"
           "0: Quit program\n\n" 
           "Enter a number to proceed: ")
    selection = is_number(msg)
    return selection

def run():
    while True:
        option = main_menu()
        if option == 1:
            products = get_products()
            display_products(products)
        elif option == 2:
            categories = get_categories()
            display_categories(categories)
        elif option == 3: 
            pass
        elif option == 4:
            pass
        elif option == 0:
                print("Please visit us again soon.\nGoodbye!")
                quit()
        else:
            print("\nPlease enter a valid number.\n")


print("\n\t>>>\tWelcome to Team Green's Online Shop!\t<<<")
print("\n>>>\tWhen the going gets tough, the tough get growing! \t<<<\n")
run()

