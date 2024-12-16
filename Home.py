
import streamlit as st

from ui.resources.stpage import Stpage
from ui.resources.data_interface import *
from ui.new_page import NewPage


class Home(Stpage):
    """
    """

    def __init__(self, title, icon, layout="centered", initial_sidebar_state="collapsed"):
        """
        """
        super().__init__(title, icon, layout, initial_sidebar_state)

        self.load_data()

        self.ume_data = st.session_state["data"]
        self.user_state = st.session_state["user_state"]

    def show_page(self):
        """
        """
        st.title("💳 My App")

        st.write(self.user_state.app_name)

    def navigation(self):
        """
        """
        self.show_navbar(self.op)

        if self.op == "man":
            if self.nav_bar == "Home":
                self.show_page()

            elif self.nav_bar == "npg":
                page = NewPage()
                page.show_page()


page = Home("Home", "💳", layout="wide", initial_sidebar_state="collapsed")
page.navigation()
