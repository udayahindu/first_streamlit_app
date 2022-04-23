
import streamlit
streamlit.title('My Mom\'s New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header('Fruityvice Fruit Advice')
fruit_choice=streamlit.text_input("what fruit would u like information about",'kiwi')
streamlit.write('user entered the '+fruit_choice)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows=my_cur.fetchall()
streamlit.text("  THE Fruit loaded list contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit=streamlit.text_input("what fruit would u like to add",'jackfruit')
streamlit.write('thanks for adding '+add_my_fruit)
