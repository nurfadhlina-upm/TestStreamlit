# import libraries
import streamlit as st
import pandas as pd
import json
import numpy as np
import os
import random
import PIL
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
# set page configuration
st.set_page_config(
page_title= "Tarot Reading",
layout="wide",
)
# front end elements of the web page
html_temp = """
<div style ="background-color:white;padding:13px">
<h1 style ="color:black;text-align:center;">Tarot Reading App</h1></div>
"""
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True)
st.caption('by Valeria Filippou ')
@st.cache
def load_data(filename):
   data = json.load(open(filename))
   return data
data=load_data('tarot-images.json')
df = pd.json_normalize(data['cards'])
df['fortune_telling_1'] = df['fortune_telling'].str[0]
df['fortune_telling_2'] = df['fortune_telling'].str[1]
df['fortune_telling_3'] = df['fortune_telling'].str[2]
df = df.fillna('')
if st.button("Reading"):
   reading = df.sample(n = 3).reset_index(drop=True)
   today = datetime.date.today()
   date = today.strftime("%d-%B-%Y")
   # identify images
   name_img_past = reading['img'].iloc[0]
   name_img_present = reading['img'].iloc[1]
   name_img_future = reading['img'].iloc[2]
   # open images
   img_past = PIL.Image.open(f'cards/{name_img_past}')
   img_present = PIL.Image.open(f'cards/{name_img_present}')
   img_future = PIL.Image.open(f'cards/{name_img_future}')
   # plot images
   fig, (past, present, future) = plt.subplots(1, 3, figsize=(5, 3))
   fig.suptitle('Your reading: Past, Present, Future on}'.format(date), fontsize=10)
   past.imshow(img_past)
   past.axis('off')
   past.set_title(reading['name'].iloc[0], fontsize=7)
   present.imshow(img_present)
   present.axis('off')
   present.set_title(reading['name'].iloc[1], fontsize=7)
   future.imshow(img_future)
   future.axis('off')
   future.set_title(reading['name'].iloc[2], fontsize=7)
   plt.show()
   st.pyplot(fig)
   # Outcomes 
   st.text('My dearest, your fortune reading is about your past,                                                           present and future.') 
   st.text('') 
   st.subheader('Regarding your past : ')
   st.text(reading['fortune_telling_1'].iloc[0])
   st.text(reading['fortune_telling_2'].iloc[0])
   st.text(reading['fortune_telling_3'].iloc[0])
   st.text('')
   st.subheader('Regarding your present: ')
   st.text(reading['fortune_telling_1'].iloc[1])
   st.text(reading['fortune_telling_2'].iloc[1])
   st.text(reading['fortune_telling_3'].iloc[1])
   st.text('')
   st.subheader('Regarding your future: ')
   st.text(reading['fortune_telling_1'].iloc[2])
   st.text(reading['fortune_telling_2'].iloc[2])
   st.text(reading['fortune_telling_3'].iloc[2])
st.sidebar.subheader("About App")
st.sidebar.info("This web app makes a tarot reading about your past, present and future.")
st.sidebar.info("Click on the 'Reading' button to make a reading.")
st.sidebar.info("Hoped you had fun.")
st.sidebar.info("Don't forget to rate this app")
feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)
if feedback:
   st.header("Thank you for rating the app!")
   st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.")
