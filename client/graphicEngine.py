import importlib

class GraphicalEngine:

    # Load library module, here the name is the file name
    # and the module the class name
    def loadLibrary(self, name, module):
        self.library = getattr(importlib.import_module(name), module)

    # Draw from library
    def draw(self):
        self.library.draw()

    # Run the library
    def run(self):
        self.library.run()

    # Close library
    def close(self):
        self.library.close()

if __name__ == '__main__':
    gE = GraphicalEngine()
    gE.loadLibrary('pygletLib', 'PygletLib')
    gL = gE.library()
    gL.run()
