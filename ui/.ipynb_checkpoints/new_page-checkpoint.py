
import pandas as pd
import streamlit as st

from streamlit_extras.colored_header import colored_header



class NewPage():
    """
    """
    
    def __init__(self):
        """
        """
        self.ume_data = st.session_state["data"]
        self.user_state = st.session_state["user_state"]
        
    
    def show_page(self):
        """
        """
        
        st.title("💳 New Page")
        
        