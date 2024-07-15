import streamlit as st
import firebase_admin
from firebase_admin import credentials
if not firebase_admin._apps:
    cred = credentials.Certificate('secret.json')
    firebase_admin.initialize_app(cred)
from firebase_admin import db
ref = db.reference(url = 'https://test-33630-default-rtdb.firebaseio.com/')

st.write("이진수 15를 2의 보수로 바꾼다면 무엇이 나올까?")
answer = st.text_input("answer")
st.write("명령어가 제한적이라 코드가 길어지는 장치의 이름은?")
pick = st.radio("Answer",["CISC","RISC","SCP","KISC","BISC"])
if st.button("Submit") :
    ref.update({"answer":answer})
    ref.update({"pick":pick})