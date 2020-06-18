# load and show an animated gif file using module pyglet
# download module pyglet from: http://www.pyglet.org/download.html
# the animated dinosaur-07.gif file is in the public domain
# download from http://www.gifanimations.com
# tested with Python2.5 and pyglet1.1a2  by  vegaseat   22apr2008
import pyglet
from pyglet.window import key

# pick an animated gif file you have in the working directory
gifs = ["gifs/sleepy_eye.gif", "gifs/matrix.gif"]
index = 0

# create a window and set it to the image size
# win = pyglet.window.Window(width=sprite.width, height=sprite.height)
win = pyglet.window.Window(fullscreen = True)

# set window background color = r, g, b, alpha
# each value goes from 0.0 to 1.0
white = 1, 1, 1, 1
pyglet.gl.glClearColor(*white)

def get_next_gif():
  return gifs[index % len(gifs)]

def get_sprite():
  ag_file = get_next_gif()
  animation = pyglet.image.load_animation(ag_file)
  return pyglet.sprite.Sprite(animation)


sprite = get_sprite()

@win.event
def on_draw():
  win.clear()
  sprite.draw()

@win.event
def on_key_press(symbol, modifiers):
  if symbol == key.N:
    global index
    index = index + 1
    global sprite
    sprite = get_sprite()
  if symbol == key.X and (modifiers & key.MOD_CTRL):
    win.close()


def main():
  pyglet.app.run()


if __name__ == "__main__": main()
