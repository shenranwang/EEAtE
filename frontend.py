import streamlit as st
import pandas as pd
import numpy as np

ALL = "All"
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
    data = data.set_index(data.columns[0])
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

options_nation = st.multiselect(
    "Choose {}".format(df.index.name),
    [ALL] + df.index.tolist(),
    ALL,
)

options_year = st.multiselect(
    "Choose year",
    [ALL] + df.columns.tolist(),
    ALL,
)

if ALL in options_nation:
    options_nation = df.index
if ALL in options_year:
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