import arcade

arcade.open_window(1000, 800, "Tortle")

arcade.set_background_color((21, 93, 209))

arcade.start_render()

arcade.draw_text("Bob the turtle", 500, 700)

arcade.draw_arc_filled(center_x=500,
                       center_y=400,
                       width=600,
                       height=300,
                       color=(140, 95, 21),
                       start_angle=0,
                       end_angle=180)

arcade.draw_ellipse_filled(385, 395, 150, 110, (41, 140, 21))
arcade.draw_ellipse_filled(670, 395, 150, 110, (41, 140, 21))

arcade.draw_ellipse_filled(150, 480, 300, 150, (41, 140, 21), 0, 180)

arcade.draw_circle_filled(150, 480, 50, arcade.csscolor.WHITE)
arcade.draw_circle_filled(150, 480, 20, arcade.csscolor.BLACK)

arcade.draw_rectangle_filled(350, 490, 60, 60, (92, 64, 13))
arcade.draw_rectangle_filled(420, 490, 60, 60, (92, 64, 13))
arcade.draw_rectangle_filled(490, 490, 60, 60, (92, 64, 13))
arcade.draw_rectangle_filled(560, 490, 60, 60, (92, 64, 13))
arcade.draw_rectangle_filled(630, 490, 60, 60, (92, 64, 13))

arcade.draw_triangle_filled(940, 420, 780, 370, 780, 470, (41, 140, 21))

arcade.draw_rectangle_filled(40, 0, 30, 300, (15, 64, 9))
arcade.draw_rectangle_filled(80, 0, 30, 320, (15, 64, 9))
arcade.draw_rectangle_filled(120, 0, 30, 310, (15, 64, 9))
arcade.draw_rectangle_filled(160, 0, 30, 400, (15, 64, 9))
arcade.draw_rectangle_filled(200, 0, 30, 340, (15, 64, 9))
arcade.draw_rectangle_filled(250, 0, 30, 310, (15, 64, 9))
arcade.draw_rectangle_filled(290, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(330, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(370, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(410, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(450, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(490, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(530, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(570, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(610, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(650, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(690, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(730, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(770, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(810, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(850, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(890, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(930, 0, 30, 390, (15, 64, 9))
arcade.draw_rectangle_filled(970, 0, 30, 390, (15, 64, 9))

arcade.finish_render()

arcade.run()