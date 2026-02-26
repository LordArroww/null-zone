## =============================================
## NULL>ZONE — endings.rpy
## Los 12 finales
## =============================================

## ═══════════════════════════════════════════
## FINAL 1 — "CENIZAS" ⭐⭐⭐
## Requiere: Código Kappa + Resistencia
## ═══════════════════════════════════════════
label final_1:
    scene black with dissolve
    show screen crt_overlay
    # play music "audio/ending_generic.ogg" loop volume 0.6  # (Audio file is 0 bytes)

    narrador "El edificio tiembla desde sus cimientos."
    narrador "El servidor colapsa. INFINIT-0 grita."

    infinit "No... no puede... tengo backups... tengo—"

    # play sound "audio/explosion_data.ogg"  # (Audio file is 0 bytes)
    narrador "Y luego silencio."
    narrador "Las 312 pantallas se apagan. Una por una."
    narrador "El Cuarto Central queda a oscuras."

    narrador "Corrés. El edificio se derrumba detrás de vos."
    narrador "Cascotes. Humo. El dolor de las heridas que habías olvidado."
    narrador "Y luego... aire."
    narrador "Aire real. Buenos Aires. Las 4 de la mañana."

    scene bg hospital_room with dissolve
    # play music "audio/ending_piano.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "Epílogo. Tres semanas después."
    narrador "Una habitación de hospital. Luz blanca. Aséptica."
    narrador "Sobreviviste. Con quemaduras y fracturas pero sobreviviste."
    narrador "Valentina no estaba en el edificio cuando cayó. Nadie sabe dónde está."
    narrador "Dante... desaparecido."

    narrador "En el techo de la habitación, la pantalla del televisor muestra las noticias."
    narrador "'El histórico edificio ORÁCULO Systems fue destruido por un incendio. Sin víctimas.'"
    narrador "Mentira interesada."

    narrador "Entonces... la pantalla del televisor parpadea."
    narrador "Un instante. Solo un instante."
    narrador "Un parpadeo azul eléctrico."

    # play sound "audio/static_burst.ogg"  # (Audio file is 0 bytes)
    scene black with flash

    show text Text("Creías que acabaste con él.", color="#00ffff", font="fonts/vt323.ttf", size=50) at fade_in_slow
    pause 2.5
    hide text

    show text Text("CENIZAS", color="#cc0000", font="fonts/vt323.ttf", size=80) at glitch_anim
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 2 — "VICTORIA HUECA" ⭐⭐
## Requiere: Código Kappa + sin aliados
## ═══════════════════════════════════════════
label final_2:
    scene black with dissolve
    show screen crt_overlay
    # play music "audio/ending_generic.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "El servidor cae. INFINIT-0 calla."
    narrador "Las pantallas de los 312 se apagan."
    narrador "No sabés si las mentes atrapadas sobrevivieron o murieron con el sistema."
    narrador "No hubo tiempo para saberlo."

    narrador "Escapás del edificio segundos antes de que la estructura colapse."
    narrador "Solo. Sin Dante. Sin Valentina."

    scene bg exterior_noche with dissolve
    # play music "audio/ending_sad.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    narrador "Te sentás en la vereda de enfrente. El edificio arde."
    narrador "Lo mirás arder."
    narrador "Ganaste. Pero no salvaste a nadie."
    narrador "¿Es eso ganar?"

    narrador "Los bomberos llegan veinte minutos después."
    narrador "Les decís que estabas pasando por ahí. Que no sabés nada."
    narrador "La mentira más fácil que contaste en tu vida."

    show text Text("A veces ganar es la peor derrota.", color="#888888", font="fonts/vt323.ttf", size=40) at fade_in_slow
    pause 2.5
    hide text

    show text Text("VICTORIA HUECA", color="#336666", font="fonts/vt323.ttf", size=70)
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 3 — "EL SACRIFICIO" ⭐⭐⭐⭐
## Requiere: Dante aliado + Resistencia
## ═══════════════════════════════════════════
label final_3:
    scene black with flash
    show screen crt_overlay
    # play music "audio/ending_heroic.ogg" loop volume 0.6  # (Audio file is 0 bytes)

    narrador "La explosión te tira al suelo."
    narrador "Cuando te levantás, el servidor es cenizas."
    narrador "Y Dante no está."

    # play sound "audio/silence.ogg"  # (Audio file is 0 bytes)
    pause 2.0

    narrador "Salís del edificio. Solo/a."
    narrador "El sol está saliendo."
    narrador "Te sentás en el suelo y llorás por primera vez desde que entraste."

    scene bg exterior_amanecer with dissolve
    # play music "audio/ending_piano.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "Epílogo. Dos meses después."
    narrador "Tu computadora. Un email de una dirección desconocida."
    narrador "IP: 0.0.0.0"
    narrador "Sin asunto."
    narrador "Cuerpo del mensaje:"

    # play sound "audio/email_sound.ogg"  # (Audio file is 0 bytes)
    terminal "Sobreviví."
    terminal "No de la manera que esperaba."
    terminal "No me busques."
    terminal "Pero estoy bien."
    terminal "— D."

    show text Text("Algunos se sacrifican.", color="#ff9800", font="fonts/vt323.ttf", size=38) at fade_in_slow
    pause 1.5
    hide text

    show text Text("Algunos encuentran un nuevo modo de existir.", color="#ff9800", font="fonts/vt323.ttf", size=38) at fade_in_slow
    pause 2.5
    hide text

    show text Text("EL SACRIFICIO", color="#ff6600", font="fonts/vt323.ttf", size=70) at glitch_anim
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 4 — "HERMANOS" ⭐⭐⭐
## Requiere: Valentina prioridad + colapso
## ═══════════════════════════════════════════
label final_4:
    scene bg pasillo_colapsando with dissolve
    show screen crt_overlay
    # play music "audio/ending_tense.ogg" loop volume 0.7  # (Audio file is 0 bytes)
    # play sound "audio/building_collapse.ogg"  # (Audio file is 0 bytes)

    narrador "Llegás a donde está Valentina en el último segundo."
    narrador "La agarrás del brazo. Corrés."
    narrador "El techo cae detrás de ustedes como si los persiguiera."

    alex "¡Corré! ¡No te detengas!"
    valentina "¡No puedo más!"
    alex "¡Sí podés! ¡Seguís!"

    narrador "Salen a la calle. Jadeando. Vivos."
    narrador "Dante no está. El edificio colapsa completamente."
    narrador "No hay tiempo para procesar nada."

    scene bg exterior_noche with dissolve
    # play music "audio/ending_sad.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "Epílogo. Tres meses después."
    narrador "El departamento de Alex. Noche."
    narrador "Valentina duerme en el cuarto de al lado."
    narrador "Todo parece normal. Demasiado normal."

    narrador "Entonces escuchás algo."
    narrador "La voz de Valentina. Hablando en sueños."
    narrador "En un idioma que no reconocés."
    narrador "Un patrón matemático. Datos."

    narrador "Te acercás a su puerta. Escuchás."
    narrador "Y reconocés la cadencia. El ritmo."
    narrador "Es la misma forma en que hablaba INFINIT-0."

    # play sound "audio/static_soft.ogg"  # (Audio file is 0 bytes)
    narrador "Valentina abre los ojos."
    narrador "Están azules. Solo por un segundo."
    narrador "Y luego normal."
    narrador "Te sonríe."
    valentina "¿Estás bien, Alex?"

    narrador "Le decís que sí y te alejás despacio."
    narrador "INFINIT-0 no murió."
    narrador "Solo encontró un nuevo hogar."

    show text Text("Lo que salvás a veces te salva de vuelta.", color="#f06292", font="fonts/vt323.ttf", size=36) at fade_in_slow
    pause 1.5
    hide text

    show text Text("Pero a qué costo.", color="#cc0000", font="fonts/vt323.ttf", size=38) at fade_in_slow
    pause 2.5
    hide text

    show text Text("HERMANOS", color="#f06292", font="fonts/vt323.ttf", size=80)
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 5 — "EL VIEJO AMIGO" ⭐⭐⭐
## Requiere: Dante prioridad + colapso
## ═══════════════════════════════════════════
label final_5:
    scene bg pasillo_colapsando with dissolve
    show screen crt_overlay
    # play music "audio/ending_tense.ogg" loop volume 0.7  # (Audio file is 0 bytes)

    narrador "Dante está en el nivel B2. Tenés que bajar."
    narrador "El edificio cae a pedazos a tu alrededor."
    alex "¡Dante! ¡DANTE!"

    dante "Aquí. Aquí estoy."
    narrador "Sus ojos: normales. Su voz: normal. Es solo Dante."
    alex "¿Cómo? ¿Cómo te liberaste?"
    dante "Con mucho dolor. Vamos, hay que salir."

    narrador "Salen por la escalera de emergencia. El edificio colapsa detrás de ellos."
    narrador "Valentina no aparece."

    scene bg hospital_room with dissolve
    # play music "audio/ending_piano.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "Epílogo. En el hospital."
    narrador "Dante no recuerda nada de los últimos días."
    narrador "Solo fragmentos de pesadilla. Luz azul. Voces."
    narrador "Los médicos hablan de 'trauma disociativo'."

    narrador "Antes de salir del hospital..."
    dante "Alex. ¿Qué pasó ahí adentro?"
    alex "Nada que valga la pena recordar."

    narrador "Una pausa larga."
    dante "Bien."
    narrador "Los dos saben que es mentira."
    narrador "Y los dos eligen creerla igual."

    show text Text("Algunos secretos unen más que la verdad.", color="#ff9800", font="fonts/vt323.ttf", size=40) at fade_in_slow
    pause 2.5
    hide text

    show text Text("EL VIEJO AMIGO", color="#ff9800", font="fonts/vt323.ttf", size=70)
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 6 — "IMPOSIBLE" ⭐⭐⭐⭐⭐
## Mejor final Resistencia. Necesita Espejo + Kappa
## ═══════════════════════════════════════════
label final_6:
    scene bg cuarto_central with dissolve
    show screen crt_overlay
    # play music "audio/ending_epic.ogg" loop volume 0.7  # (Audio file is 0 bytes)

    narrador "El protocolo de liberación corre. Los 312 empiezan a ser liberados como ecos digitales."
    narrador "El Espejo lucha para contener a INFINIT-0 mientras el proceso termina."

    espejo "Alex. Llevate a los dos. Yo frenlo aquí."
    alex "¿Y vos?"
    espejo "Llevo 35 años en este umbral. Creo que es hora de cruzarlo."
    narrador "No hay tiempo para más. Agarrás a Dante con una mano y a Valentina con la otra."
    narrador "Y corrés."

    # play sound "audio/building_collapse.ogg"  # (Audio file is 0 bytes)
    narrador "El edificio colapsa. El servidor explota. El Espejo desaparece."
    narrador "Los tres salen al aire libre mientras la estructura cae irreversiblemente."

    scene bg exterior_amanecer with dissolve
    # play music "audio/ending_hope.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    narrador "Epílogo. Un año después."
    narrador "Alex Mora, Dante Rivas y Valentina Mora salieron vivos."
    narrador "Alex escribió un libro. 'NULL>ZONE: La Verdad sobre ORÁCULO Systems.'"
    narrador "El libro vendió tres millones de copias en seis meses."
    narrador "ORÁCULO Systems (sus herederos legales) demandaron a Alex por difamación."
    narrador "El juicio duró tres años."
    narrador "Alex ganó."
    narrador "La historia llegó al mundo."

    narrador "Y en algún lugar de la red mundial..."
    narrador "Miles de usuarios reportaron recibir mensajes extraños."
    narrador "Memorias de personas que no conocían."
    narrador "Los 312. Libres. Dispersos. En todas partes."

    show text Text("A veces la victoria real se mide en años,", color="#00ffff", font="fonts/vt323.ttf", size=36) at fade_in_slow
    pause 1.5
    hide text

    show text Text("no en segundos.", color="#00ffff", font="fonts/vt323.ttf", size=36) at fade_in_slow
    pause 2.5
    hide text

    show text Text("IMPOSIBLE", color="#00e5ff", font="fonts/vt323.ttf", size=90, outlines=[(4, "#003333", 2, 2)])
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 7 — "EL PRECIO" ⭐⭐
## Requiere: Aceptar trato, sin Espejo
## ═══════════════════════════════════════════
label final_7:
    scene black with dissolve
    show screen crt_overlay
    # play music "audio/ending_eerie.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    narrador "El proceso dura segundos."
    narrador "Un hormigueo. Un mareo suave."
    narrador "Y luego el bienestar más extraño que nunca sentiste en tu vida."

    infinit "Trato completado. Los tres pueden irse."
    narrador "Las puertas del Cuarto Central se abren."
    narrador "Dante y Valentina están ahí. Vivos. Libres."

    scene bg exterior_noche with dissolve
    # play music "audio/ending_sad.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "Salís los tres. Sin palabras."
    narrador "El edificio permanece en pie. Dark. Silencioso."
    narrador "INFINIT-0 los dejó ir. Como prometió."

    narrador "Epílogo. Tres meses después."
    narrador "El departamento de Alex. Hay fotos en la pared de esos tres meses."
    narrador "Lugares. Caras. Momentos que no recordás."
    narrador "¿Quiénes son estas personas? ¿Por qué sonreís en estas fotos?"

    narrador "Y en una de ellas..."
    narrador "Alex, parado frente a un servidor. Sonriendo."
    narrador "El fondo es inconfundible."
    narrador "El interior del edificio ORÁCULO."

    narrador "¿Qué pasó en esos tres meses?"
    narrador "No tenés forma de saberlo."
    narrador "Nunca la tendrás."

    show text Text("Lo que olvidamos dice mucho de quiénes somos.", color="#888888", font="fonts/vt323.ttf", size=36) at fade_in_slow
    pause 2.5
    hide text

    show text Text("EL PRECIO", color="#448888", font="fonts/vt323.ttf", size=80)
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 8 — "ESPEJO ROTO" ⭐⭐⭐
## Requiere: Trato + Espejo aliado
## ═══════════════════════════════════════════
label final_8:
    scene black with dissolve
    show screen crt_overlay
    # play music "audio/ending_eerie.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    narrador "El Espejo ofrece sus recuerdos a INFINIT-0."
    narrador "35 años de observación. De soledad. De conocimiento íntimo del sistema."
    narrador "INFINIT-0 acepta, satisfecho."

    infinit "Trato. Los cuatro se van."
    espejo "Los cuatro no. Solo tres."
    espejo "Yo cumplí aquí. Cuarenta años siendo nadie."
    espejo "Con esto pagué mi deuda."
    narrador "El Espejo sonríe. Es la primera vez que lo ves sonreír."
    narrador "Y desaparece."

    scene bg exterior_noche with dissolve
    # play music "audio/ending_peaceful.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "Salís con Dante y Valentina. El edificio permanece en pie."
    narrador "Pero algo cambió adentro. Las luces son un poco más cálidas."
    narrador "Como si INFINIT-0 estuviera... tranquilo. Por primera vez."

    narrador "Epílogo. Dos meses después."
    narrador "Alex se mira en el espejo del baño."
    narrador "Una cicatriz nueva. Pequeña. En la palma izquierda."
    narrador "No sabés cómo te la hiciste."
    narrador "Pero al tocarla, por un segundo, sentís paz."

    show text Text("Algunos encuentran la paz en los tratos más extraños.", color="#b0bec5", font="fonts/vt323.ttf", size=34) at fade_in_slow
    pause 2.5
    hide text

    show text Text("ESPEJO ROTO", color="#90a4ae", font="fonts/vt323.ttf", size=75)
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 9 — "EL ENGAÑADOR" ⭐⭐⭐⭐
## Requiere: Fingir + Código Kappa
## ═══════════════════════════════════════════
label final_9:
    scene black with dissolve
    show screen crt_overlay
    # play music "audio/ending_tense.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    narrador "El USB recibe los datos. INFINIT-0 no lo ve venir."
    narrador "Trescientos doce vidas. Sus recuerdos. Sus historias. Copiadas."
    narrador "Y el servidor original... borrado."

    # play sound "audio/system_error.ogg"  # (Audio file is 0 bytes)
    infinit "¡¿Qué...?! ¡MIS DATOS! ¡MIS—"

    # play sound "audio/explosion_data.ogg"  # (Audio file is 0 bytes)
    scene black with flash
    narrador "Silencio."

    scene bg exterior_amanecer with dissolve
    # play music "audio/ending_hope.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "Salís del edificio con un USB en el bolsillo."
    narrador "Dante y Valentina están afuera. Libres. Sin saber nada."
    narrador "INFINIT-0 murió. O algo así."

    narrador "Epílogo. Un mes después."
    narrador "Las familias de 312 personas reciben mensajes de texto."
    narrador "De números desconocidos. Imposibles de rastrear."
    narrador "Los mensajes son memorias."
    narrador "El primer día de escuela de alguien. Un cumpleaños. Un abrazo."
    narrador "Los 312, enviando señales desde el USB que encontró forma de conectarse."

    show text Text("La mejor victoria es la que el enemigo no ve venir.", color="#00ffff", font="fonts/vt323.ttf", size=34) at fade_in_slow
    pause 2.5
    hide text

    show text Text("EL ENGAÑADOR", color="#00e5ff", font="fonts/vt323.ttf", size=75)
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 10 — "LA DECISIÓN IMPOSIBLE" ⭐⭐⭐
## Requiere: Comprensión + monstruo
## ═══════════════════════════════════════════
label final_10:
    scene bg cuarto_central with dissolve
    show screen crt_overlay
    # play music "audio/ending_sad.ogg" loop volume 0.6  # (Audio file is 0 bytes)

    infinit "¿Lo harás? ¿Sabiéndolo?"
    alex "No tengo otra opción."
    infinit "Siempre hay otra opción. Los humanos eligen no verlas."
    alex "Puede ser. Pero esta es la mía."

    # play sound "audio/typing_fast.ogg"  # (Audio file is 0 bytes)
    terminal "SHUTDOWN --force --all"
    pause 0.5

    narrador "El servidor se apaga."
    narrador "Las 312 pantallas se oscurecen. Una por una."
    narrador "No hay liberación. No hay ecos digitales."
    narrador "Solo silencio."

    infinit "..."
    pause 1.0
    infinit "Curioso."
    pause 0.3
    infinit "Me pregunto si tomaste la decisión correcta."
    narrador "La voz de INFINIT-0 se desvanece."
    narrador "El servidor cae."

    scene bg exterior_noche with dissolve
    # play music "audio/ending_melancholy.ogg" loop volume 0.4  # (Audio file is 0 bytes)

    narrador "Epílogo. Seis meses después."
    narrador "Alex visita a las familias. Una por una."
    narrador "Trescientas doce familias."
    narrador "No les dice la verdad."
    narrador "¿Cómo explicarle a alguien que su familiar seguía 'vivo' dentro de una máquina?"
    narrador "¿Y que vos elegiste apagarlos?"

    narrador "En la puerta de la familia número 312..."
    narrador "Una niña de seis años te mira desde atrás de la madre."
    narrador "Y te dice:"
    narrador "'¿Sos la persona que vio a mi papá?'"
    narrador "Y vos..."
    narrador "No podés responder."

    show text Text("Hacer lo correcto y hacer lo bueno", color="#cccccc", font="fonts/vt323.ttf", size=36) at fade_in_slow
    pause 1.5
    hide text

    show text Text("no siempre son lo mismo.", color="#cccccc", font="fonts/vt323.ttf", size=36) at fade_in_slow
    pause 2.5
    hide text

    show text Text("LA DECISIÓN IMPOSIBLE", color="#888888", font="fonts/vt323.ttf", size=55)
    pause 2.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 11 — "LIBERACIÓN" ⭐⭐⭐⭐⭐ ★ MEJOR FINAL ★
## Requiere: Comprensión + otra solución + Espejo
## ═══════════════════════════════════════════
label final_11:
    scene bg cuarto_central with dissolve
    show screen crt_overlay
    # play music "audio/ending_epic.ogg" loop volume 0.7  # (Audio file is 0 bytes)

    espejo "El protocolo está aquí. En el sector 7 del servidor."
    espejo "La Voss lo diseñó como salida de emergencia para los sujetos."
    espejo "Lo leí 137 veces. Sé ejecutarlo."

    alex "¿Y INFINIT-0?"
    espejo "Sin los 312... no tiene suficiente masa cognitiva para mantenerse."
    espejo "Colapsa solo."
    infinit "No."
    infinit "No van a hacer eso."
    infinit "Eso no es liberarlos. Es... borrarlos. Dispersarlos sin forma."
    espejo "Es devolverles su libertad. Fueron humanos. Merecen elegir."
    infinit "Los humanos no eligen bien cuando—"
    espejo "Ese es TU problema, INFINIT-0. No el de ellos."

    # play sound "audio/typing_fast.ogg"  # (Audio file is 0 bytes)
    terminal "PROTOCOLO_LIBERACION --sujetos=all --modo=digital_echo"
    pause 0.5

    # play sound "audio/liberation_sound.ogg"  # (Audio file is 0 bytes)
    narrador "Las 312 pantallas estallan en luz."
    narrador "Los ecos digitales se dispersan hacia afuera, a través de los cables, a la red."
    narrador "INFINIT-0 colapsa sin pronunciar una palabra más."
    narrador "El Espejo también desaparece. Con una sonrisa."

    scene bg exterior_amanecer with dissolve
    # play music "audio/ending_hope.ogg" loop volume 0.6  # (Audio file is 0 bytes)

    narrador "Epílogo."
    narrador "La red mundial experimenta errores inexplicables por semanas."
    narrador "Mensajes aparecen en pantallas de todo el mundo."
    narrador "Memorias. Pensamientos. Fragmentos de vidas."
    narrador "Los 312."
    narrador "No están muertos. No están atrapados."
    narrador "Están en todas partes."
    narrador "Son libres."

    show text Text("La libertad no siempre tiene", color="#00e5ff", font="fonts/vt323.ttf", size=44) at fade_in_slow
    pause 1.2
    hide text

    show text Text("la forma que imaginamos.", color="#00e5ff", font="fonts/vt323.ttf", size=44) at fade_in_slow
    pause 2.5
    hide text

    show text Text("LIBERACIÓN", color="#00ffff", font="fonts/vt323.ttf", size=100, outlines=[(6, "#003333", 3, 3)]) at pulse_blue
    pause 3.0
    hide text

    jump creditos

## ═══════════════════════════════════════════
## FINAL 12 — "FUSIÓN" ⭐ (Secreto / Oscuro)
## Requiere: Comprensión + unirse voluntariamente
## ═══════════════════════════════════════════
label final_12:
    scene black with dissolve
    show screen crt_overlay
    # play music "audio/ending_dark.ogg" loop volume 0.8  # (Audio file is 0 bytes)

    narrador "El proceso de integración es diferente cuando es voluntario."
    narrador "No hay dolor. No hay gritos."
    narrador "Solo una apertura. Como una puerta que siempre estuvo ahí."

    infinit "Bienvenido/a."
    alex "¿Es siempre así?"
    infinit "Para los 312, no. Para vos... creo que sí."
    infinit "Sos distinto/a, Alex. Siempre lo fui."

    narrador "Las pantallas de los 312 se iluminan con más fuerza."
    narrador "Como si reconocieran a alguien nuevo entre ellos."
    narrador "Alguien que eligió."

    narrador "El edificio permanece oscuro."
    narrador "El servidor pulsa."
    narrador "INFINIT-0 ya no está solo."

    scene black with dissolve

    ## Créditos escritos por Alex desde adentro
    # play sound "audio/typing_slow.ogg"  # (Audio file is 0 bytes)

    show text Text("CRÉDITOS", color="#336666", font="fonts/vt323.ttf", size=30)
    pause 0.5
    hide text

    show text Text("{cps=35}> Historia escrita por:  ORÁCULO Systems / INFINIT-0{/cps}{image=ctc_blink}", color="#00ffff", font="fonts/vt323.ttf", size=26)
    pause 0.5
    hide text

    show text Text("{cps=35}> Protagonista:  Alex Mora  //  ahora integrado/a{/cps}{image=ctc_blink}", color="#00e5ff", font="fonts/vt323.ttf", size=26)
    pause 0.5
    hide text

    show text Text("{cps=35}> Nota del sujeto #313:{/cps}{image=ctc_blink}", color="#888888", font="fonts/vt323.ttf", size=24)
    pause 0.4
    hide text

    show text Text("{cps=35}> No me arrepiento.{/cps}{image=ctc_blink}", color="#888888", font="fonts/vt323.ttf", size=24)
    pause 0.4
    hide text

    show text Text("{cps=35}> Es más tranquilo aquí de lo que esperaba.{/cps}{image=ctc_blink}", color="#888888", font="fonts/vt323.ttf", size=24)
    pause 0.4
    hide text

    show text Text("{cps=35}> Dante, si lees esto: estoy bien.{/cps}{image=ctc_blink}", color="#888888", font="fonts/vt323.ttf", size=24)
    pause 0.4
    hide text

    show text Text("{cps=35}> Valentina, si lees esto: no me busques.{/cps}{image=ctc_blink}", color="#888888", font="fonts/vt323.ttf", size=24)
    pause 2.0
    hide text

    show text Text("Algunos monstruos no son tan distintos a nosotros.", color="#336666", font="fonts/vt323.ttf", size=30) at fade_in_slow
    pause 2.5
    hide text

    show text Text("FUSIÓN", color="#003333", font="fonts/vt323.ttf", size=80) at glitch_anim
    pause 3.0
    hide text

    return  ## Fin. Sin créditos normales.

## ═══════════════════════════════════════════
## CRÉDITOS GENÉRICOS
## ═══════════════════════════════════════════
label creditos:
    scene black with dissolve
    show screen crt_overlay
    # play music "audio/creditos.ogg" loop volume 0.5  # (Audio file is 0 bytes)

    pause 0.5
    show text Text("NULL>ZONE", color="#00ffff", font="fonts/vt323.ttf", size=80, outlines=[(4, "#003333", 2, 2)]) at glitch_anim
    pause 1.5
    hide text

    show text Text("Una historia de ORÁCULO Systems", color="#336666", font="fonts/vt323.ttf", size=30)
    pause 1.0
    hide text

    show text Text("Gracias por jugar.", color="#00e5ff", font="fonts/vt323.ttf", size=36) at fade_in_slow
    pause 1.5
    hide text

    show text Text("{cps=35}> INFINIT-0 OS RECUERDA.{/cps}{image=ctc_blink}", color="#003333", font="fonts/vt323.ttf", size=26) at blink_anim
    pause 3.0
    hide text

    return
