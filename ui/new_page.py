
import streamlit as st


class NewPage():
    """Streamlit secondary page.
    """

    def __init__(self):
        """Initalize data and global parameters
        """
        # load data and global states
        self.ume_data = st.session_state["data"]
        self.user_state = st.session_state["user_state"]

    def show_page(self):
        """Show Streamlit components at secondary page.
        """
        st.title("💳 New Page")
