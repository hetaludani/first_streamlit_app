import streamlit
streamlit.title('My Parents First Diner')
streamlit.header('Breakfast Favorites')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
my_fruit_selected=streamlit.multiselect('Pick Some Fruits',list(my_fruit_list.index))
my_fruit_show=my_fruit_list.loc[my_fruit_selected]
streamlit.dataframe(my_fruit_show)
import requests
fruityvice_response=requests.get('https://fruityvice.com/api/fruit/'+'kiwi')
#streamlit.text(fruityvice_response.json())
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
streamlit.header('Fruityvice Fruit Advice')
fruit_choice=streamlit.text_input('Which fruit would you like to know about')
streamlit.write('The user entered',fruit_choice)
fruityvice_entered_choice=requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
fruityvice_normalized=pandas.json_normalize(fruityvice_entered_choice.json())
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

