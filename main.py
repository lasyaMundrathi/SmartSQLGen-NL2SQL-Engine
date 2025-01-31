import streamlit as st
from database import setup_database, read_sql_query
from genai import get_gemini_response
import pandas as pd

# Run database setup (you can set this to False once the database is set up)
setup_database()

# Streamlit App
st.set_page_config(page_title="Telecom Database Query", layout="wide")
st.title("Telecom Database Query Generator")

# User Input
question = st.text_input("Enter your natural language question:", key="input")
submit = st.button("Generate Query")

if submit:
    # Generate SQL Query using Gemini
    sql_query = get_gemini_response(question)
    st.subheader("Generated SQL Query")
    st.code(sql_query, language="sql")

    # Execute SQL Query on the Database
    rows, columns = read_sql_query(sql_query)
    if columns:
        st.subheader("Query Results")
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)
    else:
        st.error("Failed to execute query. Please check your question or database.")
