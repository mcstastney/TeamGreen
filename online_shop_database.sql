CREATE DATABASE online_shop;
USE online_shop;

-- DROP DATABASE online_shop;

CREATE TABLE categories (
	category_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL
);

INSERT INTO categories
(category_name)
VALUES
("Plant"),
("Compost"),
("Gardening tool"),
("Other");

-- DROP TABLE categories;


CREATE TABLE products (
		product_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
		product_name VARCHAR(50) NOT NULL,
        product_category INTEGER NOT NULL,
		price FLOAT(2) NOT NULL, 
		stock_quantity INTEGER NOT NULL,
        CONSTRAINT pk_product_id PRIMARY KEY (product_id),
        CONSTRAINT fk_category_id FOREIGN KEY (product_category) REFERENCES categories(category_id)
 );

 -- DROP TABLE products;

INSERT INTO products
(product_id, product_name, product_category, price, stock_quantity)
VALUES 
(1, 'Agapanthus umbellatus', 1, 5.99, 50),
(2, 'Miracle-Gro', 2, 48.99, 500),
(3, 'Growing Tray', 3, 12.49, 200),
(4, 'Dahlia - Ambition', 1, 4.9, 80),
(5, 'Bidens Golden Eye', 1, 1.69, 100),
(6, 'Spear & Jackson Bypass Loppers', 3, 29.99, 150),
(7, 'Wild Bird Seed Mix', 4, 7.99, 300),
(8, 'Vitax Q4 Multi Purpose Compost', 2, 5.49, 400),
(9, 'Gardman Tomato Planter', 3, 9.99, 120),
(10, 'Levington John Innes No. 3 Compost', 2, 6.99, 250);


CREATE TABLE customers (
		customer_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
		first_name VARCHAR(30) NOT NULL,
		last_name VARCHAR(30) NOT NULL,
		email_address VARCHAR(60) NOT NULL UNIQUE,
		address1 VARCHAR (200) NOT NULL,
		address2 VARCHAR (200),
		postcode VARCHAR(10) NOT NULL,
		mobile VARCHAR(15) NOT NULL,
		CONSTRAINT pk_customer_id  PRIMARY KEY (customer_id)
);


-- TRUNCATE customers;

INSERT INTO customers
(first_name, last_name, email_address, address1, address2, postcode, mobile)
VALUES 
("Sadie", "Lock", "sadie@hotmail.com", "23 Sherlock Way", "London", "SE8 4XG", "07966 135 567"),
("Jimmy", "Brown", "jimmyboy@gmail.com", "179 Sycamore Road", "London", "SE6 5NJ", "07944 344 211"),
("Charlotte", "Green", "cgreen@hotmail.com", "34 Adelaide Avenue", "London", "SE6 9JJ", "07943 675 498"),
("Alfie", "Ryan", "alfralf@gmail.com", "67 Farley Road", "London", "SE6 5GF", "07944 327 498"),
("Roisin", "Johns", "rosie@hotmail.com", "59 Albert Road", "Manchester", "MAN 6YY", "07967 432 190"),
("Daisy", "Duke", "daisy@hotmail.com", "21 Albacore Crescent","Bradford", "BRA 5FV", "07958 789 012"),
("India", "Frost",  "frosty@hotmail.com", "11 Bexhill Road", "Cornwall", "COR 6XA", "07943 509 120");

CREATE TABLE reviews (
    review_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    product_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP,
    CONSTRAINT pk_review_id PRIMARY KEY (review_id),
    CONSTRAINT fk_review_product_id FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO reviews (product_id, rating, review_text, review_date)
VALUES
    (1, 4, "Beautiful flowers", "2019-06-20 14:45:00"),
    (2, 5, "My grass looks amazing!", "2021-08-02 09:30:00"),
    (3, 3, "Trays could be sturdier.", "2021-04-18 12:20:00"),
    (4, 5, "Very happy with my purchase.", "2021-07-15 08:10:00"),
    (5, 4, "A lovely plant.", "2021-07-15 08:10:00");
    
SELECT * FROM reviews;

CREATE TABLE orders (
		customer_id INTEGER,
		order_id INTEGER UNIQUE,
		order_date DATE, 
		order_time TIME,
		CONSTRAINT pk_order_id PRIMARY KEY (order_id),
		CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
 
CREATE TABLE shopping_basket (
		order_id INTEGER NOT NULL,
		product_id INTEGER NOT NULL,
		quantity INTEGER NOT NULL,
		CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES products(product_id),
		CONSTRAINT fk_order_id FOREIGN KEY (order_id) REFERENCES orders(order_id)
);



