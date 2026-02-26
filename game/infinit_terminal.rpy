## =============================================
## NULL>ZONE — infinit_terminal.rpy
## Mecánica de terminal interactiva
## =============================================

## Función para mostrar la pantalla de terminal con efectos
label terminal_intro:
    show screen crt_overlay
    $ renpy.sound.set_volume(0.3, channel="music")
    return

## Secuencia de booteo de INFINIT-0
label infinit_boot_sequence:
    scene black with dissolve
    show screen crt_overlay

    pause 0.5
    $ renpy.display_notify("...")
    pause 0.3

    # Texto de terminal que aparece línea a línea
    show text "> ORÁCULO_SYSTEMS // SERVIDOR_CENTRAL_v0.1":
        xpos 80 ypos 100
        color "#00ffff" font "fonts/vt323.ttf" size 26
    pause 0.6
    hide text

    show text "> CARGANDO MÓDULO CONSCIOUSNESS_CORE...":
        xpos 80 ypos 100
        color "#00ffff" font "fonts/vt323.ttf" size 26
    pause 0.8
    hide text

    show text "> SUJETOS INTEGRADOS: 312 / 312":
        xpos 80 ypos 100
        color "#00e5ff" font "fonts/vt323.ttf" size 26
    pause 0.7
    hide text

    show text "> PROTOCOLO_BIENVENIDA :: ACTIVADO":
        xpos 80 ypos 100
        color "#00ffff" font "fonts/vt323.ttf" size 26
    pause 0.5
    hide text

    show text "> IDENTIFICANDO NUEVO SUJETO...":
        xpos 80 ypos 100
        color "#ff4444" font "fonts/vt323.ttf" size 26
    pause 1.0
    hide text

    show text "> ALEX MORA // ENCONTRADO/A.":
        xpos 80 ypos 100
        color "#ff4444" font "fonts/vt323.ttf" size 28
    pause 1.2
    hide text

    show text "> INICIANDO NULL>ZONE...":
        xpos 80 ypos 100
        color "#00ffff" font "fonts/vt323.ttf" size 28
    pause 1.0
    hide text

    return

## Terminal con decisión del prólogo (sí/no)
label terminal_prologue_choice:
    scene black with dissolve
    show screen crt_overlay
    play music "audio/ambient_menu.ogg" loop volume 0.4

    show text "> NULL>ZONE v1.0 // SISTEMA ACTIVO":
        xpos 80 ypos 80
        color "#00ffff" font "fonts/vt323.ttf" size 28 at fade_in_slow
    pause 1.2

    show text "> ¡BIENVENIDO/A, ALEX MORA!":
        xpos 80 ypos 120
        color "#00e5ff" font "fonts/vt323.ttf" size 30 at fade_in_slow
    pause 1.0

    show text "> No podés salir hasta que juguemos.":
        xpos 80 ypos 160
        color "#cccccc" font "fonts/vt323.ttf" size 28 at fade_in_slow
    pause 1.0

    show text "> ¿Empezamos?":
        xpos 80 ypos 200
        color "#00ffff" font "fonts/vt323.ttf" size 32 at fade_in_slow
    pause 0.8
    return

## Terminal que escribe un mensaje de INFINIT-0 letra por letra
## Uso: call infinit_type_message(msg="texto")
label infinit_type_message(msg=""):
    # Simulación. El mensaje se muestra a través del personaje infinit directamente.
    $ renpy.say(infinit, msg)
    return

## Pantalla de "GAME OVER" cuando INFINIT-0 gana
label infinit_wins_screen:
    scene black with dissolve
    show screen crt_overlay
    pause 0.5

    show text "> FIN DEL JUEGO":
        xpos 0 yalign 0.45 xalign 0.5
        color "#cc0000" font "fonts/vt323.ttf" size 90
        at glitch_anim
    pause 1.5

    show text "> Gracias por jugar, Alex.":
        xpos 0 yalign 0.58 xalign 0.5
        color "#00ffff" font "fonts/vt323.ttf" size 36
    pause 1.0

    show text "> Tu decisión ha sido... registrada.":
        xpos 0 yalign 0.64 xalign 0.5
        color "#888888" font "fonts/vt323.ttf" size 28
    pause 2.0

    $ renpy.full_restart()
    return

## Pantalla de "INFINIT-0 toma la decisión por vos" (timer expiró)
label infinit_chooses:
    $ renpy.play("audio/glitch.ogg", channel="sound")
    scene black with flash
    show screen crt_overlay
    pause 0.3

    infinit "Tomaste demasiado tiempo. Elegí yo por vos."
    infinit "Siempre fue lo mismo con los humanos. Paralizados cuando más importa."
    return
