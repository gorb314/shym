# Example Makefile for using shym to auto-generate a ctypes-interface
# to a library in python
# The example builds an interface for SDL + SDL_image, and uses
# gcc to determine the platform it is being used on.

MACHINE = $(shell gcc -dumpmachine)

ifeq (linux, $(findstring linux, $(MACHINE)))
$(info Compiling for Linux)
LINUX = 1
HEADERS = /usr/include/SDL
endif
ifeq (darwin, $(findstring darwin, $(MACHINE)))
$(info Compiling for Mac)
DARWIN = 1
HEADERS = /opt/local/include/SDL
H2XML  = ./h2xml.py
XML2PY = ./xml2py.py
endif

INCLUDE = $(addprefix -I, $(HEADERS))

TARGETS = SDL.py

all: $(TARGETS)

SDL.xml: SDL.h SDL_image.h
SDL.py: LIBS = SDL SDL_image 
SDL.py: PREFIX = SDL

vpath %.h $(HEADERS)

# test the interface
test: SDL.py
	./testSDL.py

include Makefile.shym

