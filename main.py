import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('D:\Gongzuo\python-Web-Project\images1\Hell.png', width=600)

with col2:
    st.title('Arman Bayat')
    content = """
    Hey, its arman, you can call m sirArman !
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images1/' + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.image('images1/' + row['image'])

