import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
st.set_page_config(
    page_title="Let's Analyze India's situation",
    page_icon='🇮🇳'

)
st.sidebar.success("select a page")
st.title("Analyzing India's Situation")
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRloRnRMK5URUTqxxN1Jlt8g_dZXhmlyoevfw&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
data2021=pd.read_csv('C:/Users/saxen/PycharmProjects/pythonProject/2021.csv')
st.markdown(
           """ 
           #### Now I am going to analyze the relationship between various parameters of world happiness report and India's rank and give some suggestion on how India can improve it's rank.
           First Let's take a glance at the dataset
           """)
st.write(data2021)
st.markdown(
           """
           ### GDP vs HAPPINESS SCORE 
           """)
fig = px.scatter(data2021, x="Logged GDP per capita",y="Ladder score",size=data2021.index, color="Country name",hover_name="Regional indicator", log_x=True, size_max=60)
st.write(fig)
st.markdown(
           """
           #### What is GDP ?
           Gross domestic product (GDP) is the standard measure of the value added created through the production of goods and services in a country during a certain period
           #### Results
           - We can see from the analysis that there is a general trend :High Gross Domestic Product of the Country ,high is the happiness score.
           - But it is does not seem true ,countries with low GDP per capita  then India have higher happiness score than India ,eg : Myanmar, Pakistan ,Nepal
           - Also Countries with higher GDP per capita seems to be less happy than Countries with lower GDP, eg: USA has more GDP per capita than Finland but Finland is the world most happiest country

            This tells us that it is certain that the richer is not necessarily the happiest. Therefore, besides income, there must be other important factors that contribute to people’s happiness besides money.
           
           #### What can we conclude ?
                     
           One possible factor is income inequality, especially for more developed countries. Canada, Australia, and European countries such as Germany, Norway, Sweden, and Finland have lower income inequality and also have higher happiness indices compared to the United States. This raises an issue that although production is important, the allocation and distribution of the production is even more important.
           
           Same is the case of India:According to the World Inequality Report 2022, the top 10 per cent of Indians had about 96 times more income on average than the bottom 50 per cent. Similarly, Oxfam International claimed that in 2021 India’s top 1 per cent owned about 77 per cent of the country’s wealth.
           ### How can we improve ?
           - Income disparity should be  reduced
           - Government should adopt  Employment Programme and Wage Policies  
           - Social Security Measures 
           - Upliftment programme for Rural People 
           """)
st.markdown(
           """
           ### Healthy life expectancy at birth  vs HAPPINESS SCORE 
           """)
fig = px.bar(data2021, x='Country name', y='Ladder score',
             hover_data=["Healthy life expectancy"], color='Country name'
             ,width=1500,height=500)
st.write(fig)
st.markdown(
    """
    #### What is Health life Expectancy at birth ?
    The average number of years that a newborn could expect to live, if he or she were to pass through life exposed to the sex- and age-specific death rates prevailing at the time of his or her birth, for a specific year, in a given country, territory, or geographic area.
    #### Results
    - It is clear a more healthy a nation , a more  happier it is .
    - European countries have particularly invested on human development in terms of health as result they are the happiest.
    - But ,there has been only a marginal improvement in India's rank  for Healthy Life Expectancy despite being a pharma capital of the world, growing medical tourism or an overall increase in healthcare facilities in the country.


    #### What can we conclude ?
    What are the problems with health infrastructure of India ?
    -  Skewed distribution of health facilities
    - Lack of manpower
    - Poor infrastructure
    - Low penetration of health insurance
    ### How can we improve ?
    - Quantum increase in budget allocations
    - Better Health education
    - Primary health care need to be developed
    - Better health infrastructure required
    -  Use of information technology to improve health

    """)

st.markdown(
           """
           ### Perceptions of corruption  vs HAPPINESS SCORE 
           """)
fig = plt.figure(figsize=(10, 4))
sns.regplot(data=data2021, x='Perceptions of corruption', y='Ladder score')
st.pyplot(fig)
fig1=plt.figure(figsize=(20,4))
plt.title("Top 60 Countries with High Perceptions of corruption")
sns.barplot(data = data2021.sort_values('Perceptions of corruption', ascending= False).head(80), x='Country name', y='Perceptions of corruption')
plt.xticks(rotation=90)
st.pyplot(fig1)
st.markdown(
    """
    #### What is Perceptions of corruption ?
    It is an index which ranks countries "by their perceived levels of public sector corruption, as determined by expert assessments and opinion surveys." 
    #### Results
    - The countries with the best scores worldwide (and least corrupted) are Denmark in the first place, followed by New Zealand, Finland, Singapore, Sweden, Switzerland, Norway, Netherlands, Luxembourg, Germany, Iceland and Canada.
    - There is a very strong inversely proportional relationship between low levels of corruption and happiness in the population of a nation.
    - India is still a long way from being a corruption-free country
    - As per a research conducted by Transparency International in 2005, more than 62 percent of Indians have paid a bribe to a public official at some time in their lives. Another report from 2008 found that about half of Indians had first hand experience paying bribes or using contacts to get services from government agencies;
    - Corruption is a serious economic issue as it adversely affects the country’s economic development and achievement of developmental goals. It promotes inefficiencies in utilisation of resources, distorts the markets, compromises quality, destroys the environment and of late has become a serious threat to national security. It adds to the deprivation of the poor and weaker sections of the economy. 

    #### What can we conclude ?
    How can be India corruption free ?
   - Control political financing to prevent excessive flow of money in politics.
   - End preferential treatment to ensure that the provision of services and the distribution of public resources do not respond to personal connections or are biased towards certain interest groups.
   - Promotion of transparent and broad access to decision-making processes.
   - Strengthen electoral integrity, prevent and punish deceptive campaigns.
   - Empower citizens, protect activists, informants and journalists.
   - Strengthen control systems and promote separation of powers.
    

    """)
st.markdown(
           """
           ### Social Support  ,Generosity vs Happiness Score
           """)
st.markdown("""
           #### What is Social Support ?
           Social support is the perception and actuality that one is cared for, has assistance available from other people, and most popularly, that one is part of a supportive social network. 
           """)
c=plt.figure(figsize=(14,7))

plt.title("Happiness Score vs Social Support")
sns.regplot(data=data2021, x='Social support', y='Ladder score');
st.pyplot(c)
a=plt.figure(figsize=(14,7))
plt.title("Top 10 Countries with Social Support")
sns.barplot(data = data2021.sort_values('Social support', ascending= False).head(10), x='Country name', y='Social support')
plt.xticks(rotation=90)
st.pyplot(a)
st.markdown("""
           #### What is Generosity ?
           Someone showing generosity is happy to give time, money, food, or kindness to people in need. Generosity is a quality — like honesty and patience — that we all probably wish we had more of. When you show generosity, you might give away things or money or put others before yourself. 
           """)
d=plt.figure(figsize=(14,7))

plt.title("Happiness Score vs Generosity")
sns.regplot(data=data2021, x='Generosity', y='Ladder score')
plt.title("Top 50 Countries with High Generosity")
st.pyplot(d)
st.markdown("""
           #### Results
           - Every year Finland scores high in all factors and especially high in the generosity factor. Nearly half of all people in Finland give money back to charity regularly and one-third of the Finish population volunteers their time. 
           - Research on social support and happiness is reviewed. Research consistently finds that people who perceive their family and friends as supportive report greater happiness than those who doubt their social network’s supportiveness
           - Though Social Support and Generosity Scores are average for India but we can always do better
           #### How can we improve ?
           - Expanding Support to elderly ,women ,orphans ,homeless can make India’s position better.

           """)
st.markdown("""
            ## Freedom to make life choices vs Happiness Score
            """)
fig = px.sunburst(data2021, path=['Regional indicator','Country name'], values='Ladder score',color='Freedom to make life choices',  width=800, height=800)
st.write(fig)
st.markdown("""
            #### What is Freedom to make life choice ?
            “Freedom to make life choices” is the national average of responses to the question “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?”
            #### Results
            - More Freedom ,More Happiness
            #### What can we conclude ?
            - Freedom is important in terms of its consequences – personal freedom entails that people are free to do things that they find value and happiness in as long as they respect the rights of others, and economic freedom is the greatest explanator of prosperity (another determinant of happiness).
            -  Happiness and freedom are very virtuous, but if they are to come at the expense of rights and freedoms of others, there would be few things more vicious.
            """)
st.markdown("""
            # How can Indians become more Happy ?
            #### The report, through some simple statistical analysis, tries to find to what extent each factor determines the happiness that they have measured. Happiness in India, in 2022, was explained mostly by ‘GDP per capita’ at 31%, then by ‘freedom to make life choices’ at 17%, and least by ‘perceptions of corruption’ at 3%. Note that the national happiness figure is not an actual combination of the factors, but is measured independently, unlike indices where the quantities of the factors are either added or multiplied to arrive at a total index value. 
            ### With the combined measures of Government and we has a citizen ,we could  improve our ranking and can become the World Happiest Country.

            """)
