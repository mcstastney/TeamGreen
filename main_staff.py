# Before running program, install via terminal:
# pip install requests
# pip install jsonify

import requests
import json


#this function is needed for staff menu to work with number options the user selects
#this function needs to be before outside of run function
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


def get_all_customers():
    result = requests.get(
        'http://127.0.0.1:5000/staff/customers',
        headers={'content-type': 'application/json'}
    )
    return result.json()

# Display customer records in a table
# The numbers refer to the spaces inbetween the column headers
def display_customers(customers):
    # Print the names of the columns with spacing.
    print("\n{:<4} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        'customer_id', 'first_name', 'last_name', 'email_address', 'address1', 'address2', 'postcode', 'mobile'))
    print('-' * 120)
    # print each customer.
    for customer in customers:
        print("{:<4} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6], customer[7]
        ))

#result is the customer record obtained from database using HTTP get request

def get_specific_customer(email_address):
    result = requests.get(
        'http://127.0.0.1:5000/staff/customers/{}'.format(email_address),
        headers={'content-type': 'application/json'}
    )
    return result.json()

#   Add product to stocklist
def add_to_stock(name, category, price, qty):

    record = {
        "product_name": name,
        "product_category": category,
        "price": price,
        "stock_quantity": qty
    }

    result = requests.post(
        'http://127.0.0.1:5000/insertproduct',
        headers={'content-type': 'application/json'},
        data=json.dumps(record)
    )
    return result.json()


#record is dictionary format, key value pairs needed to populate entire customer record and mirrors database online_shop
#result is what is posted to database using HTTP post request
def add_to_customer(first_name, last_name, email_address, address1, address2, postcode, mobile):

    record = {
        "first_name": first_name,
        "last_name": last_name,
        "email_address": email_address,
        "address1": address1,
        "address2": address2,
        "postcode": postcode,
        "mobile": mobile,
      
    }

    result = requests.post(
        'http://127.0.0.1:5000/staff/insertcustomers',
        headers={'content-type': 'application/json'},
        data=json.dumps(record)
    )
    return result.json()

#really important the RUN function is placed at the end of the other functions it will call.
def main_menu_staff():
    msg = ("\n1: View all customer records\n"
           "2: Search for customer by email address\n"
           "3: Add new customer to records\n"
           "4: Add new product to stock\n"
           "0: Quit program\n\n" 
           "Enter a number to proceed: ")
    selection = is_number(msg)
    return selection

# Functions and input to run alongside the numbered options in the menu
def run():
    while True:
        option = main_menu_staff()
        if option == 1:
           customers = get_all_customers()
           display_customers(customers)
        elif option == 2:
            email_address = input("Enter customer email: ")
            specific_customer = get_specific_customer(email_address)
            display_customers(specific_customer)
        elif option == 3:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email_address = input("Enter email address: ")
            address1 = input("Enter address1: ")
            address2 = input("Enter address2: ")
            postcode = input("Enter postcode: ")
            mobile = input("Enter mobile: ")
            add_to_customer(first_name, last_name, email_address, address1, address2, postcode, mobile)
            print("\n\033[1m{} {} has been added to the database.\033[0m\n".format(first_name, last_name))
        elif option == 4:
            prod_name = input("Enter product name: ")
            prod_category = int(input("Enter category ID (\n1. Plant, \n2. Compost, \n3. Gardening tool, \n4. Other:\n "))
            prod_price = float(input("Unit price: "))
            prod_qty = int(input("How many do you want to add to stock?: "))
            add_to_stock(prod_name, prod_category, prod_price, prod_qty)
            print("\n\033[1m{} has been added to the database.\033[0m\n".format(prod_name))
        elif option == 0:
                print("\nYour work is always appreciated.\nGoodbye!")
                quit()
        else:
            print("\nPlease enter a valid number.\n")

# Run main program / staff menu
print("\n\t>>>\t\033[1m\U0001F33A Welcome to Team Green's Staff Portal \U0001F33A\033[0m\t<<<")
print("\n>>>\t\033[1m\U0001F331 When the going gets tough, the tough get growing! \U0001F331\033[0m\t<<<\n")
run()

#these inputs and function were used to test add customer to database in the creation of this script - ignore these - but can be useful to use on their own outside of the menu
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# email_address = input("Enter email address: ")
# address1 = input("Enter address1: ")
# address2 = input("Enter address2: ")
# postcode = input("Enter postcode: ")
# mobile = input("Enter mobile: ")
# add_to_customer(first_name, last_name, email_address, address1, address2, postcode, mobile)

#these inputs and function were used to test retrieving customer records from database in the creation of this script - ignore these - but can be useful to use on their own outside of the mene
# customers = get_all_customers()
# display_customers(customers)
# email_address = input("Enter customer email: ")
# specific_customer = get_specific_customer(email_address)
# display_customers(specific_customer)
