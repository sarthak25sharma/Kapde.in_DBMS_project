import sqlite3

from queries import create_tables, insert_tuple, initialize_metadata_for_all_tables

con = sqlite3.connect("db.sqlite")


def init_users():
    data = ["('Amit Singh', 'A-123', 'Connaught Place', 'New Delhi', 'Delhi', 110001, 'India', 'M')",
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

    for p in data:
        print(insert_tuple(con, p, "User").fetchall())

    con.commit()

    print(con.execute("SELECT *FROM User;").fetchall())


def init_db():
    initialize_metadata_for_all_tables()
    create_tables(con)


if __name__ == "__main__":
    init_db()
