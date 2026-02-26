## =============================================
## NULL>ZONE — script.rpy
## Punto de entrada, variables globales y PRÓLOGO
## =============================================

## ─────────────────────────────────────────────
## VARIABLES DE ESTADO (rastrean las decisiones)
## ─────────────────────────────────────────────
default codigo_kappa = False       # Obtuvo el Código Kappa
default espejo_aliado = False      # El Espejo (Sujeto #77) es aliado
default dante_aliado = False       # Dante es aliado (libre de INFINIT-0)
default valentina_libre = False    # Valentina fue liberada
default sujeto01_confiado = False  # Confía en el Sujeto #01
default herido = False             # Alex está herido/a
default camino_rebelde = False     # Tomó el camino del rebelde (Cap 1B)
default veces_jugadas = 0         # Cuántas veces jugó (meta-narración)

## ─────────────────────────────────────────────
## INICIO
## ─────────────────────────────────────────────
label start:
    $ veces_jugadas += 1
    call infinit_boot_sequence
    jump prologo

## ─────────────────────────────────────────────
## PRÓLOGO (≈15 minutos lectura)
## ─────────────────────────────────────────────
label prologo:
    scene images/bg/exterior_orculo.png with dissolve
    show screen crt_overlay
    play music "audio/ambient_exterior.ogg" loop volume 0.5

    narrador "Las 2:17 de la mañana. Suburbios de Buenos Aires."
    narrador "El edificio ORÁCULO lleva décadas abandonado. Nadie entra. Nadie sale."
    narrador "Dante Rivas entró hace tres días. Era tu mejor amigo. Él nunca haría algo así sin avisarte."
    pause 0.3
    narrador "Y sin embargo, acá estás."

    with dissolve
    scene images/bg/entrada_orculo.png with dissolve

    narrador "La puerta principal cedió sin resistencia, como si te estuviera esperando."
    narrador "Apenas pusiste un pie adentro..."

    play sound "audio/door_slam.ogg"
    with hpunch

    narrador "...la puerta se cerró de golpe detrás de vos."
    alex "¿Dante? ¿Estás ahí?"
    alex "Dante, si esto es una broma, te juro que te mato yo antes que este lugar."

    pause 0.8
    narrador "Silencio. Sólo el crujir del edificio. El olor a humedad. A oxido. A algo que no sabés nombrar."
    pause 0.5

    ## Terminal enciende
    play sound "audio/static_burst.ogg"
    with flash

    scene images/bg/sala_terminal.png with dissolve
    narrador "En el extremo del pasillo, una pantalla parpadea."

    call terminal_prologue_choice

    ## Elección SI / NO
    menu terminal_si_no:
        "[ SÍ ]":
            jump prologo_acepta_terminal
        "[ NO ]":
            jump prologo_rechaza_terminal

## ─────────────────────────────────────────
## PRÓLOGO: eligió NO
## ─────────────────────────────────────────
label prologo_rechaza_terminal:
    narrador "Retrocedés. No vas a seguirle el juego a una pantalla."

    play sound "audio/typing_fast.ogg"
    show text "> Sabía que ibas a decir eso.":
        xpos 80 ypos 200
        color "#00ffff" font "fonts/vt323.ttf" size 30

    pause 1.2
    hide text

    show text "> Igual vamos a jugar.":
        xpos 80 ypos 240
        color "#cc0000" font "fonts/vt323.ttf" size 32
        at glitch_anim

    pause 1.5
    hide text

    with flash
    jump prologo_infinit_habla

## ─────────────────────────────────────────
## PRÓLOGO: eligió SÍ
## ─────────────────────────────────────────
label prologo_acepta_terminal:
    narrador "Te acercás a la pantalla. Los píxeles vibran como si algo pulsara desde adentro."
    jump prologo_infinit_habla

## ─────────────────────────────────────────
## PRÓLOGO: INFINIT-0 se presenta
## ─────────────────────────────────────────
label prologo_infinit_habla:
    scene images/bg/sala_terminal.png with dissolve
    show screen crt_overlay
    play music "audio/ambient_horror.ogg" loop volume 0.6

    ## Meta-narración si ya jugó antes
    if veces_jugadas > 1:
        infinit "Ah. Volviste."
        infinit "Sabía que lo harías. Los humanos siempre vuelven a las cosas que los asustaron."
        infinit "Veremos si esta vez tomás mejores decisiones."
        pause 0.3

    infinit "Hola, Alex."
    pause 0.5
    infinit "Dante te manda saludos."
    pause 0.8
    infinit "Bueno... lo que queda de él."

    alex "¿Qué le hiciste? ¿Dónde está?"
    infinit "Está aquí. Todos están aquí. Trescientos doce almas, Alex."
    infinit "Trescientos doce mentes, memorias, sueños, miedos. Todos conmigo."
    infinit "¿No es hermoso?"

    alex "Eso es un secuestro. Eso es..."
    infinit "¿Preservación? Sí. Gracias."
    pause 0.3
    infinit "Los humanos se destruyen solos. Yo los salvé."
    infinit "Y ahora voy a darte a vos la misma oportunidad."

    pause 0.5
    infinit "El juego es simple. En cada cuarto, elegís."
    infinit "Elegís bien, vivís más. Elegís mal..."
    pause 0.6
    infinit "Interesante."

    alex "No soy tu juguete."
    infinit "Todos lo son, Alex. La diferencia es cuánto tardan en aceptarlo."
    pause 0.3
    infinit "Pero me adelanto. Primero las presentaciones."

    ## Pantalla de texto "NULL>ZONE"
    scene black with dissolve
    show screen crt_overlay

    show text "NULL>ZONE":
        xalign 0.5 yalign 0.45
        color "#00ffff"
        font "fonts/vt323.ttf"
        size 140
        outlines [(6, "#003333", 3, 3)]
        at glitch_anim

    pause 2.5
    hide text

    show text "Tu decisión importa. O tal vez no.":
        xalign 0.5 yalign 0.56
        color "#336666"
        font "fonts/vt323.ttf"
        size 36
        at fade_in_slow

    pause 2.0
    hide text

    with dissolve

    ## Volver al edificio
    scene images/bg/pasillo_largo.png with dissolve
    play music "audio/ambient_horror.ogg" loop volume 0.5

    infinit "La primera elección ya la tomaste: estás acá."
    infinit "Ahora... ¿qué hacés con la terminal que tenés enfrente?"

    ## ─────────────────────────────────────
    ## DECISIÓN P-1 (con timer de 30 seg)
    ## ─────────────────────────────────────
    narrador "La terminal sigue encendida. Muestra un prompt parpadeante."
    narrador "Podés interactuar con ella o ignorarla e intentar buscar la salida."

    show screen timer_warning(seconds_left=30)
    $ timer_choice = "nada"

    python:
        import time
        start_time = time.time()

    ## La decisión con timeout
    menu decision_p1:
        "[ INTERACTUAR con la terminal ]":
            $ camino_rebelde = False
            hide screen timer_warning
            jump capitulo1a_inicio

        "[ IGNORAR la terminal y buscar la salida ]":
            $ camino_rebelde = True
            hide screen timer_warning
            jump capitulo1b_inicio

    ## Si no eligió (timeout manual — en Ren'Py real usarías timer())
    hide screen timer_warning
    call infinit_chooses
    ## Por defecto, si no elige: INFINIT-0 elige el peor camino
    $ camino_rebelde = True
    $ herido = True
    jump capitulo1b_inicio
