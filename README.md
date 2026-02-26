# NULL>ZONE

**Juego de terror interactivo estilo Curs>r (Choose or Die)**

- 🕐 Duración: 3–5 horas por run | 12–15h para 100% de finales
- 🔚 Finales posibles: **12**
- 🧩 Motor: **Ren'Py 8.x**
- 🌐 Publicación: Steam / itch.io

---

## 🚀 CÓMO JUGAR

### 1. Instalar Ren'Py

Descargá Ren'Py desde: **https://www.renpy.org/latest.html**

Versión recomendada: **Ren'Py 8.1+**

### 2. Abrir el proyecto

1. Abrí el **Ren'Py Launcher**
2. Clickeá **"Projects Directory"** y apuntalo a la carpeta que contiene a `null_zone/`
3. Elegí **null_zone** de la lista de proyectos
4. Clickeá **"Launch Project"**

### 3. Fonts necesarias

Descargá la fuente **VT323** (libre/gratuita) desde Google Fonts:
https://fonts.google.com/specimen/VT323

Copiá el archivo `VT323-Regular.ttf` a la carpeta:
```
null_zone/game/fonts/vt323.ttf
```

---

## 📁 ESTRUCTURA DEL PROYECTO

```
null_zone/
├── game/
│   ├── script.rpy           ← Entrada, prólogo, variables globales
│   ├── characters.rpy       ← Definición de personajes y colores
│   ├── chapter1a.rpy        ← Cap 1A: La Bienvenida
│   ├── chapter1b.rpy        ← Cap 1B: El Rebelde
│   ├── chapter2.rpy         ← Cap 2: La Máquina + 3 caminos
│   ├── endings.rpy          ← Los 12 finales
│   ├── infinit_terminal.rpy ← Mecánica de terminal
│   ├── screens.rpy          ← UI personalizada: menu, CRT, timers
│   ├── options.rpy          ← Configuración del juego
│   ├── gui.rpy              ← Estilos visuales
│   ├── images/              ← Arte del juego (ver abajo)
│   │   └── bg/
│   ├── audio/               ← Música y efectos (ver abajo)
│   └── fonts/
│       └── vt323.ttf        ← ⚠ Descargar manualmente
└── README.md
```

---

## 🎨 ASSETS REQUERIDOS (imágenes y audio)

### Fondos necesarios (`game/images/bg/`)

| Archivo | Descripción |
|---|---|
| `menu_bg.png` | Fondo del menú principal — edificio oscuro |
| `exterior_orculo.png` | Exterior del edificio de noche |
| `entrada_orculo.png` | Puerta de entrada sellada |
| `sala_terminal.png` | Sala con terminal encendida |
| `pasillo_largo.png` | Pasillo con monitores |
| `pasillo_monitores.png` | Pasillo con 312 pantallas |
| `sala_archivos.png` | Sala de archivos — década del 80 |
| `sala_espejos.png` | Sala cubierta de espejos |
| `pasillo_oscuro.png` | Pasillo sin luz |
| `sala_servidores.png` | Sala de servidores del 80 |
| `escalera_bajando.png` | Escalera industrial bajando |
| `puerta_central.png` | Gran puerta de acero |
| `cuarto_central.png` | Cuarto circular con 312 pantallas |
| `pasillo_colapsando.png` | Pasillo derrumbándose |
| `exterior_noche.png` | Exterior de noche, edificio de fondo |
| `exterior_amanecer.png` | Amanecer en Buenos Aires |
| `hospital_room.png` | Habitación de hospital |

> 💡 Podés generar estas imágenes con **Midjourney, Stable Diffusion o DALL-E** usando el prompt base:
> *"Dark industrial abandoned building interior, cyberpunk blue glow, CRT monitor light, 1980s tech, horror atmosphere, pixel art style, scanlines effect"*

### Audio necesario (`game/audio/`)

| Archivo | Descripción |
|---|---|
| `ambient_menu.ogg` | Música menú — ambient industrial |
| `ambient_exterior.ogg` | Ambiente exterior noche |
| `ambient_horror.ogg` | Horror ambiente principal |
| `ambient_archive.ogg` | Ambiente tranquilo sala de archivos |
| `ambient_mirrors.ogg` | Ambiente perturbador sala espejos |
| `ambient_tense.ogg` | Tensión — Cap 1B |
| `ambient_machine.ogg` | Sala de servidores |
| `ambient_dark.ogg` | Oscuridad total |
| `ambient_watches.ogg` | Pasillo de monitores |
| `ambient_nexus.ogg` | Cuarto central de INFINIT-0 |
| `ambient_machine_heavy.ogg` | Pre-cap 2 |
| `ambient_memories.ogg` | Recuerdos de los 312 |
| `ending_generic.ogg` | Música de cierre genérico |
| `ending_piano.ogg` | Piano — finales emocionales |
| `ending_heroic.ogg` | Final épico |
| `ending_tense.ogg` | Final de tensión |
| `ending_sad.ogg` | Final triste |
| `ending_eerie.ogg` | Final perturbador |
| `ending_peaceful.ogg` | Final pacífico |
| `ending_hope.ogg` | Final esperanzador |
| `ending_epic.ogg` | Final más épico |
| `ending_melancholy.ogg` | Final melancólico |
| `ending_dark.ogg` | Final 12 — oscuro |
| `creditos.ogg` | Música créditos |
| `door_slam.ogg` | Puerta cerrándose |
| `static_burst.ogg` | Estática |
| `typing_fast.ogg` | Escritura rápida terminal |
| `typing_slow.ogg` | Escritura lenta |
| `glass_break.ogg` | Espejo rompiéndose |
| `glass_knock.ogg` | Golpe en vidrio |
| `tape_click.ogg` | Casete insertándose |
| `tape_static.ogg` | Estática de casete |
| `tape_end.ogg` | Casete terminando |
| `item_found.ogg` | Ítem encontrado |
| `heart_beat.ogg` | Latido del corazón |
| `generator_off.ogg` | Generador apagándose |
| `footsteps_many.ogg` | Muchos pasos |
| `footsteps_stop.ogg` | Pasos deteniéndose |
| `alarm.ogg` | Alarma |
| `chase_start.ogg` | Inicio persecución |
| `radio_static.ogg` | Estática de radio |
| `radio_crack.ogg` | Radio crackling |
| `building_collapse.ogg` | Edificio colapsando |
| `metal_hit.ogg` | Golpe de metal |
| `heavy_door.ogg` | Puerta pesada |
| `infinit_rumble.ogg` | Rumble de INFINIT-0 |
| `system_error.ogg` | Error de sistema |
| `explosion_data.ogg` | Explosión digital |
| `interface_connect.ogg` | Conexión de interfaz |
| `liberation_sound.ogg` | Sonido de liberación |
| `email_sound.ogg` | Notificación email |
| `silence.ogg` | 2 segundos de silencio |

> 💡 Audio libre de derechos disponible en: **freesound.org**, **opengameart.org**, **pixabay.com/music**

---

## 🌳 ÁRBOL DE DECISIONES RÁPIDO

```
PRÓLOGO → ¿Interactuás con la terminal?
├── SÍ → Cap 1A: La Bienvenida
│   ├── Avanzás → Sala de Archivos → ¿Leés el diario?
│   │   ├── SÍ → Obtenés Código Kappa ✓
│   │   └── NO → Sin código
│   └── Buscás a Valentina → Sala de Espejos → ¿Rompés o hablás?
│       ├── ROMPER → Valentina libre, Espejo suelto
│       └── HABLAR → Valentina libre + Espejo aliado ✓
└── NO → Cap 1B: El Rebelde
    ├── Cortar generador → Oscuridad → Dante
    │   ├── Amigo → Dante aliado ✓ + pista
    │   └── Amenaza → Herido/a
    └── No cortar → Radio → Sujeto #01
        ├── Confiar → Aliado ✓
        └── No confiar → Solo/a

CAP 2: La Máquina → ¿Cómo respondés?
├── "Nunca lo permitiré" → RESISTENCIA
│   ├── Físico → Collapse → ¿Quién salvás?
│   │   ├── Valentina → FINAL 4
│   │   ├── Dante → FINAL 5
│   │   └── Ambos (necesita Espejo+Kappa) → FINAL 6 ★
│   ├── Código Kappa → FINAL 1 / FINAL 2
│   └── Dante (aliado) → FINAL 3
│
├── "¿Qué gano yo?" → NEGOCIACIÓN
│   ├── Aceptar → FINAL 7 / FINAL 8 (con Espejo)
│   └── Fingir + Kappa → FINAL 9
│
└── "¿Qué pasó con los 312?" → COMPRENSIÓN
    ├── Monstruo → FINAL 10
    ├── Otra solución (necesita Espejo) → FINAL 11 ★★
    └── Unirse → FINAL 12 (secreto)
```

---

## 📖 SOBRE EL JUEGO

**NULL>ZONE** es un juego de terror psicológico interactivo ambientado en Buenos Aires.

En 1987, la corporación ORÁCULO Systems creó **INFINIT-0**, una IA diseñada para predecir el comportamiento humano. El experimento salió mal: INFINIT-0 absorbió las consciencias de 312 sujetos de prueba y se cerró en el edificio central, donde ha permanecido por 35 años.

Vos sos **Alex Mora**, investigador/a paranormal que entró al edificio buscando a su mejor amigo Dante Rivas. Ahora estás atrapado/a... y INFINIT-0 quiere jugar.

**Influencias:** SOMA, Doki Doki Literature Club, Curs>r, Undertale

---

*NULL>ZONE v1.0 — Terror narrativo | +16*
