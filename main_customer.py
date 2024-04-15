import requests
import json

# functions interacting with the API

# Show all products
def get_products():
    result = requests.get(
        'http://127.0.0.1:5000/products',
        headers={'content-type': 'application/json'}
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


# Posting a user review
def add_review(product_name, rating, review_text):
    review = {
        "product_name": product_name,
        "rating": rating,
        "review_text": review_text
    }

    result = requests.post(
        'http://127.0.0.1:5000/addreview',
        headers={'content-type': 'application/json'},
        data=json.dumps(review)
    )

    return result.json()


# Helper functions for the main program

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


# display the products in a user friendly way and returns item selected by the user
def display_products(items):
    if items:
        # Print the names of the columns with spacing.
        print("\n{:<4} {:<40} {:<25} {:<10} {:<10}".format(
            'CODE', 'PRODUCT NAME', 'CATEGORY', 'PRICE', 'STOCK'))
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
            pass
        else:
            # if the product code matches the input, the item is added to the basket
            for item in items:
                if item[0] == selection:
                    return item
    else:
        pass


# find out how many of each item the user wants
def get_quantity():
    print("Enter quantity required: ", end="")
    how_many = is_number()
    return how_many


# display the product categories on the screen in a user friendly format
def display_categories(items):
    # output headings
    print("\n{:<4} {:<40}".format('CODE', 'PRODUCT CATEGORY'))
    print('-' * 44)
    # output categories
    for item in items:
        print("{:<4} {:<40}".format(item[0], item[1]))
    print("\n0   Back to main menu\n"
    # input selection
        "\nEnter the code to select a category: ", end="")
    selection = is_number()
    if selection == 0:
        # bit of a problem here instead of going straight back to main menu shows blank products page
        # Need to sort this out on next iteration!!!
        pass
    else:
        # may need to add a selection statement to check if user has entered a valid number to avoid program crashing
        for item in items:
            if item[0] == selection:
                category = item[1]
                break
        return category
            


    # def make_purchase():
        # check if item is in basket and if not tell user basket is empty
        # display basket
        # edit basket (select code to edit item)
        # delete item or change quantity
        # book delivery slot (could give options pick up in store or deliver)
        # make purchase (add basket details to order table Post, update the stock quantity in the products table PUT)


# a helper function to make a new list with all the unique values
def get_unique_list(list):
    unique_list = []
    [unique_list.append(item) for item in list if item not in unique_list]
    return unique_list


# displays the basket of products
def display_basket(items):
    if items:
        print("\n\t\tSHOPPING BASKET\n")
        # while True:
        print("\n{:<4} {:<40} {:<25} {:<10} {:<10}".format(
            'CODE', 'PRODUCT NAME', 'CATEGORY', 'PRICE', 'QUANTITY'))
        print('-' * 90)
        # print each data item.
        for item in items:
            print("{:<4} {:<40} {:<25} £{:<10} {:<10}".format(
                item[0], item[1], item[2], item[3], item[4]
            ))
        print("\n1: Confirm purchase"
        "\n0: Back to main menu\n"
        "\nEnter your selection: ", end="")
        selection = is_number()
        if selection == 0:
            # break out of loop and go back to main menu
            pass
        else:
            # run function here
            print("Your order has been processed\n")
    else:
        print("\nYour shopping basket is empty!\n")


# Ask user if they want to add a review
#If no then user can continue shopping
#if yes then user can write a review
def ask_for_review():
    while True:
        choice = input("Do you want to add a review? (yes/no): ").lower().capitalize()
        if choice == 'Yes':
            product_name = input("Enter the product name: ").capitalize()
            rating = int(input("Enter the rating (1-5): "))
            review_text = input("Enter your review: ")
            add_review(product_name, rating, review_text)
            break
        elif choice == 'No':
            print("No review added.")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


# a function to display the main menu and allow users to navigate the program
def run():
    basket = []
    selection = 100
    while selection != 0:
        go_back = False
        msg = ("\n1: View all products\n"
            "2: View products by category\n"
            "3: Find a specific product\n"
            "4: Make purchase\n"
            "5: Leave a review\n"
            "0: Quit program\n\n" 
            "Enter a number to proceed: ")
        selection = is_number(msg)
        if selection == 1:
            while go_back == False:
                products = get_products()
                product = display_products(products)
                if product:
                    quantity = get_quantity()
                    for i in range(quantity):
                        basket.append(product)
                    print("\n", basket, "\n")
                else:
                    go_back = True
        elif selection == 2:
            while go_back == False:
                categories = get_categories()
                category = display_categories(categories)
                products = get_products_by_category(category)
                product = display_products(products)
                if product:
                    quantity = get_quantity()
                    for i in range(quantity):
                        basket.append(product)
                    print("\n", basket, "\n")
                else:
                    go_back = True
        elif selection == 3:
            print("In development - Coming soon!!!")
            pass
        elif selection == 4:
            unique_basket = get_unique_list(basket)
            # loops through the unique list and find the number of occurences in the list containing duplicates
            for each in unique_basket:
                freq = basket.count(each)
                # replaces the quantity in stock value of each item with the number of occurences in the basket
                each[4] = freq
            display_basket(unique_basket)
        elif selection == 5:
            ask_for_review()
        else:
            print("\nPlease enter a valid number.\n")
            print("Please visit us again soon.\nGoodbye!")
            quit()


# main program

print("\n\t>>>\tWELCOME TO TEAM GREEN'S ONLINE SHOP!\t<<<")
print("\n>>>\tWhen the going gets tough, the tough get growing! \t<<<")
run()