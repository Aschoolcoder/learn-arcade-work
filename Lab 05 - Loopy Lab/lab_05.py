import arcade

b = arcade.color.BLACK
w = arcade.color.WHITE


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    global row
    for row in range(5, 301, 10):
        global column
        for column in range(5, 301, 10):
            x = column  # Instead of zero, calculate the proper x location using 'column'
            y = row  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    global color
    global row
    for row in range(5, 301, 10):
        global column
        for column in range(5, 301, 10):
            x = column  # Instead of zero, calculate the proper x location using 'column'
            y = row  # Instead of zero, calculate the proper y location using 'row'
            if x % 4 == 1:
                color = w
            else:
                color = b

            arcade.draw_rectangle_filled(x + 300, y, 5, 5, color)


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    global color
    global row
    for row in range(5, 301, 10):
        global column
        for column in range(5, 301, 10):
            x = column  # Instead of zero, calculate the proper x location using 'column'
            y = row  # Instead of zero, calculate the proper y location using 'row'
            if y % 4 == 1:
                color = w
            else:
                color = b

            arcade.draw_rectangle_filled(x + 600, y, 5, 5, color)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    global color
    global row
    for row in range(5, 301, 10):
        global column
        for column in range(5, 301, 10):
            x = column
            y = row
            if y % 4 == 1 and x % 4 == 1:
                color = w
            else:
                color = b

            arcade.draw_rectangle_filled(x + 900, y, 5, 5, color)


def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    global column, row
    for row in range(5, 301, 10):
        for column in range(0, row + 1, 10):
            x = row  # Instead of zero, calculate the proper x location using 'column'
            y = column  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y + 305, 5, 5, arcade.color.WHITE)


def draw_section_6():
    global column
    for column in range(5, 301, 10):
        global row
        for row in range(5, 301 - column, 10):
            x = column  # Instead of zero, calculate the proper x location using 'column'
            y = row  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 300, y + 300, 5, 5, arcade.color.WHITE)


def draw_section_7():
    global column
    for column in range(5, 301, 10):
        global row
        for row in range(5, 301, 10):
            x = column  # Instead of zero, calculate the proper x location using 'column'
            y = row + column  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 600, y + 295, 5, 5, arcade.color.WHITE)


def draw_section_8():
    global column
    for column in range(5, 301, 10):
        global row
        for row in range(5 - column, 301, 10):
            x = column  # Instead of zero, calculate the proper x location using 'column'
            y = row  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 900, y + 595, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
