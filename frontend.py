import glob
import os
import requests

import pandas as pd
import streamlit as st

from table_query import TableQA

st.title("Energy Efficient Action through Education")

tables = [os.path.basename(filepath).replace(".csv", "") for filepath in glob.glob("./data/tables/*.csv")]

options_table = st.selectbox(
    'Select table',
    tables,
)

@st.cache
def load_data(options_table):
    df = pd.read_csv(f"data/tables/{options_table}.csv")
    df = df.sort_values(["Country", "Year"]).reset_index(drop=True)
    return df

df = load_data(options_table)

options_nation = st.multiselect("Choose countries, all if not specified", df["Country"].unique())
options_year = st.multiselect("Choose years, all if not specified", df["Year"].unique())

data = df

if options_nation != []:
    data = data[data["Country"].isin(options_nation)]
if options_year != []:
    data = data[data["Year"].isin(options_year)]

data

st.header("Search")

options_table_search = st.selectbox(
    'Select table, or keep all tables',
    ["All tables"] + tables,
)

user_input = st.text_input("Ask a question about the data!", "")
filename = None if options_table_search == "All tables" else options_table_search

try:
    st.write(TableQA.get_response(user_input, filename=filename))
except:
    st.write("The question does not seem to ask relevant information.")

st.header("EETU")

container = st.container()

user_input_bot = container.text_input("Ask questions from EETU!", "")

url = "http://localhost:5005/webhooks/rest/webhook"
payload = {
"sender": "johndoe",
"message": user_input_bot
}
response = requests.post(url, json=payload)

try: 
    container.write("EETU:\n\n" + response.json()[0]["text"])
except:
    container.write("EETU:\n\n" + "Hi! Ask me a question!")
