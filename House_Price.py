import streamlit as st
import joblib
import base64
from sklearn.preprocessing import StandardScaler
st.set_page_config(page_title="House Price App",page_icon=":house:")
video=f"""
    <style>
        .vid{{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
        }}
    </style>
    <video autoplay loop muted class="vid">
        <source src="https://cdn.discordapp.com/attachments/1300827113104080960/1300827373410979860/3773486-hd_1920_1080_30fps.mp4?ex=67224166&is=6720efe6&hm=3e01e5401e52948a78b9994c5ce04144bba3bac92885c449dd4229f573e4826f&">
    </video>

"""
st.markdown(video,unsafe_allow_html=True)
st.header("House Price Prediction App")
val1=st.text_input("Enter area")
val2=st.text_input("Enter bedrooms")
val3=st.text_input("Enter bathrooms")
val4=st.text_input("Enter stories")
val5=st.text_input("Enter mainroad")
val6=st.text_input("Enter guestroom")
val7=st.text_input("Enter basement") 
val8=st.text_input("Enter hotwaterheating")
val9=st.text_input("Enter airconditioning")
val10=st.text_input("Enter parking")
val11=st.text_input("Enter prefarea")
val12=st.text_input("Enter furnishing status")
try:
    val1=float(val1)
    val2=int(val2)
    val3=int(val3)
    val4=int(val4)
    val5=int(val5)
    val6=int(val6)
    val7=int(val7)
    val8=int(val8)
    val9=int(val9)
    val10=int(val10)
    val11=int(val11)
    val12=int(val12)
except ValueError:
        st.error("Please check whether all inputs are valid")
import pandas as pd
df=pd.read_csv('Housing.csv')
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
df['main_road']=encoder.fit_transform(df.loc[:,'mainroad'])
df['guest_room']=encoder.fit_transform(df.loc[:,'guestroom'])
df['base_ment']=encoder.fit_transform(df.loc[:,'basement'])
df['hotwater_heating']=encoder.fit_transform(df.loc[:,'hotwaterheating'])
df['air_conditioning'] =encoder.fit_transform(df.loc[:,'airconditioning'])
df['pref_area']=encoder.fit_transform(df.loc[:,'prefarea'])
df['furnishing_status']=encoder.fit_transform(df.loc[:,'furnishingstatus'])
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(df.loc[:,['area','bedrooms','bathrooms','stories','main_road','guest_room','base_ment','hotwater_heating','air_conditioning','pref_area','parking','furnishing_status']])
if st.button("Check"):
    val=scaler.transform([[val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12]])
    st.write(val)
    model=joblib.load('House_Price.pkl')
    answer=model.predict(val)
    st.subheader(f"Price of house is {answer[0]}")
# https://cdn.discordapp.com/attachments/1300827113104080960/1300827373410979860/3773486-hd_1920_1080_30fps.mp4?ex=67224166&is=6720efe6&hm=3e01e5401e52948a78b9994c5ce04144bba3bac92885c449dd4229f573e4826f&?