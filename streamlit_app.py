
import streamlit
import requests
from urllib.error import URLError
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
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
    
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice=streamlit.text_input("what fruit would u like information about")
  if not fruit_choice:
    streamlit.error("please select the fruit")
  else:
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

import snowflake.connector

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor()as my_cur:
    my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
    return('thanks for adding '+add_my_fruit)
add_my_fruit=streamlit.text_input("what fruit would u like to add",'jackfruit')
if streamlit.button('add a fruit to the list'):
  my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

streamlit.stop()
