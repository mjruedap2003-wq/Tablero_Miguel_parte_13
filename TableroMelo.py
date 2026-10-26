import random
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# 1. Configuración de página
st.set_page_config(
    page_title="Tablero de Dibujo | Retos Rápidos",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilos Neón Ajustados (Fondo menos oscuro + Textos Azul Brillante)
st.markdown("""
    <style>
    /* Fondo general más claro/metálico para que resalte el tablero */
    .stApp {
        background-color: #1A1F2C !important;
        color: #FFFFFF !important;
    }

    #MainMenu, footer, header {visibility: hidden;}

    /* Título principal */
    .neon-title {
        font-size: 2.3rem;
        font-weight: 900;
        text-align: center;
        color: #00F0FF;
        text-shadow: 0 0 10px #00F0FF, 0 0 20px #00F0FF;
        margin-bottom: 0.5rem;
    }

    /* Caja de descripción de la aplicación */
    .app-description-box {
        background: rgba(0, 240, 255, 0.05);
        border: 1px solid #00F0FF;
        border-left: 5px solid #00F0FF;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 0 10px rgba(0, 240, 255, 0.2);
    }

    .app-description-text {
        color: #E2E8F0;
        font-size: 1.05rem;
        line-height: 1.6;
        margin: 0;
    }

    /* Tarjeta de reto activo */
    .challenge-box {
        background: #252D3D;
        border: 2px solid #00F0FF;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);
        margin-bottom: 1.5rem;
    }

    .challenge-title {
        color: #FF007F;
        font-size: 0.9rem;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0.3rem;
    }

    .challenge-text {
        color: #00FF66;
        font-size: 1.5rem;
        font-weight: 800;
        text-shadow: 0 0 8px #00FF66;
    }

    /* Botones Neón */
    div.stButton > button {
        width: 100%;
        background: transparent !important;
        color: #00FF66 !important;
        border: 2px solid #00FF66 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        text-shadow: 0 0 8px #00FF66 !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.2) !important;
        transition: all 0.3s ease-in-out !important;
    }

    div.stButton > button:hover {
        background-color: #00FF66 !important;
        color: #0A0E17 !important;
        box-shadow: 0 0 25px rgba(0, 255, 102, 0.8) !important;
        transform: scale(1.0
