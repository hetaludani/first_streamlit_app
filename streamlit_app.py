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
fruityvice_response=requests.get('https://fruityvice.com/api/fruit/watermelon')
streamlit.text(fruityvice_response)
