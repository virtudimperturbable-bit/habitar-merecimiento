import streamlit as st
import time
import json
import os
from datetime import datetime
import pandas as pd

# ----------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ----------------------------------------------------
st.set_page_config(
    page_title="Habitar el Merecimiento - Conciencia & Sanación",
    page_icon="🕊️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# ESTILOS CSS DE ALTA GAMA (DISEÑO EDITORIAL & ELEGANTE)
# ----------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #1E293B;
    }

    /* Ocultar elementos nativos innecesarios de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Header Principal / Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #312E81 100%);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        color: #FFFFFF;
        margin-bottom: 2rem;
        box-shadow: 0 20px 25px -5px rgba(15, 23, 42, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.4rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #C7D2FE;
        font-weight: 300;
        max-width: 800px;
        line-height: 1.6;
    }

    .badge-pill {
        display: inline-block;
        background: rgba(199, 210, 254, 0.15);
        color: #E0E7FF;
        border: 1px solid rgba(199, 210, 254, 0.3);
        padding: 0.35rem 1rem;
        border-radius: 50px;
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    /* Tarjetas UI Modernas */
    .card-box {
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 1.8rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .card-box:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
    }

    /* Tarjeta Métrica de Lujo */
    .metric-hero {
        background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid #BFDBFE;
        text-align: center;
    }

    .metric-val {
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        font-weight: 700;
        color: #1E3A8A;
        line-height: 1;
        margin: 0.5rem 0;
    }

    /* Cuadro de Citas y Decretos Espirituales */
    .parchment-box {
        background-color: #FCFDF8;
        border-radius: 16px;
        padding: 2rem;
        border-left: 6px solid #D97706;
        border-top: 1px solid #F3F4F6;
        border-right: 1px solid #F3F4F6;
        border-bottom: 1px solid #F3F4F6;
        box-shadow: 0 4px 12px rgba(217, 119, 6, 0.06);
        margin: 1.5rem 0;
    }

    .parchment-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.25rem;
        line-height: 1.8;
        color: #78350F;
        font-style: italic;
    }

    .scripture-card {
        background: linear-gradient(135deg, #FEF3C7 0%, #FFFBEB 100%);
        border-radius: 14px;
        padding: 1.5rem;
        border: 1px solid #FDE68A;
        color: #92400E;
        margin-bottom: 1rem;
    }

    .alert-danger-box {
        background-color: #FEF2F2;
        border-radius: 14px;
        padding: 1.5rem;
        border-left: 5px solid #EF4444;
        color: #991B1B;
        margin-bottom: 1.2rem;
    }

    .alert-success-box {
        background-color: #F0FDF4;
        border-radius: 14px;
        padding: 1.5rem;
        border-left: 5px solid #22C55E;
        color: #166534;
        margin-bottom: 1.2rem;
    }

    /* Tarjetas de Rutina */
    .routine-card-morning {
        background: #FFFBEB;
        border-radius: 16px;
        padding: 1.5rem;
        border-top: 5px solid #F59E0B;
        border-left: 1px solid #FDE68A;
        border-right: 1px solid #FDE68A;
        border-bottom: 1px solid #FDE68A;
        height: 100%;
    }

    .routine-card-day {
        background: #EFF6FF;
        border-radius: 16px;
        padding: 1.5rem;
        border-top: 5px solid #3B82F6;
        border-left: 1px solid #BFDBFE;
        border-right: 1px solid #BFDBFE;
        border-bottom: 1px solid #BFDBFE;
        height: 100%;
    }

    .routine-card-night {
        background: #F5F3FF;
        border-radius: 16px;
        padding: 1.5rem;
        border-top: 5px solid #8B5CF6;
        border-left: 1px solid #DDD6FE;
        border-right: 1px solid #DDD6FE;
        border-bottom: 1px solid #DDD6FE;
        height: 100%;
    }

    /* Botones Estilizados */
    .stButton>button {
        border-radius: 12px;
        font-weight: 600;
        padding: 0.6rem 1.5rem;
        transition: all 0.2s ease;
    }

    /* Mejorar Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
        border-right: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# GESTOR DE PERSISTENCIA LOCAL (JSON)
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORIAL_FILE = os.path.join(BASE_DIR, "historial_calibracion.json")

def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        try:
            with open(HISTORIAL_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def guardar_registro(puntaje, nivel_nombre, emocion_principal, notas=""):
    historial = cargar_historial()
    nuevo_registro = {
        "id": len(historial) + 1,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_corta": datetime.now().strftime("%d/%m %H:%M"),
        "puntaje": int(puntaje),
        "nivel": nivel_nombre,
        "emocion": emocion_principal,
        "notas": notas.strip() if notas else "Sin notas adicionales"
    }
    historial.append(nuevo_registro)
    with open(HISTORIAL_FILE, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)
    return nuevo_registro

def limpiar_historial():
    if os.path.exists(HISTORIAL_FILE):
        try:
            os.remove(HISTORIAL_FILE)
        except Exception:
            pass

def sembrar_datos_ejemplo():
    ejemplos = [
        {"id": 1, "fecha": "2026-10-10 09:15:00", "fecha_corta": "10/10 09:15", "puntaje": 115, "nivel": "Campo Reactivo (<200)", "emocion": "Culpa por cobrar tarifa justa", "notas": "Sensación de deuda y opresión en el pecho"},
        {"id": 2, "fecha": "2026-10-11 18:30:00", "fecha_corta": "11/10 18:30", "puntaje": 145, "nivel": "Campo Reactivo (<200)", "emocion": "Disfraz moral de falsa humildad", "notas": "Quería decir 'con poco me apaño'; apliqué Cero Leña"},
        {"id": 3, "fecha": "2026-10-12 12:00:00", "fecha_corta": "12/10 12:00", "puntaje": 220, "nivel": "El Testigo Consciente (200-300)", "emocion": "Observación de pérdida financiera", "notas": "Activé el Testigo, permití la emoción sin juzgarla"},
        {"id": 4, "fecha": "2026-10-14 10:20:00", "fecha_corta": "14/10 10:20", "puntaje": 270, "nivel": "El Testigo Consciente (200-300)", "emocion": "Entrega de lealtad familiar", "notas": "Rendición ante Dios con decreto de cancelación"},
        {"id": 5, "fecha": "2026-10-16 08:00:00", "fecha_corta": "16/10 08:00", "puntaje": 325, "nivel": "Buena Voluntad y Plenitud (>310)", "emocion": "Merecimiento y descanso", "notas": "Anclaje en Salmo 23:1. Paz profunda y sin culpa"}
    ]
    with open(HISTORIAL_FILE, "w", encoding="utf-8") as f:
        json.dump(ejemplos, f, ensure_ascii=False, indent=2)

# ----------------------------------------------------
# ESTADOS DE SESIÓN
# ----------------------------------------------------
if "testigo_activado" not in st.session_state:
    st.session_state.testigo_activado = False
if "decreto_entregado" not in st.session_state:
    st.session_state.decreto_entregado = False

# ----------------------------------------------------
# BARRA LATERAL EDITORIAL
# ----------------------------------------------------
with st.sidebar:
    st.markdown("### 🕊️ Habitar el Merecimiento")
    st.caption("Sistema de Transmutación de Conciencia & Sanación Espiritual")
    st.divider()

    pantalla = st.radio(
        "Módulos del Sistema:",
        [
            "1. Barómetro de Conciencia (Diagnóstico)",
            "2. Escáner Somático y Testigo (Nivel 200)",
            "3. Radar «Cero Leña» (Ayuno de Ego)",
            "4. Rendición Activa & Cancelación ante Dios",
            "5. Anclaje Bíblico & Buena Voluntad (>310)",
            "6. Guía de Rutina Diaria Consciente",
            "7. Historial y Progreso (Panel Local)"
        ]
    )

    st.divider()
    st.markdown("**Fundamentos:**")
    st.caption("• **Mapa de David Hawkins:** Escala de calibración interna (<200 Ego vs >310 Ser).")
    st.caption("• **Provisión Divina:** Anclaje en la Verdad (Salmo 23:1, Mateo 6:25-34, Filipenses 4:19).")

    historial_actual = cargar_historial()
    if historial_actual:
        st.divider()
        ult = historial_actual[-1]
        st.success(f"💾 **{len(historial_actual)} registros** guardados")
        st.metric("Última Calibración", f"{ult['puntaje']} pts", delta=ult['nivel'].split(' ')[0])

# ==========================================
# PANTALLA 1: BARÓMETRO DE CONCIENCIA
# ==========================================
if pantalla == "1. Barómetro de Conciencia (Diagnóstico)":
    st.markdown("""
    <div class="hero-banner">
        <div class="badge-pill">Módulo 01 • Diagnóstico de Conciencia</div>
        <div class="hero-title">Barómetro de Conciencia de Hawkins</div>
        <div class="hero-subtitle">Identifica si estás operando desde el «muñeco reactivo» del ego (<200) o si estás listo para habitar el Testigo Consciente y la Buena Voluntad (>310).</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-box">
        <h4 style="color: #1E3A8A; margin-bottom: 0.5rem;">💡 El Principio Fundamental del Espejo</h4>
        <p style="color: #475569; margin: 0;">El mundo exterior es solo un efecto. La verdadera causa reside en el estado de conciencia desde el que te vinculas con el dinero, las oportunidades y el acto de recibir. Cambiar la estrategia física sin sanar la emoción raíz solo repite el ciclo.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Diagnóstico Somático y Actitud Interior")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**1. Cuando recibes dinero, un elogio, descanso o ayuda:**")
        p1 = st.radio(
            "Selecciona tu respuesta:",
            [
                ("Me siento con culpa, en deuda o con impulso urgente de compensar", 125),
                ("Digo 'con poco me apaño' o 'primero los demás' (disfraz moral)", 150),
                ("Noto la incomodidad física pero me detengo a observarla sin huir", 220),
                ("Recibo con el corazón abierto, gratitud y sin sentirme en deuda", 310)
            ],
            format_func=lambda x: x[0],
            key="p1_rad"
        )
        
        st.markdown("**2. ¿Cómo responde tu cuerpo ante la posibilidad de prosperar o descansar?**")
        p2 = st.radio(
            "Selecciona tu respuesta:",
            [
                ("Puño cerrado: contracción en el pecho, nudo en garganta o miedo", 100),
                ("Inquietud constante: busco tareas compulsivas para justificar mi valía", 140),
                ("Respiración neutra: siento la tensión y no peleo contra ella", 210),
                ("Mano abierta: relajación profunda y permiso de habitar la paz", 320)
            ],
            format_func=lambda x: x[0],
            key="p2_rad"
        )

    with col2:
        st.markdown("**3. ¿Qué haces con los pensamientos de escasez o preocupación?**")
        p3 = st.radio(
            "Selecciona tu respuesta:",
            [
                ("Rumia continua: le doy vueltas una y otra vez buscando culpables", 110),
                ("Me quejo con otros de lo difícil que es la vida o la economía", 130),
                ("Los reconozco como chispas neutras y decido no echarles leña", 230),
                ("Cancelo el pensamiento limitante y descanso en la provisión divina", 330)
            ],
            format_func=lambda x: x[0],
            key="p3_rad"
        )

        st.markdown("**4. Relación con tu historia familiar y lealtades del pasado:**")
        p4 = st.radio(
            "Selecciona tu respuesta:",
            [
                ("Siento que tener más o descansar es traicionar la carencia familiar", 80),
                ("Me esfuerzo hasta el agotamiento para demostrar mi valor al clan", 130),
                ("Entiendo que mi linaje hizo lo que pudo y elijo no repetir el dolor", 220),
                ("Honro a mis antepasados recibiendo la vida con plenitud y sin culpa", 320)
            ],
            format_func=lambda x: x[0],
            key="p4_rad"
        )

    puntaje_promedio = int((p1[1] + p2[1] + p3[1] + p4[1]) / 4)

    if puntaje_promedio < 200:
        nivel_texto = "Campo Reactivo del Ego (<200)"
    elif puntaje_promedio < 310:
        nivel_texto = "El Testigo Consciente (200-300)"
    else:
        nivel_texto = "Buena Voluntad y Plenitud (>310)"

    st.divider()
    
    col_score1, col_score2 = st.columns([1, 2])
    with col_score1:
        st.markdown(f"""
        <div class="metric-hero">
            <div style="font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em; color: #475569; font-weight: 600;">Calibración Estimada</div>
            <div class="metric-val">{puntaje_promedio}</div>
            <div style="font-size: 0.9rem; font-weight: 600; color: #1E40AF;">{nivel_texto}</div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(min(max(puntaje_promedio / 400.0, 0.05), 1.0))
        
    with col_score2:
        if puntaje_promedio < 200:
            st.markdown(f"""
            <div class="alert-danger-box">
                <h4 style="margin-top:0;">⚠️ Nivel < 200: Operando desde el Ego Reactivo</h4>
                <p>Estás atrapado en la <b>culpa, la angustia o el autosacrificio</b>. Tu mente funciona como un muñeco reactivo que materializa precisamente lo que teme. La solución no es trabajar más duro, sino retirar la leña de la atención y activar el Testigo.</p>
            </div>
            """, unsafe_allow_html=True)
        elif 200 <= puntaje_promedio < 310:
            st.markdown(f"""
            <div class="parchment-box" style="margin: 0; padding: 1.2rem;">
                <h4 style="margin-top:0; color: #B45309;">⚖️ Nivel 200-300: Umbral del Testigo Consciente</h4>
                <p class="parchment-text" style="font-size: 1.05rem; margin: 0;">Has alcanzado la responsabilidad y el coraje. Eres capaz de observar tus emociones sin reaccionar impulsivamente ni justificarte. Estás a un paso de entregarte a la Buena Voluntad.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="alert-success-box">
                <h4 style="margin-top:0;">✨ Nivel > 310: Sintonía con la Buena Voluntad & Gracia</h4>
                <p>Te encuentras anclado en el <b>Mundo de las Causas</b>. Reconoces que la provisión y la paz son tu estado natural en Dios. En este nivel, aquello que sostienes en tu mente se materializa con fluidez y sin desgaste.</p>
            </div>
            """, unsafe_allow_html=True)

    # GUARDADO EN HISTORIAL
    st.divider()
    st.markdown("### 💾 Guardar Diagnóstico en tu Historial Local")
    
    col_save1, col_save2 = st.columns([2, 1])
    with col_save1:
        nota_usuario = st.text_input("Nota o reflexión del momento (opcional):", placeholder="Ej: Sentí incomodidad al cobrar pero frené el discurso de culpa...")
        emocion_detectada = st.selectbox("Emoción o foco predominante:", ["Herida de No Merecimiento", "Culpa por Recibir / Cobrar", "Miedo a la Escasez", "Disfraz Moral (Falsa Humildad)", "Pérdida o Duelo", "Paz y Buena Voluntad"])
    with col_save2:
        st.write("")
        st.write("")
        if st.button("📥 Registrar en Historial", type="primary", use_container_width=True):
            guardar_registro(puntaje_promedio, nivel_texto, emocion_detectada, nota_usuario)
            st.success("✅ ¡Registrado en tu historial local!")

# ==========================================
# PANTALLA 2: ESCÁNER SOMÁTICO Y TESTIGO
# ==========================================
elif pantalla == "2. Escáner Somático y Testigo (Nivel 200)":
    st.markdown("""
    <div class="hero-banner">
        <div class="badge-pill">Módulo 02 • Desidentificación Somática</div>
        <div class="hero-title">Escáner Somático y Despertar del Testigo</div>
        <div class="hero-subtitle">Paso 1: Detener la reacción física automática y cruzar la barrera crítica de los 200 puntos.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("#### 1. Evento Detonante")
        evento = st.selectbox(
            "¿Qué situación activó la alarma interna?",
            [
                "Llegada de dinero / Cobrar por mi trabajo",
                "Recibir un elogio o reconocimiento público",
                "Oportunidad de descansar o darme un gusto",
                "Una pérdida dolorosa (dinero, empleo o proyecto)",
                "Alguien ofreciéndome ayuda sin pedir nada"
            ]
        )
        
        st.markdown("#### 2. Mapa de Alarma Somática")
        zona_cuerpo = st.multiselect(
            "¿Dónde sientes la contracción en el cuerpo?",
            ["Nudo en la garganta", "Opresión en el pecho", "Plexo solar agitado / Fuego", "Tensión en mandíbula y hombros", "Agitación cardíaca"],
            default=["Opresión en el pecho"]
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("#### 3. Postura Interior")
        postura_interna = st.radio(
            "Honestidad Somática:",
            [
                "Puño cerrado: Finjo calma pero quiero que la incomodidad desaparezca ya.",
                "Mano abierta: Permito que la sensación física esté presente sin juzgarla ni pelear."
            ]
        )
        
        disfraz = st.checkbox("¿Aparece el disfraz moral? ('Yo con poco me apaño', 'no debo molestar')")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    
    st.subheader("👁️ Transmutación: Despertar al Testigo Consciente")
    st.write("Al presionar este botón, sales del personaje 'víctima/reactivo' y te posicionas como la conciencia que observa.")

    if st.button("👁️ Activar Modo Testigo Consciente", type="primary", use_container_width=True):
        st.session_state.testigo_activado = True
        
    if st.session_state.testigo_activado:
        st.markdown("""
        <div class="parchment-box">
            <h3 style="margin-top: 0; color: #78350F;">👁️ Decreto del Testigo Consciente (Nivel 200):</h3>
            <p class="parchment-text">«Yo no soy este nudo en la garganta ni esta opresión en el pecho. Yo no soy el miedo a no tener ni la culpa por recibir. Yo soy la conciencia tranquila y soberana que observa estas sensaciones pasar como nubes en el cielo.»</p>
        </div>
        """, unsafe_allow_html=True)
        st.info("💡 **Siguiente paso:** Pasa a la pantalla **3. Radar «Cero Leña»** para no alimentar el patrón con rumiaciones ni quejas.")

# ==========================================
# PANTALLA 3: RADAR CERO LEÑA
# ==========================================
elif pantalla == "3. Radar «Cero Leña» (Ayuno de Ego)":
    st.markdown("""
    <div class="hero-banner">
        <div class="badge-pill">Módulo 03 • Desatención Consciente</div>
        <div class="hero-title">Radar «Cero Leña» (Ayuno de Ego)</div>
        <div class="hero-subtitle">Paso 2: Retirar el combustible al pensamiento negativo. Lo que alimentas crece; lo que dejas de alimentar muere por inanición.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alert-danger-box">
        <h4 style="margin-top:0;">🔥 Principio de Hawkins: La Ley de la Inanición</h4>
        <p>Una sola emoción reprimida genera miles de pensamientos secundarios. Tratar de razonar con cada pensamiento es agotador. La verdadera solución es cortar la 'leña' de tu atención, tu rumia y tu queja.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("#### 💧 Identificador de Gotas (Pensamientos Sutiles)")
        g1 = st.checkbox("«Si cobro esto o me va bien, los demás me van a juzgar»")
        g2 = st.checkbox("«Tengo que cansarme y sufrir para que mi esfuerzo valga»")
        g3 = st.checkbox("«Con lo que perdí, nunca volveré a estar tranquilo»")
        g4 = st.checkbox("«Mejor me sacrifico yo para no incomodar a los demás»")
        
        if g1 or g2 or g3 or g4:
            st.caption("⚠️ **Atención:** Estás identificando gotas de combustible. ¡Retira tu atención de ellas!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("#### 🚫 Bloqueador de Queja Reactiva")
        queja = st.radio("¿Has contado tu problema o queja buscando compasión?", ["No, guardo silencio consciente", "Sí, he estado repasando la injusticia o la falta de dinero"])
        
        if queja.startswith("Sí"):
            st.error("🚫 **Atención:** La queja reactiva refuerza la identidad por debajo de 200 puntos.")
        else:
            st.success("✅ Excelente. El silencio consciente preserva tu energía elevada.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("⏳ Pausa de No-Acción (60 Segundos de Presencia)")
    st.write("Sostén la presencia en silencio sin llamar a nadie, sin justificar y sin huir.")
    
    if st.button("⏱️ Iniciar Pausa Consciente de 60 Segundos", type="primary"):
        progreso = st.progress(0)
        status = st.empty()
        for i in range(100):
            time.sleep(0.04)
            progreso.progress(i + 1)
            status.text(f"Sosteniendo la presencia limpia sin alimentar la emoción... {int((i+1)*0.6)}s")
        st.success("✨ ¡Has permitido que la emoción se disipe por inanición sin echarle leña!")

# ==========================================
# PANTALLA 4: RENDICIÓN ACTIVA Y CANCELACIÓN
# ==========================================
elif pantalla == "4. Rendición Activa & Cancelación ante Dios":
    st.markdown("""
    <div class="hero-banner">
        <div class="badge-pill">Módulo 04 • Expiación & Entrega</div>
        <div class="hero-title">Rendición Activa y Cancelación ante Dios</div>
        <div class="hero-subtitle">Paso 3: Entregar la raíz emocional a una Inteligencia Superior para su disolución definitiva.</div>
    </div>
    """, unsafe_allow_html=True)

    emocion_a_entregar = st.selectbox(
        "Selecciona el conflicto o herida a entregar:",
        [
            "Herida de No Merecimiento y Culpa por Recibir",
            "Dolor de Pérdida, Vacío o Duelo",
            "Miedo a la Escasez y Afán por el Futuro",
            "Resentimiento y Necesidad de Tener la Razón"
        ]
    )

    if emocion_a_entregar == "Herida de No Merecimiento y Culpa por Recibir":
        decreto = """«Reconozco esta emoción de culpa e indignidad en mi cuerpo. No la combato ni la alimento con pensamientos de pequeñez. 
Cancelo en mi mente cualquier creencia de que debo pagar con sufrimiento, sacrificio o agotamiento para tener derecho a ser amado y sustentado. 
Padre Santo, te entrego esta herida a la expiación para que Tú la disuelvas. Renuncio a la falsa humildad y me abro a recibir Tu gracia.»"""
    elif emocion_a_entregar == "Dolor de Pérdida, Vacío o Duelo":
        decreto = """«Reconozco este vacío y este dolor de pérdida. No huyo de él ni me refugio en el papel de víctima. 
Cancelo en mi mente la idea de que he quedado desamparado o separado de la Fuente. 
Padre, pongo este duelo en Tus manos para su completa sanación; reconozco que mi plenitud proviene de Ti y no de las formas pasajeras.»"""
    else:
        decreto = """«Reconozco este miedo y esta necesidad de controlar el porvenir. No peleo contra él. 
Cancelo todo pensamiento de escasez y de soledad en el mundo. 
Padre, descanso en Tu provisión infinita y te entrego todas mis preocupaciones.»"""

    st.markdown(f"""
    <div class="parchment-box">
        <h4 style="margin-top:0; color:#78350F;">🕊️ Decreto de Cancelación y Expiación:</h4>
        <p class="parchment-text">{decreto}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🕊️ Entregar y Cancelar Programa ante Dios", type="primary", use_container_width=True):
        st.balloons()
        st.success("✨ Carga entregada. La mente profunda ha disuelto la creencia limitante.")

# ==========================================
# PANTALLA 5: ANCLAJE BÍBLICO Y BUENA VOLUNTAD (>310)
# ==========================================
elif pantalla == "5. Anclaje Bíblico & Buena Voluntad (>310)":
    st.markdown("""
    <div class="hero-banner">
        <div class="badge-pill">Módulo 05 • El Mundo de las Causas</div>
        <div class="hero-title">Anclaje Bíblico y Buena Voluntad (>310)</div>
        <div class="hero-subtitle">Paso 4: Fijar la mente en la Provisión Divina y la Verdad respaldada por la Palabra de Dios.</div>
    </div>
    """, unsafe_allow_html=True)

    categoria_biblica = st.selectbox(
        "Selecciona el fundamento bíblico para tu día:",
        [
            "Suficiencia y Provisión (Salmo 23 y Filipenses 4)",
            "Vencer el Afán y la Ansiedad (Mateo 6)",
            "Liberación de la Culpa y Condenación (Romanos 8)",
            "Consuelo en la Pérdida y el Dolor (Salmo 34 y 147)",
            "Poder, Valentía y Fe (Josué 1 y 2 Timoteo 1)"
        ]
    )

    if categoria_biblica.startswith("Suficiencia"):
        v_text = "<b>Salmo 23:1:</b> <i>«Jehová es mi pastor; nada me faltará.»</i><br><br><b>Filipenses 4:19:</b> <i>«Mi Dios, pues, suplirá todo lo que os falta conforme a sus riquezas en gloria en Cristo Jesús.»</i>"
    elif categoria_biblica.startswith("Vencer el Afán"):
        v_text = "<b>Mateo 6:26, 33:</b> <i>«Mirad las aves del cielo... vuestro Padre celestial las alimenta. ¿No valéis vosotros mucho más? Buscad primeramente el reino de Dios... y todas estas cosas os serán añadidas.»</i>"
    elif categoria_biblica.startswith("Liberación de la Culpa"):
        v_text = "<b>Romanos 8:1:</b> <i>«Ahora, pues, ninguna condenación hay para los que están en Cristo Jesús.»</i>"
    elif categoria_biblica.startswith("Consuelo en la Pérdida"):
        v_text = "<b>Salmo 34:18:</b> <i>«Cercano está Jehová a los quebrantados de corazón; y salva a los contritos de espíritu.»</i>"
    else:
        v_text = "<b>2 Timoteo 1:7:</b> <i>«Porque no nos ha dado Dios espíritu de cobardía, sino de poder, de amor y de dominio propio.»</i>"

    st.markdown(f"""
    <div class="scripture-card">
        <h4 style="margin-top:0;">📖 Promesas Divinas:</h4>
        <div style="font-size: 1.1rem; line-height: 1.7;">{v_text}</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader("Oración y Decreto de Identidad en Dios")

    st.markdown("""
    <div class="alert-success-box">
        <h3 style="margin-top:0; font-family: 'Playfair Display', serif;">Padre Santo que estás en los cielos:</h3>
        <p style="font-size: 1.15rem; line-height: 1.8;">
        Hoy elijo reconocerme pleno y abundante.<br>
        Reconozco que la abundancia que forma parte de Ti también forma parte de mí.<br>
        Hoy decido reafirmar en mi mente que <b>nada me puede faltar</b>, porque Tú eres mi Pastor y estoy completamente sostenido por Ti.<br>
        Cancelo toda necesidad de sufrimiento y elijo vivir desde la Buena Voluntad, la paz y el gozo. Amén.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💾 Guardar Anclaje 310+ en mi Historial", type="primary", use_container_width=True):
        guardar_registro(325, "Buena Voluntad y Plenitud (>310)", "Anclaje Espiritual 310+", f"Compromiso con {categoria_biblica}")
        st.success("✨ ¡Anclaje 310+ registrado en tu historial diario!")

# ==========================================
# PANTALLA 6: GUÍA DE RUTINA DIARIA
# ==========================================
elif pantalla == "6. Guía de Rutina Diaria Consciente":
    st.markdown("""
    <div class="hero-banner">
        <div class="badge-pill">Módulo 06 • Ritmo de Práctica</div>
        <div class="hero-title">Guía de Rutina Diaria: Ritmo Consciente</div>
        <div class="hero-subtitle">Integra la práctica sin caer en la trampa del sobreesfuerzo infantil o la hipervigilancia.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alert-danger-box">
        <h4 style="margin-top:0;">⚠️ La Trampa de la Hipervigilancia</h4>
        <p>Intentar registrarte 15 veces al día es una manifestación sutil del no merecimiento: creer que debes agotarte para ser digno de sanar. Como enseña Jesús en <b>Mateo 6:27</b>: <i>«¿Quién podrá, afanándose, añadir un codo a su estatura?»</i>. El cambio ocurre en la presencia tranquila.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="routine-card-morning">
            <h3 style="color:#B45309; margin-top:0;">🌅 Mañana (3-5 min)</h3>
            <p><b>Anclaje en las Causas:</b></p>
            <ul>
                <li>Entra a Pantalla 5 (Anclaje Bíblico).</li>
                <li>Recita el Decreto del Ser.</li>
                <li>Ancla el Salmo 23:1 antes de sumergirte en el trabajo.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="routine-card-day">
            <h3 style="color:#1E40AF; margin-top:0;">⚡ Día (En vivo)</h3>
            <p><b>Presencia Somática:</b></p>
            <ul>
                <li>Al cobrar o recibir: Mano Abierta.</li>
                <li>Al recibir elogios: Frenar el disfraz moral.</li>
                <li>Al querer quejarte: Cero Leña.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="routine-card-night">
            <h3 style="color:#6D28D9; margin-top:0;">🌙 Noche (3-5 min)</h3>
            <p><b>Auditoría y Cierre:</b></p>
            <ul>
                <li>Abre el Barómetro y registra tu jornada.</li>
                <li>Entrega cualquier culpa en Pantalla 4.</li>
                <li>Descansa en paz sabiendo que Dios sostiene tu vida.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📋 Checklist Diario de Práctica")
    c1 = st.checkbox("🌅 Mañana: Realicé mi anclaje del Ser antes de reaccionar al mundo.")
    c2 = st.checkbox("⚡ Día: Detuve un impulso de culpa, queja o contracción ante una bendición.")
    c3 = st.checkbox("🌙 Noche: Cierro la jornada soltando el control y descansando en Dios.")

    if c1 and c2 and c3:
        if st.button("💾 Registrar Cumplimiento Diario", type="primary", use_container_width=True):
            guardar_registro(325, "Buena Voluntad y Plenitud (>310)", "Rutina Diaria Completa", "Completó Mañana, Día y Noche en paz.")
            st.success("✅ ¡Jornada consciente registrada en el historial!")

# ==========================================
# PANTALLA 7: HISTORIAL Y PROGRESO
# ==========================================
elif pantalla == "7. Historial y Progreso (Panel Local)":
    st.markdown("""
    <div class="hero-banner">
        <div class="badge-pill">Módulo 07 • Métricas & Persistencia</div>
        <div class="hero-title">Historial y Progreso Consciente</div>
        <div class="hero-subtitle">Monitorea visualmente tu evolución desde el modo reactivo (<200) hacia la Buena Voluntad (>310).</div>
    </div>
    """, unsafe_allow_html=True)

    historial = cargar_historial()

    col_t1, col_t2, col_t3 = st.columns([2, 1, 1])
    with col_t1:
        st.write(f"📁 **Persistencia local activa:** `historial_calibracion.json`")
    with col_t2:
        if not historial and st.button("🧪 Cargar Datos de Prueba"):
            sembrar_datos_ejemplo()
            st.rerun()
    with col_t3:
        if historial and st.button("🗑️ Limpiar Historial"):
            limpiar_historial()
            st.rerun()

    if not historial:
        st.info("ℹ️ No hay registros guardados. Haz tu primer diagnóstico en la Pantalla 1 o presiona 'Cargar Datos de Prueba'.")
    else:
        df = pd.DataFrame(historial)

        total_s = len(df)
        prom_pts = int(df["puntaje"].mean())
        max_p = int(df["puntaje"].max())
        altas = len(df[df["puntaje"] >= 310])

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Registros Totales", total_s)
        m2.metric("Promedio Calibración", f"{prom_pts} pts")
        m3.metric("Máximo Alcanzado", f"{max_p} pts")
        m4.metric("Días en >310", f"{altas} ({int(altas/total_s*100)}%)")

        st.divider()
        st.subheader("📈 Gráfica de Evolución Temporal")
        
        chart_df = df[["fecha_corta", "puntaje"]].set_index("fecha_corta")
        st.line_chart(chart_df, y="puntaje", color="#3B82F6")

        st.divider()
        st.subheader("📋 Registro Detallado")
        disp_df = df[["id", "fecha", "puntaje", "nivel", "emocion", "notas"]].copy()
        disp_df.columns = ["#", "Fecha/Hora", "Puntaje", "Nivel", "Foco/Emoción", "Notas"]
        st.dataframe(disp_df, use_container_width=True, hide_index=True)

        st.divider()
        col_ex1, col_ex2 = st.columns(2)
        with col_ex1:
            st.download_button("📥 Descargar CSV (Excel)", disp_df.to_csv(index=False).encode("utf-8"), "historial_conciencia.csv", "text/csv", use_container_width=True)
        with col_ex2:
            st.download_button("📥 Descargar Respaldo JSON", json.dumps(historial, ensure_ascii=False, indent=2).encode("utf-8"), "historial_conciencia.json", "application/json", use_container_width=True)
