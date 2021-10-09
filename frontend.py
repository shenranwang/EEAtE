import streamlit as st
import pandas as pd
import numpy as np
import os
import glob
from table_query import TableQA

DL_PATH = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/'
table_dict = {
    'Greenhouse gas emissions by source sector': 'sdg_13_10.tsv.gz',
    'Greenhouse gas emissions per capita': 't2020_rd300.tsv.gz',
}

@st.cache
def load_data(table_dict, options_table):
    data = pd.read_csv(DL_PATH + table_dict[options_table], sep='\t')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    #for column in data.columns:
    #    print("column:", column)
    #    data[column] = pd.to_numeric(data[column], downcast='float')
    return data

options_table = st.selectbox(
    'Select table',
    table_dict.keys(),
)

st.title(options_table)

df = load_data(table_dict, options_table)
df = df.set_index(df.columns[0])

container = st.container()

options_nation = container.multiselect(
    "Choose {}".format(df.index.name.split("\\")[0]),
    df.index.tolist(),
    [],
)
all_nations = container.checkbox("Select all", True, key=0)

options_year = container.multiselect(
    "Choose {}".format(df.index.name.split("\\")[1]),
    df.columns.tolist(),
    [],
)
all_years = container.checkbox("Select all", True, key=1)

if all_nations:
    options_nation = df.index
if all_years:
    options_year = df.columns

data = df.loc[options_nation][options_year]
st.dataframe(data)

# if len(data) < 5:
#    st.write(data.columns)
#    transposed = data.transpose()
#    data2 = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])
#    a = data.info()
#    c = transposed.info()
#    b = data2.info()
#    st.line_chart(data2)

st.title("Search")
tables = [os.path.basename(filepath).replace(".csv", "") for filepath in glob.glob("./data/tables/*.csv")]

container_search = st.container()

options_search = container_search.selectbox(
    "Choose {}".format("data table"),
    tables,
)
all_search = container_search.checkbox("Select all", True, key=2)
user_input = container_search.text_input("Ask a question!", "")

if all_search:
    try:
        st.write(TableQA.get_response(user_input))
    except:
        st.write("The question does not seem to ask relevant information.")
else:
    try:
        st.write(TableQA.get_response(user_input, filename=options_search))
    except:
        st.write("The question does not seem to ask relevant information.")


