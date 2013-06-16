#!/usr/bin/python

from SDL import *
from OpenGL.GL import *

SDL_Init(SDL_INIT_VIDEO)
screen = SDL_SetVideoMode(300, 300, 8, SDL_HWSURFACE|SDL_OPENGL|SDL_ANYFORMAT)

glClearColor(0.5, 0, 0, 0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

SDL_GL_SwapBuffers()

while True:
	event = SDL_Event()
	status = SDL_WaitEvent(event);
	if event:
		if event.type == SDL_KEYDOWN:
			key = SDL_GetKeyName(event.key.keysym.sym)
			print "key", key, "was pressed"
		if event.key.keysym.sym == SDLK_ESCAPE:
			print "quitting"
			break

SDL_Quit()
