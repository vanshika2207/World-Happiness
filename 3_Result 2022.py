import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
st.set_page_config(
    page_title='Result of World Happiness',
    page_icon='🏳️'

)

st.title('Result of World Happiness 2022')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRk8YHC-eQy2xqxcAcJ3cG4l-pu53nR3RAXa6LByWieod1rRSlXmoQ_6vgrXb5KG6lvF7o&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
st.title("Let's look at the dataset first")
data2021=pd.read_csv('C:/Users/saxen/PycharmProjects/pythonProject/2021.csv')
st.write(data2021)
fig = px.choropleth(data_frame=data2021,locations="Country name",locationmode="country names",color="Ladder score",title="Country wise happiness score")
st.write(fig)
st.sidebar.success("select a page")
st.markdown(
    """
    ### Points to note :
    - Finland topped the list for the fifth time in a row, according to the 10th edition of the World Happiness Report.
    - Finland was followed by Denmark, Iceland, Switzerland, and the Netherlands
    - Among other western countries, while the United States managed to bag the 16th position, Britain was ranked 17th and France 20th.
    - India continued to fare poorly in the world happiness index, with its position marginally improving to 136 as against last year’s 139.
    - Among the South Asian nations, only Taliban-ruled Afghanistan fared worse than India
    - Afghanistan was named the most unhappy country in the world, ranking last on the index of 146 countries.
    - Nepal (84), Bangladesh (94), Pakistan (121) and Sri Lanka (127) managed to get better ranks in the list.
  
"""
)


