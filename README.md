# Welcome to Tech Friday - Pygame Demonstration
## Login
### USER:  citevent
### PASS:  eventacc99
***
This presentation for Tech Friday is a very brief introduction to using the Python game engine Pygame. 
To get a full indepth tutorial on this subject I recommend that you watch ["The ultimate introduction to Pygame"](https://youtu.be/AY9MnQ4x3zk?si=eHUOPduFXs4LrxJO)
***
## Adding Surfaces
test_surf = pygame.Surface((100,100)) # create a surface object (rectangle)
test_surf.fill('Red') # set color of test_surf to red

## Adding Images to Surface
sky_surf = pygame.image.load('Sky.png').convert() # create a surface object (before loop)

screen.blit(sky_surf,(0,0)) # adds the surface object to the screen (inside loop)

## Additional Surfaces
