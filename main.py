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
        app = option_menu(
            menu_title=None,
            options=['Home','Account','Display','Predict I','Prediction','Watchlist'],
            default_index=1,
            orientation="horizontal",
            
            )

        
        if app == "Home":
            Home.app()
        if app == "Account":
            Account.app()    
        if app == "Display":
            Display.app()        
        if app == 'Predict I':
            Predict.app()
        if app == 'Prediction':
            DeepPrediction.app() 
        if app == 'Watchlist':
            Watchlist.app()   
             
          
             
    run()            
         