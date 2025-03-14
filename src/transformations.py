import menu_utils
import canvas_utils
import lines
import circles

class Transformations:
    def __init__(self, line_drawer, circle_drawer, canvas, menu):
        self.line_drawer = line_drawer
        self.circle_drawer = circle_drawer
        self.canvas = canvas
        self.menu = menu
        self.transformation_menus = {
            "Translação": self.draw_translation_menu,
            "Escala": self.draw_scaling_menu,
            "Rotação": self.draw_rotacao_menu,
            "Reflexão": self.draw_reflexao_menu,
            "Cisalhamento": self.draw_cisalhamento_menu
        }
        
        # variables for transformations
        self.slider1_value = 0
        self.slider2_value = 0
        self.dropdown1_value = 0
        
    def update_dropdown_value(self, eixo):
        """Atualiza a translação no eixo selecionado e no valor do slider."""
        print(f"Eixo selecionado: {eixo}")  # Apenas para debug, pode ser removido
        self.slider1 = eixo

    def update_slider_value(self, value, slider_id):
        """Function that receives the value of the slider and the identifier of the slider, and updates the corresponding slider value."""
        if slider_id == "slider1":
            self.slider1_value = int(value)
            print(f"Slider 1 = {value}")
        elif slider_id == "slider2":
            self.slider2_value = int(value)
            print(f"Slider 2 = {value}")

    def start_transformations(self):
        print("Aplicando transformações")
        self.draw_transformation_menu("Translação")
    
    def leave_transformations(self):
        self.slider1_value = 0
        self.slider2_value = 0
        self.dropdown1_value = 0
        menu_utils.draw_default_menu(self.menu, self.canvas)
    
    def draw_transformation_menu(self, transformation_name):
        """Clears the menu, adds the dropdown, calls the specific transformation menu, and adds return button."""
        menu_utils.clear_menu(self.menu)
        
        self.slider1_value = 0
        self.slider2_value = 0
        self.dropdown1_value = 0

        menu_utils.add_dropdown_to_menu(
            self.menu,
            ["Translação", "Escala", "Rotação", "Reflexão", "Cisalhamento"],
            self.draw_transformation_menu,
            defaut_value= transformation_name
        )

        if transformation_name in self.transformation_menus:
            self.transformation_menus[transformation_name]()
        
        menu_utils.add_button_to_menu(self.menu, "Voltar", lambda: self.leave_transformations(), "red")

    # transalacao
    def draw_translation_menu(self):
        menu_utils.add_slider_to_menu(self.menu, "Translação em x (em pixels)", -100, 100, lambda  valor: self.update_slider_value(valor, "slider1"), initial=0)
        menu_utils.add_slider_to_menu(self.menu, "Translação em y (em pixels)", -100, 100, lambda  valor: self.update_slider_value(valor, "slider2"), initial=0)
        menu_utils.add_button_to_menu(self.menu, "Aplicar translação", lambda: self.apply_translation(), "#6495ED")
            
    def apply_translation(self):
        """Applies translation using the pixel values for x and y axis."""
        
        print("Applying translation")
        canvas_utils.clear_canvas(self.canvas)
        lines = self.line_drawer.get_stored_lines()
        circles = self.circle_drawer.get_stored_circles()
        
        for line in lines:
            line.x1 = line.x1 + self.slider1_value
            line.y1 = line.y1 + self.slider2_value
            line.x2 = line.x2 + self.slider1_value
            line.y2 = line.y2 + self.slider2_value
        
        for circle in circles:
            circle.xc = circle.xc + self.slider1_value
            circle.yc = circle.yc + self.slider2_value
            
        self.line_drawer.set_stored_lines(lines)
        self.circle_drawer.set_stored_circles(circles)

    # scaling
    def draw_scaling_menu(self):
        menu_utils.add_slider_to_menu(self.menu, "scaling em x", -50, 50, lambda  valor: self.update_slider_value(valor, "slider1"), initial=0)
        menu_utils.add_slider_to_menu(self.menu, "scaling em y", -50, 50, lambda  valor: self.update_slider_value(valor, "slider2"), initial=0)
        menu_utils.add_button_to_menu(self.menu, "Aplicar scaling", lambda: self.apply_scaling(), "#6495ED")
    
    def apply_scaling(self):
        """Applies scaling using the value for x and y"""
        print("Applying scaling")

        canvas_utils.clear_canvas(self.canvas)
        lines = self.line_drawer.get_stored_lines()
        circles = self.circle_drawer.get_stored_circles()
        
        center_x = 0
        center_y = 0
        
        print("\n=== Linhas antes da escala ===")
        for line in lines:
            print(f"Antes: ({line.x1}, {line.y1}) -> ({line.x2}, {line.y2})")

        for line in lines:
            line.x1 = (line.x1 - center_x) * self.slider1_value + center_x
            line.y1 = (line.y1 - center_y) * self.slider2_value + center_y
            line.x2 = (line.x2 - center_x) * self.slider1_value + center_x
            line.y2 = (line.y2 - center_y) * self.slider2_value + center_y

        print("\n=== Linhas depois da escala ===")
        for line in lines:
            print(f"Depois: ({line.x1}, {line.y1}) -> ({line.x2}, {line.y2})")

        print("\n=== Círculos antes da escala ===")
        for circle in circles:
            print(f"Antes: centro=({circle.xc}, {circle.yc}), raio={circle.radius}")

        for circle in circles:
            circle.xc = (circle.xc - center_x) * self.slider1_value + center_x
            circle.yc = (circle.yc - center_y) * self.slider2_value + center_y
            circle.radius *= abs(self.slider1_value) # radius must not be negative

        print("\n=== Círculos depois da escala ===")
        for circle in circles:
            print(f"Depois: centro=({circle.xc}, {circle.yc}), raio={circle.radius}")

        self.line_drawer.set_stored_lines(lines)
        self.circle_drawer.set_stored_circles(circles)

    # rotacao
    def draw_rotacao_menu(self):
        menu_utils.add_button_to_menu(self.menu, "Aplicar rotação", lambda: print("rotação"), "#6495ED")

    # reflexao
    def draw_reflexao_menu(self):
        menu_utils.add_dropdown_to_menu(self.menu, ["Eixo X", "Eixo Y"], lambda: print("sla"))
        menu_utils.add_button_to_menu(self.menu, "Aplicar reflexão", lambda: print("reflexão"), "#6495ED")

    # cisilhamento
    def draw_cisalhamento_menu(self):
        menu_utils.add_button_to_menu(self.menu, "Aplicar cisilhamento", lambda: print("cisilhamento"), "#6495ED")
