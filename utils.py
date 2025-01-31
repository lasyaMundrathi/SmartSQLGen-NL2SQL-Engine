import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to get the environment variable for API Key
def get_api_key():
    return os.getenv("GOOGLE_API_KEY")
