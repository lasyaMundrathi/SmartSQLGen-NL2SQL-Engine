## Overview

This project is a **production-level Streamlit application** designed to interact with a telecom database. It allows users to input natural language questions and generates corresponding SQL queries using **Google Gemini AI**. The SQL queries are executed on an SQLite database, and the results are displayed in a user-friendly interface. This application demonstrates expertise in **Generative AI**, **database management**, and **frontend development**.
## Features

- **Natural Language to SQL Translation**: Leverages Google Gemini AI to convert user questions into SQL queries.
- **Streamlit Interface**: Provides an intuitive UI for interacting with the application.
- **SQLite Database Integration**: Manages telecom-related data in three tables: Broadband, MobileUsage, and InternetPlans.
- **Dynamic Query Execution**: Executes AI-generated SQL queries and displays results in tabular format.
- **Production-Ready Code**: Implements robust error handling and modular design for scalability.
### File Structure:

```bash
project/
│
├── main.py
├── database.py
├── genai.py
├── utils.py
├── .env
└── requirements.txt
```
### Demonstration



https://github.com/user-attachments/assets/9d2049e8-bc07-4d43-9061-638adf65b399





## Table of Contents

1. [Installation](#installation)
2. [Database Schema](#database-schema)
3. [Technologies Used](#technologies-used)
4. [Key Highlights](#key-highlights)
5. [Future Enhancements](#future-enhancements)
## INSTALLATION
### Prerequisites
Python 3.10
Required Python libraries:
streamlit
sqlite3
pandas
google-generativeai
python-dotenv
### Setup Instructions
1. Install the dependencies using pip install -r requirements.txt.
2. Ensure the .env file is present and contains your Google API key.
3. Run the Streamlit app with the command: streamlit run main.py.

## Database Schema

The SQLite database (`telecom.db`) contains three tables:

### 1. Broadband Table

| Column           | Type    | Description                                   |
|-------------------|---------|-----------------------------------------------|
| Provider          | TEXT    | Name of the broadband provider                |
| Plan Name         | TEXT    | Name of the broadband plan                    |
| Speed (Mbps)      | INTEGER | Maximum download speed in Mbps                |
| Price ($)         | REAL    | Monthly cost of the broadband plan            |
| Contract (Months) | INTEGER | Contract duration in months                   |

### 2. MobileUsage Table

| Column           | Type    | Description                                   |
|-------------------|---------|-----------------------------------------------|
| User ID          | TEXT    | Unique identifier for each mobile user       |
| Plan Name        | TEXT    | Name of the mobile data plan                  |
| Data Usage (GB)  | INTEGER | Data consumed by the user in GB               |
| Call Minutes     | INTEGER | Total call minutes used by the user           |
| Monthly Bill ($) | REAL    | Total monthly bill amount                     |

### 3. InternetPlans Table

| Column              | Type    | Description                                |
|----------------------|---------|--------------------------------------------|
| Plan ID             | TEXT    | Unique identifier for each internet plan  |
| Plan Name           | TEXT    | Name of the internet plan                 |
| Download Speed (Mbps)| INTEGER | Maximum download speed of the plan        |
| Upload Speed (Mbps)  | INTEGER | Maximum upload speed of the plan          |
| Monthly Cost ($)     | REAL    | Monthly cost of the internet plan         |

### Technologies Used

- **Frontend**: Streamlit for building an interactive UI.
- **Backend**:
  - SQLite for database management.
  - Google Gemini AI for natural language processing and SQL generation.
- **Programming Language**: Python
- **Environment Management**: `dotenv` for secure API key handling.

### Key Highlights

1. **Generative AI Integration**
   - Utilizes Google Gemini AI (`gemini-1.5-flash`) to translate natural language into precise SQL queries.
   - Demonstrates expertise in integrating cutting-edge AI technologies into real-world applications.

2. **Production-Level Design**
   - Modular code structure ensures scalability and maintainability.
   - Includes robust error handling for database operations and API calls.

3. **User-Friendly Interface**
   - Clean, interactive UI built with Streamlit, suitable for both technical and non-technical users.

4. **Real-Time Query Execution**
   - Executes AI-generated SQL queries on an SQLite database and displays results instantly.

### Future Enhancements

1. Add support for more databases (e.g., PostgreSQL, MySQL).
2. Implement multi-turn conversations using Google Gemini's chat capabilities.
3. Enhance query generation accuracy with fine-tuned prompts.
4. Add user authentication for secure access to sensitive data.

