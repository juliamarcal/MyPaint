import menu_utils

def start_transformations(menu, canvas):
    print("Aplicando transformações")
    create_transformations_menu(menu, canvas)
    
    
def create_transformations_menu(menu, canvas):
    menu_utils.clear_menu(menu)
    menu_utils.add_button_to_menu(menu, "Cancelar", lambda: menu_utils.draw_default_menu(menu, canvas), "red")