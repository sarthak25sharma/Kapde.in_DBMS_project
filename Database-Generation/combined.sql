CREATE DATABASE IF NOT EXISTS KAPDE;

USE KAPDE;

CREATE TABLE IF NOT EXISTS User (
    UserID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(255) NOT NULL,
    CustomerFlag BOOLEAN NOT NULL,
    HouseNumber VARCHAR(255) NOT NULL,
    Locality VARCHAR(255) NOT NULL,
    City VARCHAR(255) NOT NULL,
    State VARCHAR(255) NOT NULL,
    PinCode INT NOT NULL,
    Gender VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Credentials (
    ID INT NOT NULL PRIMARY KEY,
    HashedPassword VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Admin (
    AdminID INT NOT NULL PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS Brand (
    BrandID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    BrandName VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Product (
    ProductID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ProductName NOT NULL VARCHAR(255),
    Description VARCHAR(255),
    Price FLOAT NOT NULL,
    BrandID INT NOT NULL,
    FOREIGN KEY (BrandID) REFERENCES Brand(BrandID) -- Product "Created By" brand relationship
);

CREATE TABLE IF NOT EXISTS Warehouse (
    WarehouseID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    WarehouseName VARCHAR(255) NOT NULL,
    ContactInfo INT NOT NULL,
    ShopNumber VARCHAR(255) NOT NULL,
    Locality VARCHAR(255) NOT NULL,
    City VARCHAR(255) NOT NULL,
    State VARCHAR(255) NOT NULL,
    PinCode INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Cart (
    UserID INT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES User(UserID) -- Each user has exactly one cart
);

CREATE TABLE IF NOT EXISTS CartItem (
    CartItemID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Quantity INT NOT NULL,
    ProductID INT NOT NULL,
    UserID INT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    -- "IsCartProduct"
    FOREIGN KEY (UserID) REFERENCES User(UserID) -- "CartContains" belongs to which art
);

CREATE TABLE IF NOT EXISTS Order (
    OrderID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalAmount FLOAT NOT NULL,
    HouseNo INT NOT NULL,
    Locality VARCHAR(255) NOT NULL,
    City VARCHAR(255) NOT NULL,
    State VARCHAR(255) NOT NULL,
    Pincode INT NOT NULL,
    PayMethod VARCHAR(255) NOT NULL,
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

CREATE TABLE IF NOT EXISTS OrderItem (
    OrderItemID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Order(OrderID),
    -- "OrderContains" belongs to which order
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) -- "IsOrderProduct"
);

-- RELATIONSHIPS
-- Warehouse STORES Product
CREATE TABLE IF NOT EXISTS Stores (
    ProductID INT NOT NULL,
    WarehouseID INT NOT NULL,
    Quantity INT,
    PRIMARY KEY (ProductID, WarehouseID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID)
);

-- Brand SUPPLIES Warehouse
CREATE TABLE IF NOT EXISTS Supplies (
    BrandID INT NOT NULL,
    WarehouseID INT NOT NULL,
    Quantity INT,
    PRIMARY KEY (BrandID, WarehouseID),
    FOREIGN KEY (BrandID) REFERENCES Brand(BrandID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID)
);

-- Orders TERNARY relationship
CREATE TABLE IF NOT EXISTS Orders (
    CartItemID INT NOT NULL,
    OrderID INT NOT NULL,
    OrderItemID INT NOT NULL,
    PRIMARY KEY (CartItemID, OrderID, OrderItemID),
    FOREIGN KEY (CartItemID) REFERENCES CartItem(CartItemID),
    FOREIGN KEY (OrderID) REFERENCES Order(OrderID),
    FOREIGN KEY (OrderItemID) REFERENCES OrderItem(OrderItemID)
);


-- POPULATE THE DATABASE

INSERT INTO user (customer_flag, user_name, house_number, locality, city, state, pin_code, country, gender)
VALUES (1, 'Amit Singh', 'A-123', 'Connaught Place', 'New Delhi', 'Delhi', 110001, 'India', 'Male'),
       (1, 'Deepika Sharma', 'B-456', 'Koregaon Park', 'Pune', 'Maharashtra', 411001, 'India', 'Female'),
       (1, 'Vikram Patel', 'C-789', 'Koramangala', 'Bangalore', 'Karnataka', 560001, 'India', 'Male'),
       (1, 'Ananya Gupta', 'D-456', 'Baner', 'Pune', 'Maharashtra', 411045, 'India', 'Female'),
       (1, 'Rahul Kumar', 'E-789', 'Malviya Nagar', 'Jaipur', 'Rajasthan', 302017, 'India', 'Male'),
       (1, 'Neha Agarwal', 'F-101', 'Viman Nagar', 'Pune', 'Maharashtra', 411014, 'India', 'Female'),
       (1, 'Rajesh Singh', 'G-123', 'Bandra', 'Mumbai', 'Maharashtra', 400050, 'India', 'Male'),
       (1, 'Pooja Sharma', 'H-456', 'Sadar Bazaar', 'Agra', 'Uttar Pradesh', 282001, 'India', 'Female'),
       (1, 'Sandeep Kumar', 'I-789', 'Indiranagar', 'Bangalore', 'Karnataka', 560008, 'India', 'Male'),
       (1, 'Anjali Mishra', 'J-101', 'Gomti Nagar', 'Lucknow', 'Uttar Pradesh', 226010, 'India', 'Female'),
       (1, 'Manoj Patel', 'K-123', 'Ballygunge', 'Kolkata', 'West Bengal', 700019, 'India', 'Male'),
       (1, 'Shreya Gupta', 'L-456', 'Jayanagar', 'Bangalore', 'Karnataka', 560011, 'India', 'Female'),
       (1, 'Arun Kumar', 'M-789', 'Anna Nagar', 'Chennai', 'Tamil Nadu', 600040, 'India', 'Male'),
       (1, 'Riya Singh', 'N-101', 'Alipore', 'Kolkata', 'West Bengal', 700027, 'India', 'Female'),
       (1, 'Sanjay Sharma', 'O-123', 'Hinjewadi', 'Pune', 'Maharashtra', 411057, 'India', 'Male'),
       (1, 'Ananya Verma', 'P-456', 'Juhu', 'Mumbai', 'Maharashtra', 400049, 'India', 'Female'),
       (1, 'Vivek Gupta', 'Q-789', 'Nungambakkam', 'Chennai', 'Tamil Nadu', 600034, 'India', 'Male'),
       (1, 'Preeti Patel', 'R-101', 'Kukatpally', 'Hyderabad', 'Telangana', 500072, 'India', 'Female'),
       (1, 'Kunal Shah', 'S-123', 'M.G. Road', 'Bangalore', 'Karnataka', 560001, 'India', 'Male'),
       (1, 'Swati Mishra', 'T-456', 'Jayanagar', 'Bangalore', 'Karnataka', 560069, 'India', 'Female'),
       (1, 'Rahul Sharma', 'U-789', 'Hazratganj', 'Lucknow', 'Uttar Pradesh', 226001, 'India', 'Male'),
       (1, 'Shivani Gupta', 'V-101', 'Dadar', 'Mumbai', 'Maharashtra', 400014, 'India', 'Female'),
       (1, 'Alok Singh', 'W-123', 'Salt Lake City', 'Kolkata', 'West Bengal', 700064, 'India', 'Male'),
       (1, 'Meera Patel', 'X-456', 'Pashan', 'Pune', 'Maharashtra', 411021, 'India', 'Female'),
       (1, 'Rahul Verma', 'Y-789', 'Thiruvanmiyur', 'Chennai', 'Tamil Nadu', 600041, 'India', 'Male'),
       (1, 'Kavya Sharma', 'Z-101', 'Koramangala', 'Bangalore', 'Karnataka', 560034, 'India', 'Female'),
       (1, 'Amit Singh', 'AA-123', 'Hadapsar', 'Pune', 'Maharashtra', 411028, 'India', 'Male'),
       (1, 'Shweta Gupta', 'AB-456', 'Kalina', 'Mumbai', 'Maharashtra', 400098, 'India', 'Female');


INSERT INTO warehouse (warehouse_name, contact_number, shop_number, locality, city, state, pin_code, country)
VALUES ('The Great Delhi Warehouse', '9870345678', '102', 'Central Delhi', 'Delhi', 'Delhi', 110001, 'India'),
       ('The Classic Mumbai Warehouse', '9870123456', '267', 'South Mumbai', 'Mumbai', 'Maharashtra', 400001, 'India'),
       ('Bangalore Storage', '98709870654', '394', 'Koramangala', 'Bangalore', 'Karnataka', 560001, 'India'),
       ('Chennai Depot', '9870234567', '507', 'T. Nagar', 'Chennai', 'Tamil Nadu', 600001, 'India'),
       ('Kolkata Distribution Center', '9870789654', '623', 'Salt Lake City', 'Kolkata', 'West Bengal', 700001, 'India'),
       ('Hyderabad Supply Hub', '9870456789', '735', 'Gachibowli', 'Hyderabad', 'Telangana', 500001, 'India'),
       ('Pune Logistics', '9870234567', '852', 'Koregaon Park', 'Pune', 'Maharashtra', 411001, 'India'),
       ('Ahmedabad Warehouse', '9870789654', '924', 'Vastrapur', 'Ahmedabad', 'Gujarat', 380001, 'India'),
       ('Surat Distribution Center', '9870123456', '103', 'Adajan', 'Surat', 'Gujarat', 395001, 'India'),
       ('Jaipur Storage', '98709870654', '287', 'Malviya Nagar', 'Jaipur', 'Rajasthan', 302001, 'India'),
       ('Lucknow Warehouse', '9870345678', '394', 'Gomti Nagar', 'Lucknow', 'Uttar Pradesh', 226001, 'India'),
       ('Kanpur Depot', '9870123456', '407', 'Civil Lines', 'Kanpur', 'Uttar Pradesh', 208001, 'India'),
       ('Nagpur Storage', '98709870654', '523', 'Dharampeth', 'Nagpur', 'Maharashtra', 440001, 'India'),
       ('Indore Distribution Center', '9870234567', '635', 'Vijay Nagar', 'Indore', 'Madhya Pradesh', 452001, 'India'),
       ('Thane Warehouse', '9870789654', '752', 'Thane West', 'Thane', 'Maharashtra', 400601, 'India'),
       ('Bhopal Depot', '9870456789', '824', 'Arera Colony', 'Bhopal', 'Madhya Pradesh', 462001, 'India'),
       ('Visakhapatnam Warehouse', '9870234567', '903', 'Dwaraka Nagar', 'Visakhapatnam', 'Andhra Pradesh', 530001, 'India'),
       ('Patna Storage', '9870789654', '127', 'Kankarbagh', 'Patna', 'Bihar', 800001, 'India'),
       ('Ludhiana Warehouse', '9870123456', '203', 'Model Town', 'Ludhiana', 'Punjab', 141001, 'India'),
       ('Agra Workshop', '9870987654', '367', 'Sadar Bazaar', 'Agra', 'Uttar Pradesh', 282001, 'India');


INSERT INTO brand (brand_name)
VALUES ('Louis Vuitton'),
       ('Gucci'),
       ('Prada'),
       ('CHANEL'),
       ('Dior'),
       ('Hermès'),
       ('Ralph Lauren'),
       ('Versace'),
       ('Balenciaga'),
       ('Adidas'),
       ('Armani'),
       ('Burberry'),
       ('Dolce and Gabbana logo'),
       ('Nike'),
       ('Fendi'),
       ('Saint Laurent'),
       ('ZARA'),
       ('Valentino');


INSERT INTO product (product_name, product_description, price, brandID)
VALUES ('CHANEL Baggy Textured Jogger 3XL', 'Trendy Jogger by CHANEL', 3314, 3),
       ('Burberry Oversized Denim Jeans S', 'Trendy Jeans by Burberry', 4147, 11),
       ('ZARA Oversized Textured Pullover XL', 'Trendy Pullover by ZARA', 4415, 16),
       ('Ralph Lauren Relaxed Denim Short 3XL', 'Trendy Short by Ralph Lauren', 4691, 6),
       ('Armani Straight Corduroy Sweater XL', 'Trendy Sweater by Armani', 2661, 10),
       ('Saint Laurent Baggy Denim Jacket M', 'Trendy Jacket by Saint Laurent', 4708, 15),
       ('ZARA Loose Ribbed Blazer XXL', 'Trendy Blazer by ZARA', 4775, 16),
       ('ZARA Oversized Ribbed Sweatshirt XXS', 'Trendy Sweatshirt by ZARA', 2931, 16),
       ('Fendi Slim Denim Capri XXS', 'Trendy Capri by Fendi', 3826, 14),
       ('Nike Relaxed Corduroy Jeans 3XL', 'Trendy Jeans by Nike', 2687, 13),
       ('Ralph Lauren Relaxed Textured Capri XXS', 'Trendy Capri by Ralph Lauren', 3671, 6),
       ('Prada Relaxed Denim Blazer L', 'Trendy Blazer by Prada', 2269, 2),
       ('Fendi Baggy Denim Cargo S', 'Trendy Cargo by Fendi', 4402, 14),
       ('Armani Slim Corduroy Jacket XXL', 'Trendy Jacket by Armani', 2315, 10),
       ('Nike Oversized Ribbed Pant XXL', 'Trendy Pant by Nike', 2611, 13),
       ('Louis Vuitton Oversized Denim Shirt XL', 'Trendy Shirt by Louis Vuitton', 4995, 0),
       ('Hermes Oversized Ribbed Coat XL', 'Trendy Coat by Hermes', 3041, 5),
       ('CHANEL Loose Corduroy Jogger S', 'Trendy Jogger by CHANEL', 2422, 3),
       ('Dior Straight Textured Jacket XL', 'Trendy Jacket by Dior', 3312, 4),
       ('Gucci Regular Colour-Block Overshirt S', 'Trendy Overshirt by Gucci', 2188, 1),
       ('ZARA Relaxed Textured Shirt L', 'Trendy Shirt by ZARA', 2638, 16),
       ('CHANEL Baggy Textured Pullover L', 'Trendy Pullover by CHANEL', 3687, 3),
       ('Valentino Baggy Plain Jacket M', 'Trendy Jacket by Valentino', 2898, 17),
       ('Dior Relaxed Colour-Block Capri S', 'Trendy Capri by Dior', 4305, 4),
       ('Dior Oversized Ribbed Sweatshirt XL', 'Trendy Sweatshirt by Dior', 4405, 4),
       ('Gucci Slim Colour-Block Sweatpants XL', 'Trendy Sweatpants by Gucci', 2497, 1),
       ('Valentino Relaxed Denim Coat S', 'Trendy Coat by Valentino', 3865, 17),
       ('Burberry Baggy Textured Cargo XS', 'Trendy Cargo by Burberry', 3124, 11),
       ('Hermes Regular Textured Short XXS', 'Trendy Short by Hermes', 3519, 5),
       ('Armani Baggy Denim Sweatshirt L', 'Trendy Sweatshirt by Armani', 3538, 10),
       ('Burberry Regular Denim Jogger S', 'Trendy Jogger by Burberry', 2420, 11),
       ('Hermes Relaxed Ribbed Jeans L', 'Trendy Jeans by Hermes', 3223, 5),
       ('Fendi Baggy Denim Jeans XL', 'Trendy Jeans by Fendi', 3294, 14),
       ('Burberry Loose Ribbed Short S', 'Trendy Short by Burberry', 3190, 11),
       ('Balenciaga Baggy Corduroy Capri S', 'Trendy Capri by Balenciaga', 2629, 8),
       ('Ralph Lauren Loose Plain Cargo XL', 'Trendy Cargo by Ralph Lauren', 4729, 6),
       ('ZARA Straight Denim Jogger XS', 'Trendy Jogger by ZARA', 3279, 16),
       ('Fendi Baggy Colour-Block Capri M', 'Trendy Capri by Fendi', 2810, 14),
       ('Burberry Slim Corduroy Short S', 'Trendy Short by Burberry', 4745, 11),
       ('Valentino Relaxed Colour-Block Sweatpants 3XL', 'Trendy Sweatpants by Valentino', 3843, 17),
       ('Balenciaga Slim Denim Pant M', 'Trendy Pant by Balenciaga', 3163, 8),
       ('Ralph Lauren Relaxed Denim Overshirt M', 'Trendy Overshirt by Ralph Lauren', 2986, 6),
       ('Burberry Regular Plain Cargo L', 'Trendy Cargo by Burberry', 3893, 11),
       ('Armani Loose Ribbed Sweatpants 3XL', 'Trendy Sweatpants by Armani', 4754, 10),
       ('Dior Loose Denim Trousers XXL', 'Trendy Trousers by Dior', 2687, 4),
       ('CHANEL Oversized Denim Trousers XXS', 'Trendy Trousers by CHANEL', 4292, 3),
       ('Gucci Straight Textured Hoodie XXS', 'Trendy Hoodie by Gucci', 2176, 1),
       ('Fendi Baggy Denim Shirt XXL', 'Trendy Shirt by Fendi', 4375, 14),
       ('Ralph Lauren Baggy Textured Capri XXS', 'Trendy Capri by Ralph Lauren', 2742, 6),
       ('Louis Vuitton Relaxed Textured Sweatshirt XXL', 'Trendy Sweatshirt by Louis Vuitton', 4414, 0);


INSERT INTO Order (OrderID, UserID, OrderDate, TotalAmount, HouseNo, Locality, City, State, Pincode, PayMethod) 
VALUES  (9, '2024-02-12', 12913, 'Y-2525', 'Rajbagh', 'Srinagar', 'Jammu and Kashmir', 190001, 'Netbanking'),
        (22, '2024-02-12', 14984, 'U-2121', 'Sector 15', 'Faridabad', 'Haryana', 121001, 'Credit Card'),
        (11, '2024-02-12', 13783, 'T-2020', 'Sanjay Place', 'Agra', 'Uttar Pradesh', 282001, 'Debit Card'),
        (23, '2024-02-12', 16176, 'AD-3030', 'Paona Bazaar', 'Imphal', 'Manipur', 795001, 'Credit Card'),
        (18, '2024-02-12', 12799, 'A-101', 'Colaba', 'Mumbai', 'Maharashtra', 400001, 'UPI'),
        (10, '2024-02-12', 9780, 'B-202', 'Connaught Place', 'Delhi', 'Delhi', 110001, 'Cash on Delivery'),
        (18, '2024-02-12', 14454, 'AC-2929', 'Tadong', 'Gangtok', 'Sikkim', 737101, 'Cash on Delivery'),
        (20, '2024-02-12', 11018, 'M-1313', 'Dhantoli', 'Nagpur', 'Maharashtra', 440001, 'Netbanking'),
        (16, '2024-02-12', 15962, 'U-2121', 'Sector 15', 'Faridabad', 'Haryana', 121001, 'Debit Card'),
        (21, '2024-02-12', 13965, 'L-1212', 'Civil Lines', 'Kanpur', 'Uttar Pradesh', 208001, 'Cash on Delivery'),
        (10, '2024-02-12', 16271, 'W-2323', 'Jubilee Chowk', 'Rajkot', 'Gujarat', 360001, 'Netbanking'),
        (17, '2024-02-12', 12845, 'I-909', 'Adajan', 'Surat', 'Gujarat', 395001, 'Debit Card'),
        (23, '2024-02-12', 14538, 'D-404', 'T Nagar', 'Chennai', 'Tamil Nadu', 600001, 'Credit Card'),
        (12, '2024-02-12', 14932, 'D-404', 'T Nagar', 'Chennai', 'Tamil Nadu', 600001, 'Credit Card'),
        (23, '2024-02-12', 16763, 'AB-2828', 'Rajpur Road', 'Dehradun', 'Uttarakhand', 248001, 'Credit Card'),
        (19, '2024-02-12', 15137, 'C-303', 'Indiranagar', 'Bangalore', 'Karnataka', 560001, 'Credit Card'),
        (6, '2024-02-12', 14938, 'U-2121', 'Sector 15', 'Faridabad', 'Haryana', 121001, 'Credit Card'),
        (17, '2024-02-12', 12115, 'AD-3030', 'Paona Bazaar', 'Imphal', 'Manipur', 795001, 'Debit Card'),
        (21, '2024-02-12', 15539, 'C-303', 'Indiranagar', 'Bangalore', 'Karnataka', 560001, 'UPI'),
        (5, '2024-02-12', 11736, 'B-202', 'Connaught Place', 'Delhi', 'Delhi', 110001, 'Netbanking');

INSERT INTO OrderItem (OrderItemID, OrderID, ProductID, Quantity) 
VALUES  (0, 0, 0, 1),
        (1, 0, 29, 1),
        (2, 0, 22, 1),
        (3, 0, 40, 1),
        (4, 1, 10, 1),
        (5, 1, 49, 1),
        (6, 1, 12, 1),
        (7, 1, 25, 1),
        (8, 2, 32, 1),
        (9, 2, 26, 1),
        (10, 2, 18, 1),
        (11, 2, 18, 1),
        (12, 3, 42, 1),
        (13, 3, 43, 1),
        (14, 3, 27, 1),
        (15, 3, 24, 1),
        (16, 4, 14, 1),
        (17, 4, 40, 1),
        (18, 4, 49, 1),
        (19, 4, 14, 1),
        (20, 5, 9, 1),
        (21, 5, 30, 1),
        (22, 5, 25, 1),
        (23, 5, 46, 1),
        (24, 6, 33, 1),
        (25, 6, 49, 1),
        (26, 6, 18, 1),
        (27, 6, 29, 1),
        (28, 7, 44, 1),
        (29, 7, 31, 1),
        (30, 7, 25, 1),
        (31, 7, 14, 1),
        (32, 8, 15, 1),
        (33, 8, 26, 1),
        (34, 8, 44, 1),
        (35, 8, 2, 1),
        (36, 9, 17, 1),
        (37, 9, 3, 1),
        (38, 9, 29, 1),
        (39, 9, 0, 1),
        (40, 10, 3, 1),
        (41, 10, 42, 1),
        (42, 10, 47, 1),
        (43, 10, 18, 1),
        (44, 11, 37, 1),
        (45, 11, 8, 1),
        (46, 11, 31, 1),
        (47, 11, 41, 1),
        (48, 12, 21, 1),
        (49, 12, 14, 1),
        (50, 12, 49, 1),
        (51, 12, 8, 1),
        (52, 13, 24, 1),
        (53, 13, 34, 1),
        (54, 13, 5, 1),
        (55, 13, 33, 1),
        (56, 14, 45, 1),
        (57, 14, 49, 1),
        (58, 14, 38, 1),
        (59, 14, 18, 1),
        (60, 15, 23, 1),
        (61, 15, 40, 1),
        (62, 15, 47, 1),
        (63, 15, 32, 1),
        (64, 16, 21, 1),
        (65, 16, 37, 1),
        (66, 16, 43, 1),
        (67, 16, 21, 1),
        (68, 17, 9, 1),
        (69, 17, 29, 1),
        (70, 17, 14, 1),
        (71, 17, 36, 1),
        (72, 18, 42, 1),
        (73, 18, 47, 1),
        (74, 18, 1, 1),
        (75, 18, 27, 1),
        (76, 19, 19, 1),
        (77, 19, 20, 1),
        (78, 19, 31, 1),
        (79, 19, 21, 1);

