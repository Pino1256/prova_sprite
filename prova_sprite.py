import arcade
import os
# from arcade import *

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.sprite = None
        self.sprite_sasso=None
        self.playerSpriteList = arcade.SpriteList()
        self.SassoSpriteList = arcade.SpriteList()
        self.setup()

        self.sasso_setup()

        self.keys_pressed = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }

    def sasso_setup(self):
        self.sprite= arcade.Sprite("./assets/sasso.png")

        self.sprite_sasso.center_x = 200
        self.sprite_sasso.center_y = 200
        self.sprite_sasso.scale_x = 0.1
        self.sprite_sasso.scale_y = 0.1

        self.SassoSpriteList.append(self.sprite)

    def setup(self):
        
        self.sprite = arcade.Sprite("./assets/tile0.png")

        self.sprite.center_x = 100
        self.sprite.center_y = 100
        self.sprite.scale_x = 1.5
        self.sprite.scale_y = 1.0

        self.playerSpriteList.append(self.sprite)

        

    def on_draw(self):
        self.clear()
        self.playerSpriteList.draw()
        self.SassoSpriteList.draw()
        
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

