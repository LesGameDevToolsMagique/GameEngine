#ifndef GRAPHICAL_ENGINE_HPP_
# define GRAPHICAL_ENGINE_HPP_

# include <iostream>

//
// GraphicalEngine class with load the graphic library
// and use the methods to draw the game
//
class GraphicalEngine
{
private:
  void _loadLibrary(); // May have to change the prototype later

public:
  GraphicalEngine();
  ~GraphicalEngine();

  void run();
  void start();
  void close();

  void draw();

};

#endif // ! GRAPHICAL_ENGINE_HPP_
