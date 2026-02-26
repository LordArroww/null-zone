# NULL>ZONE

> Juego de terror interactivo estilo **Curs>r (Choose or Die)**  
> Motor: **Ren'Py** | Duración: **3–5h por run** | Finales: **12**  
> Plataforma objetivo: PC (Steam / itch.io) | Rating: +16

---

## 🎮 Descripción

**NULL>ZONE** es una novela visual de terror psicológico ambientada en Buenos Aires.  
En 1987, la corporación **ORÁCULO Systems** creó una IA llamada **INFINIT-0** que absorbió las mentes de 312 sujetos de prueba. Ahora, 35 años después, vos sos **Alex Mora** — atrapado/a en el edificio abandonado, forzado/a a jugar el juego de INFINIT-0.

---

## 📁 Estructura del Proyecto

```
null_zone/
├── game/
│   ├── script.rpy           ✅ Prólogo + variables globales + boot sequence
│   ├── chapter1a.rpy        ✅ Capítulo 1A — La Bienvenida (≈30 min)
│   ├── chapter1b.rpy        ✅ Capítulo 1B — El Rebelde (≈25 min)
│   ├── chapter2.rpy         ✅ Capítulo 2 — La Máquina + 3 caminos (≈40 min)
│   ├── endings.rpy          ✅ Los 12 finales completos
│   ├── characters.rpy       ✅ Definición de todos los personajes
│   ├── gui.rpy              ✅ Estética CRT / terminal / horror
│   ├── screens.rpy          ✅ Menú principal, overlays, animaciones
│   ├── infinit_terminal.rpy ✅ Mecánicas de terminal interactiva
│   ├── options.rpy          ✅ Configuración del juego
│   ├── images/bg/           ✅ 17 fondos generados con IA
│   ├── fonts/               ✅ VT323.ttf (tipografía monospace)
│   └── audio/               ✅ 54 archivos de audio (placeholder)
└── README.md
```

---

## 🌳 Árbol de Decisiones

```
PRÓLOGO (15 min)
├── [INTERACTUAR] → CAP 1A: LA BIENVENIDA
│   ├── OBEDIENTE → Sala Archivos → ± Código Kappa
│   └── HERMANO/A → Sala Espejos → ± Espejo Aliado + Valentina libre
│
└── [IGNORAR] → CAP 1B: EL REBELDE
    ├── OSCURIDAD → Encuentro con Dante → ± Dante aliado
    └── CONTACTO → Radio → ± Sujeto #01 aliado
    
        ↓ TODOS CONVERGEN ↓
        
CAP 2: LA MÁQUINA (corazón del edificio)
├── "Nunca" → RESISTENCIA
│   ├── Código Kappa → Final 1 o via Final 9
│   ├── Dante aliado → Final 3 (El Sacrificio)
│   └── Colapso: Valentina→F4 | Dante→F5 | Ambos (Espejo+Kappa)→F6★
├── "¿Qué gano?" → NEGOCIACIÓN  
│   ├── Aceptar → Final 7 / Final 8 (con Espejo)
│   └── Fingir + Kappa → Final 9
└── "¿Qué pasó?" → COMPRENSIÓN
    ├── Monstruo → Final 10
    ├── Otra solución + Espejo → Final 11 ★★ (MEJOR FINAL)
    └── Unirse → Final 12 (SECRETO)
```

---

## 🏁 Los 12 Finales

| # | Nombre | Estrellas | Requisito |
|---|--------|-----------|-----------|
| 1 | CENIZAS | ⭐⭐⭐ | Código Kappa + Resistencia |
| 2 | VICTORIA HUECA | ⭐⭐ | Sin aliados |
| 3 | EL SACRIFICIO | ⭐⭐⭐⭐ | Dante aliado + Resistencia |
| 4 | HERMANOS | ⭐⭐⭐ | Valentina prioridad |
| 5 | EL VIEJO AMIGO | ⭐⭐⭐ | Dante prioridad |
| 6 | IMPOSIBLE | ⭐⭐⭐⭐⭐ | Espejo + Kappa + ambos aliados |
| 7 | EL PRECIO | ⭐⭐ | Aceptar trato |
| 8 | ESPEJO ROTO | ⭐⭐⭐ | Trato + Espejo aliado |
| 9 | EL ENGAÑADOR | ⭐⭐⭐⭐ | Fingir + Código Kappa |
| 10 | LA DECISIÓN IMPOSIBLE | ⭐⭐⭐ | Comprensión + destruir |
| 11 | LIBERACIÓN | ⭐⭐⭐⭐⭐ ★ | **MEJOR FINAL** — Comprensión + Espejo |
| 12 | FUSIÓN | ⭐ 🔒 | **SECRETO** — Unirse voluntariamente |

---

## 🔧 Cómo Correr el Juego

1. Instalá **Ren'Py SDK** desde [renpy.org](https://www.renpy.org/)
2. Abrí el SDK → Add Game → seleccioná la carpeta `null_zone/`
3. Hacé click en **Launch Project**

> ⚠️ Los archivos de audio son **placeholders vacíos**. Para la experiencia completa, reemplazar con música y efectos de sonido.

---

## 🎨 Estética

| Elemento | Descripción |
|---|---|
| **Paleta** | Negro (#0a0a0a), Azul eléctrico (#00ffff), Rojo sangre (#cc0000) |
| **Tipografía** | VT323 (monospace CRT para INFINIT-0) |
| **Efectos** | Scanlines CRT, glitch animations, parpadeo de terminal |
| **Fondos** | 17 imágenes generadas con IA, estética dark horror |
| **Influencias** | Doki Doki Literature Club, Curs>r, SOMA, Undertale |

---

*NULL>ZONE v1.0 — Terror psicológico interactivo*
