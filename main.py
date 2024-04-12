# Before running program, install via terminal:
# pip install requests
# pip install jsonify

import requests
import json



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


def display_products(items):
    # Print the names of the columns.
    print("{:<4} {:<40} {:<60} {:<10} {:<10}".format(
        'CODE', 'NAME', 'DESCRIPTION', 'PRICE', 'STOCK'))
    print('-' * 125)

    # print each data item.
    for item in items:
        print("{:<4} {:<40} {:<60} £{:<10} {:<10}".format(
            item[0], item[1], item[2], item[3], item[4]
        ))


# get_welcome_page not working for me. Is it working for anyone else?
# Wondering if it is because the data is not in json format?

# get_welcome_page()
products = get_products()
display_products(products)