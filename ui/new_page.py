
from ui.resources.stplotly import plot_data
import streamlit as st

import os
import sys
sys.path.append(os.getcwd())


class NewPage():
    """Streamlit secondary page.
    """

    def __init__(self):
        """Initalize data and global parameters.
        """
        # load data and global states
        self.ume_data = st.session_state["data"]
        self.user_state = st.session_state["user_state"]

    def show_page(self):
        """Show Streamlit components at secondary page.
        """
        st.title("💳 New Page")

        # show dataframe
        st.dataframe(self.ume_data)

        # build plot data
        pplot = {
            "x": self.ume_data.index,
            "bar-1": {
                "y": self.ume_data["volume"], "name": "Customers train", "percent": False
            },
            "line-1": {
                "y": self.ume_data["risco"], "name": "Train risk", "percent": True, "secondary": True
            },
        }
        title = f"""
                <b>Distribuição de risco - {len(self.ume_data)}</b><br>
        <span style="font-size:14px;color:lightgrey"><i>
            Subtítulo
        </i></span>
        """

        # show plot
        st.plotly_chart(plot_data(pplot, title, ylabel="Clientes",
                        ylabel2="Risco"), use_container_width=True)
