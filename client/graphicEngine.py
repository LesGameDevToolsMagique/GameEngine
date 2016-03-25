import importlib

class GraphicalEngine:

    # Load library by name
    def loadLibrary(self, name):
        if not self.library:
            self.library = importlib.import_module(name)

    # Draw from library
    def draw(self):
        self.library.draw()

    # Run the library
    def run(self):
        self.library.run()

    # Close library
    def close(self):
        self.library.close()
