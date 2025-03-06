import menu_utils

def start_clipping(menu, canvas):
    print("Aplicando recorte")
    create_clipping_menu(menu, canvas)
    
def create_clipping_menu(menu, canvas):
    menu_utils.clear_menu(menu)
    menu_utils.add_button_to_menu(menu, "Cancelar", lambda: menu_utils.draw_default_menu(menu, canvas), "red")