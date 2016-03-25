import pyglet

class PygletLib:

    def __init__(self):
        # self.content = {}
        # self.game_resources = resources.Resources('../resources')
        # self.game_resources.addImage('head', 'pika.jpg');
        # self.game_resources.setImageDimension(self.game_resources.assets['head'], 50, 50)
        self.initWindow(1000, 1000)


    # Open a window
    def initWindow(self, width, height):
        self.window = pyglet.window.Window(width, height)

    # Draw
    def draw(self):
        for key, value in self.contents.iteritems():
            self.game_resources.assets[key].blit(value['x'], value['y'])

    # Run pyglet app
    def run(self):
        pyglet.app.run()
