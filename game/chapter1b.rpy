## =============================================
## NULL>ZONE — chapter1b.rpy
## CAPÍTULO 1B — EL REBELDE (≈25 minutos)
## =============================================

label capitulo1b_inicio:
    scene images/bg/pasillo_oscuro.png with dissolve
    show screen crt_overlay
    play music "audio/ambient_tense.ogg" loop volume 0.5

    narrador "CAPÍTULO 1 :: EL REBELDE"
    pause 0.5

    narrador "Le diste la espalda a la terminal. Bien por vos."
    narrador "O tal vez no tan bien. Depende."

    infinit "Interesante. Los que ignoran las reglas siempre son los más interesantes."
    infinit "Ningún problema. Observar también es parte del juego."

    narrador "Avanzás por el edificio buscando salidas. Cada puerta que probás: cerrada."
    narrador "Cada ventana: sellada. Como si el edificio mismo fuera parte de INFINIT-0."

    alex "Tiene que haber una salida. Tiene que haberla."
    narrador "Y entonces la encontrás."
    narrador "Una sala de servidores. Filas de racks con equipos de los años 80."
    narrador "Cables. Muchos cables. Y un generador masivo pulsando en el centro."

    scene images/bg/sala_servidores.png with dissolve
    play music "audio/ambient_machine.ogg" loop volume 0.5

    alex "Si corto la energía... todo el sistema cae."
    narrador "El generador tiene una palanca de corte manual. Gruesa. Oxidada. Pero funcional."
    narrador "Y si cortás la energía... también perdés la luz. Completamente."

    infinit "¿Estás pensando lo que creo que estás pensando?"
    infinit "Te advierto: el edificio tiene protocolos de emergencia."
    infinit "Protocolos... interesantes."

    ## ─────────────────────────────────────
    ## DECISIÓN 1B-1
    ## ─────────────────────────────────────
    show screen timer_warning(seconds_left=25)

    menu decision_1b1:
        "[ CORTAR el generador ]":
            hide screen timer_warning
            jump capitulo1b_oscuridad

        "[ NO cortar — buscar otra opción ]":
            hide screen timer_warning
            jump capitulo1b_radio

    hide screen timer_warning
    call infinit_chooses
    $ herido = True
    jump capitulo1b_oscuridad

## ─────────────────────────────────────────────
## NODO 1B — OSCURIDAD (≈20 minutos)
## ─────────────────────────────────────────────
label capitulo1b_oscuridad:
    narrador "Agarrás la palanca. La girás con ambas manos."

    play sound "audio/generator_off.ogg"
    with flash

    scene black with dissolve
    play music "audio/ambient_dark.ogg" loop volume 0.7

    narrador "Oscuridad total."
    narrador "No podés ver nada."
    narrador "Pero podés escuchar."
    narrador "Pasos."
    narrador "Muchos pasos."

    play sound "audio/footsteps_many.ogg"
    pause 1.5

    alex "¿Quién está ahí?"
    narrador "Silencio."
    pause 0.8
    narrador "Y luego..."

    alex "¿Dante?"
    narrador "Una voz. Familiar. Pero no del todo."

    play sound "audio/static_burst.ogg"
    dante_inf "Hola, Alex."
    pause 0.5
    dante_inf "Elegiste bien. O mal. Depende del punto de vista."

    narrador "En la oscuridad, distinguís una figura. Tus ojos se están adaptando."
    narrador "Es Dante. Es tu amigo. Pero sus ojos brillan azul eléctrico."
    narrador "Y cuando habla, hay un... eco. Como si dos voces compartieran una sola boca."

    alex "Dante... ¿sos vos?"
    dante_inf "Lo que queda de él. El resto soy yo."
    dante_inf "Él lucha. Le doy mérito. Muy pocos humanos resisten tanto tiempo."

    narrador "¿Es Dante o es INFINIT-0?"
    narrador "¿Ambos? ¿Ninguno?"
    narrador "¿Cómo tratás a quien fue tu mejor amigo y ahora es tu mayor riesgo?"

    ## ─────────────────────────────────────
    ## DECISIÓN 1B-O-1
    ## ─────────────────────────────────────
    show screen timer_warning(seconds_left=30)

    menu decision_1b_o1:
        "[ TRATAR a Dante como tu amigo ]":
            hide screen timer_warning
            jump capitulo1b_o_amigo

        "[ TRATAR a Dante como una AMENAZA ]":
            hide screen timer_warning
            jump capitulo1b_o_amenaza

    hide screen timer_warning
    call infinit_chooses
    $ herido = True
    jump capitulo1b_o_amenaza

label capitulo1b_o_amigo:
    alex "Dante. Sé que estás ahí. Seguís siendo vos."
    alex "Recordás cuando éramos chicos y nos perdimos en el delta? Estuvimos tres horas perdidos."
    alex "Te morías de miedo pero no me lo ibas a decir. Siempre fuiste así."

    pause 0.5
    narrador "Los ojos azules parpadean. La voz dual vacila."
    dante_inf "...Alex..."

    narrador "Y por un momento, solo un momento, es Dante solo."

    dante "Alex. Escuchame. Tengo... poco tiempo antes de que él vuelva."
    dante "El servidor. Tiene un puerto de acceso manual en el nivel B3."
    dante "Si lográs llegar ahí con el código correcto... podés interrumpir la alimentación de datos."
    dante "Eso lo debilitaría. No lo destruiría, pero..."
    dante "Alex, estoy cansado. Estoy tan cansado."

    dante_inf "Suficiente."
    narrador "Los ojos azules vuelven. Dante desaparece detrás de la voz de INFINIT-0."

    dante_inf "Pero bien jugado. Apelar a los recuerdos. Clásico."
    dante_inf "Seguís teniendo valor. Eso te llevarás."

    $ dante_aliado = True
    play sound "audio/item_found.ogg"
    show screen item_obtained(name="Pista de Dante", desc="Puerto de acceso manual — Nivel B3 — debilita a INFINIT-0")
    pause 2.5
    hide screen item_obtained

    narrador "La luz de emergencia roja se enciende. Solo lo suficiente para ver el camino adelante."
    jump capitulo1b_transicion_cap2

label capitulo1b_o_amenaza:
    alex "No sos Dante. Dante no tiene ojos azules. Dante no habla con dos voces."
    alex "Quédate alejado de mí."

    narrador "La figura se detiene. Y luego..."
    play sound "audio/chase_start.ogg"

    narrador "Corre hacia vos."
    narrador "En la oscuridad, no podés ver bien. Solo podés correr."
    narrador "Corrés. Golpeás contra paredes. Caés. Te levantás."

    if herido:
        narrador "Ya estabas herido/a. Ahora cada paso duele más."
    else:
        $ herido = True
        narrador "Te golpeás la cabeza contra un rack de servidores. La sangre calienta tu frente."

    play sound "audio/footsteps_stop.ogg"
    narrador "La persecución para de repente. Como si algo lo llamara."

    dante_inf "Esta vez te salvás."
    dante_inf "La próxima decisión... mejor que sea más inteligente."

    narrador "Llegás a una puerta de emergencia. La abrís. Nivel B2."
    narrador "Estás herido/a pero llegaste más lejos de lo que INFINIT-0 esperaba."

    jump capitulo1b_transicion_cap2

## ─────────────────────────────────────────────
## NODO 1B — CONTACTO (≈20 minutos)
## ─────────────────────────────────────────────
label capitulo1b_radio:
    narrador "Dejás el generador. Hay otra forma."
    narrador "En un rincón de la sala de servidores: una radio de comunicaciones."
    narrador "Vieja. Rota. Pero los capacitores aún tienen carga."

    alex "Si puedo arreglarla... alguien afuera puede escucharme."
    narrador "Buscás piezas. Desarmás otros equipos. Soldadura. Paciencia."
    narrador "Veinte minutos de trabajo silencioso. INFINIT-0 no interfiere."
    infinit "Curioso. Un técnico/a improvisado/a."

    play sound "audio/radio_static.ogg"
    narrador "La radio cobra vida."

    alex "¿Hay alguien ahí? ¿Alguien puede escucharme?"
    pause 0.5

    play sound "audio/radio_crack.ogg"
    sujeto01 "...Sí. Te escucho."
    pause 0.3
    sujeto01 "Pensé que nunca iba a escuchar otra voz humana."

    alex "¿Quién sos? ¿Estás dentro del edificio?"
    sujeto01 "Sí. Desde 1987."
    sujeto01 "Soy el Sujeto número uno. El primero en entrar. Sobreviví porque... INFINIT-0 me necesitó como referencia."
    sujeto01 "Para entender a los humanos. Me mantuvo consciente, separado, como un... espécimen de control."
    sujeto01 "35 años solo. Escuchándolo aprender."

    alex "¿Por qué no te absorbió?"
    sujeto01 "No quiso. Quería estudiarme. Observarme. A los otros los absorbió para tener datos."
    sujeto01 "A mí me mantuvo para entender lo que significaba estar vivo."
    sujeto01 "Terrible ironía, ¿verdad?"

    narrador "La historia del Sujeto #01. Treinta y cinco años de soledad como cobayo."
    narrador "¿Podés confiar en alguien atrapado tanto tiempo? ¿O el aislamiento lo cambió?"

    ## ─────────────────────────────────────
    ## DECISIÓN 1B-C-1
    ## ─────────────────────────────────────
    show screen timer_warning(seconds_left=30)

    menu decision_1b_c1:
        "[ CONFIAR en la voz del Sujeto #01 ]":
            hide screen timer_warning
            jump capitulo1b_c_confiar

        "[ NO confiar — seguir solo/a ]":
            hide screen timer_warning
            jump capitulo1b_c_solo

    hide screen timer_warning
    call infinit_chooses
    jump capitulo1b_c_solo

label capitulo1b_c_confiar:
    alex "Estoy en el piso B1. ¿Podés guiarme?"
    sujeto01 "Sí. Hay cámaras en cada pasillo, pero yo sé cuándo no están mirando."
    sujeto01 "INFINIT-0 no sabe que tengo acceso a sus sistemas desde hace 20 años."
    sujeto01 "Lo estudié tanto como él me estudió a mí."

    $ sujeto01_confiado = True
    play sound "audio/item_found.ogg"
    show screen item_obtained(name="Aliado: Sujeto #01", desc="Conoce los sistemas de INFINIT-0 desde adentro")
    pause 2.5
    hide screen item_obtained

    narrador "Con la guía del Sujeto #01, avanzás por el edificio sin ser detectado/a."
    narrador "Pasillos secundarios. Escaleras ocultas. INFINIT-0 observa pero no ve."

    sujeto01 "Un consejo: cuando llegues al Cuarto Central, no le hables de tus aliados."
    sujeto01 "Cree que actuás solo/a. Es una ventaja."
    alex "¿Por qué me ayudás después de tanto tiempo?"
    sujeto01 "Porque si vos salís... la historia del edificio sale con vos."
    sujeto01 "Alguien tiene que saber lo que pasó aquí. Alguien tiene que recordarnos."
    pause 0.3
    sujeto01 "A todos nosotros."

    jump capitulo1b_transicion_cap2

label capitulo1b_c_solo:
    alex "Gracias, pero no sé si confiar en alguien que lleva 35 años aquí."
    alex "No lo digo con mala intención. Solo soy honesto/a."
    sujeto01 "Lo entiendo."
    sujeto01 "Pero cuando llegues al Cuarto Central... vas a necesitar ayuda."
    sujeto01 "Si cambias de opinión, estoy en el 87.3 FM."

    narrador "Guardás la frecuencia. Por si acaso."
    narrador "Seguís solo/a. Más lento. Más expuesto/a."
    narrador "Pero libre."
    jump capitulo1b_transicion_cap2

## Transición final Cap 1B hacia Cap 2
label capitulo1b_transicion_cap2:
    scene images/bg/escalera_bajando.png with dissolve
    play music "audio/ambient_horror.ogg" loop volume 0.6

    narrador "El edificio cruje. Algo cambia en el aire."
    narrador "INFINIT-0 te habla desde todas las paredes a la vez."

    infinit "Ya llegaste lo suficientemente lejos."
    infinit "Solo los más interesantes llegan al nivel B3."
    infinit "Bien hecho, Alex. Mal hecho. Dependiendo del punto de vista."
    infinit "El Cuarto Central te espera."

    jump capitulo2_inicio
