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
label main_menu:
    call screen main_menu
    return

init python:
    import datetime
    import random

    # Función que devuelve el texto distorsionado de login. Cambia de 1998 a Hoy.
    def get_glitch_login_text(st, at):
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # 5% de probabilidad de mostrar basura / frame corrupto rápido
        if random.random() < 0.05:
            glitch_chars = "".join(random.choice("!@#$%^&*()_+|~-=\\`:\";'<>?,./") for _ in range(25))
            text = Text(glitch_chars, color="#ffffff", font="fonts/vt323.ttf", size=32)
            return text, random.uniform(0.05, 0.15)
            
        # 8% de probabilidad de mostrar la fecha actual y mantenerla por más tiempo
        elif random.random() < 0.08:
            text = Text("LAST LOGIN: " + current_time, color="#ff4444", font="fonts/vt323.ttf", size=32)
            # Se queda en pantalla entre 0.8 y 2.0 segundos
            return text, random.uniform(0.8, 2.0)
            
        else:
            text = Text("LAST LOGIN: 14/08/1998 02:17:00", color="#00e5ff", font="fonts/vt323.ttf", size=32)
            return text, 0.1

image dynamic_login_text = DynamicDisplayable(get_glitch_login_text)

# LA SALA DEL SERVIDOR: COMPOSICIÓN DINÁMICA DE BACKGROUND MÁS BRANDING
image bg sala_terminal:
    # 1. Creamos un espacio mayor para hacer panning (1920 -> 2100)
    contains:
        Transform("images/bg/sala_terminal.png", size=(2100, 1180))
        # Efecto de respiración LENTO (movimiento sutil de cámara)
        xpos -100 ypos -50
        linear 10.0 xpos 0 ypos 0
        linear 10.0 xpos -100 ypos -50
        repeat



    # 3. El texto críptico flotando en la escena como si fuera de un monitor
    contains:
        "dynamic_login_text"
        xpos 80 ypos 80
        # Efecto de viñeta fosforescente
        blur 1.0


default persistent.beta_unlocked = False

## ─────────────────────────────────────────────
## LAUNCHER BETA ANTI-PIRATEO (SPLASHSCREEN)
## ─────────────────────────────────────────────
label splashscreen:
    if persistent.beta_unlocked:
        return

    scene black
    show screen crt_overlay
    
    show text Text(">>> INICIANDO PROTOCOLO DE CONEXIÓN BETA <<<", color="#00ffff", font="fonts/vt323.ttf", size=40) at truecenter
    pause 2.0
    hide text
    
    $ attempts = 0
    
    label beta_login_loop:
        $ beta_code = renpy.input("INGRESE CÓDIGO DE ACCESO BETA (Único Uso):", length=20).strip().upper()
        
        # En una beta real offline, la única forma de "un solo uso" es validarlo con un ID, 
        # pero como no tenemos backend, validamos una master list o master key:
        if beta_code == "NULL2026" or beta_code == "TESTER-ZERO":
            $ persistent.beta_unlocked = True
            show text Text("ACCESO CONCEDIDO. BIENVENIDO/A.", color="#00ff00", font="fonts/vt323.ttf", size=40) at truecenter
            pause 2.0
            hide text
            return
        else:
            $ attempts += 1
            if attempts >= 3:
                show text Text("ACCESO DENEGADO.\nINTENTO DE DISTRIBUCIÓN ILEGAL DETECTADO.", color="#ff0000", font="fonts/vt323.ttf", size=40) at truecenter, glitch_anim
                pause 2.5
                hide text
                
                # Efecto glitch asustadizo infinito
                with flash
                show text Text("¿PENSABAS QUE PODÍAS ENGAÑAR A INFINIT-0?", color="#cc0000", font="fonts/vt323.ttf", size=80) at truecenter, glitch_anim
                pause 2.0
                show text Text("TU TERMINAL AHORA ME PERTENECE.", color="#ff4444", font="fonts/vt323.ttf", size=60) at truecenter
                pause 2.0
                
                $ renpy.quit()
            else:
                show text Text("CÓDIGO INVÁLIDO O YA UTILIZADO.", color="#ff0000", font="fonts/vt323.ttf", size=40) at truecenter
                pause 1.0
                hide text
                jump beta_login_loop

label start:
    $ _game_menu_screen = "preferences"
    $ veces_jugadas += 1
    call infinit_boot_sequence
    jump prologo

## ─────────────────────────────────────────────
## PRÓLOGO (≈15 minutos lectura)
## ─────────────────────────────────────────────
label prologo:
    scene bg exterior_infinit with dissolve
    show screen crt_overlay
    # play music "audio/ambient_exterior.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    narrador "Las 2:17 de la mañana. Suburbios de Buenos Aires."
    narrador "El edificio INFINIT lleva décadas abandonado. Nadie entra. Nadie sale."
    narrador "Dante Rivas entró hace tres días. Era tu mejor amigo. Él nunca haría algo así sin avisarte."
    pause 0.3
    narrador "Y sin embargo, acá estás."

    with dissolve
    scene bg entrada_infinit with dissolve

    narrador "La puerta principal cedió sin resistencia, como si te estuviera esperando."
    narrador "Apenas pusiste un pie adentro..."

    # play sound "audio/door_slam.ogg"  # (Audio file is 0 bytes)
    with hpunch
    
    scene bg entrada_infinit_cerrada with dissolve

    narrador "...la puerta se cerró de golpe detrás de vos."
    alex "¿Dante? ¿Estás ahí?"
    alex "Dante, si esto es una broma, te juro que te mato yo antes que este lugar."

    pause 0.8
    narrador "Silencio. Sólo el crujir del edificio. El olor a humedad. A oxido. A algo que no sabés nombrar."
    pause 0.5

    ## Terminal enciende
    # play sound "audio/static_burst.ogg"  # (Audio file is 0 bytes)
    with flash

    scene bg sala_terminal with dissolve
    narrador "En el extremo del pasillo, una pantalla parpadea."

    call terminal_prologue_choice

    ## Elección SI / NO
    menu terminal_si_no:
        "[[ SÍ ]":
            jump prologo_acepta_terminal
        "[[ NO ]":
            jump prologo_rechaza_terminal

## ─────────────────────────────────────────
## PRÓLOGO: eligió NO
## ─────────────────────────────────────────
label prologo_rechaza_terminal:
    narrador "Retrocedés. No vas a seguirle el juego a una pantalla."

    # play sound "audio/typing_fast.ogg"  # (Audio file is 0 bytes)
    show text Text("> Sabía que ibas a decir eso.", color="#00ffff", font="fonts/vt323.ttf", size=30)
    pause 1.2
    hide text

    show text Text("> Igual vamos a jugar.", color="#cc0000", font="fonts/vt323.ttf", size=32) at glitch_anim
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
    scene bg sala_terminal with dissolve
    show screen crt_overlay
    # play music "audio/ambient_horror.ogg" loop volume 0.6  # (Audio file is 0 bytes)

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

    show text Text("NULL>ZONE", color="#00ffff", font="fonts/vt323.ttf", size=140, outlines=[(6, "#003333", 3, 3)]) at glitch_anim
    pause 2.5
    hide text

    show text Text("Tu decisión importa. O tal vez no.", color="#336666", font="fonts/vt323.ttf", size=36) at fade_in_slow
    pause 2.0
    hide text

    with dissolve

    ## Volver al edificio
    scene bg pasillo_largo with dissolve
    # play music "audio/ambient_horror.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    infinit "La primera elección ya la tomaste: estás acá."
    infinit "Ahora... ¿qué hacés con la terminal que tenés enfrente?"

    ## ─────────────────────────────────────
    ## DECISIÓN P-1 (con timer de 30 seg)
    ## ─────────────────────────────────────
    narrador "La terminal sigue encendida. Muestra un prompt parpadeante."
    narrador "Podés interactuar con ella o ignorarla e intentar buscar la salida."

    # Llama a la pantalla de timer, se le pasa el tiempo y a dónde saltar si se acaba
    show screen timer_warning(time_limit=30, timeout_label="prologo_timeout")

    ## La decisión
    menu decision_p1:
        "[[ INTERACTUAR con la terminal ]":
            hide screen timer_warning
            $ camino_rebelde = False
            jump capitulo1a_inicio

        "[[ IGNORAR la terminal y buscar la salida ]":
            hide screen timer_warning
            $ camino_rebelde = True
            jump capitulo1b_inicio

## ─────────────────────────────────────────
## PRÓLOGO: Timeout (INFINIT-0 elige)
## ─────────────────────────────────────────
label prologo_timeout:
    hide screen timer_warning
    call infinit_chooses
    ## Por defecto, si no elige: INFINIT-0 elige el peor camino
    $ camino_rebelde = True
    $ herido = True
    jump capitulo1b_inicio
