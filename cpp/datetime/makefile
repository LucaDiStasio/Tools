CXX = g++
CXXFLAGS = -std=c++11 -I/usr/lib/x86_64-linux-gnu/
INCLUDES = 
LD = icc
LDFLAGS := -L/usr/lib/x86_64-linux-gnu/ -lboost_filesystem -lboost_program_options -lboost_system

#/home/ubuntu/workspace/boost
#/home/ubuntu/workspace/boost/stage/lib

SOURCES = datetime.cpp
HEADERS = datetime.h
OBJ     = main.o datetime.o

.SUFFIXES: .cpp

all: date

date: $(OBJ)
	$(CXX) $(CXXFLAGS) $(OBJ) -o date $(LDFLAGS)
	
main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp
	
datetime.o: datetime.cpp datetime.h
	$(CXX) $(CXXFLAGS) -c datetime.cpp

clean:
	rm -f main
	rm -f *.o
	rm -f *.i
	rm -f *.lst
	rm -f output.*