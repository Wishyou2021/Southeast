import streamlit as st  
from PIL import Image
import pandas as pd
import xlrd  
import openpyxl
df = pd.read_excel("SOUTHEAST_Central_Star.xlsx",sheet_name="工作表1",usecols="A:H") 
def AtlantaHawks_Star():
  st.header('Atlanta Hawks三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Bob Pettit', 'Dikembe Mutombo', 'Jamal Crawford'])
    if option=='Bob Pettit':
      new_df = df[0:1]
      st.dataframe(new_df)
    if option=='Dikembe Mutombo':
      new_df = df[1:2]
      st.dataframe(new_df)
    if option=='Jamal Crawford':
      new_df = df[2:3]
      st.dataframe(new_df)
  with col2:
    if option=='Bob Pettit':
      image = Image.open('Bob Pettit.jpg')
      st.image(image)
    if option=='Dikembe Mutombo':
      image = Image.open('Dikembe Mutombo.jpg')
      st.image(image)
    if option=='Jamal Crawford':
      image = Image.open('Jamal Crawford.jpg')
      st.image(image)
def CharlotteHornets_Star():
  st.header('Charlotte Hornets三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Kemba Walker', 'Dell Curry', 'Larry Johnson'])
    if option=='Kemba Walker':
      new_df = df[4:5]
      st.dataframe(new_df)
    if option=='Dell Curry':
      new_df = df[5:6]
      st.dataframe(new_df)
    if option=='Larry Johnson':
      new_df = df[6:7]
      st.dataframe(new_df)
  with col2:
    if option=='Kemba Walker':
      image = Image.open('Kemba Walker.jpg')
      st.image(image)
    if option=='Dell Curry':
      image = Image.open('Dell Curry.jpg')
      st.image(image)
    if option=='Larry Johnson':
      image = Image.open('Larry Johnson.jpg')
      st.image(image)
def MiamiHeat_Star():
  st.header('Miami Heat三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Alonzo Mourning', 'Dwyane Wade', 'LeBron James'])
    if option=='Alonzo Mourning':
      new_df = df[8:9]
      st.dataframe(new_df)
    if option=='Dwyane Wade':
      new_df = df[9:10]
      st.dataframe(new_df)
    if option=='LeBron James':
      new_df = df[10:11]
      st.dataframe(new_df)
  with col2:
    if option=='Alonzo Mourning':
      image = Image.open('Alonzo Mourning.jpg')
      st.image(image)
    if option=='Dwyane Wade':
      image = Image.open('Dwyane Wade.jpg')
      st.image(image)
    if option=='LeBron James':
      image = Image.open('LeBron James.jpg')
      st.image(image)
def OrlandoMagic_Star():
  st.header('Orlando Magic三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Dwight Howard', 'Darrell Armstrong', 'Shaquille ONeal'])
    if option=='Dwight Howard':
      new_df = df[12:13]
      st.dataframe(new_df)
    if option=='Darrell Armstrong':
      new_df = df[13:14]
      st.dataframe(new_df)
    if option=='Shaquille ONeal':
      new_df = df[14:15]
      st.dataframe(new_df)
  with col2:
    if option=='Dwight Howard':
      image = Image.open('Dwight Howard.jpg')
      st.image(image)
    if option=='Darrell Armstrong':
      image = Image.open('Darrell Armstrong.jpg')
      st.image(image)
    if option=='Shaquille ONeal':
      image = Image.open('Shaquille ONeal.jpg')
      st.image(image)
def WashingtonWizards_Star():
  st.header('Washington Wizards三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Wes Unseld', 'Elvin Hayes', 'Earl Monroe'])
    if option=='Wes Unseld':
      new_df = df[16:17]
      st.dataframe(new_df)
    if option=='Elvin Hayes':
      new_df = df[17:18]
      st.dataframe(new_df)
    if option=='Earl Monroe':
      new_df = df[18:19]
      st.dataframe(new_df)
  with col2:
    if option=='Wes Unseld':
      image = Image.open('Wes Unseld.jpg')
      st.image(image)
    if option=='Elvin Hayes':
      image = Image.open('Earl Monroe.jpg')
      st.image(image)
    if option=='Earl Monroe':
      image = Image.open('Elvin Hayes.jpg')
      st.image(image) 
      
