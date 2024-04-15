from flask import Flask, request, jsonify
from db_utils import get_all_records, get_categories, get_products_by_cat, insert_new_product, get_all_customer_details, get_specific_customer_detail, insert_new_customer, add_review


#   Create application
app = Flask(__name__)


#   Homepage (GET endpoint. NB: because GET is the default, don't need to specify the methods)
@app.route("/")
def home():
    # data returned to user when they access this route
    return ("<h1>\U0001F33A Welcome to TeamGreen's online shop\U0001F33A</h1>"
            "<h2>\U0001F331 When the going gets tough, the tough get growing! \U0001F331</h2>")


#   Products page (GET endpoint)
@app.route('/products')
def show_products():
    res = get_all_records() # function imported from db_utils file
    return jsonify(res)


#   Categories pages (GET endpoint)
@app.route('/categories')
def show_categories():
    res = get_categories() # function imported from db_utils file
    return jsonify(res)

@app.route('/products/<category>')
def show_products_cat(category):
    res = get_products_by_cat(category)
    return jsonify(res)


#   Add a new product to products (POST endpoint)
@app.route('/insertproduct', methods=['POST'])
def add_new_product():
    record = request.get_json()
    insert_new_product(record)
    print(record)
    return jsonify(record)


# (GET endpoint) used to display customer details
@app.route ('/staff/customers')
def show_customer_details():
    res = get_all_customer_details() # function imported from db_utils file
    return jsonify(res)
#   Add a new product to products (POST endpoint)


# (POST endpoint) to add a customer review
@app.route('/addreview', methods=['POST'])
def add_new_review():
    review = request.get_json()
    add_review(review)
    print(review)
    return jsonify(review)


# (GET endpoint) used to locate customer record by email
@app.route ('/staff/customers/<email_address>')
def get_specific_customer(email_address):
    res = get_specific_customer_detail(email_address) # function imported from db_utils file
    return jsonify(res)


#(POST endpoint) where we will add a new customer record
@app.route ('/staff/insertcustomers', methods=['POST'])
def add_new_customer():
    record = request.get_json()
    insert_new_customer(record)
    print(record)
    return jsonify(record)




# run flask server / application with debug
if __name__ == "__main__":
    app.run(debug=True)



# Code for future development

# Add a new order to orders table (POST endpoint)
# @app.route('/insertorder', methods=['POST'])
# def add_new_order():
#     order = request.get_json()
#     insert_new_order(order)
#     print(order)
#     return jsonify(order)







#   Reference note
# when you run the app.py it creates a developer URL: http://127.0.0.1:5000