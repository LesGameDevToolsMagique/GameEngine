import pyglet

class PygletLib:

    def __init__(self):
        self.content = {}

        options = { 'center': True }
        self.add_text('question', 'label', 'Question coming soon', options)

    # Open a window
    def initWindow(self, width, height):
        self.window = pyglet.window.Window(width, height)

    # Draw
    def draw(self):
        for key, value in self.content.iteritems():

            if value['opts']['center']:
                value['opts']['x'] = self.window.width//2
                value['opts']['y'] = self.window.height//2

            if value['type'] == 'label':
                self.draw_label(value['text'], value['opts']);

    # Update content
    def update(self, content):
        for key, value in content.iteritems():
            self.content[key] = value

    # Add a text to containers
    def add_text(self, id, type, text, options):
        document = { 'type': type, 'text': text, 'opts': options }
        self.content[id] = document

    def draw_label(self, text, opts):
        document = pyglet.text.decode_text(text)
        pyglet.text.Label(document.text, font_name='Times New Roman', font_size=36, x=opts['x'], y=opts['y'], anchor_x='center', anchor_y='center').draw()

    # Run pyglet app
    def run(self):
        @self.window.event
        def on_draw():
            self.window.clear()

            # Don't forget to uncomment when receiving object from server
            # self.update(new_object)

            self.draw()

        pyglet.app.run()
