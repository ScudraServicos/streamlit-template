
import pandas as pd
import streamlit as st

from ui.resources.user_state import *


@st.cache_resource(show_spinner="User state...")
def load_user_state():
    """Load and cache global app states.
    """
    user_state = UserState()

    return user_state


@st.cache_resource(show_spinner="Loading data...")
def load_app_data():
    """Load and cache app data.
    """

    return pd.DataFrame()
