import json
from graphicalEngine import GraphicalEngine

class GameEngine:

    # Store the graphical engine
    def loadGraphicalEngine(self, graphicalEngine):
        self.graphicalEngine = graphicalEngine

    # Read json file and return the content in a dictionary
    def readJsonFile(self, path):
        with open(path) as json_data:
            data = json.loads(json_data.read())
            json_data.close()
            return data;
