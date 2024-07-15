import streamlit as st
import firebase_admin
from firebase_admin import credentials
if not firebase_admin._apps:
    cred = credentials.Certificate('secret.json')
    firebase_admin.initialize_app(cred)
from firebase_admin import db
ref = db.reference(url = 'https://test-33630-default-rtdb.firebaseio.com/')

student_num = st.text_input("st_num")
name = st.text_input("st_name")
if st.button("Save") :
    ref.update({"name":name})
    ref.update({"num":student_num})