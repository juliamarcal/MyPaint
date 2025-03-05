import utils

def apply_transformations(menu, canvas):
    print("Aplicando transformações")
    create_transformations_menu(menu, canvas)
    
    
def create_transformations_menu(menu, canvas):
    buttons = [
        {"text": "...", "command": lambda: print("Definir Ponto Inicial"), "color": "#6495ED"},
        {"text": "...", "command": lambda: print("Definir Ponto Final"), "color": "#6495ED"},
        {"text": "Cancelar", "command": lambda: utils.draw_default_menu(menu, canvas), "color": "red"}
    ]
    utils.clear_menu(menu)
    utils.add_buttons_to_menu(menu, buttons)