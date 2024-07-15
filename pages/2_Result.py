import streamlit as st
import firebase_admin
from firebase_admin import credentials
if not firebase_admin._apps:
    cred = credentials.Certificate('secret.json')
    firebase_admin.initialize_app(cred)
from firebase_admin import db
name = db.reference('name',url = 'https://test-33630-default-rtdb.firebaseio.com/')
num = db.reference('num',url = 'https://test-33630-default-rtdb.firebaseio.com/')
pick = db.reference('pick',url = 'https://test-33630-default-rtdb.firebaseio.com/')
answer = db.reference('answer',url = 'https://test-33630-default-rtdb.firebaseio.com/')

result = "0"
if(pick.get() == "RISC" and answer.get() == "0001") :
    result = "10"
elif(answer.get() == "0001") :
    result = "5"
elif(pick.get() == "RISC") :
    result = "5"
st.write(num.get() + name.get() + "님의 점수는 " + result + "점입니다.")