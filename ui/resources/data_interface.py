
import numpy as np
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
    # Gerar dados aleatórios
    np.random.seed(42)  # Para resultados reproduzíveis
    volume_clientes = np.random.randint(
        50, 500, size=10)  # Volume entre 50 e 500

    # Gerar faixas de atraso como score em décimos (0.0 a 1.0)
    risco_credito = np.round(np.linspace(0, 1, num=10), 1)

    # Criar o DataFrame
    dados = pd.DataFrame({
        'volume': volume_clientes,
        'risco': risco_credito
    })

    return dados
