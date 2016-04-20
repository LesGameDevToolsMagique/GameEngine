import pyglet

# Load resources from a directory and store all the assets in a dictionary
class Resources:

    def __init__(self, ressourcePath):
        self.assets = {}
        pyglet.resource.path = [ressourcePath]
        pyglet.resource.reindex()

    def addImage(self, key, image):
        self.assets[key] = pyglet.resource.image(image)

    def setImageDimension(self, image, width, height):
        image.width = width
        image.height = height
