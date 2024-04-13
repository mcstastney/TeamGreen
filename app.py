from flask import Flask, request, jsonify
from db_utils import get_all_records, get_categories, get_products_by_cat, insert_new_product


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



# run flask server / application with debug
if __name__ == "__main__":
    app.run(debug=True)







#   Reference note
# when you run the app.py it creates a developer URL: http://127.0.0.1:5000