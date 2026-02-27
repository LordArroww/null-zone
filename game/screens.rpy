## =============================================
## NULL>ZONE — screens.rpy
## Pantallas personalizadas: menú, terminal CRT, etc.
## =============================================

## ─────────────────────────────────────────────
## EFECTO CRT / SCANLINES (overlay global)
## ─────────────────────────────────────────────
screen crt_overlay():
    zorder 100
    add "#000000" alpha 0.08
    # Scanlines — overlay oscuro sutil
    add Solid("#000000") alpha 0.06

## ─────────────────────────────────────────────
## PANTALLA DE TERMINAL INTERACTIVA
## ─────────────────────────────────────────────
screen terminal_screen(prompt="", history=[]):
    modal True
    zorder 200

    add "#0a0a0a"

    frame:
        background "#0a0a0a"
        xfill True
        yfill True
        xpadding 80
        ypadding 60

        vbox:
            spacing 4
            # Historia de la terminal
            for line in history:
                text line:
                    color "#00ffff"
                    font "fonts/vt323.ttf"
                    size 28
                    outlines [(1, "#003333", 0, 0)]

            # Prompt actual + cursor parpadeante
            hbox:
                text "> " color "#00ffff" font "fonts/vt323.ttf" size 28
                text prompt color "#00e5ff" font "fonts/vt323.ttf" size 28
                text "_":
                    color "#00ffff"
                    font "fonts/vt323.ttf"
                    size 28
                    at blink_anim

## ─────────────────────────────────────────────
## TRANSICIONES PERSONALIZADAS
## ─────────────────────────────────────────────
define flash = Fade(0.1, 0.0, 0.1, color="#ffffff")

## ─────────────────────────────────────────────
## ANIMACIONES
## ─────────────────────────────────────────────
transform blink_anim:
    alpha 1.0
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat

transform glitch_anim:
    xoffset 0
    pause 0.1
    xoffset 5
    pause 0.05
    xoffset -5
    pause 0.05
    xoffset 0
    pause 2.0
    repeat

transform scanline_move:
    yoffset 0
    linear 8.0 yoffset 1080
    yoffset -100
    repeat

transform fade_in_slow:
    alpha 0.0
    linear 2.0 alpha 1.0

transform pulse_blue:
    alpha 0.4
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.4
    repeat

## ─────────────────────────────────────────────
## PANTALLA DEL MENÚ PRINCIPAL
## ─────────────────────────────────────────────
screen main_menu():
    tag menu
    style_prefix "main_menu"

    add "bg menu_bg"
    # CRT overlay
    add Solid("#0a0a0a") alpha 0.5

    # Título
    vbox:
        xalign 0.5
        yalign 0.3
        spacing 20

        text "NULL>ZONE":
            xalign 0.5
            color "#00ffff"
            font "fonts/vt323.ttf"
            size 120
            outlines [(4, "#003333", 2, 2)]
            at glitch_anim

        text "Un juego de INFINIT Systems":
            xalign 0.5
            color "#336666"
            font "fonts/vt323.ttf"
            size 32

    # Botones del menú
    vbox:
        xalign 0.5
        yalign 0.65
        spacing 18

        textbutton "[[ NUEVA PARTIDA ]":
            xalign 0.5
            action Start()
            style "main_menu_button"

        textbutton "[[ CONTINUAR ]":
            xalign 0.5
            action ShowMenu("load")
            style "main_menu_button"

        textbutton "[[ OPCIONES ]":
            xalign 0.5
            action ShowMenu("preferences")
            style "main_menu_button"

        textbutton "[[ SALIR ]":
            xalign 0.5
            action Quit(confirm=not main_menu)
            style "main_menu_button"

    # Versión
    text "v1.0 — itch.io / Steam":
        xalign 0.98
        yalign 0.98
        color "#003333"
        font "fonts/vt323.ttf"
        size 22

## ─────────────────────────────────────────────
## ESTILOS
## ─────────────────────────────────────────────
style main_menu_button:
    background Frame(Solid("#001111"), 0, 0)
    hover_background Frame(Solid("#002222"), 0, 0)
    xpadding 40
    ypadding 14

style main_menu_button_text:
    color "#00ffff"
    hover_color "#ffffff"
    font "fonts/vt323.ttf"
    size 38
    outlines [(2, "#003333", 1, 1)]

## ─────────────────────────────────────────────
## PANTALLA DE PAUSA DE TIEMPO LIMITADO
## ─────────────────────────────────────────────
screen timer_warning(time_limit=30, timeout_label=None):
    zorder 150
    default seconds_left = time_limit

    # El temporizador real
    timer 1.0 action If(seconds_left > 0, true=SetScreenVariable("seconds_left", seconds_left - 1), false=Return("timeout_ocurrido")) repeat True

    frame:
        background Solid("#cc000044")
        xalign 0.5
        yalign 0.0
        ypos 10
        xpadding 40
        ypadding 10
        hbox:
            spacing 12
            text "⚠ INFINIT-0 ELIGE EN:":
                color "#ff4444"
                font "fonts/vt323.ttf"
                size 28
            text "[seconds_left]s":
                color "#ffffff"
                font "fonts/vt323.ttf"
                size 28

## ─────────────────────────────────────────────
## NOTIFICACIÓN DE ÍTEM OBTENIDO
## ─────────────────────────────────────────────
screen item_obtained(name, desc):
    zorder 160
    frame:
        background Solid("#001a1a")
        xalign 1.0
        yalign 0.0
        xpos -20
        ypos 80
        xpadding 30
        ypadding 20
        vbox:
            spacing 6
            text ">> ARCHIVADO <<":
                color "#00ffff"
                font "fonts/vt323.ttf"
                size 22
            text "[name]":
                color "#ffffff"
                font "fonts/vt323.ttf"
                size 26
            text "[desc]":
                color "#888888"
                font "fonts/vt323.ttf"
                size 20

## ─────────────────────────────────────────────
## HUD — VARIABLES ACTIVAS (para debug, opcional)
## ─────────────────────────────────────────────
# screen debug_hud():
#     zorder 300
#     vbox:
#         xpos 10
#         ypos 10
#         text "codigo_kappa: [codigo_kappa]" color "#ffffff" size 20
#         text "espejo_aliado: [espejo_aliado]" color "#ffffff" size 20
#         text "dante_aliado: [dante_aliado]" color "#ffffff" size 20
#         text "valentina_libre: [valentina_libre]" color "#ffffff" size 20
#         text "herido: [herido]" color "#ffffff" size 20
