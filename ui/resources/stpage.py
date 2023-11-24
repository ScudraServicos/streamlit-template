
import streamlit as st
import hydralit_components as hc

import gc
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

import sys
sys.path.append("data-science-functions/")

from ui.resources.data_interface import *



class Stpage():
    """
        Streamlit default page
    """
    
    def __init__(self, title, icon, layout="centered", initial_sidebar_state="collapsed",):
        """
            layout: wide, centered
            initial_sidebar_state: expanded, collapsed
        """
        
        st.set_page_config(
            page_title=title, page_icon=title, layout=layout, initial_sidebar_state=initial_sidebar_state
        )
        
        # set streamlit header z-index
        st.markdown('''
            <style>
                .stApp header {
                    z-index: 0;
                }
                .block-container {
                    padding-top: 2rem;
                    padding-left: 1rem;
                    padding-right: 4rem;
                    padding-bottom: 10rem;
                }
            </style>
        ''', unsafe_allow_html=True)
        
        self.sidebar_menu = [
            {"label":"Main", "icon": "💳", "id":"man",},
        ]
        self.op = "man"
        
        
    def login(self):
        """
        """
        with open("config.yaml") as file:
            config = yaml.load(file, Loader=SafeLoader)

        authenticator = stauth.Authenticate(
            config["credentials"],
            config["cookie"]["name"],
            config["cookie"]["key"],
            config["cookie"]["expiry_days"],
            config["preauthorized"]
        )
        name, authentication_status, username = authenticator.login("Login", "main")
        
        if st.session_state["authentication_status"] == False:
            st.error("Username/password is incorrect")
        elif st.session_state["authentication_status"] == None:
            st.warning("Please enter your username and password")
        elif st.session_state["authentication_status"]:
            #authenticator.logout("Logout", "main") #sidebar, main
            return True
        return False
        
        
    def load_data(self):
        """
        """
        ume_data = load_application_data()
        st.session_state["data"] = ume_data
        
        user_state = load_user_state()
        st.session_state["user_state"] = user_state
        
        gc.collect()
        
        
    def show_navbar(self, page="mdl"):
        """
        """
        self.menu_data = []
        if page == "man":
            self.menu_data = [
                {"label":"New Page", "icon": "📖", "id":"npg",},
            ]
        
        over_theme = {'txc_inactive': '#F0F8FF'}
        #over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'blue'}#,'option_active':'blue'}
        self.nav_bar = hc.nav_bar(
            menu_definition=self.menu_data,
            override_theme=over_theme,
            home_name='Home',
            #login_name='Logout',
            hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
            sticky_nav=True, #at the top or not
            sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
        )
        
        
    def show_sidebar(self):
        """
        """
        with st.sidebar:
            self.op = hc.option_bar(
                #title='Credit', 
                key='PrimaryOption', option_definition=self.sidebar_menu, horizontal_orientation=False
            )
            
            
    def events(self):
        pass
        
        
    def show_page(self):
        pass
        