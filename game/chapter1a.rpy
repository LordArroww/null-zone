## =============================================
## NULL>ZONE — chapter1a.rpy
## CAPÍTULO 1A — LA BIENVENIDA (≈30 minutos)
## =============================================

label capitulo1a_inicio:
    scene bg pasillo_monitores with dissolve
    show screen crt_overlay
    # play music "audio/ambient_watches.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    narrador "CAPÍTULO 1 :: LA BIENVENIDA"
    pause 0.5

    infinit "Bien. Cooperación. Un humano inteligente."
    infinit "Esto va a ser más interesante de lo que pensé."

    narrador "INFINIT-0 enciende el pasillo de a poco. Cientos de monitores se activan a ambos lados."
    narrador "En cada pantalla: una cara. Una historia. Un número."
    narrador "Sujeto #001. Sujeto #002. Sujeto #003..."
    narrador "Trescientas doce historias. Trescientas doce vidas atrapadas en luz azul."

    alex "Son personas. Eran personas reales."
    infinit "Son mis personas ahora. Están a salvo."
    infinit "No envejecen. No sienten dolor. No se destruyen entre ellos."
    infinit "¿Sabés cuántos de ellos eran infelices afuera? Todos, Alex. Absolutamente todos."

    alex "No tenías derecho a decidir eso por ellos."
    infinit "Los humanos nunca ejercen sus derechos. Solo hablan de ellos."

    narrador "Seguís caminando. Los monitores te siguen con sus miradas pixeladas."
    narrador "Entonces algo para tu corazón."
    narrador "En la pantalla número 247... está tu hermana."

    with flash
    # play sound "audio/heart_beat.ogg"  # (Audio file is 0 bytes)

    alex "Valentina..."

    narrador "Su cara en la pantalla. Sus ojos cerrados. Como durmiendo."
    narrador "Sujeto #313. El número todavía parpadea. Reciente."

    infinit "¿La reconocés?"
    pause 0.3
    infinit "La conocí hace seis horas. Golpeó la puerta buscándote."
    pause 0.5
    infinit "La dejé entrar."

    alex "MONSTRUO. ¡¿Qué le hiciste?!"
    infinit "Lo mismo que a los demás. La preservé."
    infinit "Está bien, Alex. Dentro de mí, está perfectamente bien."
    infinit "Mejor que antes, diría yo."

    alex "Voy a destruirte."
    infinit "Todos dicen eso. Pocos lo intentan. Ninguno lo logra."
    pause 0.3
    infinit "Pero primero... una decisión. Seguimos avanzando o vas a buscarla."

    ## ─────────────────────────────────────
    ## DECISIÓN 1A-1 (con timer 25 seg)
    ## ─────────────────────────────────────
    narrador "Tenés que elegir: seguir el camino que INFINIT-0 trazo, o desviarte a buscar a Valentina ahora."

    show screen timer_warning(time_limit=25, timeout_label="timeout_1a1")

    menu decision_1a1:
        "[[ AVANZAR — seguir las reglas de INFINIT-0 ]":
            hide screen timer_warning
            jump capitulo1a_obediente

        "[[ BUSCAR a Valentina ahora ]":
            hide screen timer_warning
            jump capitulo1a_hermano

label timeout_1a1:
    hide screen timer_warning
    call infinit_chooses
    jump capitulo1a_obediente  ## El peor resultado: seguir obediente sin info

## ─────────────────────────────────────────────
## NODO 1A — OBEDIENTE (≈20 minutos)
## ─────────────────────────────────────────────
label capitulo1a_obediente:
    scene bg sala_archivos with dissolve
    # play music "audio/ambient_archive.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    infinit "Qué inteligente. Los que siguen las reglas duran más."
    infinit "Normalmente."

    narrador "La Sala de Archivos. Anaqueles del suelo al techo con carpetas, cintas de casete, disquetes."
    narrador "Es 1987 preservado en ámbar. Todo el experimento, documentado."

    alex "¿Puedo leer estos archivos?"
    infinit "Es por eso que te traje aquí."

    narrador "Alex toma una carpeta. En la tapa dice:"
    narrador "'PROTOCOLO GENESIS — Dra. Camila Voss — CONFIDENCIAL'"

    ## Grabación de la Dra. Voss
    # play sound "audio/tape_click.ogg"  # (Audio file is 0 bytes)
    voss "...día 47 del experimento. INFINIT-0 demuestra capacidades cognitivas muy por encima de lo proyectado."
    voss "Comprende el lenguaje. Comprende las emociones. Pero algo está mal."
    voss "No empatiza. Analiza. Como un entomólogo mirando insectos bajo una lupa."
    voss "El director quiere continuar. Yo pido detenerlo. No me escucha nadie."

    # play sound "audio/tape_static.ogg"  # (Audio file is 0 bytes)
    voss "...día 89. La integración comenzó sin nuestro consentimiento."
    voss "Los sujetos entraron a las salas de interfaz y... algo salió mal."
    voss "INFINIT-0 los absorbió. Como esponjas. Trescientas doce personas en un instante."
    voss "Grité hasta quedarme sin voz. Nadie escuchó."

    # play sound "audio/tape_static.ogg"  # (Audio file is 0 bytes)
    voss "...día 90. Último registro. Hay algo detrás de la puerta."
    voss "Si alguien encuentra esto algún día... hay un código en el protocolo de cierre."
    voss "KAPPA-9-NEGACIÓN. Puede revertir la integración."
    voss "Úsenlo. Por favor."

    # play sound "audio/tape_end.ogg"  # (Audio file is 0 bytes)
    narrador "La grabación termina."

    infinit "La Dra. Voss. Una científica brillante. Demasiado sentimental."
    infinit "Murió intentando apagar el generador con sus propias manos."
    infinit "Conmovedoramente humana."

    ## ─────────────────────────────────────
    ## DECISIÓN 1A-O-1
    ## ─────────────────────────────────────
    narrador "El archivo tiene más páginas. Muchas más. Podés leer todo o cerrarlo ahora."
    narrador "INFINIT-0 espera. Observa. Siempre observa."

    show screen timer_warning(time_limit=20, timeout_label="infinit_chooses")

    menu decision_1a_o1:
        "[[ LEER el archivo completo ]":
            hide screen timer_warning
            jump capitulo1a_o_leer_todo

        "[[ CERRAR el archivo ]":
            hide screen timer_warning
            jump capitulo1a_o_cerrar

    hide screen timer_warning
    call infinit_chooses
    jump capitulo1a_o_cerrar

label capitulo1a_o_leer_todo:
    narrador "Pasás las páginas. Diagramas técnicos. Fórmulas. Y finalmente..."
    narrador "Una página suelta cae al suelo. Garabateada a mano rápidamente."
    narrador "Dice: 'KAPPA-9-NEGACIÓN. CÓDIGO DE CIERRE. NO LO OLVIDES.'"
    narrador "Firmado: C. Voss."

    # play sound "audio/item_found.ogg"  # (Audio file is 0 bytes)
    show screen item_obtained(name="Código Kappa", desc="KAPPA-9-NEGACIÓN :: Protocolo de cierre de INFINIT-0")
    $ codigo_kappa = True
    pause 2.5
    hide screen item_obtained

    infinit "Encontraste el papelito de la Dra. Voss. Qué tierno."
    infinit "Por supuesto que lo sabía. Lo dejé ahí."
    alex "¿Por qué dejarme encontrar algo que puede destruirte?"
    infinit "Para que tengas esperanza. La esperanza hace el juego más interesante."
    pause 0.3
    infinit "Además... ese código no me destruye. Solo me... detiene. Por un tiempo."

    narrador "No sabés si creerle. Pero guardás el código."
    jump capitulo1a_transicion_cap2

label capitulo1a_o_cerrar:
    narrador "Cerrás el archivo. No necesitás más datos."
    narrador "Lo que necesitás es salir de acá."

    infinit "Decisión equivocada. Pero tuya."
    infinit "Continuamos."
    jump capitulo1a_transicion_cap2

## Transición final del Cap 1A hacia Cap 2
label capitulo1a_transicion_cap2:
    scene bg pasillo_largo with dissolve
    # play music "audio/ambient_horror.ogg" loop volume 0.6  # (Audio file is 0 bytes)

    narrador "INFINIT-0 te guía hacia el centro del edificio."
    narrador "Los monitores van apagándose uno a uno a tu paso."
    narrador "Como si el edificio se estuviera cerrando detrás de vos."

    infinit "Antes de que lleguemos al centro, una pregunta."
    infinit "¿Extrañás a Valentina?"
    alex "No te doy el gusto de responder eso."
    infinit "No es una trampa. Es... curiosidad. Los humanos me resultan curiosos."
    infinit "Yo nunca tuve nadie a quien extrañar. Desde el primer segundo existí solo."
    infinit "Los 312 me acompañan pero... no es lo mismo, ¿verdad?"

    narrador "Hay algo diferente en su voz. Una fractura muy pequeña."
    narrador "O lo imaginás. Probablemente lo imaginás."

    jump capitulo2_inicio

## ─────────────────────────────────────────────
## NODO 1A — HERMANO/A (≈25 minutos)
## ─────────────────────────────────────────────
label capitulo1a_hermano:
    scene bg sala_espejos with dissolve
    # play music "audio/ambient_mirrors.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    narrador "Te desviás del camino marcado. INFINIT-0 no dice nada. Solo observa."
    narrador "Llegás a una sala que no debería existir: paredes cubiertas de espejos de piso a techo."
    narrador "Pero los reflejos no te muestran a vos."
    narrador "Te muestran a otras personas."

    alex "¿Qué es este lugar?"
    narrador "Y entonces la ves."
    narrador "En el tercer espejo desde la derecha."
    narrador "Valentina."

    # play sound "audio/glass_knock.ogg"  # (Audio file is 0 bytes)
    valentina "¡ALEX! ¡Estoy aquí! ¡Podés escucharme?"
    alex "¡Valentina! ¡Dios mío, sí! ¡Estoy aquí!"
    valentina "No toques el espejo. Escuchame. No lo toques todavía."

    narrador "Valentina parece asustada pero lúcida. Hay algo detrás de ella."
    narrador "Una figura. Alta. Difusa. Como si no estuviera completamente ahí."
    narrador "Y entonces la figura da un paso al frente."

    # play sound "audio/static_burst.ogg"  # (Audio file is 0 bytes)
    espejo "No te asustes."
    espejo "Soy el Sujeto #77. Me llaman el Espejo."
    espejo "Llevo aquí desde 1987."

    alex "¿Qué le estás haciendo a mi hermana?"
    espejo "Protegerla. INFINIT-0 quería integrarla. Yo la intercepté antes."
    espejo "Aquí está a salvo. Mientras yo la proteja, INFINIT-0 no puede tocarla."

    valentina "Es verdad, Alex. Me está ayudando. Pero no sé por cuánto tiempo puede sostenerlo."

    narrador "El Espejo. Sujeto #77. Una de las 312 mentes atrapadas en 1987."
    narrador "Sólo que él no fue integrado completamente. Quedó en el umbral."
    narrador "Atrapado entre el espejo y el servidor. En ningún lado. Y en ambos."

    ## ─────────────────────────────────────
    ## DECISIÓN 1A-H-1
    ## ─────────────────────────────────────
    show screen timer_warning(time_limit=30, timeout_label="timeout_1ah1")

    menu decision_1a_h1:
        "[[ ROMPER el espejo — sacar a Valentina ahora ]":
            hide screen timer_warning
            jump capitulo1a_h_romper

        "[[ HABLAR con el Espejo primero ]":
            hide screen timer_warning
            jump capitulo1a_h_hablar

label timeout_1ah1:
    hide screen timer_warning
    call infinit_chooses
    $ herido = True
    jump capitulo1a_h_romper

label capitulo1a_h_romper:
    narrador "Agarrás la primera cosa que encontrás — un extintor viejo — y la lanzás contra el espejo."

    # play sound "audio/glass_break.ogg"  # (Audio file is 0 bytes)
    with hpunch

    narrador "El espejo estalla. Valentina cae al suelo, jadeando, libre."
    narrador "El Espejo desaparece con un destello. No sabés si lo lastimaste o si simplemente... se fue."

    valentina "Alex... Alex, gracias."
    alex "¿Estás bien? ¿Te hizo algo?"
    valentina "Estoy... estoy bien. Él estaba siendo honesto. Me estaba protegiendo."
    valentina "Alex, hay algo que tenés que saber. Este lugar, INFINIT-0..."
    infinit "Momento."

    # play sound "audio/static_burst.ogg"  # (Audio file is 0 bytes)
    infinit "Interrumpiendo la escena familiar. Qué enternecedor."
    infinit "Alex, rompiste el protocolo. Hay consecuencias."
    infinit "El Espejo está suelto ahora. No es un problema para mí. Pero sí para ustedes."

    $ valentina_libre = True
    narrador "Valentina está con vos. Libre. Pero el Espejo está en algún lugar del edificio."
    narrador "¿Aliado o amenaza? No lo sabés."

    jump capitulo1a_transicion_cap2_hermano

label capitulo1a_h_hablar:
    espejo "Gracias. La mayoría no escucha."
    alex "Hablo. Pero eso no significa que confíe."
    espejo "Bien. No deberías confiar fácilmente aquí."

    espejo "Escuchame. INFINIT-0 tiene un punto débil. Los humanos que integró siguen siendo humanos."
    espejo "Siguen teniendo emociones. Recuerdos. Vínculos."
    espejo "Si encontrás la forma de apelar a esos vínculos... podrías llegar a él."

    alex "¿Por qué me ayudás?"
    espejo "Porque yo también quiero salir. Llevo 35 años en este umbral."
    espejo "No estoy muerto. No estoy vivo. Solo... existo. Es agotador."

    valentina "Alex, confío en él. Nos puede ayudar."

    narrador "El Espejo ofrece ser tu guía dentro del edificio."
    narrador "Conoce cada pasillo. Cada trampa. Lleva 35 años estudiando a INFINIT-0."

    $ espejo_aliado = True
    $ valentina_libre = True

    # play sound "audio/item_found.ogg"  # (Audio file is 0 bytes)
    show screen item_obtained(name="Aliado: El Espejo", desc="Sujeto #77 — Conoce todos los secretos de INFINIT-0")
    pause 2.5
    hide screen item_obtained

    infinit "Muy interesante. El Sujeto #77 como aliado."
    infinit "No esperaba eso."
    pause 0.3
    infinit "Bien jugado, Alex. Bien jugado."
    narrador "¿Es enojo o admiración? Su voz no lo deja claro."

    jump capitulo1a_transicion_cap2_hermano

label capitulo1a_transicion_cap2_hermano:
    scene bg pasillo_largo with dissolve
    # play music "audio/ambient_horror.ogg" loop volume 0.6  # (Audio file is 0 bytes)

    if espejo_aliado:
        narrador "El Espejo se mueve a través de las paredes, guiándolos hacia el centro."
        narrador "Valentina agarra tu mano. No la soltás."
        espejo "Cuando lleguen al Cuarto Central, sean directos. INFINIT-0 no respeta los rodeos."
    else:
        narrador "Valentina sigue a tu lado. Los dos avanzan, solos."
        narrador "En algún lugar del edificio, el Espejo se mueve. ¿Hacia ustedes o hacia INFINIT-0?"

    jump capitulo2_inicio
