# This is a code that creates a picture of a winter mountainside view.

import arcade

arcade.open_window(800, 800, "Winter Morning")

arcade.set_background_color((120, 182, 240))

arcade.start_render()

# mountain
arcade.draw_polygon_filled(((0, 123),
                           (340, 160),
                           (690, 540),
                           (720, 430),
                           (800, 280),
                            (800, 0),
                            ),
                           (86, 98, 110))
arcade.draw_rectangle_filled(0, 0, 1000000000000, 250, (86, 98, 110))

# sun
arcade.draw_circle_filled(190, 700, 80, (255, 204, 0))

# snow
arcade.draw_rectangle_filled(0, 0, 200, 400, (255, 255, 255), 22)
arcade.draw_rectangle_filled(300, 0, 400, 300, (255, 255, 255))
arcade.draw_arc_filled(600, 120, 480, 140, (255, 255, 255), 0, 180)
arcade.draw_triangle_filled(690, 540, 560, 400, 720, 430, (255, 255, 255))
arcade.draw_rectangle_filled(690, 0, 100000, 250, (255, 255, 255))

# brick house
arcade.draw_rectangle_filled(280, 160, 90, 70, (128, 31, 11))
arcade.draw_rectangle_filled(245, 210, 10, 30, (153, 129, 127))
arcade.draw_rectangle_outline(280, 155, 90, 60, (94, 61, 61), 5)
arcade.draw_triangle_filled(280, 240, 220, 180, 340, 180, (64, 32, 29))
arcade.draw_ellipse_filled(245, 240, 7, 20, (59, 57, 57))
arcade.draw_ellipse_filled(240, 270, 7, 20, (59, 57, 57))
arcade.draw_ellipse_filled(250, 300, 7, 20, (59, 57, 57))
arcade.draw_rectangle_filled(260, 160, 15, 15, (0, 0, 0))
arcade.draw_rectangle_filled(300, 160, 15, 15, (0, 0, 0))
arcade.draw_rectangle_filled(280, 140, 10, 20, (79, 51, 15))

# clouds
arcade.draw_circle_filled(300, 548, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(268, 534, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(324, 540, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(300, 528, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(150, 528, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(128, 514, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(174, 530, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(150, 518, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(700, 728, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(667, 704, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(733, 710, 35, (214, 210, 206, 150))
arcade.draw_circle_filled(700, 715, 35, (214, 210, 206, 150))

# trees
arcade.draw_rectangle_filled(180, 150, 15, 30, (77, 40, 11))
arcade.draw_triangle_filled(180, 220, 160, 150, 200, 150, (58, 84, 43))
arcade.draw_rectangle_filled(380, 150, 15, 30, (77, 40, 11))
arcade.draw_triangle_filled(380, 220, 360, 150, 400, 150, (58, 84, 43))
arcade.draw_rectangle_filled(500, 190, 15, 30, (77, 40, 11))
arcade.draw_triangle_filled(500, 260, 480, 190, 520, 190, (58, 84, 43))
arcade.draw_rectangle_filled(580, 200, 15, 30, (77, 40, 11))
arcade.draw_triangle_filled(580, 270, 560, 200, 600, 200, (58, 84, 43))

arcade.finish_render()

arcade.run()
