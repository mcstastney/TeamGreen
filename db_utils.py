import mysql.connector
from config import HOST, USER, PASSWORD

db_name = "online_shop"

# Create an exception class called DbConnectionError
class DbConnectionError(Exception):
    pass


# Connect to 'shop_online' MySQL database.
# Ensure you have entered your details in the config.py file
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


# Show all tables in database
def _show_all_table_in_specific_db(database_name):
    specific_db = _connect_to_specific_db(database_name)
    mycursor = specific_db.cursor()
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)


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
        query = """select p.product_id, p.product_name, c.category_name, p.price, p.stock_quantity
                   from products as p
                   inner join categories as c
                   where p.product_category = c.category_id
                   order by p.product_name;"""
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


# Get categories of products from the database
def get_categories():
    try:
        db_name = "online_shop"
        db_connection = _connect_to_specific_db(db_name)
        my_cursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        #   Query to select all categories of product
        query = """select c.category_id, c.category_name
                   from categories as c;""" 
        my_cursor.execute(query)
        result = my_cursor.fetchall() # this is a list with db records where each record is a tuple
        my_cursor.close()

        print(result)
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Get all products in a specific category
def get_products_by_cat(category):
    try:
        db_name = "online_shop"
        db_connection = _connect_to_specific_db(db_name)
        my_cursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        #   Query to select all product within a given category
        query = """select p.product_id, p.product_name, c.category_name, p.price, p.stock_quantity
                from products as p
                inner join categories as c on p.product_category = c.category_id
                where c.category_name = '{category}'
                order by p.product_name;""".format(category=category)
        my_cursor.execute(query)
        result = my_cursor.fetchall() # this is a list with db records where each record is a tuple
        my_cursor.close()

        print(result)
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Add a new product to the database
def insert_new_product(record):
    try:
        #  connect to db
        db_name = "online_shop"
        db_connection = _connect_to_specific_db(db_name)
        my_cursor = db_connection.cursor()

        #  query
        query = """INSERT INTO products ({}) VALUES ('{}', '{}', '{}', {})""".format(
            ', '.join(record.keys()),
            record['product_name'],
            record['product_category'],
            record['price'],
            record['stock_quantity'],
        )

        my_cursor.execute(query)
        db_connection.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
        my_cursor.close()

    except Exception:
        raise DbConnectionError()

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("{} added to database".format(record['product_name']))


# Add a new review to the 'reviews' table
def add_review(review):
    try:
        #  connect to db
        db_name = "online_shop"
        db_connection = _connect_to_specific_db(db_name)
        my_cursor = db_connection.cursor()

        #  query
        query = """INSERT INTO reviews ({}) VALUES ('{}', '{}', '{}')""".format(
            ', '.join(review.keys()),
            review['product_id'],
            review['rating'],
            review['review_text'],
        )

        my_cursor.execute(query)
        db_connection.commit()
        my_cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Review for product ID: {} added to database".format(review['product_id']))


# Get all customer records
def get_all_customer_details():
    try:
            #connect to db
            db_name="online_shop"
            db_connection = _connect_to_specific_db(db_name)
            my_cursor = db_connection.cursor()
            print("Connected to DB: %s"  % db_name)
            query = "SELECT * from online_shop.customers"
            my_cursor.execute(query)
            result = my_cursor.fetchall()
            my_cursor.close()

            print(result)
            return result
    except Exception:
          raise DbConnectionError("Fail to read data from DB")
    
    finally:
          if db_connection:
                db_connection.close()
                print("DB connection is closed")




# Get the record of a specific customer
def get_specific_customer_detail(email_address):
    try:
        db_name = "online_shop"
        db_connection = _connect_to_specific_db(db_name)
        my_cursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        #   Query to select all product within a given category
        query = """select * from online_shop.customers
                where email_address = '{email_address}';""".format(email_address=email_address)
        print(query)
        my_cursor.execute(query)
        result = my_cursor.fetchall() # this is a list with db records where each record is a tuple
        my_cursor.close()

        print(result)
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Add a new customer record to the database
def insert_new_customer(record):
    try:
        #  connect to db
        db_name = "online_shop"
        db_connection = _connect_to_specific_db(db_name)
        my_cursor = db_connection.cursor()

        #  query
        query = """INSERT INTO customers ({}) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            ', '.join(record.keys()),
            record['first_name'],
            record['last_name'],
            record['email_address'],
            record['address1'],
            record['address2'],
            record['postcode'],
            record['mobile'],
        )

        my_cursor.execute(query)
        db_connection.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
        my_cursor.close()

    except Exception:
        raise DbConnectionError()

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("{} added to database".format(record['email_address']))


# Testing the functions work as intended
# _connect_to_specific_db(db_name)
# _show_all_table_in_specific_db(db_name)
#get_all_records()
#get_categories()
#get_products_by_cat("Plant")
#get_specific_customer_details("daisy@hotmail.com")


#   Sample records for testing purposes
# testrecord = {
#     'product_name': 'Gooseberry bush',
#     'product_category': 1,
#     'price': 5.00,
#     'stock_quantity': 35}
# insert_new_product(testrecord)

# testreview = {
#     'product_id': 10,
#     'rating': 5,
#     'review_text': 'Great compost for germinating seedings.'}
# add_review(testreview)

# IF TIME - get timestamp working in add_review
# # review_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')