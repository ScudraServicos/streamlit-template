
import pandas as pd
import streamlit as st

from ui.resources.user_state import *



@st.cache_resource(show_spinner="User state...")
def load_user_state():
    
    user_state = UserState()
    
    return user_state
    
    
@st.cache_resource(show_spinner="Loading backtest data...")
def load_application_data():
    
    return pd.DataFrame()
    