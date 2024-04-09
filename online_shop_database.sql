CREATE DATABASE online_shop;
USE online_shop;

CREATE TABLE products (
		product_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
		product_name VARCHAR(50) NOT NULL,
        product_description VARCHAR(150) NOT NULL,
		price FLOAT(2) NOT NULL, 
		stock_quantity INTEGER NOT NULL,
        CONSTRAINT pk_product_id PRIMARY KEY (product_id)
 );

INSERT INTO products
(product_id, product_name, product_description, price, stock_quantity)
VALUES 
(1, 'Agapanthus umbellatus', 'Lilac-blue flowers on tall, dark, upright stems', 5.99, 50),
(2, 'Miracle-Gro', '4 in 1 Lawn food, Weed & Moss Prevention', 48.99, 500),
(3, 'Growing Tray', 'Tray with 18cm x 9cm Square Pots', 12.49, 200),
(4, 'Dahlia - Ambition', 'Striking purple blooms for any display', 4.9, 80),
(5, 'Bidens Golden Eye', 'Essential trailing plant for containers', 1.69, 100),
(6, 'Spear & Jackson Bypass Loppers', 'Ideal for cutting and pruning larger stems', 29.99, 150),
(7, 'Wild Bird Seed Mix', 'Perfect for attracting a variety of wild birds', 7.99, 300),
(8, 'Vitax Q4 Multi Purpose Compost', 'High quality compost for various garden applications', 5.49, 400),
(9, 'Gardman Tomato Planter', 'Perfect for growing tomatoes, peppers and aubergines', 9.99, 120),
(10, 'Levington John Innes No. 3 Compost', 'Suitable for mature plants and shrubs', 6.99, 250),
(11, 'Neudorff Sluggo Slug & Snail Killer', 'Effectively controls slugs and snails', 6.49, 200),
(12, 'Hozelock Wall Mounted Fast Reel', 'Premium hose reel for gardens of all sizes', 89.99, 80),
(13, 'Westland Growmore Garden Fertiliser', 'General purpose fertiliser for all-around garden use', 14.99, 180),
(14, 'Evergreen 4 in 1 Lawn Feed', 'High performance treatment for all lawn types', 19.99, 300),
(15, 'Doff Liquid Growmore Plant Food', 'Balanced plant food for various types', 3.99, 400),
(16, 'Nemasys Vine Weevil Killer', 'Natural solution to control vine weevil grubs', 12.99, 100),
(17, 'Flymo EasiLife 150 Robotic Lawn Mower', 'Advanced mower for lawns up to 150m²', 599.99, 20),
(18, 'Haxnicks Bamboo Plant Labels', 'Eco-friendly labels for identifying plants', 2.49, 600),
(19, 'Spear & Jackson Elements Digging Fork', 'Durable fork for digging and turning soil', 17.99, 100),
(20, 'Tildenet Garden Netting', 'Versatile netting for protecting crops and plants', 8.49, 200),
(21, 'Wolf Garten Hand Trowel', 'High quality trowel for planting and transplanting', 5.99, 150),
(22, 'Bosmere Garden Kneeler', 'Comfortable kneeler for reducing strain while gardening', 14.49, 120),
(23, 'Wilkinson Sword Border Spade', 'High quality spade for edging borders', 24.99, 80),
(24, 'Westland Aftercut Lawn Feed', 'Triple action treatment for a healthy lawn', 12.99, 250),
(25, 'Draper Stainless Steel Hand Fork', 'Corrosion resistant fork for planting and weeding', 7.99, 180),
(26, 'Gardman Hanging Basket Bracket', 'Sturdy bracket for hanging baskets and bird feeders', 3.49, 400),
(27, 'Roundup Path & Drive Weedkiller', 'Fast acting weedkiller for paths and driveways', 14.99, 100),
(28, 'Burgon & Ball Bulb Planter', 'High quality planter for planting bulbs', 29.99, 90),
(29, 'Draper Stainless Steel Hand Trowel', 'Durable trowel for various gardening tasks', 6.99, 220),
(30, 'Gardman Premium Garden Riddle', 'Perfect for removing stones and debris from soil', 9.49, 150),
(31, 'Monstera deliciosa', 'Large, glossy leaves with natural holes', 24.99, 80),
(32, 'Fiddle Leaf Fig', 'Large, fiddle-shaped leaves', 39.99, 60),
(33, 'Lavandula angustifolia', 'Fragrant lavender blooms', 3.49, 200),
(34, 'Pothos', 'Vining plant with heart-shaped leaves', 6.99, 220),
(35, 'Gardman Premium Garden Riddle', 'Perfect for removing stones and debris from soil', 9.49, 150),
(36, 'Rosa Rugosa', 'Fragrant, pink or white flowers', 14.99, 70),
(37, 'Foxglove', 'Tall spikes of tubular flowers', 3.99, 120),
(38, 'Echinacea purpurea', 'Daisy-like flowers in shades of pink and purple', 6.49, 100),
(39, 'Hollyhock', 'Tall spikes of colorful flowers', 5.99, 80),
(40, 'Salvia nemorosa', 'Spikes of purple, pink, or blue flowers', 7.49, 90),
(41, 'Lupinus', 'Tall spikes of pea-like flowers', 4.99, 110),
(42, 'Penstemon', 'Tubular flowers in various colors', 8.99, 60),
(43, 'Delphinium', 'Tall spikes of blue, pink, or white flowers', 9.49, 50),
(44, 'Campanula', 'Bell-shaped flowers in shades of blue, purple, or white', 5.99, 70),
(45, 'Coreopsis', 'Daisy-like flowers in shades of yellow, orange, or pink', 3.99, 100);


CREATE TABLE customers (
		customer_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
		first_name VARCHAR(30) NOT NULL,
		last_name VARCHAR(30) NOT NULL,
		email_address VARCHAR(60) NOT NULL UNIQUE,
		address1 VARCHAR (200) NOT NULL,
		address2 VARCHAR (200),
		postcode VARCHAR(10) NOT NULL,
		mobile INTEGER (13) NOT NULL,
		CONSTRAINT pk_customer_id  PRIMARY KEY (customer_id)
);

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
