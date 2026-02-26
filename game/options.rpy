## =============================================
## NULL>ZONE — options.rpy
## =============================================

define config.name = "NULL>ZONE"
define config.version = "1.0.0"
define gui.show_name = True

define config.save_directory = "null_zone-1.0"

define config.window_icon = None
# define config.main_menu_music = "audio/ambient_menu.ogg"  # Deshabilitado por ahora porque pesa 0 bytes

## ─────────────────────────────────────────────
## DEFINICIONES DE IMÁGENES (BACKGROUNDS)
## ─────────────────────────────────────────────
image bg cuarto_central = Transform("images/bg/cuarto_central.png", size=(1920, 1080))
image bg entrada_orculo = Transform("images/bg/entrada_orculo.png", size=(1920, 1080))
image bg escalera_bajando = Transform("images/bg/escalera_bajando.png", size=(1920, 1080))
image bg exterior_amanecer = Transform("images/bg/exterior_amanecer.png", size=(1920, 1080))
image bg exterior_noche = Transform("images/bg/exterior_noche.png", size=(1920, 1080))
image bg exterior_orculo = Transform("images/bg/exterior_orculo.png", size=(1920, 1080))
image bg hospital_room = Transform("images/bg/hospital_room.png", size=(1920, 1080))
image bg menu_bg = Transform("images/bg/menu_bg.png", size=(1920, 1080))
image bg pasillo_colapsando = Transform("images/bg/pasillo_colapsando.png", size=(1920, 1080))
image bg pasillo_largo = Transform("images/bg/pasillo_largo.png", size=(1920, 1080))
image bg pasillo_monitores = Transform("images/bg/pasillo_monitores.png", size=(1920, 1080))
image bg pasillo_oscuro = Transform("images/bg/pasillo_oscuro.png", size=(1920, 1080))
image bg puerta_central = Transform("images/bg/puerta_central.png", size=(1920, 1080))
image bg sala_archivos = Transform("images/bg/sala_archivos.png", size=(1920, 1080))
image bg sala_espejos = Transform("images/bg/sala_espejos.png", size=(1920, 1080))
image bg sala_servidores = Transform("images/bg/sala_servidores.png", size=(1920, 1080))
# La vieja imagen se omite porque bg sala_terminal ahora es un bloque ATL dinámico en script.rpy

## Pantalla de inicio y Menú In-Game
define config.start_callbacks = []
define config.game_menu = "preferences"

## Resolución
define config.screen_width = 1920
define config.screen_height = 1080

## Frame rate
define config.framerate = 60

## Modo ventana por defecto
define config.default_fullscreen = False

## Auto-guardado
define config.autosave_slots = 6
define config.quicksave_slots = 1

## Palabras por minuto por defecto (lento para atmósfera)
default preferences.text_cps = 40

## Sin skip por defecto en diálogo no leído
default preferences.skip_unseen = False

## Transiciones
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.end_splash_transition = dissolve

## Guardado
define config.has_autosave = True
define config.has_quicksave = True

## Voice
define config.has_voice = False
