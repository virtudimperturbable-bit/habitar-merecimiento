import streamlit as st
import time
import json
import os
from datetime import datetime
import pandas as pd

# Configuración de página
st.set_page_config(
    page_title="Habitar el Merecimiento - Conciencia y Sanación",
    page_icon="🕊️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos visuales personalizados
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        border-radius: 10px;
        padding: 1.2rem;
        border-left: 5px solid #3B82F6;
        margin-bottom: 1rem;
    }
    .quote-box {
        background-color: #EFF6FF;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        border-left: 4px solid #2563EB;
        font-style: italic;
        color: #1E40AF;
        margin: 1rem 0;
    }
    .scripture-box {
        background-color: #FEF3C7;
        border-radius: 8px;
        padding: 1.2rem;
        border-left: 4px solid #D97706;
        color: #78350F;
        margin: 1rem 0;
    }
    .alert-ego {
        background-color: #FEE2E2;
        border-radius: 8px;
        padding: 1rem;
        border-left: 4px solid #DC2626;
        color: #991B1B;
    }
    .save-box {
        background-color: #F0FDF4;
        border-radius: 8px;
        padding: 1.2rem;
        border-left: 4px solid #16A34A;
        color: #166534;
        margin: 1rem 0;
    }
    .routine-morning {
        background-color: #FFFBEB;
        border-radius: 8px;
        padding: 1.2rem;
        border-left: 5px solid #F59E0B;
        margin-bottom: 1rem;
    }
    .routine-day {
        background-color: #EFF6FF;
        border-radius: 8px;
        padding: 1.2rem;
        border-left: 5px solid #3B82F6;
        margin-bottom: 1rem;
    }
    .routine-night {
        background-color: #F5F3FF;
        border-radius: 8px;
        padding: 1.2rem;
        border-left: 5px solid #8B5CF6;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# GESTOR DE GUARDADO LOCAL (JSON)
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
# INICIALIZACIÓN DE SESIÓN
# ----------------------------------------------------
if "testigo_activado" not in st.session_state:
    st.session_state.testigo_activado = False
if "decreto_entregado" not in st.session_state:
    st.session_state.decreto_entregado = False
if "puntuacion_actual" not in st.session_state:
    st.session_state.puntuacion_actual = 160

# ----------------------------------------------------
# BARRA LATERAL DE NAVEGACIÓN
# ----------------------------------------------------
st.sidebar.title("🕊️ Navegación")
st.sidebar.markdown("**Sistema 'Habitar el Merecimiento'**")
st.sidebar.markdown("*Fundamentado en el mapa de conciencia de David Hawkins y promesas bíblicas.*")

pantalla = st.sidebar.radio(
    "Selecciona la pantalla interactiva:",
    [
        "1. Barómetro de Conciencia (Diagnóstico)",
        "2. Escáner Somático y Despertar del Testigo",
        "3. Radar «Cero Leña» (Ayuno de Ego)",
        "4. Rendición Activa y Cancelación ante Dios",
        "5. Anclaje Bíblico y Buena Voluntad (>310)",
        "6. Guía de Rutina Diaria (Ritmo Consciente)",
        "7. Historial y Progreso Diario (Guardado Local)"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Niveles clave de Hawkins:")
st.sidebar.caption("• **< 200**: Modo Reactivo / Ego (Culpa, Miedo, Orgullo)")
st.sidebar.caption("• **200**: El Testigo Consciente (Coraje, Verdad)")
st.sidebar.caption("• **310+**: Buena Voluntad (Apertura, Plenitud, Gracia)")

historial_actual = cargar_historial()
if historial_actual:
    st.sidebar.divider()
    st.sidebar.success(f"💾 **{len(historial_actual)} registros** guardados localmente")
    ultimo_puntaje = historial_actual[-1]["puntaje"]
    st.sidebar.metric("Última Calibración", f"{ultimo_puntaje} pts")

# ==========================================
# PANTALLA 1: BARÓMETRO DE CONCIENCIA
# ==========================================
if pantalla == "1. Barómetro de Conciencia (Diagnóstico)":
    st.markdown('<div class="main-title">Barómetro de Conciencia de Hawkins</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Descubre si estás operando desde el "muñeco reactivo" (<200) o desde el Ser Consciente (>200 y >310)</div>', unsafe_allow_html=True)

    st.info("💡 **Ley fundamental**: El mundo exterior es solo un espejo que refleja lo que sostienes internamente. Cambiar la estrategia física sin cambiar el estado de conciencia no erradica el bloqueo.")

    st.subheader("Cuestionario Somático y de Conciencia")
    
    col1, col2 = st.columns(2)
    
    with col1:
        p1 = st.radio(
            "1. Cuando recibes dinero, un elogio, descanso o ayuda:",
            [
                ("Me siento con culpa, en deuda o con impulso urgente de compensar", 125),
                ("Digo 'con poco me apaño' o 'primero los demás' (disfraz moral)", 150),
                ("Noto la incomodidad física pero me detengo a observarla sin huir", 220),
                ("Recibo con el corazón abierto, gratitud y sin sentirme en deuda", 310)
            ],
            format_func=lambda x: x[0]
        )
        
        p2 = st.radio(
            "2. ¿Cómo responde tu cuerpo ante la posibilidad de prosperar o descansar?",
            [
                ("Puño cerrado: contracción en el pecho, nudo en garganta o miedo", 100),
                ("Inquietud constante: busco problemas o tareas para justificar mi existencia", 140),
                ("Respiración neutra: siento la tensión y no peleo contra ella", 210),
                ("Mano abierta: relajación profunda y permiso de habitar la paz", 320)
            ],
            format_func=lambda x: x[0]
        )

    with col2:
        p3 = st.radio(
            "3. ¿Qué haces con los pensamientos negativos o de escasez?",
            [
                ("Rumia continua: le doy vueltas una y otra vez buscando culpables", 110),
                ("Me quejo con otros de lo injusta o difícil que es la vida", 130),
                ("Los reconozco como chispas neutras y decido no echarles leña", 230),
                ("Cancelo el pensamiento limitante y descanso en la provisión divina", 330)
            ],
            format_func=lambda x: x[0]
        )

        p4 = st.radio(
            "4. Relación con tu historia familiar o lealtades del pasado:",
            [
                ("Siento que tener más o descansar es traicionar el sufrimiento de mi linaje", 80),
                ("Me esfuerzo hasta el agotamiento para demostrar mi valía", 130),
                ("Entiendo que mi linaje hizo lo que pudo y elijo no repetir el dolor", 220),
                ("Bendigo a mis antepasados y honro la vida viviendo con plenitud", 320)
            ],
            format_func=lambda x: x[0]
        )

    puntaje_promedio = int((p1[1] + p2[1] + p3[1] + p4[1]) / 4)
    st.session_state.puntuacion_actual = puntaje_promedio

    if puntaje_promedio < 200:
        nivel_texto = "Campo Reactivo del Ego (<200)"
    elif puntaje_promedio < 310:
        nivel_texto = "El Testigo Consciente (200-300)"
    else:
        nivel_texto = "Buena Voluntad y Plenitud (>310)"

    st.divider()
    st.subheader("Resultado de Calibración Estimada")
    
    col_score1, col_score2 = st.columns([1, 2])
    with col_score1:
        st.metric(label="Calibración Actual", value=f"{puntaje_promedio} pts", delta=f"{puntaje_promedio - 200} sobre el umbral crítico")
        st.progress(min(max(puntaje_promedio / 400.0, 0.05), 1.0))
        
    with col_score2:
        if puntaje_promedio < 200:
            st.markdown(f"""
            <div class="alert-ego">
                <h4>⚠️ Estado: {nivel_texto}</h4>
                <p>Estás operando bajo la influencia de la <b>culpa, el miedo o el autosacrificio</b>. Tu mente está atrapada en el <i>muñeco reactivo</i>, manifestando precisamente lo que teme. La solución no es exigirte más, sino retirar el combustible al ego y despertar al Testigo.</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("👉 **Ruta recomendada**: Pasa a la pantalla **2. Escáner Somático** para activar el Testigo y desidentificarte.")
        elif 200 <= puntaje_promedio < 310:
            st.markdown(f"""
            <div class="quote-box">
                <h4>⚖️ Estado: {nivel_texto}</h4>
                <p>Has alcanzado el umbral del <b>Coraje y la Responsabilidad</b>. Eres capaz de observar tus emociones sin actuar reactivamente ni justificarte. Estás listo para soltar la queja y entregarte a la Buena Voluntad.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="scripture-box">
                <h4>✨ Estado: {nivel_texto}</h4>
                <p>Te encuentras anclado en el <b>Mundo de las Causas</b>. Reconoces que la abundancia y la paz son tu estado natural en Dios. En este nivel, aquello que sostienes en tu mente se materializa sin desgaste ni lucha.</p>
            </div>
            """, unsafe_allow_html=True)

    # SECCIÓN DE GUARDADO LOCAL
    st.divider()
    st.markdown('<div class="save-box"><h4>💾 Guardar este Diagnóstico en tu Historial Local</h4><p>Registra este chequeo para seguir tu evolución a lo largo de los días y semanas.</p></div>', unsafe_allow_html=True)
    
    col_save1, col_save2 = st.columns([2, 1])
    with col_save1:
        nota_usuario = st.text_input("Nota o reflexión del momento (opcional):", placeholder="Ej: Me sentí con culpa al cobrar por el proyecto, pero frené la justificación...")
        emocion_detectada = st.selectbox("Emoción o foco predominante:", ["Herida de No Merecimiento", "Culpa por Recibir / Cobrar", "Miedo a la Escasez", "Disfraz Moral (Falsa Humildad)", "Pérdida o Duelo", "Paz y Buena Voluntad"])
    with col_save2:
        st.write("")
        st.write("")
        if st.button("📥 Guardar en Historial", type="primary"):
            guardar_registro(puntaje_promedio, nivel_texto, emocion_detectada, nota_usuario)
            st.success("✅ ¡Diagnóstico guardado en tu archivo local! Puedes verlo en la pestaña '7. Historial y Progreso Diario'.")

# ==========================================
# PANTALLA 2: ESCÁNER SOMÁTICO Y TESTIGO
# ==========================================
elif pantalla == "2. Escáner Somático y Despertar del Testigo":
    st.markdown('<div class="main-title">Escáner Somático y Despertar del Testigo</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Paso 1: Detener la reacción automática del cuerpo y cruzar la barrera de los 200</div>', unsafe_allow_html=True)

    st.write("Cada vez que recibes dinero, un elogio o una oportunidad de descanso, o cuando experimentas una pérdida, tu sistema nervioso reacciona automáticamente.")

    col1, col2 = st.columns(2)
    with col1:
        evento = st.selectbox(
            "¿Qué situación detonó tu emoción actual?",
            [
                "Llegada de dinero / Cobrar por mi trabajo",
                "Recibir un elogio o reconocimiento público",
                "Oportunidad de descansar o darme un gusto",
                "Una pérdida dolorosa (dinero, empleo, persona o proyecto)",
                "Alguien ofreciéndome ayuda sin pedir nada a cambio"
            ]
        )
        
        zona_cuerpo = st.multiselect(
            "¿En qué zona de tu cuerpo sientes la contracción o alarma?",
            ["Nudo en la garganta", "Opresión en el pecho", "Vacío o fuego en el estómago/plexo", "Tensión en hombros y mandíbula", "Agitación cardíaca"],
            default=["Opresión en el pecho"]
        )

    with col2:
        postura_interna = st.radio(
            "Honestidad somática: ¿Cuál es tu postura interior en este momento?",
            [
                "Puño cerrado: Finjo calma pero quiero que la incomodidad se vaya ya.",
                "Mano abierta: Permito que la sensación física esté presente sin juzgarla ni pelear."
            ]
        )
        
        disfraz = st.checkbox("¿Aparece el disfraz moral? ('Yo con poco me apaño', 'primero los demás', 'no merezco esto')")

    st.divider()
    
    st.subheader("El Despertar del Testigo (Nivel 200)")
    st.write("Al presionar este botón, sales de la identidad del 'muñeco reactivo' y asumes el lugar del observador consciente.")

    if st.button("👁️ Activar Modo Testigo", type="primary"):
        st.session_state.testigo_activado = True
        st.success("¡Modo Testigo Activado! Has cruzado conscientemente hacia los 200 puntos.")
        
    if st.session_state.testigo_activado:
        st.markdown("""
        <div class="quote-box">
            <h3>👁️ Declaración del Testigo Consciente:</h3>
            <p><b>«Yo no soy este nudo en la garganta ni esta opresión en el pecho. Yo no soy el miedo a no tener o la culpa por recibir. Yo soy la conciencia tranquila que observa estas sensaciones pasar como nubes en el cielo.»</b></p>
        </div>
        """, unsafe_allow_html=True)
        st.info("Paso siguiente: Ve a **3. Radar «Cero Leña»** para no alimentar el patrón con pensamientos o quejas.")

# ==========================================
# PANTALLA 3: RADAR CERO LEÑA
# ==========================================
elif pantalla == "3. Radar «Cero Leña» (Ayuno de Ego)":
    st.markdown('<div class="main-title">Radar «Cero Leña» (Ayuno de Ego)</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Paso 2: Retirar el combustible al ego. Lo que refuerzas crece; lo que dejas de alimentar muere.</div>', unsafe_allow_html=True)

    st.warning("⚠️ **Advertencia de Hawkins**: Una emoción primaria estancada genera miles de pensamientos. Tratar de discutir con cada pensamiento es inútil si sigues echándole la 'leña' de tu atención, tu rumia o tu queja.")

    st.subheader("1. Identificador de Gotas de Agua (Pensamientos Sutiles)")
    st.write("Selecciona los pensamientos sutiles que has estado alimentando hoy:")
    
    g1 = st.checkbox("«Si cobro esto o me va bien, los demás me van a juzgar o rechazar»")
    g2 = st.checkbox("«Tengo que cansarme y sufrir para que mi esfuerzo sea válido»")
    g3 = st.checkbox("«Con la pérdida que tuve, la vida nunca volverá a ser plena»")
    g4 = st.checkbox("«Mejor me sacrifico yo para que otros estén tranquilos»")
    
    if g1 or g2 or g3 or g4:
        st.markdown('<div class="alert-ego"><b>🔥 Alerta:</b> Esas son las pequeñas gotas que mantienen viva la hoguera de tu escasez. ¡Retira tu atención de ellas ahora!</div>', unsafe_allow_html=True)

    st.subheader("2. Detector de la Queja Reactiva")
    st.write("¿Has estado contando tu problema a otros buscando consuelo o sintiéndote víctima?")
    queja = st.radio("¿Has participado en quejas o reproches hoy?", ["No, me mantengo en silencio consciente", "Sí, he estado repasando la injusticia o la falta de dinero"])
    
    if queja.startswith("Sí"):
        st.error("🚫 **Detén la queja inmediatamente**: Contar el problema refuerza la identidad del ego en niveles por debajo de 200 y neutraliza la sanación.")

    st.subheader("3. Pausa de No-Acción (Dejar madurar la emoción)")
    st.write("Permanece en silencio durante 60 segundos observando la sensación física sin huir, sin llamar a nadie y sin gastar compulsivamente.")
    
    if st.button("⏳ Iniciar Temporizador de No-Acción (60s)"):
        progreso = st.progress(0)
        status = st.empty()
        for i in range(100):
            time.sleep(0.04)
            progreso.progress(i + 1)
            status.text(f"Sosteniendo la presencia sin alimentar la emoción... {int((i+1)*0.6)}s")
        st.success("¡Excelente! Has permitido que la energía comience a disiparse por inanición sin echarle leña.")

# ==========================================
# PANTALLA 4: RENDICIÓN ACTIVA Y CANCELACIÓN
# ==========================================
elif pantalla == "4. Rendición Activa y Cancelación ante Dios":
    st.markdown('<div class="main-title">Rendición Activa y Cancelación ante Dios</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Paso 3: Entregar la raíz emocional a una Inteligencia Superior para su disolución total</div>', unsafe_allow_html=True)

    st.info("🕊️ Hawkins enseña que el ego no puede desarmarse a sí mismo. La verdadera liberación ocurre cuando nos rendimos y entregamos el conflicto a Dios.")

    emocion_a_entregar = st.selectbox(
        "¿Qué emoción o herida vas a entregar hoy?",
        [
            "Herida de No Merecimiento y Culpa por Recibir",
            "Dolor de Pérdida, Vacío o Duelo",
            "Miedo a la Escasez y Afán por el Futuro",
            "Resentimiento y Necesidad de Tener la Razón"
        ]
    )

    st.subheader("Decreto de Cancelación y Expiación")
    st.write("Lee en voz alta con total devoción y certeza:")

    if emocion_a_entregar == "Herida de No Merecimiento y Culpa por Recibir":
        decreto = """«Reconozco esta emoción de culpa e indignidad en mi cuerpo. No la combato ni la alimento con pensamientos de pequeñez. 
Cancelo en mi mente cualquier creencia de que debo pagar con sufrimiento, sacrificio o agotamiento para tener derecho a ser amado y sustentado. 
Padre Santo, te entrego esta herida a la expiación para que Tú la disuelvas. Renuncio a la falsa humildad y me abro a recibir Tu gracia.»"""
    elif emocion_a_entregar == "Dolor de Pérdida, Vacío o Duelo":
        decreto = """«Reconozco este vacío y este dolor de pérdida. No huyo de él ni me refugio en el papel de víctima. 
Cancelo en mi mente la idea de que he quedado desamparado o separado de la Fuente. 
Padre, pongo este duelo en Tus manos para su completa sanación; reconozco que mi plenitud y mi vida provienen de Ti y no de las formas pasajeras.»"""
    else:
        decreto = """«Reconozco este miedo y esta necesidad de controlar el porvenir. No peleo contra él. 
Cancelo todo pensamiento de escasez y de soledad en el mundo. 
Padre, descanso en Tu provisión infinita y te entrego todas mis preocupaciones.»"""

    st.markdown(f'<div class="quote-box" style="font-size: 1.15rem; line-height: 1.6;">{decreto}</div>', unsafe_allow_html=True)

    if st.button("🕊️ Entregar y Cancelar ante Dios", type="primary"):
        st.session_state.decreto_entregado = True
        st.balloons()
        st.success("La carga ha sido entregada. La mente profunda ha cancelado el programa limitante.")

# ==========================================
# PANTALLA 5: ANCLAJE BÍBLICO Y BUENA VOLUNTAD (>310)
# ==========================================
elif pantalla == "5. Anclaje Bíblico y Buena Voluntad (>310)":
    st.markdown('<div class="main-title">Anclaje Bíblico y Buena Voluntad (> 310)</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Paso 4: Fijar la mente en el Mundo de las Causas respaldado por la Palabra de Dios</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="scripture-box">
        <h3>✨ Nivel 310: El Poder de la Buena Voluntad</h3>
        <p>A partir de los 310 puntos en la escala de Hawkins, la mente se sintoniza con la Gracia. Ya no operas desde el esfuerzo o la manipulación externa, sino desde la convicción de que todo bien está provisto por el Padre.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Promesas Bíblicas para Desactivar los Estados Bajos")
    
    categoria_biblica = st.selectbox(
        "Selecciona el fundamento bíblico que necesitas hoy:",
        [
            "Suficiencia y Provisión (Salmo 23 y Filipenses 4)",
            "Vencer el Afán y la Ansiedad (Mateo 6)",
            "Liberación de la Culpa y Condenación (Romanos 8)",
            "Consuelo en la Pérdida y el Dolor (Salmo 34 y 147)",
            "Poder, Valentía y Fe (Josué 1 y 2 Timoteo 1)"
        ]
    )

    if categoria_biblica.startswith("Suficiencia"):
        st.markdown("""
        > **Salmo 23:1**: *«Jehová es mi pastor; nada me faltará.»*  
        > **Filipenses 4:19**: *«Mi Dios, pues, suplirá todo lo que os falta conforme a sus riquezas en gloria en Cristo Jesús.»*
        """)
    elif categoria_biblica.startswith("Vencer el Afán"):
        st.markdown("""
        > **Mateo 6:26, 33**: *«Mirad las aves del cielo, que no siembran, ni siegan, ni recogen en graneros; y vuestro Padre celestial las alimenta. ¿No valéis vosotros mucho más que ellas? [...] Mas buscad primeramente el reino de Dios y su justicia, y todas estas cosas os serán añadidas.»*  
        > **Filipenses 4:6-7**: *«Por nada estéis afanosos, sino sean conocidas vuestras peticiones delante de Dios en toda oración y ruego, con acción de gracias. Y la paz de Dios, que sobrepasa todo entendimiento, guardará vuestros corazones y vuestros pensamientos.»*
        """)
    elif categoria_biblica.startswith("Liberación de la Culpa"):
        st.markdown("""
        > **Romanos 8:1**: *«Ahora, pues, ninguna condenación hay para los que están en Cristo Jesús.»*  
        > **Salmo 103:12**: *«Cuanto está lejos el oriente del occidente, hizo alejar de nosotros nuestras rebeliones.»*
        """)
    elif categoria_biblica.startswith("Consuelo en la Pérdida"):
        st.markdown("""
        > **Salmo 34:18**: *«Cercano está Jehová a los quebrantados de corazón; y salva a los contritos de espíritu.»*  
        > **Salmo 147:3**: *«Él sana a los quebrantados de corazón, y venda sus heridas.»*
        """)
    else:
        st.markdown("""
        > **Josué 1:9**: *«Mira que te mando que te esfuerces y seas valiente; no temas ni desmayes, porque Jehová tu Dios estará contigo en dondequiera que vayas.»*  
        > **2 Timoteo 1:7**: *«Porque no nos ha dado Dios espíritu de cobardía, sino de poder, de amor y de dominio propio.»*
        """)

    st.divider()
    st.subheader("Oración y Decreto Final del Ser (Nivel 310+)")
    st.write("Sella tu jornada con esta afirmación de identidad:")

    st.markdown("""
    <div class="quote-box" style="font-size: 1.2rem; line-height: 1.7; background-color: #F0FDF4; border-left: 5px solid #16A34A; color: #166534;">
        <b>Padre Santo que estás en los cielos:</b><br>
        Hoy elijo reconocerme pleno y abundante.<br>
        Reconozco que la abundancia que forma parte de Ti también forma parte de mí.<br>
        Hoy decido reafirmar en mi mente y en mi conciencia que <b>nada me puede faltar</b>, porque Tú eres mi Pastor y estoy completamente sostenido por Ti.<br>
        Cancelo toda necesidad de sufrimiento y elijo vivir desde la Buena Voluntad, la paz y el gozo. Amén.
    </div>
    """, unsafe_allow_html=True)

    compromiso = st.checkbox("✅ Firmo conscientemente: Hoy habitaré este estado de descanso y confianza plena sin sabotear mi bienestar.")
    if compromiso:
        st.success("🎉 ¡Calibración confirmada en Buena Voluntad (>310)! Camina hoy con la certeza de que tu sustento es divino.")
        if st.button("💾 Guardar este Anclaje 310+ en mi Historial"):
            guardar_registro(320, "Buena Voluntad y Plenitud (>310)", "Anclaje Espiritual 310+", f"Compromiso sellado con {categoria_biblica}")
            st.success("✨ ¡Anclaje 310+ registrado en tu historial diario!")

# ==========================================
# PANTALLA 6: GUÍA DE RUTINA DIARIA (RITMO CONSCIENTE)
# ==========================================
elif pantalla == "6. Guía de Rutina Diaria (Ritmo Consciente)":
    st.markdown('<div class="main-title">Guía de Rutina Diaria: Ritmo Consciente</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Aprende a integrar el sistema de forma natural y sostenible: Mañana, Tarde y Noche</div>', unsafe_allow_html=True)

    # ALERTA DE HIPERVIGILANCIA
    st.markdown("""
    <div class="alert-ego">
        <h4>⚠️ ¿Cuántas veces al día registrarse? La trampa de la «hipervigilancia»</h4>
        <p>Creer que <i>«cuantas más veces mejor»</i> o intentar registrarte 10 o 15 veces al día es una manifestación sutil de la <b>herida del merecimiento</b>: la creencia inconsciente de que para ser digno debes desgastarte, sobreexigirte o trabajar sin tregua.</p>
        <p>David Hawkins advertía que el ego puede utilizar las herramientas de sanación como un mecanismo de control. Además, como enseña Jesús en <b>Mateo 6:27</b>: <i>«¿Y quién de vosotros podrá, por mucho que se afane, añadir a su estatura un codo?»</i>. La verdadera transformación ocurre en el descanso y en la presencia, no en la obsesión compulsiva.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("El Ritmo Consciente en 3 Momentos")

    col_m, col_d, col_n = st.columns(3)

    with col_m:
        st.markdown("""
        <div class="routine-morning">
            <h3>🌅 1. Mañana (3 a 5 min)</h3>
            <h4>Calibración y Anclaje en las Causas</h4>
            <p><b>Momento:</b> Al despertar, antes de revisar mensajes o sumergirte en el afán laboral.</p>
            <p><b>Acción en la app:</b></p>
            <ul>
                <li>Entra directo a <b>Pantalla 5 (Anclaje Bíblico)</b>.</li>
                <li>Recita el Decreto del Ser reconociendo que tu sustento proviene del Padre.</li>
                <li>Ancla en tu mente el <b>Salmo 23:1</b>: <i>«Jehová es mi pastor; nada me faltará»</i>.</li>
            </ul>
            <p><b>Propósito:</b> Estableces tu identidad desde el <b>Mundo de las Causas</b> antes de reaccionar a los efectos del día.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_d:
        st.markdown("""
        <div class="routine-day">
            <h3>⚡ 2. Durante el Día</h3>
            <h4>Presencia Somática en Vivo</h4>
            <p><b>Momento:</b> Solo cuando surjan detonantes reales en tus actividades cotidianas.</p>
            <p><b>Acción en el cuerpo (sin obsesión):</b></p>
            <ul>
                <li><b>Al cobrar o recibir dinero:</b> Detén la urgencia de justificar o compensar; practica la <b>Mano Abierta</b>.</li>
                <li><b>Al recibir elogios o ayuda:</b> Frena el disfraz moral de <i>«yo con poco me apaño»</i>.</li>
                <li><b>Al querer quejarte:</b> Recuerda que la queja es leña pura; guarda silencio consciente (<b>Cero Leña</b>).</li>
            </ul>
            <p><b>Propósito:</b> Reentrenar tu sistema nervioso en el momento exacto en que la vida te ofrece abundancia.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_n:
        st.markdown("""
        <div class="routine-night">
            <h3>🌙 3. Noche (3 a 5 min)</h3>
            <h4>Auditoría de Cero Leña y Cierre</h4>
            <p><b>Momento:</b> Antes de acostarte, cerrando la jornada en paz.</p>
            <p><b>Acción en la app:</b></p>
            <ul>
                <li>Abre <b>Pantalla 1 (Barómetro)</b> y responde con honestidad sobre tu jornada.</li>
                <li>Revisa si caíste en quejas o rumiaciones y guárdalo en tu <b>Historial Local</b>.</li>
                <li>Si hubo culpa o pérdida, haz el decreto de entrega de <b>Pantalla 4</b>.</li>
                <li>Descansa en <b>Filipenses 4:6-7</b>: entregando toda ansiedad a Dios.</li>
            </ul>
            <p><b>Propósito:</b> Desconectar la mente del autosacrificio y permitir que el cuerpo descanse en gracia.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # CHECKLIST INTERACTIVO DIARIO
    st.subheader("📋 Checklist de Práctica Consciente de Hoy")
    st.write("Marca los pasos que lograste habitar conscientemente durante el día:")

    c_manana = st.checkbox("🌅 **Mañana:** Realicé mi anclaje del Ser y recordé que mi valor no depende de mi autosacrificio.")
    c_dia = st.checkbox("⚡ **Día:** Detuve al menos un impulso de queja, contracción o culpa ante una oportunidad de bienestar.")
    c_noche = st.checkbox("🌙 **Noche:** Cierro el día soltando el control y descansando en la provisión del Padre celestial.")

    if c_manana and c_dia and c_noche:
        st.markdown("""
        <div class="save-box">
            <h4>🎉 ¡Ritmo Consciente Completado Exitosamente!</h4>
            <p>Has sostenido tu conciencia despierta a lo largo del día sin caer en la trampa de la autoexigencia.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("💾 Registrar Cumplimiento Diario en el Historial", type="primary"):
            guardar_registro(325, "Buena Voluntad y Plenitud (>310)", "Rutina Diaria Consciente", "Completó con éxito el ritmo de Mañana, Día y Noche sin sobreesfuerzo.")
            st.success("✅ ¡Rutina diaria registrada en tu archivo local! Calibración anclada en Buena Voluntad (>310).")

# ==========================================
# PANTALLA 7: HISTORIAL Y PROGRESO DIARIO
# ==========================================
elif pantalla == "7. Historial y Progreso Diario (Guardado Local)":
    st.markdown('<div class="main-title">Historial y Progreso Consciente</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Monitorea cómo tu sistema evoluciona del modo reactivo (<200) a la Buena Voluntad (>310)</div>', unsafe_allow_html=True)

    historial = cargar_historial()

    # Opciones de gestión superior
    col_tools1, col_tools2, col_tools3 = st.columns([2, 1, 1])
    with col_tools1:
        st.write(f"📁 **Archivo local de persistencia:** `historial_calibracion.json`")
    with col_tools2:
        if not historial:
            if st.button("🧪 Cargar Datos de Ejemplo"):
                sembrar_datos_ejemplo()
                st.rerun()
    with col_tools3:
        if historial:
            if st.button("🗑️ Limpiar Historial"):
                limpiar_historial()
                st.rerun()

    if not historial:
        st.info("ℹ️ Aún no tienes registros guardados en tu historial local. Realiza tu primer test en la pantalla **'1. Barómetro de Conciencia'** o pulsa el botón **'Cargar Datos de Ejemplo'** para explorar la gráfica y el análisis.")
    else:
        df = pd.DataFrame(historial)

        # Métricas principales
        total_sesiones = len(df)
        promedio_pts = int(df["puntaje"].mean())
        max_pts = int(df["puntaje"].max())
        sesiones_altas = len(df[df["puntaje"] >= 310])
        pct_altas = int((sesiones_altas / total_sesiones) * 100)

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Registros Totales", total_sesiones)
        m2.metric("Promedio Histórico", f"{promedio_pts} pts")
        m3.metric("Máxima Calibración", f"{max_pts} pts")
        m4.metric("En Buena Voluntad (>310)", f"{sesiones_altas} ({pct_altas}%)")

        st.divider()

        # Gráfico de evolución de puntaje
        st.subheader("📈 Evolución de tu Calibración de Conciencia")
        
        # Preparación para gráfico
        chart_data = df[["fecha_corta", "puntaje"]].copy()
        chart_data = chart_data.set_index("fecha_corta")
        st.line_chart(chart_data, y="puntaje", color="#2563EB")
        
        st.caption("🟢 **Zona Superior (>310)**: Buena Voluntad y Plenitud | 🟡 **Zona Media (200-310)**: Testigo Consciente | 🔴 **Zona Inferior (<200)**: Modo Reactivo del Ego")

        st.divider()

        # Tabla interactiva con el historial detallado
        st.subheader("📋 Registro Detallado de Sesiones")
        
        display_df = df[["id", "fecha", "puntaje", "nivel", "emocion", "notas"]].copy()
        display_df.columns = ["#", "Fecha y Hora", "Puntaje", "Nivel de Conciencia", "Foco / Emoción", "Notas y Reflexiones"]
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)

        # Herramientas de exportación
        st.subheader("📤 Exportar tus Registros")
        col_exp1, col_exp2 = st.columns(2)
        
        with col_exp1:
            csv_data = display_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Descargar Historial en CSV (Excel)",
                data=csv_data,
                file_name="historial_calibracion_conciencia.csv",
                mime="text/csv"
            )
            
        with col_exp2:
            json_data = json.dumps(historial, ensure_ascii=False, indent=2).encode("utf-8")
            st.download_button(
                label="📥 Descargar Archivo JSON de Respaldo",
                data=json_data,
                file_name="historial_calibracion_conciencia.json",
                mime="application/json"
            )
