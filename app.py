# Before running the program, in terminal run the following:
# pip install flask

from flask import Flask, request, jsonify
from db_utils import get_all_records


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




# run flask server / application with debug
if __name__ == "__main__":
    app.run(debug=True)







#   Reference notes

# when you run the app.py it creates a developer URL: http://127.0.0.1:5000
# use this in postman + the route (e.g. "/create-user")

# path parameter example
# "/get-user/6226"

# query parameter example
# "/get-user/6226?extra = hello world"
# ?extra = hello world is an additional variable that can be passed along the route