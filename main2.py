import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.title('TThe Best Company')
    content = """
    this is the text u are reading and there is no reason to read that and i
    dunno why u read this. wow !
    """
    st.info(content)

st.title('Our Team')

col3, col4, col5 = st.columns([0.75, 0.75, 0.75])

df = pd.read_csv('data.csv')

with col3:
    for index, row in df[:4].iterrows():
        st.header(f'{row['first name'].title()} {row['last name'].title()}')
        st.write(row['role'])
        st.image('images/' + row['image'])

with col4:
    for index, row in df[4:8].iterrows():
        st.header(f'{row['first name'].title()} {row['last name'].title()}')
        st.write(row['role'])
        st.image('images/' + row['image'])

with col5:
    for index, row in df[8:12].iterrows():
        st.header(f'{row['first name'].title()} {row['last name'].title()}')
        st.write(row['role'])
        st.image('images/' + row['image'])
