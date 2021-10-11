import arcade

arcade.open_window(1000, 800, 'master sword')

arcade.set_background_color(arcade.csscolor.GREY)

arcade.start_render()

# Color variables
GOLD = 199, 164, 70
MASTER_SWORD_PURPLE = 20, 17, 99
BLADE_GRAY = 216, 223, 235


# Flower function
def draw_flower(x, y):
    """draws a flower
    idk how to get tilt angle"""
    arcade.draw_rectangle_filled(x, y, 10, 75, (168, 171, 82))
    arcade.draw_circle_filled(x, y + 40, 15, (230, 225, 195))


# pedestal

arcade.draw_rectangle_filled(500, 300, 200, 120, (115, 138, 105))
arcade.draw_rectangle_outline(500, 300, 200, 120, (93, 99, 24), 5)
arcade.draw_rectangle_filled(500, 300, 50, 30, (76, 87, 68))

# Blade
arcade.draw_rectangle_filled(500, 400, 35, 200, BLADE_GRAY)
arcade.draw_triangle_filled(500, 480, 525, 500, 475, 500, BLADE_GRAY)
arcade.draw_rectangle_filled(500, 517.5, 49, 35, BLADE_GRAY)
arcade.draw_triangle_filled(500, 555, 525, 535, 475, 535, BLADE_GRAY)
arcade.draw_rectangle_filled(500, 575, 30, 100, BLADE_GRAY)

# Blade-hilt intersection
arcade.draw_rectangle_filled(500, 600, 30, 60, MASTER_SWORD_PURPLE)
arcade.draw_ellipse_filled(500, 570, 22, 50, BLADE_GRAY)
arcade.draw_rectangle_filled(487, 570, 5, 5, GOLD)
arcade.draw_rectangle_filled(513, 570, 5, 5, GOLD)
arcade.draw_triangle_filled(500, 600, 505, 610, 495, 610, GOLD)
arcade.draw_triangle_filled(500, 620, 505, 610, 495, 610, GOLD)
arcade.draw_rectangle_filled(500, 599, 4, 10, GOLD)

# Wings
arcade.draw_polygon_filled(((485, 620),
                            (460, 630),
                            (455, 635),
                            (460, 625),
                            (465, 610),
                            (485, 600),
                            ),
                           MASTER_SWORD_PURPLE)
arcade.draw_polygon_filled(((515, 620),
                            (540, 630),
                            (545, 635),
                            (540, 625),
                            (535, 610),
                            (515, 600),
                            ),
                           MASTER_SWORD_PURPLE)
arcade.draw_arc_filled(470, 600, 60, 60, MASTER_SWORD_PURPLE, 20, 180, 90)
arcade.draw_rectangle_filled(460, 570, 30, 30, arcade.csscolor.GREY, 75)
arcade.draw_arc_filled(530, 600, 60, 60, MASTER_SWORD_PURPLE, 0, 163, 270)
arcade.draw_rectangle_filled(540, 570, 30, 30, arcade.csscolor.GREY, 285)

# beginning of handle
arcade.draw_arc_filled(485, 620, 13, 8, arcade.csscolor.GREY, 0, 150)
arcade.draw_arc_filled(515, 620, 13, 8, arcade.csscolor.GREY, 30, 180)

# handle
arcade.draw_rectangle_filled(500, 660, 13, 65, MASTER_SWORD_PURPLE)
arcade.draw_polygon_filled(((497, 680),
                            (490, 690),
                            (495, 700),
                            (505, 700),
                            (510, 690),
                            (503, 680),
                            ),
                           MASTER_SWORD_PURPLE)

# Tri-force inscription
arcade.draw_triangle_outline(500, 507.5, 510, 525.5, 490, 525.5, (201, 201, 201), 3)
arcade.draw_triangle_outline(500, 525.5, 504, 517.5, 496, 517.5, (201, 201, 201), 3)
arcade.draw_rectangle_filled(500, 527.5, 3, 10, (201, 201, 201))
arcade.draw_rectangle_filled(510, 519.5, 7, 3, (201, 201, 201))
arcade.draw_rectangle_filled(490, 519.5, 7, 3, (201, 201, 201))

# Flowers
arcade.draw_rectangle_filled(450, 350, 10, 75, (168, 171, 82), 170)
arcade.draw_circle_filled(445, 380, 15, (230, 225, 195))
draw_flower(550, 335)

arcade.finish_render()

arcade.run()
