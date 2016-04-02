RM = rm -rf
CXX = clang++
SDL = -lsfml-graphics -lsfml-audio -lsfml-window -lsfml-system

# If your compiler is a bit older you may need to change -std=c++11 to -std=c++0x
CXXFLAGS = -Wall -c -std=c++11
LDFLAGS = $(SDL)

SRCS = test.cpp

OBJS = $(SRCS:.cpp=.o)

EXE = SFML_Test

all: $(EXE)

$(EXE): $(OBJS)
	$(CXX) $(LDFLAGS) $< -o $@

main.o: $(SRCS)
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(EXE)

re: fclean all

.PHONY:
	clean fclean all re
