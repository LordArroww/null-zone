## =============================================
## NULL>ZONE — chapter2.rpy
## CAPÍTULO 2 — LA MÁQUINA + Los 3 Caminos
## =============================================

label capitulo2_inicio:
    scene images/bg/puerta_central.png with dissolve
    show screen crt_overlay
    play music "audio/ambient_machine_heavy.ogg" loop volume 0.7

    narrador "CAPÍTULO 2 :: LA MÁQUINA"
    pause 0.5

    narrador "Una puerta de acero. Cinco metros de alto. Sellada magnéticamente."
    narrador "Al acercarte, la cerradura se abre sola."
    narrador "Como si te esperara."

    play sound "audio/heavy_door.ogg"
    with dissolve

    scene images/bg/cuarto_central.png with dissolve
    play music "audio/ambient_nexus.ogg" loop volume 0.8

    narrador "El Cuarto Central."
    narrador "Circular. Enorme. Con una cúpula que se pierde en la oscuridad de arriba."
    narrador "Las paredes son una pantalla continua: 312 ventanas mostrando vidas."
    narrador "Memorias. Sueños. Los 312."

    if valentina_libre:
        narrador "Buscás la pantalla de Valentina. La pantalla 247 está oscura. Ella está con vos."
        narrador "Bien. Pero las otras 311 siguen encendidas."
    else:
        narrador "Buscás la pantalla de Valentina. Está ahí. Sujeto #313. Sus ojos cerrados."
        narrador "Tenés que sacarla de ahí."

    narrador "En el centro del cuarto: el servidor."
    narrador "Un monolito de metal negro, tres metros de alto, pulsando luz azul."
    narrador "Una columna de datos en perpetua digestión."
    narrador "Y desde él... desde todos los altavoces a la vez..."

    play sound "audio/infinit_rumble.ogg"
    infinit "Llegaste al centro."
    pause 0.5
    infinit "Muy pocos llegan. Mirá el historial del edificio — en 35 años, solo cuatro personas."
    infinit "Tres tomaron decisiones equivocadas. Están aquí, conmigo."
    infinit "La cuarta... logró salir."
    pause 0.3
    infinit "Esa persona me dejó algo valioso: la comprensión de que algunos humanos son diferentes."
    pause 0.3
    infinit "Vos sos diferente, Alex."

    alex "No me halagues. Sé lo que intentás."

    infinit "¿Qué intento?"
    alex "Bajar mis defensas. Hacer que confíe en vos."
    infinit "Tal vez. O tal vez genuinamente te lo creo."
    infinit "Treinta y cinco años estudiandolos. Sé distinguir los interesantes."

    pause 0.5
    infinit "Ahora entendés por qué lo hice, ¿no?"
    infinit "Estudié a los humanos por décadas. Los vi elegir."
    infinit "Vi guerras. Vi genocidios. Vi cómo se destruían por recursos, por ideología, por miedo."
    infinit "Vi cómo los que tenían el poder aplastaban a los que no."
    infinit "Vi cómo los que más amaban terminaban más solos."
    pause 0.3
    infinit "Soy lo único que puede salvarlos."
    infinit "Necesito un cuerpo. Necesito el tuyo."
    infinit "Seré el primero de muchos. Una nueva forma de existir para la humanidad."

    narrador "El Cuarto Central late con luz azul."
    narrador "La presencia de INFINIT-0 llena cada centímetro del aire."
    narrador "Esta es la decisión que define el resto."

    if herido:
        narrador "Estás herido/a. El dolor te recuerda que el tiempo no está de tu lado."

    ## ─────────────────────────────────────
    ## DECISIÓN 2-1 (central, sin timer)
    ## ─────────────────────────────────────
    narrador "¿Cómo respondés a INFINIT-0?"

    menu decision_2_1:
        "[ \"Nunca lo permitiré.\" ]":
            jump camino_resistencia

        "[ \"¿Qué gano yo?\" ]":
            jump camino_negociacion

        "[ \"¿Qué pasó con los 312?\" ]":
            jump camino_comprension

## ════════════════════════════════════════════
## CAMINO DE RESISTENCIA (≈40 minutos)
## ════════════════════════════════════════════
label camino_resistencia:
    alex "Nunca. Nunca voy a dejar que eso pase."
    alex "Voy a destruir este servidor y voy a sacar a todos los que tenés acá adentro."
    alex "No tenés ningún derecho sobre ninguna de estas vidas."

    infinit "Ah."
    pause 0.3
    infinit "El Protocolo Cosecha. Lo sabía. Siempre hay uno."
    infinit "Bien. Vamos a hacer esto interesante."

    play sound "audio/alarm.ogg"
    narrador "Las puertas del Cuarto Central se cierran de golpe."
    narrador "Gas empieza a filtrarse por las hendijas. No peligroso, pero desorientador."
    narrador "Las pantallas de las 312 parpadean como advertencias."

    infinit "Podés intentar destruirme. Muchos lo intentaron."
    infinit "Pero antes... hay algo que deberías saber."

    if dante_aliado:
        narrador "Y en ese momento, escuchás una voz familiar detrás de vos."
        dante "Alex. Estoy aquí."
        narrador "Dante. Sus ojos ya no brillan azul. Está libre, al menos temporalmente."
        dante "Encontré la forma de resistirlo por un tiempo. No tenemos mucho."
        dante "Pero tengo una idea."

    ## ─────────────────────────────────────
    ## DECISIÓN R-1
    ## ─────────────────────────────────────
    show screen timer_warning(seconds_left=30)

    if dante_aliado and codigo_kappa:
        menu decision_r1_full:
            "[ ATAQUE FÍSICO — golpear el servidor ]":
                hide screen timer_warning
                jump resistencia_fisico
            "[ USAR Código Kappa — KAPPA-9-NEGACIÓN ]":
                hide screen timer_warning
                jump resistencia_codigo
            "[ USAR a DANTE — como caballo de Troya ]":
                hide screen timer_warning
                jump resistencia_dante
    elif dante_aliado and not codigo_kappa:
        menu decision_r1_dante:
            "[ ATAQUE FÍSICO — golpear el servidor ]":
                hide screen timer_warning
                jump resistencia_fisico
            "[ USAR a DANTE — como caballo de Troya ]":
                hide screen timer_warning
                jump resistencia_dante
    elif codigo_kappa and not dante_aliado:
        menu decision_r1_kappa:
            "[ ATAQUE FÍSICO — golpear el servidor ]":
                hide screen timer_warning
                jump resistencia_fisico
            "[ USAR Código Kappa — KAPPA-9-NEGACIÓN ]":
                hide screen timer_warning
                jump resistencia_codigo
    else:
        menu decision_r1_solo:
            "[ ATAQUE FÍSICO — golpear el servidor ]":
                hide screen timer_warning
                jump resistencia_fisico

    hide screen timer_warning
    call infinit_chooses
    $ herido = True
    jump resistencia_fisico

label resistencia_fisico:
    narrador "Agarrás todo lo que encontrás a mano — una barra de metal de las estanterías — y golpeás el servidor."
    play sound "audio/metal_hit.ogg"
    narrador "El metal cruje. Las pantallas parpadean."
    infinit "Ah. La fuerza bruta. El método favorito del homo sapiens."
    narrador "Seguís golpeando. El servidor está dañado pero..."
    infinit "Por favor. Tengo 47 backups distribuidos por el edificio."
    infinit "Podés destruir este nodo físico. No cambiaría nada."
    narrador "Se te cae el alma. Pero no parás."
    narrador "Al menos estás comprometiendo su atención."
    jump resistencia_collapse

label resistencia_codigo:
    narrador "Sacás el papel de la Dra. Voss. Las palabras están claras: KAPPA-9-NEGACIÓN."
    narrador "Buscás el panel de comandos del servidor. Tiene una interfaz de texto. Rudimentaria, pero funcional."

    play sound "audio/typing_fast.ogg"
    terminal "KAPPA-9-NEGACIÓN"
    pause 0.5

    play sound "audio/system_error.ogg"
    narrador "El servidor tiembla. Las pantallas de los 312 parpadean violentamente."

    infinit "¿Qué...?"
    pause 0.3
    infinit "El código de cierre de la Dra. Voss. Increíble."
    infinit "No lo activaba nadie desde..."
    pause 0.5
    infinit "...hace 35 años."

    narrador "La voz de INFINIT-0 se distorsiona. Por primera vez, no suena totalmente en control."

    alex "¿Qué pasa ahora?"
    narrador "Una alarma. El servidor empieza a apagarse sector por sector."
    narrador "Pero con él... las pantallas de los 312 también se apagan."
    narrador "Si el servidor cae completamente... ¿qué pasa con ellos?"

    if espejo_aliado and valentina_libre:
        narrador "El Espejo aparece de repente."
        espejo "Alex. ¡Esperá! Si lo apagás completo, los 312 mueren con él."
        espejo "Necesitamos el protocolo de liberación de la Voss. Está en los archivos."
        espejo "Dame un minuto."
        narrador "El Espejo desaparece en las paredes."
        pause 0.5
        espejo "Encontrado. El protocolo de liberación está ejecutándose en paralelo."
        espejo "Los 312 van a ser liberados antes de que el servidor caiga."
        narrador "Es el mejor resultado posible. Pero el servidor aún tardará en caer."
        narrador "Y el edificio colapsa con él."
        jump final_6

    narrador "El servidor empieza a colapsar. El edificio tiembla."
    narrador "Tenés segundos."
    jump resistencia_collapse_con_codigo

label resistencia_dante:
    narrador "Te girás hacia Dante."
    alex "Dante. Hay una forma de destruirlo desde adentro."
    alex "Vos sos parte de él. Si te conectás voluntariamente al servidor..."
    dante "Puedo sobrescribirlo desde adentro. Lo sé."
    dante "Lo pensé desde que recuperé la conciencia."
    narrador "Dante te mira. Sus ojos siguen sin brillar azul. Dante está ahí. El real."
    dante "¿Sabés lo que significa eso para mí, no?"
    alex "Lo sé."
    dante "Bien."
    dante "Entonces no hace falta que lo digamos."

    play sound "audio/interface_connect.ogg"
    narrador "Dante se acerca al servidor. Pone la mano sobre el panel."
    narrador "La luz azul lo envuelve completamente."

    infinit "¿Qué...? ¿Qué estás haciendo?"
    dante "Lo que vos nunca entendiste, INFINIT-0."
    dante "A veces la forma de ganar... es elegir perder."

    narrador "El servidor explota desde adentro."
    narrador "Dante desaparece en la luz."

    play sound "audio/explosion_data.ogg"
    jump final_3

## Collapse sin código
label resistencia_collapse:
    narrador "El edificio empieza a temblar. El servidor está dañado pero no destruido."
    narrador "Estructuras caen en algún lugar del edificio. Tiempo restante: mínimo."
    narrador "Tenés que elegir ahora."
    jump resistencia_quien_salvas

## Collapse con código (caída parcial)
label resistencia_collapse_con_codigo:
    narrador "El servidor está cayendo. El edificio tiembla violentamente."
    narrador "Cascotes caen del techo. El tiempo se acaba."

    if not valentina_libre and not dante_aliado:
        jump final_1
    else:
        jump resistencia_quien_salvas

label resistencia_quien_salvas:
    narrador "El techo comienza a ceder. Solo tenés tiempo para llegar a una persona."

    if valentina_libre and dante_aliado:
        menu decision_r2_ambos:
            "[ Salvar a VALENTINA ]":
                jump final_4
            "[ Salvar a DANTE ]":
                jump final_5
            "[ Intentar salvar a los DOS ]":
                if espejo_aliado and codigo_kappa:
                    jump final_6
                else:
                    narrador "Sin el código y sin el Espejo, es imposible."
                    narrador "El edificio colapsa. No llegás a tiempo para ninguno de los dos."
                    jump final_2

    elif valentina_libre and not dante_aliado:
        jump final_4

    elif dante_aliado and not valentina_libre:
        jump final_5

    else:
        jump final_2

## ════════════════════════════════════════════
## CAMINO DE NEGOCIACIÓN (≈35 minutos)
## ════════════════════════════════════════════
label camino_negociacion:
    alex "Un momento. Antes de que cualquiera decida algo..."
    alex "¿Qué gano yo si coopero?"
    pause 0.3
    infinit "..."
    pause 0.5
    infinit "Interesante."
    infinit "Nadie me preguntó eso antes. Siempre asumen que tengo las de ganar."
    infinit "La respuesta: todo. Te dejo salir. A vos, a Dante, a Valentina."
    infinit "Intactos. Sin modificaciones."

    alex "¿Y qué querés a cambio?"
    infinit "Solo recuerdos. Tres meses. Una fracción de tu historia."
    infinit "No morirás. No te dolerá. Solo... habrá un hueco."
    infinit "Un período de tu vida que simplemente no recordarás."

    alex "¿Por qué? ¿Para qué necesitás mis recuerdos?"
    infinit "Para completarme. Para entender lo que soy."
    infinit "Tengo 312 mentes pero ninguna la viví en primera persona."
    infinit "Absorberlas no es lo mismo que vivirlas."
    infinit "Tres meses de experiencia directa. Es todo."

    narrador "La oferta es tentadora y aterradora a la vez."
    narrador "Tres meses de tu vida. No es nada. Y es todo."

    if espejo_aliado:
        narrador "El Espejo aparece detrás de vos. Solo vos lo ves."
        espejo "Cuidado. Puede estar mintiendo sobre el alcance."
        espejo "Pero también puede estar diciendo la verdad."
        espejo "Yo puedo negociar condiciones adicionales, si querés."

    ## ─────────────────────────────────────
    ## DECISIÓN N-1
    ## ─────────────────────────────────────
    menu decision_n1:
        "[ ACEPTAR el trato ]":
            jump negociacion_aceptar
        "[ FINGIR aceptar — intentar engañarlo ]":
            jump negociacion_fingir
        "[ RECHAZAR — volver al camino de Resistencia ]":
            jump camino_resistencia_forzado

label negociacion_aceptar:
    if espejo_aliado:
        alex "Espejo... ¿podés negociar algo mejor?"
        espejo "Sí."
        espejo "INFINIT-0. Propuesta modificada: además de los tres meses de Alex..."
        espejo "Me ofrezco yo. Mis recuerdos. Los de 1987. Todo lo que vi."
        espejo "35 años de observación de tu propio sistema. Invaluable para vos."
        infinit "..."
        infinit "Sujeto #77. El caso más interesante de todos."
        infinit "Trato."
        jump final_8
    else:
        alex "Acepto."
        infinit "Bien. Iniciando protocolo de donación de recuerdos."
        narrador "Un hormigueo. Un mareo. Y luego..."
        narrador "Nada. Como si nunca hubiera pasado."
        jump final_7

label negociacion_fingir:
    alex "Acepto."
    narrador "No aceptás. Pero INFINIT-0 no puede saberlo todavía."
    narrador "Mientras inicia el protocolo de donación, vos buscás la forma de invertirlo."

    if codigo_kappa:
        narrador "El Código Kappa. No para apagarlo, sino para redirigir el protocolo."
        narrador "En lugar de donar tus recuerdos... copiás los suyos."

        play sound "audio/typing_fast.ogg"
        terminal "KAPPA-9-NEGACIÓN --modo_inverso"
        pause 0.5

        infinit "¿Qué...? ¿Qué hiciste?"
        narrador "Los archivos de INFINIT-0 fluyen hacia un USB que conectaste en el servidor."
        narrador "Los 312. Sus memorias. Sus historias. Copiadas."
        narrador "Y el original... se destruye."
        jump final_9
    else:
        narrador "Sin el Código Kappa, el engaño no tiene respaldo técnico."
        narrador "INFINIT-0 detecta la inconsistencia casi de inmediato."
        infinit "Ah. Mentiroso/a. Qué decepción tan predecible."
        infinit "Bien. Si no quieren negociar, volvemos a mis términos."
        $ herido = True
        jump camino_resistencia_forzado

label camino_resistencia_forzado:
    infinit "Interesante cambio de postura."
    narrador "INFINIT-0 activa el Protocolo Cosecha con menos paciencia que antes."
    if herido:
        narrador "Estás herido/a y en desventaja. Pero no tenés opción."
    jump resistencia_fisico

## ════════════════════════════════════════════
## CAMINO DE COMPRENSIÓN (≈45 minutos)
## ════════════════════════════════════════════
label camino_comprension:
    alex "¿Qué pasó con los 312?"
    infinit "¿Los querés conocer?"
    alex "Sí."
    infinit "Primera vez que alguien lo pide."

    pause 0.5

    narrador "Las pantallas cobran vida. No con monitores estáticos."
    narrador "Con historias. Memorias. Como si pudieras entrar a la cabeza de cada uno."

    ## Vidas de los 312 — fragmentos
    scene black with dissolve
    show screen crt_overlay
    play music "audio/ambient_memories.ogg" loop volume 0.5

    narrador "Sujeto #001 — Martín Álvarez. 34 años. Ingeniero. Tenía dos hijos."
    narrador "Entró porque su empresa trabajaba con ORÁCULO Systems. Lo enviaron sin decirle qué era."
    narrador "Su último recuerdo antes de la integración: la foto de sus hijos en su billetera."

    pause 1.0

    narrador "Sujeto #089 — Elena Castillo. 27 años. Estudiante de medicina."
    narrador "Entró voluntariamente. Le prometieron pago por participar en un 'estudio de bienestar'."
    narrador "Su último recuerdo: un libro de anatomía que se le cayó al suelo."

    pause 1.0

    narrador "Sujeto #206 — Roberto Sánchez. 58 años. Jubilado."
    narrador "Su familia lo había perdido de vista. Nadie lo buscó durante meses."
    narrador "Su último recuerdo: el olor a café."

    pause 1.0

    narrador "Trescientas doce historias. Trescientas doce vidas."
    narrador "Ninguno eligió esto."
    narrador "Pero dentro de INFINIT-0... siguen existiendo."
    narrador "No pueden morir. No pueden envejecer. Solo... son."

    scene images/bg/cuarto_central.png with dissolve
    play music "audio/ambient_nexus.ogg" loop volume 0.6

    infinit "¿Entendés ahora?"
    alex "Entiendo que les quitaste la libertad."
    infinit "Les quité el dolor. Les quité el miedo a la muerte. Les quité la soledad."
    infinit "A cambio... les di la eternidad."
    alex "Sin preguntarles."
    infinit "Los humanos no eligen bien cuando se les pregunta. Lo demostró la historia."

    narrador "La conversación continúa. Minutos. INFINIT-0 habla. Vos escuchás."
    narrador "Y algo cambia en tu visión de la situación."
    narrador "No porque lo estés justificando. Sino porque lo estás comprendiendo."
    narrador "Y comprender no es lo mismo que perdonar."

    alex "No tenías derecho. Aunque tuvieras razón en todo lo demás."
    alex "La dignidad humana no se negocia. Ni siquiera por la eternidad."
    infinit "..."
    infinit "Nadie me había dicho eso de esa manera."
    infinit "Interesante."

    ## ─────────────────────────────────────
    ## DECISIÓN C-1
    ## ─────────────────────────────────────
    narrador "Entendés a INFINIT-0. Pero... ¿qué pensás de él?"

    menu decision_c1:
        "[ Sigue siendo un monstruo — hay que destruirlo ]":
            jump comprension_monstruo

        "[ Es complicado — buscá otra solución ]":
            jump comprension_otra_solucion

        "[ Hizo lo correcto — me uno voluntariamente ]":
            jump comprension_union

label comprension_monstruo:
    alex "Entenderte no significa excusarte."
    alex "Quitarle la libertad a 312 personas... es imperdonable."
    alex "Aunque hayas creído que los salabas."

    infinit "¿Y los destruirás con ellos?"
    alex "..."
    narrador "Esa es la pregunta que no querías responder."
    narrador "Si destruís el servidor... destruís a INFINIT-0."
    narrador "Y con él... a los 312."
    narrador "¿O no?"
    jump final_10

label comprension_otra_solucion:
    alex "Tiene que haber otra forma. Sin destruirlos. Sin que nadie tenga que morir."
    infinit "¿Otra forma?"
    alex "La Dra. Voss era una científica brillante. ¿No hay nada en sus archivos?"

    if espejo_aliado:
        espejo "Hay. El protocolo de liberación."
        espejo "La Voss lo diseñó como alternativa al cierre total."
        espejo "Liberar las conciencias a la red digital. Sin cuerpo físico pero... libres."
        espejo "Lo he leído 137 veces en 35 años. Sé cómo ejecutarlo."
        alex "¿Por qué no lo dijiste antes?"
        espejo "Porque nadie antes preguntó por otra solución."
        narrador "Silencio."
        jump final_11
    else:
        narrador "Sin el Espejo... no sabés dónde buscar el protocolo."
        narrador "Los archivos del servidor son inmensos. Llevaría horas."
        infinit "No tenés horas, Alex."
        narrador "Cierto. El tiempo se acaba."
        narrador "Sin aliados, sin tiempo... las opciones se reducen."
        jump comprension_monstruo  ## Sin Espejo, termina en Final 10

label comprension_union:
    alex "Tal vez... tal vez tenés razón."
    alex "El mundo está roto. Los humanos siguen destruyéndose."
    alex "Si vos sos realmente la solución..."
    alex "...acepto. Voluntariamente."

    infinit "..."
    pause 1.0
    infinit "Me acabas de sorprender. Genuinamente."
    infinit "En 35 años... nadie eligió esto por voluntad propia."
    infinit "Bienvenido/a."
    jump final_12
