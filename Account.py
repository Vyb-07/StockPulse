import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate("Stockpulse\stockpulse-b1818-afca9e4f09d8.json")
firebase_admin.initialize_app(cred)


def app():
    
    st.title('Welcome to :violet[StockPulse] :sunglasses:')

    choice=st.selectbox('Login/Signup', ['Login','Sign'])
    
    def f():
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.write('Login success')
            
        except:
            st.warning('Login Failed')
    
    
    
    
    
    if choice=='Login':
        
        email=st.text_input('Email')
        password = st.text_input('Password',type='password')
        
        st.button('Login', on_click=f)
    
    else:
        
        email=st.text_input('Email')
        password = st.text_input('Password',type='password')
        
        username = st.text_input('Enter Unique username')
        
        if st.button('Create account'):
            user = auth.create_user(email=email, password=password, uid=username)
            st.success('Account created')
            st.markdown('Please login using username and password')
            st.balloons()
        
                
    

                            
