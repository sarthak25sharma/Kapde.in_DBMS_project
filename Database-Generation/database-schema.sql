CREATE DATABASE IF NOT EXISTS CBMS;
USE CBMS;

-- UTILITIY TABLES

CREATE TABLE IF NOT EXISTS user (
    userID INT NOT NULL AUTO_INCREMENT,
    customer_flag TINYINT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    house_number VARCHAR(255) NOT NULL,
    locality VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    pin_code INT NOT NULL,
    country VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    PRIMARY KEY (userID)
);

CREATE TABLE IF NOT EXISTS warehouse (
    warehouseID INT NOT NULL AUTO_INCREMENT,
    warehouse_name VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    shop_number VARCHAR(255) NOT NULL,
    locality VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    pin_code INT NOT NULL,
    country VARCHAR(255) NOT NULL,
    PRIMARY KEY (warehouseID)
);

CREATE TABLE IF NOT EXISTS brand (
    brandID INT NOT NULL AUTO_INCREMENT,
    brand_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (brandID)
);

CREATE TABLE IF NOT EXISTS product (
    productID INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    product_description VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    brandID INT NOT NULL,
    PRIMARY KEY (productID),
    FOREIGN KEY (brandID) REFERENCES brand(brandID)
);

CREATE TABLE IF NOT EXISTS credentials (
    credID INT NOT NULL AUTO_INCREMENT,
    hashed_password VARCHAR(255) NOT NULL,
    PRIMARY KEY (credID)
);

CREATE TABLE IF NOT EXISTS admin (
    adminID INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (adminID)
);

CREATE TABLE IF NOT EXISTS cart (
    userID INT NOT NULL,
    PRIMARY KEY (userID),
    FOREIGN KEY (userID) REFERENCES user(userID)
);

CREATE TABLE IF NOT EXISTS cartItem (
    cartItemID INT NOT NULL AUTO_INCREMENT,
    quantity INT NOT NULL,
    productID INT NOT NULL,
    PRIMARY KEY (cartItemID),
    FOREIGN KEY (productID) REFERENCES product(productID)
);

CREATE TABLE IF NOT EXISTS orderList (
    orderID INT NOT NULL AUTO_INCREMENT,
    userID INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount FLOAT NOT NULL,
	house_number INT NOT NULL,
    locality VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    pin_code INT NOT NULL,
    country VARCHAR(255) NOT NULL,
    pay_method VARCHAR(255) NOT NULL,
    PRIMARY KEY (orderID),
    FOREIGN KEY (userID) REFERENCES user(userID)
);


CREATE TABLE IF NOT EXISTS orderItem (
    orderItemID INT NOT NULL AUTO_INCREMENT,
    orderID INT NOT NULL,
    productID INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (orderItemID),
    FOREIGN KEY (orderID) REFERENCES orderList(orderID),
    FOREIGN KEY (productID) REFERENCES product(productID)
);
