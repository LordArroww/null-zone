## =============================================
## NULL>ZONE — characters.rpy
## Definición de personajes
## =============================================

# Colores del juego
# Negro: #0a0a0a
# Azul eléctrico: #00ffff
# Rojo sangre: #cc0000
# Blanco sucio: #e0e0e0
# Gris apagado: #7a7a7a

# --- ALEX MORA (Jugador) ---
define alex = Character(
    "ALEX",
    color="#e0e0e0",
    who_bold=True,
    what_color="#e0e0e0",
    who_outlines=[(2, "#000000", 0, 0)],
    what_italic=False,
)

# --- INFINIT-0 (IA / Antagonista) ---
# Tipografía monospace, azul eléctrico
define infinit = Character(
    "INFINIT-0",
    color="#00ffff",
    who_bold=True,
    what_color="#00e5ff",
    who_outlines=[(2, "#000000", 0, 0)],
    what_italic=True,
    what_suffix=" _",
)

# --- DANTE RIVAS ---
define dante = Character(
    "DANTE",
    color="#ff9800",
    who_bold=True,
    what_color="#ffcc80",
    who_outlines=[(2, "#000000", 0, 0)],
)

# --- DANTE poseído por INFINIT-0 ---
define dante_inf = Character(
    "DANTE / INFINIT-0",
    color="#00ffff",
    who_bold=True,
    what_color="#b2ebf2",
    what_italic=True,
)

# --- VALENTINA MORA ---
define valentina = Character(
    "VALENTINA",
    color="#f06292",
    who_bold=True,
    what_color="#f8bbd0",
    who_outlines=[(2, "#000000", 0, 0)],
)

# --- EL ESPEJO (Sujeto #77) ---
define espejo = Character(
    "[ ESPEJO ]",
    color="#b0bec5",
    who_bold=True,
    what_color="#cfd8dc",
    what_italic=True,
    who_outlines=[(2, "#000000", 0, 0)],
)

# --- SUJETO #01 (Voz por radio) ---
define sujeto01 = Character(
    "VOZ EN LA RADIO :: Sujeto #01",
    color="#a5d6a7",
    who_bold=True,
    what_color="#c8e6c9",
    what_italic=True,
)

# --- DRA. CAMILA VOSS (grabaciones, diario) ---
define voss = Character(
    "Dra. CAMILA VOSS — [grabación 1987]",
    color="#ffe082",
    who_bold=True,
    what_color="#fff9c4",
    what_italic=True,
)

# --- Sistema: texto de terminal / narrador ---
define terminal = Character(
    None,
    color="#00ffff",
    what_color="#00ffff",
    what_prefix="> ",
    what_suffix="",
    what_font="fonts/vt323.ttf",
    what_size=28,
)

define narrador = Character(
    None,
    color="#7a7a7a",
    what_color="#b0b0b0",
    what_italic=True,
)
