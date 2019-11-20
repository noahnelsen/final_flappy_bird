"""LAB 12 """

import arcade
import random

SCREEN_WIDTH = 501
SCREEN_HEIGHT = 501


def buildings(x, y):
    arcade.draw_rectangle_filled(x, y, 25, 100, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(x + 60, y, 50, 100, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(x + 120, y, 50, 200, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(200, y, 50, 200, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(260, y, 50, 150, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(320, y, 50, 250, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(400, y, 50, 100, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(460, y, 60, 75, arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(520, y, 50, 100, arcade.color.DARK_GRAY)


def tree_line(x, y):
    arcade.draw_circle_filled(x - 250, y + 10, 25, arcade.color.LIGHT_GREEN)
    arcade.draw_circle_filled(x - 150, y + 10, 25, arcade.color.LIGHT_GREEN)
    arcade.draw_circle_filled(x - 50, y + 10, 25, arcade.color.LIGHT_GREEN)
    arcade.draw_circle_filled(x + 50, y + 10, 25, arcade.color.LIGHT_GREEN)
    arcade.draw_circle_filled(x + 150, y + 10, 25, arcade.color.LIGHT_GREEN)
    arcade.draw_circle_filled(x + 250, y + 10, 25, arcade.color.LIGHT_GREEN)
    arcade.draw_rectangle_filled(x, y, SCREEN_WIDTH, 50, arcade.color.LIGHT_GREEN)


def cloud(x, y):
    arcade.draw_circle_filled(x, y, 15, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x + 10, y, 15, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x - 10, y, 20, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x - 20, y + 5, 15, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x - 30, y, 15, arcade.color.WHITE_SMOKE)


class TopWall():
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

    def update(self):
        self.position_x += self.change_x

        if self.position_x < -50:
            self.position_x = 800
            self.position_y = random.randrange(400, 500)



class BottomWall():
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

    def update(self):
        self.position_x += self.change_x

        if self.position_x < -50:
            self.position_x = 800
            self.position_y = random.randrange(0, 100)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 12")
        self.twall1 = TopWall(500, 500, -20, 0, 50, 200, arcade.color.FOREST_GREEN)
        self.twall2 = TopWall(800, 500, -20, 0, 50, 200, arcade.color.FOREST_GREEN)
        self.twall3 = TopWall(1100, 500, -20, 0, 50, 200, arcade.color.FOREST_GREEN)

        self.bwall1 = BottomWall(500, 0, -20, 0, 50, 300, arcade.color.FOREST_GREEN)
        self.bwall2 = BottomWall(800, 0, -20, 0, 50, 300, arcade.color.FOREST_GREEN)
        self.bwall3 = BottomWall(1100, 0, -20, 0, 50, 300, arcade.color.FOREST_GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BABY_BLUE)
        cloud(250, 300)
        cloud(120, 250)
        cloud(400, 200)
        cloud(450, 100)
        cloud(50, 100)
        cloud(225, 150)
        buildings(10, 50)
        tree_line(250, 0)
        self.twall1.draw()
        self.twall2.draw()
        self.twall3.draw()
        self.bwall1.draw()
        self.bwall2.draw()
        self.bwall3.draw()

    def update(self, delta_time):
        self.twall1.update()
        self.twall2.update()
        self.twall3.update()

        self.bwall1.update()
        self.bwall2.update()
        self.bwall3.update()


def main():
    window = MyGame()
    arcade.run()


main()