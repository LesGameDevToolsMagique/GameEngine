import pyglet

class PygletLib:

    def __init__(self):
        self.content = {}

    # Open a window
    def initWindow(self, width, height):
        self.window = pyglet.window.Window(width, height)

    # Draw content
    def draw(self):
        for key, value in self.content.iteritems():

            # Center horizontally and vertically
            if 'center' in value['opts'] and value['opts']['center']:
                value['opts']['x'] = self.window.width//2
                value['opts']['y'] = self.window.height//2

            # Center horizontally
            if 'center-width' in value['opts'] and value['opts']['center-width']:
                value['opts']['x'] = self.window.width//2

            # Draw label
            if value['type'] == 'label':
                self.draw_label(value['text'], value['opts']);

            # Add input box
            if value['type'] == 'input_box':
                self.draw_quads(value['opts'])
                self.draw_input_box(value['text'], value['opts']);

    # Update content
    def update(self, instructions):
        for key, value in instructions.iteritems():

            # Add or update content
            if value['action'] == 'update':
                self.content[key] = value['content']

            # Delete content
            if value['action'] == 'delete':
                del self.content[key]

    # Add a text to containers
    def add_text(self, id, type, text, options):
        document = { 'type': type, 'text': text, 'opts': options }
        self.content[id] = document

    # Draw label
    def draw_label(self, text, opts):
        document = pyglet.text.decode_text(text)
        pyglet.text.Label(document.text, font_name='Times New Roman', font_size=36, x=opts['x'], y=opts['y'], anchor_x='center', anchor_y='center').draw()

    # Draw input box
    def draw_input_box(self, text, opts):
        document = pyglet.text.decode_text(text)
        pyglet.text.Label(document.text, font_name='Times New Roman', font_size=36, color=(0, 0, 0, 255), x=opts['x'], y=opts['y'], anchor_x='center', anchor_y='center').draw()

    # Draw quads
    def draw_quads(self, opts):
        upLeft = (opts['x'] - opts['width']//2, opts['y'] + opts['height']//2)
        upRight = (opts['x'] + opts['width']//2, opts['y'] + opts['height']//2)
        downLeft = (opts['x'] - opts['width']//2, opts['y'] - opts['height']//2)
        downRight = (opts['x'] + opts['width']//2, opts['y'] - opts['height']//2)

        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', (upLeft[0], upLeft[1],
                                      upRight[0], upRight[1],
                                      downRight[0], downRight[1],
                                      downLeft[0], downLeft[1])))

    # Run pyglet app
    def run(self):
        @self.window.event
        def on_draw():
            self.window.clear()

            # Don't forget to uncomment when receiving object from server
            # self.update(new_object)

            self.draw()

        pyglet.app.run()
