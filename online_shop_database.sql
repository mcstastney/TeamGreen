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
        product_category VARCHAR(50) NOT NULL,
		price FLOAT(2) NOT NULL, 
		stock_quantity INTEGER NOT NULL,
        CONSTRAINT pk_product_id PRIMARY KEY (product_id)
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

select p.product_name, c.category_name, p.price, p.stock_quantity
from products as p
inner join categories as c
where p.product_category = c.category_id
order by p.product_name;

select c.category_id, c.category_name
from categories as c;

select p.product_id, p.product_name, c.category_name, p.price, p.stock_quantity
                from products as p
                inner join categories as c on p.product_category = c.category_id
                where c.category_name = "Plant"
                order by p.product_name;
