import sqlite3
from typing import List, Any

from tabulate import tabulate

from tables import User, Brand, Product, CartItem

import queries

con = sqlite3.connect("db.sqlite")

USER_ID = [2]
IS_USER_LOGGED_IN = False

IS_ADMIN_LOGGED_IN = False


def init_users():
    users = ["('Amit Singh', 'A-123', 'Connaught Place', 'New Delhi', 'Delhi', 110001, 'India', 'M')",
             "('Deepika Sharma', 'B-456', 'Koregaon Park', 'Pune', 'Maharashtra', 411001, 'India', 'F')",
             "('Vikram Patel', 'C-789', 'Koramangala', 'Bangalore', 'Karnataka', 560001, 'India', 'M')",
             "('Ananya Gupta', 'D-456', 'Baner', 'Pune', 'Maharashtra', 411045, 'India', 'F')",
             "('Rahul Kumar', 'E-789', 'Malviya Nagar', 'Jaipur', 'Rajasthan', 302017, 'India', 'M')",
             "('Neha Agarwal', 'F-101', 'Viman Nagar', 'Pune', 'Maharashtra', 411014, 'India', 'F')",
             "('Rajesh Singh', 'G-123', 'Bandra', 'Mumbai', 'Maharashtra', 400050, 'India', 'M')",
             "('Pooja Sharma', 'H-456', 'Sadar Bazaar', 'Agra', 'Uttar Pradesh', 282001, 'India', 'F')",
             "('Sandeep Kumar', 'I-789', 'Indiranagar', 'Bangalore', 'Karnataka', 560008, 'India', 'M')",
             "('Anjali Mishra', 'J-101', 'Gomti Nagar', 'Lucknow', 'Uttar Pradesh', 226010, 'India', 'F')",
             "('Manoj Patel', 'K-123', 'Ballygunge', 'Kolkata', 'West Bengal', 700019, 'India', 'M')",
             "('Shreya Gupta', 'L-456', 'Jayanagar', 'Bangalore', 'Karnataka', 560011, 'India', 'F')",
             "('Arun Kumar', 'M-789', 'Anna Nagar', 'Chennai', 'Tamil Nadu', 600040, 'India', 'M')",
             "('Riya Singh', 'N-101', 'Alipore', 'Kolkata', 'West Bengal', 700027, 'India', 'F')",
             "('Sanjay Sharma', 'O-123', 'Hinjewadi', 'Pune', 'Maharashtra', 411057, 'India', 'M')",
             "('Ananya Verma', 'P-456', 'Juhu', 'Mumbai', 'Maharashtra', 400049, 'India', 'F')",
             "('Vivek Gupta', 'Q-789', 'Nungambakkam', 'Chennai', 'Tamil Nadu', 600034, 'India', 'M')",
             "('Preeti Patel', 'R-101', 'Kukatpally', 'Hyderabad', 'Telangana', 500072, 'India', 'F')",
             "('Kunal Shah', 'S-123', 'M.G. Road', 'Bangalore', 'Karnataka', 560001, 'India', 'M')",
             "('Swati Mishra', 'T-456', 'Jayanagar', 'Bangalore', 'Karnataka', 560069, 'India', 'F')",
             "('Rahul Sharma', 'U-789', 'Hazratganj', 'Lucknow', 'Uttar Pradesh', 226001, 'India', 'M')",
             "('Shivani Gupta', 'V-101', 'Dadar', 'Mumbai', 'Maharashtra', 400014, 'India', 'F')",
             "('Alok Singh', 'W-123', 'Salt Lake City', 'Kolkata', 'West Bengal', 700064, 'India', 'M')",
             "('Meera Patel', 'X-456', 'Pashan', 'Pune', 'Maharashtra', 411021, 'India', 'F')",
             "('Rahul Verma', 'Y-789', 'Thiruvanmiyur', 'Chennai', 'Tamil Nadu', 600041, 'India', 'M')",
             "('Kavya Sharma', 'Z-101', 'Koramangala', 'Bangalore', 'Karnataka', 560034, 'India', 'F')",
             "('Amit Singh', 'AA-123', 'Hadapsar', 'Pune', 'Maharashtra', 411028, 'India', 'M')",
             "('Shweta Gupta', 'AB-456', 'Kalina', 'Mumbai', 'Maharashtra', 400098, 'India', 'F')", ]

    for u in users:
        queries.insert_user(con, u)

    con.commit()


def init_brands():
    brands = [('Louis Vuitton'),
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
              ('Valentino')]

    for b in brands:
        queries.insert_brand(con, b)

    con.commit()


def init_products():
    products = ["('CHANEL Baggy Textured Jogger 3XL', 'Trendy Jogger by CHANEL', 3314, 4)",
                "('Burberry Oversized Denim Jeans S', 'Trendy Jeans by Burberry', 4147, 12)",
                "('ZARA Oversized Textured Pullover XL', 'Trendy Pullover by ZARA', 4415, 17)",
                "('Ralph Lauren Relaxed Denim Short 3XL', 'Trendy Short by Ralph Lauren', 4691, 7)",
                "('Armani Straight Corduroy Sweater XL', 'Trendy Sweater by Armani', 2661, 11)",
                "('Saint Laurent Baggy Denim Jacket M', 'Trendy Jacket by Saint Laurent', 4708, 16)",
                "('ZARA Loose Ribbed Blazer XXL', 'Trendy Blazer by ZARA', 4775, 17)",
                "('ZARA Oversized Ribbed Sweatshirt XXS', 'Trendy Sweatshirt by ZARA', 2931, 17)",
                "('Fendi Slim Denim Capri XXS', 'Trendy Capri by Fendi', 3826, 15)",
                "('Nike Relaxed Corduroy Jeans 3XL', 'Trendy Jeans by Nike', 2687, 14)",
                "('Ralph Lauren Relaxed Textured Capri XXS', 'Trendy Capri by Ralph Lauren', 3671, 7)",
                "('Prada Relaxed Denim Blazer L', 'Trendy Blazer by Prada', 2269, 3)",
                "('Fendi Baggy Denim Cargo S', 'Trendy Cargo by Fendi', 4402, 15)",
                "('Armani Slim Corduroy Jacket XXL', 'Trendy Jacket by Armani', 2315, 11)",
                "('Nike Oversized Ribbed Pant XXL', 'Trendy Pant by Nike', 2611, 14)",
                "('Louis Vuitton Oversized Denim Shirt XL', 'Trendy Shirt by Louis Vuitton', 4995, 1)",
                "('Hermes Oversized Ribbed Coat XL', 'Trendy Coat by Hermes', 3041, 6)",
                "('CHANEL Loose Corduroy Jogger S', 'Trendy Jogger by CHANEL', 2422, 4)",
                "('Dior Straight Textured Jacket XL', 'Trendy Jacket by Dior', 3312, 5)",
                "('Gucci Regular Colour-Block Overshirt S', 'Trendy Overshirt by Gucci', 2188, 2)",
                "('ZARA Relaxed Textured Shirt L', 'Trendy Shirt by ZARA', 2638, 17)",
                "('CHANEL Baggy Textured Pullover L', 'Trendy Pullover by CHANEL', 3687, 4)",
                "('Valentino Baggy Plain Jacket M', 'Trendy Jacket by Valentino', 2898, 18)",
                "('Dior Relaxed Colour-Block Capri S', 'Trendy Capri by Dior', 4305, 5)",
                "('Dior Oversized Ribbed Sweatshirt XL', 'Trendy Sweatshirt by Dior', 4405, 5)",
                "('Gucci Slim Colour-Block Sweatpants XL', 'Trendy Sweatpants by Gucci', 2497, 2)",
                "('Valentino Relaxed Denim Coat S', 'Trendy Coat by Valentino', 3865, 18)",
                "('Burberry Baggy Textured Cargo XS', 'Trendy Cargo by Burberry', 3124, 12)",
                "('Hermes Regular Textured Short XXS', 'Trendy Short by Hermes', 3519, 6)",
                "('Armani Baggy Denim Sweatshirt L', 'Trendy Sweatshirt by Armani', 3538, 11)",
                "('Burberry Regular Denim Jogger S', 'Trendy Jogger by Burberry', 2420, 12)",
                "('Hermes Relaxed Ribbed Jeans L', 'Trendy Jeans by Hermes', 3223, 6)",
                "('Fendi Baggy Denim Jeans XL', 'Trendy Jeans by Fendi', 3294, 15)",
                "('Burberry Loose Ribbed Short S', 'Trendy Short by Burberry', 3190, 12)",
                "('Balenciaga Baggy Corduroy Capri S', 'Trendy Capri by Balenciaga', 2629, 9)",
                "('Ralph Lauren Loose Plain Cargo XL', 'Trendy Cargo by Ralph Lauren', 4729, 7)",
                "('ZARA Straight Denim Jogger XS', 'Trendy Jogger by ZARA', 3279, 17)",
                "('Fendi Baggy Colour-Block Capri M', 'Trendy Capri by Fendi', 2810, 15)",
                "('Burberry Slim Corduroy Short S', 'Trendy Short by Burberry', 4745, 12)",
                "('Valentino Relaxed Colour-Block Sweatpants 3XL', 'Trendy Sweatpants by Valentino', 3843, 18)",
                "('Balenciaga Slim Denim Pant M', 'Trendy Pant by Balenciaga', 3163, 9)",
                "('Ralph Lauren Relaxed Denim Overshirt M', 'Trendy Overshirt by Ralph Lauren', 2986, 7)",
                "('Burberry Regular Plain Cargo L', 'Trendy Cargo by Burberry', 3893, 12)",
                "('Armani Loose Ribbed Sweatpants 3XL', 'Trendy Sweatpants by Armani', 4754, 11)",
                "('Dior Loose Denim Trousers XXL', 'Trendy Trousers by Dior', 2687, 5)",
                "('CHANEL Oversized Denim Trousers XXS', 'Trendy Trousers by CHANEL', 4292, 4)",
                "('Gucci Straight Textured Hoodie XXS', 'Trendy Hoodie by Gucci', 2176, 2)",
                "('Fendi Baggy Denim Shirt XXL', 'Trendy Shirt by Fendi', 4375, 15)",
                "('Ralph Lauren Baggy Textured Capri XXS', 'Trendy Capri by Ralph Lauren', 2742, 7)",
                "('Louis Vuitton Relaxed Textured Sweatshirt XXL', 'Trendy Sweatshirt by Louis Vuitton', 4414, 1)"]

    for p in products:
        queries.insert_product(con, p)

    con.commit()


def init_cart_items():
    cart_items = ["(35, 5, 5)",
                  "(6, 27, 4)",
                  "(44, 3, 8)",
                  "(46, 13, 13)",
                  "(25, 7, 15)",
                  "(29, 15, 3)",
                  "(50, 13, 15)",
                  "(23, 19, 3)",
                  "(16, 17, 6)",
                  "(50, 25, 14)",
                  "(32, 26, 3)",
                  "(50, 5, 15)",
                  "(24, 12, 5)",
                  "(20, 11, 4)",
                  "(26, 17, 11)",
                  "(15, 21, 7)",
                  "(43, 28, 9)",
                  "(24, 13, 9)",
                  "(4, 28, 5)",
                  "(10, 15, 11)",
                  "(41, 2, 13)",
                  "(35, 13, 1)",
                  "(39, 6, 11)",
                  "(16, 13, 9)",
                  "(22, 2, 3)",
                  "(40, 6, 11)",
                  "(44, 8, 10)",
                  "(11, 7, 3)",
                  "(7, 10, 15)",
                  "(22, 5, 8)"]

    for c in cart_items:
        queries.insert_cart_item(con, c)

    con.commit()


def populate():
    init_users()
    init_brands()
    init_products()
    init_cart_items()
    queries.add_triggers(con)
    # print(queries.remove_product_having_id(con, 35).fetchall()) # Trigger 1
    con.commit()


def commit_all():
    con.commit()


def search_product():
    product_name = input("Enter product name to search: ")
    search_results = queries.search_product_by_name(con, product_name)
    if search_results is not None:
        search_results = search_results.fetchall()
        if len(search_results) == 0:
            print("No products")
            return
        queries.print_table(con, Product, search_results)


# ADMIN FUNCTIONS - INVENTORY MANAGEMENT

def set_user_logged_in(val: bool):
    global IS_USER_LOGGED_IN
    IS_USER_LOGGED_IN = val


def remove_product():
    print("Remove product")
    product_id = int(input("Enter product id"))
    queries.remove_product_having_id(con, product_id)
    if queries is None:
        print("No products were removed")


def add_product():
    print("Add product")
    name = input("Enter product name: ")
    price = float(input("Enter product price: ").strip())
    description = input("Enter product description: ").strip()
    brand_id = int(input("Enter product brand_id: "))
    # ({Product.name}, {Product.description}, {Product.price}, {Product.brand_id})
    params = f"('{name}', '{description}', {price}, {brand_id})"
    queries.insert_product(con, params)


def print_all_tables():
    queries.print_tables(con)


# USER FUNCTIONS

def login_as_user(user_id: int, password: str) -> bool:
    password = password.strip()

    results = queries.search_user_by_id_pass(con, user_id, password)
    if results is None or len(results.fetchall()) == 0:
        print("No such user")
        return False

    user_tuple = results.fetchone()
    set_user_logged_in(True)
    print("changing global user_id to", user_id)
    USER_ID[0] = user_id
    print(USER_ID[0])
    return True


def logout_as_user():
    set_user_logged_in(False)


def view_products():
    queries.print_table(con, Product)


def get_user_cart(user_id: int = USER_ID[0]) -> list[Any]:
    print("viewing user_cart, the user id is ", user_id)
    headers, cursor = queries.show_user_cart(con, user_id)
    data = cursor.fetchall()
    print(tabulate(data, headers=headers, tablefmt="rounded_grid"))
    return data


def add_product_to_cart():
    print("Add product to cart")
    product_id = int(input("Enter product id: ").strip())
    quantity = int(input("Enter quantity:").strip())
    params = f"({product_id}, {USER_ID[0]}, {quantity})"
    queries.insert_cart_item(con, params)


def place_order():
    print("Place order")
    data = get_user_cart(USER_ID[0])
    total = 0
    for item in data:
        total += item[-1]
    print("Total order amount: Rs.", total)

    key = input("Enter y to place the order and x to go back: ").strip()
    if key != 'y':
        print("Going back...")
        return
    print("Placing order...")
    otp = input("Enter your OTP: ")
    if otp.lower().strip() == "abc":
        queries.place_order(con, USER_ID[0])
        print("Order placed successfully!")
        queries.print_tables(con)
    else:
        print("Invalid OTP!")


def init_db():
    queries.initialize_metadata_for_all_tables()
    queries.create_tables(con)


if __name__ == "__main__":
    init_db()
