import mysql.connector
from datetime import datetime
from config import HOST, USER, PASSWORD

db_name = "online_shop"

# creating an exception class called DbConnectionError
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


# The following code connects you to shop_online MySQL database. 
#Ensure you have entered your details in the config.py file
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database='online_shop'
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)


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


# a function get the different categories of products from the database
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


# a function to get all products in a specific category
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


# a function to add a new product to the database
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


# Following code allocates relevent product id to the product name entered by user
def get_product_id(product_name):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "SELECT product_id FROM products WHERE product_name = %s"
        cursor.execute(sql, (product_name,))
        result = cursor.fetchone()
        if result:
            return result[0]  # Return the correct product ID for the product name entered
        else:
            print("Product not found.")
            return None
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# Adds a new review to the 'reviews' table once user has completed their answers
# Adds time stamp of the date user adds the review
def add_review(product_name, rating, review_text):
    try:
        product_id = get_product_id(product_name)
        if product_id is not None:
            connection = connect_to_db()
            cursor = connection.cursor()
            sql = "INSERT INTO reviews (product_id, rating, review_text, review_date) VALUES (%s, %s, %s, NOW())"
            values = (product_id, rating, review_text)
            cursor.execute(sql, values)
            connection.commit()
            print("Review added successfully")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# Following code allocates relevent product id to the product name entered by user
def get_product_id(product_name):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "SELECT product_id FROM products WHERE product_name = %s"
        cursor.execute(sql, (product_name,))
        result = cursor.fetchone()
        if result:
            return result[0]  # Return the correct product ID for the product name entered
        else:
            print("Product not found.")
            return None
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# Adds a new review to the 'reviews' table once user has completed their answers
# Adds time stamp of the date user adds the review
def add_review(product_name, rating, review_text):
    try:
        product_id = get_product_id(product_name)
        if product_id is not None:
            connection = connect_to_db()
            cursor = connection.cursor()
            sql = "INSERT INTO reviews (product_id, rating, review_text, review_date) VALUES (%s, %s, %s, NOW())"
            values = (product_id, rating, review_text)
            cursor.execute(sql, values)
            connection.commit()
            print("Review added successfully")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


#this function is used to obtain all customer records
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


#this function is used to obtain the record of a specific customer
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


# a function to add a new customer record to the database
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
#get_specific_customer("daisy@hotmail.com")


#   Sample record for testing purposes
# testrecord = {
#     'product_id': 11,
#     'product_name': 'Gooseberry bush',
#     'product_category': 'Plant',
#     'price': 5.00,
#     'stock_quantity': 35}
# insert_new_product(testrecord)

