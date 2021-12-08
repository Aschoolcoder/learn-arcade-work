import arcade
import random

def main():
    arcade.open_window(800, 800, "8-bit hyrule")
    arcade.set_background_color((70, 190, 250))
    arcade.start_render()
    link_x = 0
    link_y = random.randrange(100, 301)
    arcade.draw_polygon_filled(((0, 0),
                                (0, 300),
                                (300, 350),
                                (500, 450,),
                                (700, 400),
                                (800, 350),
                                (800, 0)
                                ),
                                (41, 166, 0))
    while link_x <= 800:
        arcade.draw_rectangle_filled(link_x, link_y, 20, 90, (163, 99, 11))

        # Tree top
        arcade.draw_circle_filled(link_x, link_y + 30, 30, (23, 92, 0))
        link_x += random.randrange(70, 101)
        link_y += random.randrange(-25, 50)
    for i in range(0, 800, 150):
        # cloud loop 548
        cloud_y = random.randrange(600, 700)
        arcade.draw_circle_filled(i, cloud_y, 35, (214, 210, 206, 150))
        arcade.draw_circle_filled(i - 32, cloud_y - 14, 35, (214, 210, 206, 150))
        arcade.draw_circle_filled(i + 24, cloud_y - 8, 35, (214, 210, 206, 150))



    arcade.run()


main()