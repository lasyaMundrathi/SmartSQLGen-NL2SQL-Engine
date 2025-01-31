import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure GenAI API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define Prompt
prompt = """
You are an expert in translating natural language questions into SQL queries. The database contains three tables: Broadband, MobileUsage, and InternetPlans.

Table Descriptions:

1. Broadband Table:
The Broadband table stores details about internet broadband plans offered by various providers. Each row represents a broadband plan.
Provider (TEXT): The name of the company providing the broadband service (e.g., "Provider A").
Plan Name (TEXT): The name of the broadband plan (e.g., "Basic", "Standard").
Speed (Mbps) (INTEGER): The maximum internet download speed in megabits per second (e.g., 100).
Price ($) (REAL): The monthly cost of the broadband plan in US dollars (e.g., 60.0).
Contract (Months) (INTEGER): The duration of the contract in months (e.g., 12).

2. MobileUsage Table:
The MobileUsage table tracks users’ mobile data usage and call history. Each row represents an individual user's mobile usage details.
User ID (TEXT): A unique identifier for each mobile user (e.g., "User_1").
Plan Name (TEXT): The name of the mobile data plan subscribed to (e.g., "Premium").
Data Usage (GB) (INTEGER): The amount of mobile data consumed in gigabytes (e.g., 50).
Call Minutes (INTEGER): The number of minutes spent on phone calls (e.g., 300).
Monthly Bill ($) (REAL): The total monthly bill amount in US dollars (e.g., 40.0).

3. InternetPlans Table:
The InternetPlans table lists internet plans with different speed and cost options. Each row contains a unique internet plan’s specifications.
Plan ID (TEXT): A unique identifier for each internet plan (e.g., "Plan_1").
Plan Name (TEXT): The name of the internet plan (e.g., "Unlimited").
Download Speed (Mbps) (INTEGER): The maximum download speed of the internet plan in megabits per second (e.g., 200).
Upload Speed (Mbps) (INTEGER): The maximum upload speed of the internet plan in megabits per second (e.g., 50).
Monthly Cost ($) (REAL): The monthly cost of the internet plan in US dollars (e.g., 50.0).

Important Guidelines:
Always select all relevant columns as requested.
Use correct column names with double quotes " if they contain spaces or special characters.
Avoid returning incomplete results or omitting columns unless explicitly requested.
Use single quotes ' ' for text values.
Do not use backticks (`) or triple backticks (```).
"""

# Function to generate SQL queries using Google Gemini AI
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-1.5-flash")
    input_text = prompt + "\n" + question
    response = model.start_chat(history=[]).send_message(input_text)
    return response.text
