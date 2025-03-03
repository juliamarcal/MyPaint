import utils

def draw_line(canvas, menu):
    print("Desenhando uma reta")
    create_line_menu(menu)
    
def create_line_menu(menu):
    print("Desenhando uma reta")

    buttons = [
        {"text": "Selecione o ponto inicial", "command": lambda: print("Definir Ponto Inicial")},
        {"text": "Selecione o ponto final", "command": lambda: print("Definir Ponto Final")},
        {"text": "Selecione a cor", "command": lambda: print("cor")},
        {"text": "Desenhar reta", "command": lambda: print("Desenhando Reta")},
        {"text": "Cancelar", "command": lambda: print("Cancelar")}
    ]
    utils.add_buttons_to_menu(menu, buttons)