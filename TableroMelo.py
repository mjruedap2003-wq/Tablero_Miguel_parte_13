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
        transform: scale(1.02);
    }

    /* Sidebar y Textos en Azul Brillante */
    section[data-testid="stSidebar"] {
        background-color: #121722 !important;
        border-right: 2px solid #00F0FF !important;
    }

    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] .stMarkdown {
        color: #00F0FF !important;
        font-weight: bold !important;
        text-shadow: 0 0 5px rgba(0, 240, 255, 0.5);
    }

    /* Marco para el lienzo del canvas */
    iframe[title="streamlit_drawable_canvas.canvas"] {
        border: 3px solid #00F0FF !important;
        border-radius: 10px !important;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.4) !important;
    }

    /* Color Pickers y Sliders ajustados */
    div[data-testid="stColorPicker"], div[data-testid="stSlider"] {
        background-color: #1A2232;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #00F0FF;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Encabezado
st.markdown('<h1 class="neon-title">🎨 TABLERO DE DIBUJO & RETOS RÁPIDOS 🖌️</h1>', unsafe_allow_html=True)

# 4. Sección para tu párrafo explicativo
st.markdown("""
    <div class="app-description-box">
        <p class="app-description-text">
            <strong>📌 Sobre esta aplicación:</strong><br>
            Escribe aquí tu párrafo explicando el propósito de la app. Puedes detallar cómo funciona el lienzo interactivo, la dinámica de los retos aleatorios y las herramientas de personalización disponibles en el panel lateral.
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. Banco de Retos Cotidianos y Fáciles
CHALLENGES = [
    "Un gato durmiendo una siesta.",
    "Una taza de café caliente botando humo.",
    "Un carro sencillo vista de lado.",
    "Una rebanada de pizza de queso.",
    "Un árbol de manzanas.",
    "Un helado en cono de 2 bolas.",
    "Un sol sonriente con gafas de sol.",
    "Una casa de campo clásica con chimenea.",
    "Un cohete despegando al espacio.",
    "Un pez dentro de una pecera redonda.",
    "Un perro feliz moviendo la cola.",
    "Un pastel de cumpleaños con velas.",
    "Un barco navegando en el mar.",
    "Un bombillo encendido (idea)."
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
            <div class="challenge-title">✏️ Reto para dibujar ahora ✏️</div>
            <div class="challenge-text">"{st.session_state.current_challenge}"</div>
        </div>
    """, unsafe_allow_html=True)

# 6. Barra Lateral (Propiedades del Tablero)
with st.sidebar:
    st.subheader("🛠️ Propiedades del Tablero")

    st.markdown("---")
    st.markdown("### 📐 Dimensiones")
    canvas_width = st.slider("Ancho del tablero", 300, 1000, 700, 50)
    canvas_height = st.slider("Alto del tablero", 200, 700, 450, 50)

    st.markdown("---")
    st.markdown("### 🖌️ Herramientas")
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('Ancho de línea', 1, 40, 8)

    st.markdown("---")
    st.markdown("### 🎨 Colores")
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")

# 7. Renderizado del Canvas
col_canvas, _ = st.columns([1, 0.01])

with col_canvas:
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 127, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}",
    )
