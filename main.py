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



# Show all products
def show_all_products():
    result = requests.get(
        'http://127.0.0.1:5000/products',
        headers= {'content-type': 'application/json'}
    )
    return result.json()