## =============================================
## NULL>ZONE — gui.rpy
## Customización visual — estética CRT / terror
## =============================================

## Color de fondo general
define gui.accent_color = "#00ffff"
define gui.idle_color = "#006666"
define gui.idle_small_color = "#004444"
define gui.hover_color = "#00ffff"
define gui.selected_color = "#00ffff"
define gui.insensitive_color = "#333333"
define gui.muted_color = "#003333"
define gui.hover_muted_color = "#005555"
define gui.text_color = "#cccccc"
define gui.interface_text_color = "#cccccc"

## Fuente principal
define gui.default_font = "fonts/vt323.ttf"
define gui.interface_font = "fonts/vt323.ttf"
define gui.glyph_font = "DejaVuSans.ttf"

## Tamaños de texto
define gui.text_size = 30
define gui.name_text_size = 30
define gui.interface_text_size = 30
define gui.button_text_size = 30
define gui.label_text_size = 30
define gui.notify_text_size = 24
define gui.title_text_size = 70

## Cuadro de diálogo
define gui.textbox_height = 220
define gui.textbox_yalign = 1.0

define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.dialogue_xpos = 402
define gui.dialogue_width = 1116

## Menú de elecciones
define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = "fonts/vt323.ttf"
define gui.choice_button_text_size = 33
define gui.choice_button_text_color = "#00ffff"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_selected_idle_color = "#00ffff"
define gui.choice_button_text_selected_hover_color = "#ffffff"

## Barra de skip / notificaciones
define gui.bar_size = 38
define gui.bar_tile = False
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_size = 18
define gui.scrollbar_tile = False
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.vbar_size = 18
define gui.vbar_tile = False
define gui.vbar_borders = Borders(6, 6, 6, 6)

## Botones generales
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = "fonts/vt323.ttf"
define gui.button_text_size = 30
define gui.button_text_idle_color = gui.interface_text_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_idle_color = gui.selected_color
define gui.button_text_selected_hover_color = gui.hover_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Main menu
define gui.main_menu_background = "images/bg/menu_bg.png"
define gui.game_menu_background = "images/bg/menu_bg.png"

## Posicionamiento del textbox
define gui.textbox_xalign = 0.5
