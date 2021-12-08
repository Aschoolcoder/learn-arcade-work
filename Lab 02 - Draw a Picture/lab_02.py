# This is a code that creates a picture of a winter mountainside view.

import arcade

arcade.open_window(800, 800, "Winter Morning")

arcade.set_background_color((120, 182, 240))

arcade.start_render()

arcade.draw_rectangle_filled(400, 400, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(425, 400, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(450, 425, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(475, 425, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(500, 425, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(525, 425, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(500, 400, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(475, 375, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(450, 375, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(400, 375, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(400, 350, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(400, 325, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(375, 300, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(375, 325, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(350, 350, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(325, 350, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(325, 325, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(350, 375, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(375, 375, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(375, 350, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(425, 350, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(450, 325, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(475, 300, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(525, 300, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(525, 275, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(600, 300, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(600, 275, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(550, 300, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(550, 275, 25, 75, (255, 193, 48))
arcade.draw_rectangle_filled(575, 325, 25, 25, (77, 255, 0))
arcade.draw_rectangle_filled(575, 300, 25, 25, (71, 50, 0))
arcade.draw_rectangle_filled(537.5, 350, 150, 25, (71, 50, 0))
arcade.draw_rectangle_filled(562.5, 375, 150, 25, (71, 50, 0))
arcade.draw_rectangle_filled(562.5, 400, 100, 25, (71, 50, 0))

arcade.finish_render()

arcade.run()