import arcade

arcade.open_window(1000, 800, 'master sword')

arcade.set_background_color(arcade.csscolor.GREY)

# Color variables
GOLD = 199, 164, 70
MASTER_SWORD_PURPLE = 20, 17, 99
BLADE_GRAY = 216, 223, 235


def master_sword(x, y):
    """this function draws a master sword, input x and y to move it"""
    arcade.draw_rectangle_filled(x, y, 35, 200, (216, 223, 235))
    arcade.draw_triangle_filled(x, y + 80, x + 25, y + 100, x - 25, y + 100, (216, 223, 235))
    arcade.draw_rectangle_filled(x, y + 117.5, 49, 35, (216, 223, 235))
    arcade.draw_triangle_filled(x, y + 155, x + 25, y + 135, x - 25, y + 135, (216, 223, 235))
    arcade.draw_rectangle_filled(x, y + 175, 30, 100, (216, 223, 235))
    arcade.draw_triangle_filled(x, y - 133, x - 17.7, y - 100, x + 17.7, y - 100, BLADE_GRAY)

    # Blade-hilt intersection
    arcade.draw_rectangle_filled(x, y + 200, 30, 60, (20, 17, 99))
    arcade.draw_ellipse_filled(x, y + 170, 22, 50, (216, 223, 235))
    arcade.draw_rectangle_filled(x - 13, y + 170, 5, 5, GOLD)
    arcade.draw_rectangle_filled(x + 13, y + 170, 5, 5, GOLD)
    arcade.draw_triangle_filled(x, y + 200, x + 5, y + 210, x - 5, y + 210, GOLD)
    arcade.draw_triangle_filled(x, y + 220, x + 5, y + 210, x - 5, y + 210, GOLD)
    arcade.draw_rectangle_filled(x, y + 199, 4, 10, GOLD)

    # Wings
    arcade.draw_polygon_filled(((x - 15, y + 220),
                                (x - 40, y + 230),
                                (x - 45, y + 235),
                                (x - 40, y + 225),
                                (x - 35, y + 210),
                                (x - 15, y + 200),
                                ),
                               (20, 17, 99))
    arcade.draw_polygon_filled(((x + 15, y + 220),
                                (x + 40, y + 230),
                                (x + 45, y + 235),
                                (x + 40, y + 225),
                                (x + 35, y + 210),
                                (x + 15, y + 200),
                                ),
                               (20, 17, 99))
    arcade.draw_arc_filled(x - 30, y + 200, 60, 60, MASTER_SWORD_PURPLE, 20, 180, 90)
    arcade.draw_rectangle_filled(x - 40, y + 170, 30, 30, arcade.csscolor.GREY, 75)
    arcade.draw_arc_filled(x + 30, y + 200, 60, 60, MASTER_SWORD_PURPLE, 0, 163, 270)
    arcade.draw_rectangle_filled(x + 40, y + 170, 30, 30, arcade.csscolor.GREY, 285)

    # beginning of handle
    arcade.draw_arc_filled(x - 15, y + 220, 13, 8, arcade.csscolor.GREY, 0, 150)
    arcade.draw_arc_filled(x + 15, y + 220, 13, 8, arcade.csscolor.GREY, 30, 180)

    # handle
    arcade.draw_rectangle_filled(x, y + 260, 13, 65, MASTER_SWORD_PURPLE)
    arcade.draw_polygon_filled(((x - 3, y + 280),
                                (x - 10, y + 290),
                                (x - 5, y + 300),
                                (x + 5, y + 300),
                                (x + 10, y + 290),
                                (x + 3, y + 280),
                                ),
                               MASTER_SWORD_PURPLE)

    # Tri-force inscription
    arcade.draw_triangle_outline(x, y + 107.5, x + 10, y + 125.5, x - 10, y + 125.5, (201, 201, 201), 3)
    arcade.draw_triangle_outline(x, y + 125.5, x + 4, y + 117.5, x - 4, y + 117.5, (201, 201, 201), 3)
    arcade.draw_rectangle_filled(x, y + 127.5, 3, 10, (201, 201, 201))
    arcade.draw_rectangle_filled(x + 10, y + 119.5, 7, 3, (201, 201, 201))
    arcade.draw_rectangle_filled(x - 10, y + 119.5, 7, 3, (201, 201, 201))


arcade.start_render()

master_sword(150, 300)
master_sword(400, 300)
master_sword(800, 300)

arcade.finish_render()

arcade.run()
