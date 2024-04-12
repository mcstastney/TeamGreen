#   Before running the program, in terminal run the following:
#   pip install mysql-connector-python

import mysql.connector
from config import HOST, USER, PASSWORD

db_name = "online_shop"

class DbConnectionError(Exception):
    pass

#   Connect to database using the credentials imported from config file

def _connect_to_specific_db(database_name):
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database = database_name
    )
    print("Connected to DB: %s" % db_name)

    return mydb

_connect_to_specific_db(db_name)



# Show all tables in database

def _show_all_table_in_specific_db(database_name):
    specific_db = _connect_to_specific_db(database_name)
    mycursor = specific_db.cursor()
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

_show_all_table_in_specific_db(db_name)



#   Select all records in the 'products' table in the 'online_shop' DB

def get_all_records():
    try:
        #   Connect to DB
        db_name = "online_shop"
        db_connection = _connect_to_specific_db(db_name)

        #   Add cursor object to execute queries / actions in DB
        my_cursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        #   Query to select all data in 'products' table
        query = "SELECT * FROM products" #  Edit this query to only show useful info to customer i.e. product_name, product_description, price)
        my_cursor.execute(query)
        result = my_cursor.fetchall() # this is a list with db records where each record is a tuple

        #   Close the cursor after query executed
        my_cursor.close()

        # Print and Return the fetched records
        print(result)
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

get_all_records()




# TEST CODE - Insert new product into the 'products' table in the 'online_shop' DB

# record = {
#     'product_id': 46,
#     'product_name': 'Blue Spruce',
#     'product_description': 'Blue Spruce has a strong blue tinge to its needles which makes it a very desirable Christmas Tree.',
#     'price': 35.00,
#     'stock_quantity': 35,
# }


# def insert_new_record(record):
#     try:
#         #  connect to db
#         db_name = "online_shop"
#         db_connection = _connect_to_specific_db(db_name)
#         my_cursor = db_connection.cursor()
#         print("Connected to DB: %s" % db_name)
#
#         #  query
#         query = """INSERT INTO products ({}) VALUES ('{}', '{}', '{}', '{}', {})""".format(
#             ', '.join(record.keys()),
#             record['product_id'],
#             record['product_name'],
#             record['product_description'],
#             record['price'],
#             record['stock_quantity'],
#         )
#
#         my_cursor.execute(query)
#         db_connection.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
#         my_cursor.close()
#
#
#     except Exception:
#         raise DbConnectionError("Failed to read data from DB")
#
#     finally:
#         if db_connection:
#             db_connection.close()
#             print("DB connection is closed")
#
#     print("New product added to database")
#
# insert_new_record(record)