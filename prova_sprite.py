import arcade
import os
# from arcade import *

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.sprite = None
        self.playerSpriteList = arcade.SpriteList()

        self.setup()

        self.keys_pressed = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }

    def setup(self):
        
        self.sprite = arcade.Sprite("./assets/tile0.png")

        self.sprite.center_x = 100
        self.sprite.center_y = 100
        self.sprite.scale_x = 1.5
        self.sprite.scale_y = 1.0

        self.playerSpriteList.append(self.sprite)

        

    def on_draw(self):
        self.playerSpriteList.draw()
        
    def on_update(self, deltaTime):
        speed = 4  # velocità del personaggio

        if self.keys_pressed['up']:
            self.sprite.center_y += speed
        if self.keys_pressed['down']:
            self.sprite.center_y -= speed
        if self.keys_pressed['left']:
            self.sprite.center_x -= speed
        if self.keys_pressed['right']:
            self.sprite.center_x += speed
    
    def on_key_press(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.W]:
            self.keys_pressed['up'] = True
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.keys_pressed['down'] = True
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.keys_pressed['left'] = True
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.keys_pressed['right'] = True
    
    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.W]:
            self.keys_pressed['up'] = False
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.keys_pressed['down'] = False
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.keys_pressed['left'] = False
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.keys_pressed['right'] = False

def main():
    game = MyGame(
        600, 600, "Il mio giochino"
    )
    arcade.run()


if __name__ == "__main__":
    main()

