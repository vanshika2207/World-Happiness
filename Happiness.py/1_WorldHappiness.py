import streamlit as st
st.set_page_config(
    page_title='World Happiness',
    page_icon='😊'

)
st.title('World Happiness Report')
st.sidebar.success("select a page")
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlnH6y3aFC0-ali4L9J2Iyn9nKeK2BLxd6eA&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
from PIL import Image
image = Image.open('C:/Users/saxen/PycharmProjects/pythonProject/wh.jpg')
st.image(image, caption='World Happiness')
st.markdown(
        """
        The World Happiness Report is a landmark survey of the state of global happiness

        The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness.

        The happiness scores and rankings use data from the Gallup World Poll.
        This year marks the 10th anniversary of the World Happiness Report, which uses global survey data to report how people evaluate their own lives in more than 150 countries worldwide..

    
        

        ### The World Happiness Report 2022 reveals a bright light in dark times. The pandemic brought not only pain and suffering but also an increase in social support and benevolence.
        As we battle the ills of disease and war, it is essential to remember the universal desire for happiness and the capacity of individuals to rally to each other’s support in times of great need.
        ### Indicators of World Happiness Report
        
        The rankings are based on polling (Gallup World Poll) which looks at six variables:
 

        - Gross Domestic Product Per Capita (Purchasing Power Parity).
        - Social Support.
        - Healthy life expectancy at birth.
        - Freedom to make life choices.
        - Generosity.
        - Perceptions of corruption.

        Respondents are asked to rate their own current lives on a 0-10 scale.

        ### For more details visit here:

        - [Official website](https://worldhappiness.report/)
        
    """
    )

