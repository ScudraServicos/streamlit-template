
import streamlit as st


class NewPage():
    """
    """

    def __init__(self):
        """
        """
        # load data and global states
        self.ume_data = st.session_state["data"]
        self.user_state = st.session_state["user_state"]

    def show_page(self):
        """
        """
        st.title("💳 New Page")
