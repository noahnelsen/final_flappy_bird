"""LAB 12 """

import arcade
import random

SCREEN_WIDTH = 501
SCREEN_HEIGHT = 501
SPRITE_SCALING_WALL = .2
SPRITE_SCALING_BIRD = 2


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


class TopWall(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x -= 2

        if self.center_x < -50:
            self.center_y = random.randrange(400, 500)
            self.center_x = 500


class Bird(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 12")

        self.bird_list = None
        self.top_wall_list = None

    def setup(self):
        self.top_wall_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()

        self.bird_sprite = arcade.Sprite("Flappy Bird.png", SPRITE_SCALING_BIRD)
        self.bird_sprite.center_x = 50
        self.bird_sprite.center_y = 50
        self.bird_list.append(self.bird_sprite)

        top = TopWall("a37ba1146bd745.png", SPRITE_SCALING_WALL)
        top.center_x = 300
        top.center_y = 250

        self.top_wall_list.append(top)

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

        self.top_wall_list.draw()
        self.bird_list.draw()

    # def update(self, delta_time):
        # self.top_wall_list.update()


def main():
    window = MyGame()
    arcade.run()


main()