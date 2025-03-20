import math
import menu_utils
import canvas_utils

class Transformations:
    """
    A class to handle various 2D geometric transformations including translation, scaling,
    rotation, reflection, and shearing on a canvas.
    """
    def __init__(self, line_drawer, circle_drawer, canvas, menu):
        """
        Initializes the Transformations class with drawing utilities and menu elements.
        
        :param line_drawer: Object responsible for drawing and managing lines.
        :param circle_drawer: Object responsible for drawing and managing circles.
        :param canvas: The canvas object where transformations are applied.
        :param menu: The menu object used to interact with transformations.
        """
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
    
    def start_transformations(self):
        """Begins the transformation process by displaying the default menu (Translation)."""
        self.draw_transformation_menu("Translação")
    
    def draw_transformation_menu(self, transformation_name):
        """
        Clears the menu and displays the options for the selected transformation.
        
        :param transformation_name: The name of the transformation to be applied.
        """
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
    
    def leave_transformations(self):
        """Resets transformation values and returns to the default menu."""
        self.slider1_value = 0
        self.slider2_value = 0
        self.dropdown1_value = 0
        menu_utils.draw_default_menu(self.menu, self.canvas)

    # dinamic updates
    def update_dropdown_value(self, eixo):
        """Updates the selected axis for transformations."""
        self.dropdown1_value = eixo

    def update_slider_value(self, value, slider_id):
        """
        Updates the value of the specified slider.
        
        :param value: The new value for the slider.
        :param slider_id: Identifier of the slider ('slider1' or 'slider2').
        """
        if slider_id == "slider1":
            self.slider1_value = int(value)
        elif slider_id == "slider2":
            self.slider2_value = int(value)

    # translation
    def draw_translation_menu(self):
        """Displays the translation menu options in the UI."""
        menu_utils.add_slider_to_menu(self.menu, "Translação em x (em pixels)", -100, 100, lambda  valor: self.update_slider_value(valor, "slider1"), initial=0)
        menu_utils.add_slider_to_menu(self.menu, "Translação em y (em pixels)", -100, 100, lambda  valor: self.update_slider_value(valor, "slider2"), initial=0)
        menu_utils.add_button_to_menu(self.menu, "Aplicar translação", lambda: self.apply_translation(), "#6495ED")
            
    def apply_translation(self):
        """Applies translation using the pixel values for x and y axes."""
        
        print(f"Applying translation T({self.slider1_value}, {self.slider2_value})")
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

    def do_translation_to_coord(self, tx, ty, lines, circles):
        """Applies translation using the pixel values for x and y axes."""
        lines = self.line_drawer.get_stored_lines()
        circles = self.circle_drawer.get_stored_circles()
        
        for line in lines:
            line.x1 = line.x1 + tx
            line.y1 = line.y1 + ty
            line.x2 = line.x2 + tx
            line.y2 = line.y2 + ty
        
        for circle in circles:
            circle.xc = circle.xc + tx
            circle.yc = circle.yc + ty
            
        return lines, circles

    # scaling
    def draw_scaling_menu(self):
        """Displays the scaling menu options in the UI."""
        menu_utils.add_slider_to_menu(self.menu, "escala em x", -50, 50, lambda  valor: self.update_slider_value(valor, "slider1"), initial=1)
        menu_utils.add_slider_to_menu(self.menu, "escala em y", -50, 50, lambda  valor: self.update_slider_value(valor, "slider2"), initial=1)
        menu_utils.add_button_to_menu(self.menu, "Aplicar escala", lambda: self.apply_scaling(), "#6495ED")
    
    def apply_scaling(self):
        """Applies scaling transformation based on the slider values."""
        
        print(f"Applying scaling S({self.slider1_value}, {self.slider2_value})")

        canvas_utils.clear_canvas(self.canvas)
        lines = self.line_drawer.get_stored_lines()
        circles = self.circle_drawer.get_stored_circles()

        # Compute center of all shapes
        all_x = [line.x1 for line in lines] + [line.x2 for line in lines] + [circle.xc for circle in circles]
        all_y = [line.y1 for line in lines] + [line.y2 for line in lines] + [circle.yc for circle in circles]

        center_x = round(sum(all_x) / len(all_x)) if all_x else 0
        center_y = round(sum(all_y) / len(all_y)) if all_y else 0

        # Step 1: Translate shapes to (0,0)
        lines, circles = self.do_translation_to_coord(-center_x, -center_y, lines, circles)

        # Step 2: Apply Scaling
        for line in lines:
            line.x1 = round(line.x1 * self.slider1_value)
            line.y1 = round(line.y1 * self.slider2_value)
            line.x2 = round(line.x2 * self.slider1_value)
            line.y2 = round(line.y2 * self.slider2_value)

        for circle in circles:
            circle.xc = round(circle.xc * self.slider1_value)
            circle.yc = round(circle.yc * self.slider2_value)
            circle.radius = round(circle.radius * abs((self.slider1_value + self.slider2_value) / 2))  # Prevent negative radius

        # Step 3: Translate Back to Original Position
        lines, circles = self.do_translation_to_coord(center_x, center_y, lines, circles)

        # Ensure integer values before storing
        for line in lines:
            line.x1, line.y1, line.x2, line.y2 = map(int, (line.x1, line.y1, line.x2, line.y2))
        
        for circle in circles:
            circle.xc, circle.yc, circle.radius = map(int, (circle.xc, circle.yc, circle.radius))

        self.line_drawer.set_stored_lines(lines)
        self.circle_drawer.set_stored_circles(circles)

    # rotation
    def draw_rotation_menu(self):
        """Displays the rotation menu options in the UI."""
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

    # reflection
    def draw_reflection_menu(self):
        """Displays the reflection menu options in the UI."""
        menu_utils.add_dropdown_to_menu(self.menu, ["Eixo X", "Eixo Y"], lambda value: self.update_dropdown_value(value))
        menu_utils.add_button_to_menu(self.menu, "Aplicar reflexão", lambda: self.apply_reflexion(), "#6495ED")

    def apply_reflexion(self):
        """Applies reflection to stored lines and circles using dropdown1_value (axis)."""
        print(f"Applying reflexion on \"{self.dropdown1_value}\"")
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
        """Displays the shearing menu options in the UI."""
        menu_utils.add_dropdown_to_menu(self.menu, ["Eixo X", "Eixo Y"], lambda value: self.update_dropdown_value(value))
        menu_utils.add_slider_to_menu(self.menu, "Deformaçaõ (em pixels)", -2.0, 2.0, lambda  valor: self.update_slider_value(valor, "slider1"), initial=0)
        menu_utils.add_button_to_menu(self.menu, "Aplicar cisilhamento", lambda: self.apply_shearing(), "#6495ED")
    
    def apply_shearing(self):
        """Applies shearing to stored lines using dropdown1_value (axis) and slider1_value (deformation factor)."""

        print("Applying sheering in \"{self.dropdown1_value}\" whith deformation of factor {self.slider1_value}")
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
