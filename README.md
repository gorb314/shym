shym
====

Automated python interface creation with ctypes

Overview
--------

shym is a makefile wrapper around the h2xml and xml2py tools from
ctypes-dev, which automates the creation of an interface to python
from whatever library you want.

Currently I use it to auto-generate an interface to SDL (and SDL_image),
which works well enough that I can use it with the standard python
opengl bindings.

See the testSDL.py and testOpenGL.py files for example usage.

Motivation
----------

There are *many* python/SDL interfaces out there. Also, a lot 
of people seem to have (re)implemented the auto-generation of interfaces
for python, esp. for use with SDL.

So why another one?

This one just modifies the generated interface file to return the 
POINTER.contents back from SDL. So while the auto-generated interface
will pass back a POINTER(SDL_Surface), for example, using shym you get
a plain SDL_Surface (or None, of the function you called returned Null.

This makes the interface a slight bit easier to use, and so it gets
out of my way and I can simply start using SDL.




