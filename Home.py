
import streamlit as st

from ui.resources.stpage import Stpage
from ui.new_page import NewPage


class Home(Stpage):
    """Streamlit home page.
    """

    def __init__(
        self,
        title: str,
        icon: str,
        layout: str = "centered",
        initial_sidebar_state: str = "collapsed"
    ):
        """Initalize Home page with viewport parameters.

            Parameters
            ----------
            title : str
                Plot title.
            icon : str
                Plot icon as a emoji string
            layout : str
                Layout type can take the values wide or centered
            initial_sidebar_state : str 
                Sidebar config can take the values expanded or collapsed
        """
        super().__init__(title, icon, layout, initial_sidebar_state)

        self.load_data()

        self.ume_data = st.session_state["data"]
        self.user_state = st.session_state["user_state"]

    def navigation(self):
        """Show navigation menu.
        """
        self.show_navbar(self.page_group)

        if self.page_group == "man":
            if self.nav_bar == "Home":
                self.show_page()

            elif self.nav_bar == "npg":
                page = NewPage()
                page.show_page()

    def show_page(self):
        """Show Streamlit components at Home page.
        """
        st.title("💳 My App")

        st.write(self.user_state.app_name)


page = Home("Home", "💳", layout="wide", initial_sidebar_state="collapsed")
page.navigation()
# page.show_sidebar()
