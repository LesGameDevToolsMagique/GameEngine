import pyglet

# Load resources from a directory and store all the assets in a dictionary
class Resources:

    def __init__(self):
        self.assets = {}
        self.resourcePath = []

    # Add resource path, path can be an array
    def addResourcePath(self, path):
        self.resourcePath.append(path)

    # Add resource to assets array
    def addImage(self, key, image):
        self.assets[key] = pyglet.resource.image(image)

    # Set resource dimension
    def setImageDimension(self, image, width, height):
        image.width = width
        image.height = height

    # Load all resource path contain in resourcePath array
    def loadResourcePath(self):
        pyglet.resource.path = self.resourcePath
        pyglet.resource.reindex()
