import streamlit as st

from streamlit_option_menu import option_menu


import Home, Account, Display, Predict, DeepPrediction, Watchlist



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Stock Pulse ',
                options=['Home','Account','Display','Predict','DeepPrediction','Watchlist'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "3!important","background-color":'#1f1f1f'},
        "icon": {"color": "#144c7b", "font-size": "14px"}, 
        "nav-link": {"color":"white","font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#005eb8"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            Home.app()
        if app == "Account":
            Account.app()    
        if app == "Display":
            Display.app()        
        if app == 'Predict':
            Predict.app()
        if app == 'DeepPrediction':
            DeepPrediction.app() 
        if app == 'Watchlist':
            Watchlist.app()   
             
          
             
    run()            
         