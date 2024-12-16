
import gc
import streamlit as st
import hydralit_components as hc

from ui.resources.data_interface import load_app_data, load_user_state


class Stpage():
    """Streamlit default page.
    """

    def __init__(
        self,
        title: str,
        icon: str,
        layout: str = "centered",
        initial_sidebar_state: str = "collapsed",
    ):
        """Initalize the Streamlit app UI. 

            Parameters
            ----------
            title : str
                Plot title.
            icon : str
                Plot icon as a emoji string.
            layout : str
                Layout type can take the values wide or centered.
            initial_sidebar_state : str 
                Sidebar config can take the values expanded or collapsed.
        """

        st.set_page_config(
            page_title=title, page_icon=icon, layout=layout, initial_sidebar_state=initial_sidebar_state
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

        self.page_group = "man"

    def load_data(self):
        """Load application data and global states variables from data_interface.
        """
        ume_data = load_app_data()
        st.session_state["data"] = ume_data

        user_state = load_user_state()
        st.session_state["user_state"] = user_state

        gc.collect()

    def show_navbar(self, page_group: str = "man"):
        """Show navbar menu for a specifc page

            Parameters
            ----------
            page_group : str
                Page group identification.
        """
        menu_data = []
        if page_group == "man":
            menu_data = [
                {"label": "New Page", "icon": "📖", "id": "npg", },
            ]

        over_theme = {'txc_inactive': '#F0F8FF'}
        self.nav_bar = hc.nav_bar(
            menu_definition=menu_data,
            override_theme=over_theme,
            home_name='Home',
            # login_name='Logout',
            # will show the st hamburger as well as the navbar now!
            hide_streamlit_markers=False,
            sticky_nav=True,  # at the top or not
            sticky_mode='sticky',  # jumpy or not-jumpy, but sticky or pinned
        )

    def show_sidebar(self):
        """Shows Streamlit app sidebar.
        """
        sidebar_menu = [
            {"label": "Main", "icon": "💳", "id": "man", },
        ]
        with st.sidebar:
            self.page_group = hc.option_bar(
                # title='Credit',
                key='PrimaryOption', option_definition=sidebar_menu, horizontal_orientation=False
            )
