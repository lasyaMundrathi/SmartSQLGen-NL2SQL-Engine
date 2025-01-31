import sqlite3
import pandas as pd
import os

# Absolute path for the SQLite database
db_path = os.path.abspath("telecom.db")

# Function to create and verify database tables
def setup_database():
    connection = sqlite3.connect(db_path)

    # Create Broadband Table
    broadband_df = pd.DataFrame({
        "Provider": ["Provider A", "Provider B", "Provider C", "Provider D", "Provider E"],
        "Plan Name": ["Basic", "Standard", "Premium", "Unlimited", "Family"],
        "Speed (Mbps)": [10, 50, 100, 500, 1000],
        "Price ($)": [20, 40, 60, 80, 100],
        "Contract (Months)": [6, 12, 24, 36, 6]
    })
    broadband_df.to_sql("Broadband", connection, index=False, if_exists="replace")

    # Create MobileUsage Table
    mobile_usage_df = pd.DataFrame({
        "User ID": [f"User_{i+1}" for i in range(10)],
        "Plan Name": ["Basic", "Standard", "Premium", "Unlimited", "Family"] * 2,
        "Data Usage (GB)": [5, 10, 20, 50, 100] * 2,
        "Call Minutes": [100, 200, 300, 400, 500] * 2,
        "Monthly Bill ($)": [20, 30, 40, 50, 60] * 2
    })
    mobile_usage_df.to_sql("MobileUsage", connection, index=False, if_exists="replace")

    # Create InternetPlans Table
    internet_plans_df = pd.DataFrame({
        "Plan ID": [f"Plan_{i+1}" for i in range(10)],
        "Plan Name": ["Basic", "Standard", "Premium", "Unlimited", "Family"] * 2,
        "Download Speed (Mbps)": [25, 50, 100, 200, 500] * 2,
        "Upload Speed (Mbps)": [5, 10, 20, 50, 100] * 2,
        "Monthly Cost ($)": [20, 30, 40, 50, 60] * 2
    })
    internet_plans_df.to_sql("InternetPlans", connection, index=False, if_exists="replace")

    connection.close()

# Function to retrieve query results from SQLite
def read_sql_query(sql, db=db_path):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        columns = [description[0] for description in cur.description]
        conn.close()
        return rows, columns
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None, None
