#!/usr/bin/python

import SDL
import ctypes

# init SDL
SDL.SDL_Init(SDL.SDL_INIT_VIDEO)
screen = SDL.SDL_SetVideoMode(300, 300, 8, SDL.SDL_SWSURFACE|SDL.SDL_ANYFORMAT)

# Load an image into a surface
image = SDL.IMG_Load("test.png")

# fill the screen with white
SDL.SDL_FillRect(screen, None, 0xffffffff);

# Blit onto the screen surface
SDL.SDL_BlitSurface(image, None, screen, None)

# Update the modified region of the screen
SDL.SDL_UpdateRect(screen, 0, 0, screen.w, screen.h)

while True:
	event = SDL.SDL_Event()
	status = SDL.SDL_WaitEvent(event);
	if event:
		if event.type == SDL.SDL_KEYDOWN:
			key = SDL.SDL_GetKeyName(event.key.keysym.sym)
			if event.key.keysym.sym == SDL.SDLK_ESCAPE:
				break
		if event.type == SDL.SDL_QUIT:
			break


# Free the allocated image
SDL.SDL_FreeSurface(image)



