## =============================================
## NULL>ZONE — options.rpy
## =============================================

define config.name = "NULL>ZONE"
define config.version = "1.0.0"
define gui.show_name = True

define config.save_directory = "null_zone-1.0"

define config.window_icon = None
define config.main_menu_music = "audio/ambient_menu.ogg"

## Pantalla de inicio
define config.start_callbacks = []

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
define preferences.text_cps = 40

## Sin skip por defecto en diálogo no leído
define preferences.skip_unseen = False

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
