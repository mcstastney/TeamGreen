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

prod_id = int(input("Enter product ID: "))
prod_name = input("Enter product name: ")
prod_category = int(input("Enter category ID (\n1. Plant, \n2. Compost, \n3. Gardening tool, \n4. Other:\n "))
prod_price = float(input("Unit price: "))
prod_qty = int(input("How many do you want to add to stock?: "))
add_to_stock(prod_id, prod_name, prod_category, prod_price, prod_qty)

