import utils

def draw_line(menu, canvas):
    create_line_menu(menu, canvas)
    
def create_line_menu(menu, canvas):
    buttons = [
        {"text": "Selecione o ponto inicial", "command": lambda: print("Definir Ponto Inicial"), "color": "#6495ED"},
        {"text": "Selecione o ponto final", "command": lambda: print("Definir Ponto Final"), "color": "#6495ED"},
        {"text": "cor", "command": lambda: print("cor"), "color": "black"},
        {"text": "Desenhar reta", "command": lambda: print("Desenhando Reta"), "color": "dark green"},
        {"text": "Cancelar", "command": lambda: utils.draw_default_menu(menu, canvas), "color": "red"}
    ]
    utils.clear_menu(menu)
    utils.add_buttons_to_menu(menu, buttons)