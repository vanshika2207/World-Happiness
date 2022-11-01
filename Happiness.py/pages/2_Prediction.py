import streamlit as st
st.set_page_config(
    page_title='Predicting Happiness Score',
    page_icon='❓'

)
st.sidebar.success("select a page")
st.title('Predicting  Happiness Score of Countries ')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSo80gWv-JmvV4MD-1DMuRA6ObgD04iinS_Jg&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
st.markdown(
            """
            ###  PREDICTING THE HAPPINESS SCORE OF A COUNTRY USING MULTI LINEAR REGRESSION 
            
            Variables used in dataset:
            
            - Happiness Rank: A country's rank on a world scale - determined by how high their happiness score is.
            - Happiness Score: A score given to a country based on adding up the rankings that a population has given to each category (normalized)
            - Country: The country in question
            - Region: The region that the country belongs too (different than continent)
            - Economy: GDP per capita of the country - individuals rank they quality of life based on the amount they earn
            - Family: quality of family life, nuclear and joint family
            - Health: ranking healthcare availability and average life expectancy in the country
            - Freedom: how much an individual is able to conduct them self based on their free will
            - Trust: in the government to not be corrupt
            - Generosity: how much their country is involved in peacekeeping and global aid
            - Dystopia Residual: Dystopia happiness score (1.85) i.e. the score of a hypothetical country that has a lower rank than the lowest ranking country on the report, plus the residual value of each country (a number that is left over from the normalization of the variables which cannot be explained).  
            
            
            [click here to see the dataset](https://www.kaggle.com/datasets/unsdsn/world-happiness)
            """)



import pickle
pickle_in = open('Happiness.py/regression.pkl', 'rb')
regression = pickle.load(pickle_in)
# this is the main function in which we define our webpage
def prediction(Economy, Family,Health, Freedom, Trust, Generosity, Dystopia_Residual):
    prediction = regression.predict([
        [Economy, Family,Health, Freedom, Trust, Generosity, Dystopia_Residual]])
    return  prediction
def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:cyan;padding:13px"> 
    <h1 style ="color:black;text-align:center;">PREDICTING HAPPINESS SCORES </h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    Economy = st.number_input("Enter points for GDP of the country")
    Family = st.number_input("Enter points for Social Support/Family  of the country")
    Health = st.number_input("Enter points for health (life expectancy at birth) of the country")
    Freedom = st.number_input("Enter points for the freedom score of the country")
    Trust = st.number_input("Enter points for the perception of corruption (trust) of the country")
    Generosity=st.number_input("Enter points for generosity of the country")
    Dystopia_Residual=st.number_input("enter dystopia residual")
    if st.button("Predict"):
        result = prediction(Economy, Family,Health, Freedom, Trust, Generosity, Dystopia_Residual)
        st.success('Happiness Score is is {}'.format(result))



if __name__ == '__main__':
    main()



