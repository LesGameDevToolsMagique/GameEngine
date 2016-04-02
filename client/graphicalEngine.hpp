#ifndef GRAPHICAL_ENGINE_HPP_
# define GRAPHICAL_ENGINE_HPP_

# include <iostream>
# include <dlfcn.h> // Add this line is the cpp file after

//
// GraphicalEngine class with load the graphic library
// and use the methods to draw the game
//
class GraphicalEngine
{
private:
  GraphicalEngine _library;

public:
  GraphicalEngine();
  ~GraphicalEngine();

  void loadLibrary(); // May have to change the prototype later

  void run();
  void start();
  void close();

  void draw();
};

#endif // ! GRAPHICAL_ENGINE_HPP_
