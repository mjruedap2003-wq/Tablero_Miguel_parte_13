import random
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# 1. Configuración de página
st.set_page_config(
    page_title="CyberCanvas | Drawing Studio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilos Neón Cyberpunk (CSS)
st.markdown("""
    <style>
    /* Fondo oscuro general */
    .stApp {
        background-color: #0A0E17 !important;
        color: #E2E8F0 !important;
    }

    #MainMenu, footer, header {visibility: hidden;}

    /* Título principal con resplandor cian */
    .neon-title {
        font-size: 2.3rem;
        font-weight: 900;
        text-align: center;
        color: #00F0FF;
        text-shadow: 0 0 10px #00F0FF, 0 0 20px #00F0FF, 0 0 40px #0077FF;
        margin-bottom: 0.5rem;
    }

    /* Caja de retos futurista */
    .challenge-box {
        background: #121826;
        border: 2px solid #FF007F;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 0 20px rgba(255, 0, 127, 0.4);
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
        text-shadow: 0 0 10px #00FF66;
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
        transform: scale(1.02);
    }

    /* Estilo del Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0D131F !important;
        border-right: 2px solid #00F0FF !important;
    }

    /* Color Pickers y Sliders */
    div[data-testid="stColorPicker"], div[data-testid="stSlider"] {
        background-color: #121826;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #00F0FF;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Encabezado
st.markdown('<h1 class="neon-title">⚡ CYBERCANVAS: DRAWING STUDIO 🎨</h1>', unsafe_allow_html=True)

# 4. Banco de Retos de Dibujo Cyberpunk / Sci-Fi
CHALLENGES = [
    "Un gato cyborg con implantes de neón y gafas holográficas.",
    "Un puesto de ramen futurista bajo la lluvia en un callejón nocturno.",
    "El rostro de un androide sintético reparando sus propios cables.",
    "Un vehículo volador de carreras con estelas de luz cian.",
    "Un robot callejero tocando la guitarra en una ciudad distópica.",
    "Una planta cibernética creciendo dentro de una batería de plasma.",
    "Un cazador de recompensas con un brazo robótico y abrigo largo.",
    "Un dron mensajero entregando un paquete misterioso.",
    "Un grafiti holográfico en la pared de un rascacielos.",
    "Un casco cyberpunk personalizado con pegatinas y pantalla LED.",
    "Un samurai cibernético sosteniendo una katana de luz.",
    "Una criatura alienígena usando un ordenador antiguo."
]

# Estado de sesión para guardar el reto activo
if "current_challenge" not in st.session_state:
    st.session_state.current_challenge = random.choice(CHALLENGES)

# Layout de la zona del reto
col_btn, col_txt = st.columns([1, 3])

with col_btn:
    if st.button("🎲 NUEVO RETO", type="primary"):
        st.session_state.current_challenge = random.choice(CHALLENGES)

with col_txt:
    st.markdown(f"""
        <div class="challenge-box">
            <div class="challenge-title">⚠️ Reto de dibujo activo ⚠️</div>
            <div class="challenge-text">"{st.session_state.current_challenge}"</div>
        </div>
    """, unsafe_allow_html=True)

# 5. Barra Lateral (Propiedades del Tablero)
with st.sidebar:
    st.subheader("🛠️ Panel de Control Neón")

    st.markdown("---")
    st.markdown("### 📐 Dimensiones")
    canvas_width = st.slider("Ancho del tablero", 300, 1000, 700, 50)
    canvas_height = st.slider("Alto del tablero", 200, 700, 450, 50)

    st.markdown("---")
    st.markdown("### 🖌️ Herramientas")
    drawing_mode = st.selectbox(
        "Modo de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('Ancho del trazo', 1, 40, 5)

    st.markdown("---")
    st.markdown("### 🎨 Paleta Cyberpunk")
    stroke_color = st.color_picker("Color de trazo", "#00F0FF")
    bg_color = st.color_picker("Color de fondo", "#0A0E17")

# 6. Renderizado del Canvas
col_canvas, _ = st.columns([1, 0.01])

with col_canvas:
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 127, 0.3)",  # Relleno con transparencia rosada neón
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}",
    )
