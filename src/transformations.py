import math
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
            "Rotação": self.draw_rotation_menu,
            "Reflexão": self.draw_reflection_menu,
            "Cisalhamento": self.draw_shearing_menu
        }
        
        # variables for transformations
        self.slider1_value = 0
        self.slider2_value = 0
        self.dropdown1_value = 0
        
    def update_dropdown_value(self, eixo):
        """Atualiza a translação no eixo selecionado e no valor do slider."""
        print(f"Eixo selecionado: {eixo}")
        self.dropdown1_value = eixo

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
        self.update_dropdown_value("Eixo X")

        menu_utils.add_dropdown_to_menu(
            self.menu,
            ["Translação", "Escala", "Rotação", "Reflexão", "Cisalhamento"],
            self.draw_transformation_menu,
            defaut_value= transformation_name
        )

        if transformation_name in self.transformation_menus:
            self.transformation_menus[transformation_name]()
        
        menu_utils.add_button_to_menu(self.menu, "Voltar", lambda: self.leave_transformations(), "red")

    # translation  OKAY
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

    # scaling OKAY
    def draw_scaling_menu(self):
        menu_utils.add_slider_to_menu(self.menu, "escala em x", -50, 50, lambda  valor: self.update_slider_value(valor, "slider1"), initial=0)
        menu_utils.add_slider_to_menu(self.menu, "escala em y", -50, 50, lambda  valor: self.update_slider_value(valor, "slider2"), initial=0)
        menu_utils.add_button_to_menu(self.menu, "Aplicar escala", lambda: self.apply_scaling(), "#6495ED")
    
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

    # rotation OKAY
    def draw_rotation_menu(self):
        menu_utils.add_slider_to_menu(self.menu, "Rotação em graus", -180, 180, lambda  valor: self.update_slider_value(valor, "slider1"), initial=0)
        menu_utils.add_button_to_menu(self.menu, "Aplicar rotação", lambda: self.apply_rotation(), "#6495ED")

    def apply_rotation(self):
        """Applies rotation to stored lines using slider1_value (angle in degrees)."""
        print(f"Applying rotation: {self.slider1_value} degrees")

        radians = math.radians(self.slider1_value) # Convert degrees to radians

        canvas_utils.clear_canvas(self.canvas)
        lines = self.line_drawer.get_stored_lines()

        for line in lines:
            # Step 1: Find center of the line segment
            center_x = (line.x1 + line.x2) / 2
            center_y = (line.y1 + line.y2) / 2

            # Step 2: Translate points to the origin (subtract center)
            x1_rel, y1_rel = line.x1 - center_x, line.y1 - center_y
            x2_rel, y2_rel = line.x2 - center_x, line.y2 - center_y

            # Step 3: Rotate around the origin
            x1_rot = x1_rel * math.cos(radians) - y1_rel * math.sin(radians)
            y1_rot = x1_rel * math.sin(radians) + y1_rel * math.cos(radians)

            x2_rot = x2_rel * math.cos(radians) - y2_rel * math.sin(radians)
            y2_rot = x2_rel * math.sin(radians) + y2_rel * math.cos(radians)

            # Step 4: Translate points back to original center
            line.x1, line.y1 = int(round(x1_rot + center_x)), int(round(y1_rot + center_y))
            line.x2, line.y2 = int(round(x2_rot + center_x)), int(round(y2_rot + center_y))

        self.line_drawer.set_stored_lines(lines)
        self.circle_drawer.redraw_all_circles()

    # reflection OKAY
    def draw_reflection_menu(self):
        menu_utils.add_dropdown_to_menu(self.menu, ["Eixo X", "Eixo Y"], lambda value: self.update_dropdown_value(value))
        menu_utils.add_button_to_menu(self.menu, "Aplicar reflexão", lambda: self.apply_reflexion(), "#6495ED")

    def apply_reflexion(self):
        canvas_utils.clear_canvas(self.canvas)
        lines = self.line_drawer.get_stored_lines()
        circles = self.circle_drawer.get_stored_circles()
        
        if self.dropdown1_value == "Eixo X":
            for circle in circles:
                circle.yc = -1 * circle.yc

            for line in lines:
                line.y1 = -1 * line.y1
                line.y2 = -1 * line.y2
            
        elif self.dropdown1_value == "Eixo Y":
            for circle in circles:
                circle.xc = -1 * circle.xc
            
            for line in lines:
                line.x1 = -1 * line.x1
                line.x2 = -1 * line.x2

        self.circle_drawer.set_stored_circles(circles)
        self.line_drawer.set_stored_lines(lines)

    # shearing
    def draw_shearing_menu(self):
        menu_utils.add_dropdown_to_menu(self.menu, ["Eixo X", "Eixo Y"], lambda value: self.update_dropdown_value(value))
        menu_utils.add_slider_to_menu(self.menu, "Deformaçaõ (em pixels)", -2.0, 2.0, lambda  valor: self.update_slider_value(valor, "slider1"), initial=0)
        menu_utils.add_button_to_menu(self.menu, "Aplicar cisilhamento", lambda: self.apply_shearing(), "#6495ED")
    
    def apply_shearing(self):
        canvas_utils.clear_canvas(self.canvas)
        lines = self.line_drawer.get_stored_lines()

        shear_factor = float(self.slider1_value)

        if self.dropdown1_value == "Eixo X":
            for line in lines:
                line.x1 += int(round(shear_factor * line.y1))
                line.x2 += int(round(shear_factor * line.y2))

        elif self.dropdown1_value == "Eixo Y":
            for line in lines:
                line.y1 += int(round(shear_factor * line.x1))
                line.y2 += int(round(shear_factor * line.x2))

        self.line_drawer.set_stored_lines(lines)
        self.circle_drawer.redraw_all_circles()