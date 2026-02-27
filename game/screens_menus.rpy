## =============================================
## MENÚS INTERNOS COMPLETOS - NULL>ZONE
## =============================================

init python:
    # Traducciones nativas de los prompts de salir / volver al menú
    config.translations["Are you sure you want to quit?"] = "¿ESTÁS SEGURO QUE QUERÉS SALIR?"
    config.translations["Are you sure you want to return to the main menu?\nThis will lose unsaved progress."] = "¿VOLVER AL MENÚ PRINCIPAL?\n(SE PERDERÁ TODO EL PROGRESO)"

screen navigation():
    hbox:
        xalign 0.5
        yalign 0.95
        spacing 40

        textbutton "[[ VOLVER ]":
            action Return()
            text_font "fonts/vt323.ttf"
            text_size 35
            text_color "#00ffff"
            text_hover_color "#ffffff"
            xalign 0.5
            
        textbutton "[[ OPCIONES ]":
            action ShowMenu("preferences")
            text_font "fonts/vt323.ttf"
            text_size 35
            text_color "#00ffff"
            text_hover_color "#ffffff"
            xalign 0.5
            
        textbutton "[[ MENÚ PRINCIPAL ]":
            action MainMenu()
            text_font "fonts/vt323.ttf"
            text_size 35
            text_color "#00ffff"
            text_hover_color "#ffffff"
            xalign 0.5
            
        textbutton "[[ SALIR ]":
            action Quit(confirm=True)
            text_font "fonts/vt323.ttf"
            text_size 35
            text_color "#00ffff"
            text_hover_color "#ffffff"
            xalign 0.5

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    if not main_menu:
        # El velo negro se dibuja PRIMERO
        add Solid("#020202") alpha 0.90
    else:
        add "bg menu_bg"
    
    # Después dibujamos los componentes superpuestos interactivos
    use navigation
    
    # Este transclude inyecta el contenido de preferences o de quien llame a game_menu, SIEMPRE POR ENCIMA
    transclude

screen preferences():
    tag menu
    use game_menu(_("Opciones"))

    vbox:
        xalign 0.5
        ypos 100
        text "[[ MODO DE SISTEMA ]]" color "#00ffff" font "fonts/vt323.ttf" size 60

    hbox:
        xalign 0.5
        ypos 300
        spacing 150

        # Bloque de Volumen rediseñado para que no use las barras raras por defecto
        vbox:
            spacing 20
            text "VOLUMEN DE MÚSICA" color "#00e5ff" font "fonts/vt323.ttf" size 30 xalign 0.5
            hbox:
                xalign 0.5
                spacing 20
                textbutton "[-]" action Preference("music volume", 0.0) text_font "fonts/vt323.ttf" text_size 35 text_color "#00ffff"
                textbutton "[+]" action Preference("music volume", 1.0) text_font "fonts/vt323.ttf" text_size 35 text_color "#ff0044"

            null height 20
            
            text "VOLUMEN DE RUIDOS" color "#00e5ff" font "fonts/vt323.ttf" size 30 xalign 0.5
            hbox:
                xalign 0.5
                spacing 20
                textbutton "[-]" action Preference("sound volume", 0.0) text_font "fonts/vt323.ttf" text_size 35 text_color "#00ffff"
                textbutton "[+]" action Preference("sound volume", 1.0) text_font "fonts/vt323.ttf" text_size 35 text_color "#ff0044"

        vbox:
            spacing 20
            text "TAMAÑO DE PANTALLA" color "#00e5ff" font "fonts/vt323.ttf" size 30 xalign 0.5
            textbutton "[[ MAXIMIZAR ]":
                xalign 0.5
                action Preference("display", "fullscreen")
                text_font "fonts/vt323.ttf"
                text_size 35
                text_color "#00ffff"
                text_hover_color "#ffffff"
            textbutton "[[ VENTANA ]":
                xalign 0.5
                action Preference("display", "window")
                text_font "fonts/vt323.ttf"
                text_size 35
                text_color "#00ffff"
                text_hover_color "#ffffff"

screen save():
    tag menu
    use file_slots(_("Guardar Partida"))

screen load():
    tag menu
    use file_slots(_("Cargar Partida"))

screen file_slots(title):
    use game_menu(title)

    vbox:
        xalign 0.5
        ypos 100
        text title color "#00ffff" font "fonts/vt323.ttf" size 60

    grid 3 2:
        xalign 0.5
        yalign 0.45
        spacing 30
        
        for i in range(1, 7):
            button:
                action FileAction(i)
                xysize (320, 160)
                background Solid("#002222")
                hover_background Solid("#005555")
                
                vbox:
                    xalign 0.5 yalign 0.5 spacing 10
                    text "SLOT 0[i]" color "#00ffff" font "fonts/vt323.ttf" size 30
                    text FileTime(i, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Vacío")) color "#888888" size 20

screen yesno_prompt(message, yes_action, no_action):
    modal True
    zorder 200
    
    add Solid("#000000") alpha 0.9

    frame:
        background Solid("#001111")
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50

        vbox:
            xalign 0.5
            spacing 40

            text message color "#00ffff" font "fonts/vt323.ttf" size 40 text_align 0.5

            hbox:
                xalign 0.5
                spacing 80

                textbutton "[[ SÍ ]":
                    action yes_action
                    text_font "fonts/vt323.ttf"
                    text_size 40
                    text_color "#00ffff"
                    text_hover_color "#ffffff"
                textbutton "[[ NO ]":
                    action no_action
                    text_font "fonts/vt323.ttf"
                    text_size 40
                    text_color "#00ffff"
                    text_hover_color "#ffffff"

screen quick_menu():
    zorder 100
    if quick_menu:
        pass
        
    # Binding invisible para ESC y Click Derecho
    key "game_menu" action ShowMenu("preferences")
