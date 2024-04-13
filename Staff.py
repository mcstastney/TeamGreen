# Before running program, install via terminal:
# pip install requests
# pip install jsonify

import requests
import json

#   Add product to stocklist
def add_to_stock(id, name, category, price, qty):

    record = {
        "product_id": id,
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

# prod_id = int(input("Enter product ID: "))
# prod_name = input("Enter product name: ")
# prod_category = int(input("Enter category ID (\n1. Plant, \n2. Compost, \n3. Gardening tool, \n4. Other:\n "))
# prod_price = float(input("Unit price: "))
# prod_qty = int(input("How many do you want to add to stock?: "))
# add_to_stock(prod_id, prod_name, prod_category, prod_price, prod_qty)

def get_all_customers():
    result = requests.get(
        'http://127.0.0.1:5000/staff/customers',
        headers={'content-type': 'application/json'}
    )
    return result.json()

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


def get_specific_customer(email_address):
    result = requests.get(
        'http://127.0.0.1:5000/staff/customers/{}'.format(email_address),
        headers={'content-type': 'application/json'}
    )
    return result.json()



customers = get_all_customers()
display_customers(customers)

email_address = input("Enter customer email: ")
#email_address = "daisy@hotmail.com"
specific_customer = get_specific_customer(email_address)
display_customers(specific_customer)


