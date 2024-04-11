# Welcome to Tech Friday - Pygame Demonstration
#### https://github.com/UM-Flint-CSC/Tech_Friday
***
This presentation for Tech Friday is a very brief introduction to using the Python game engine Pygame. 
To get a full indepth tutorial on this subject I recommend that you watch ["The ultimate introduction to Pygame"](https://youtu.be/AY9MnQ4x3zk?si=eHUOPduFXs4LrxJO)
***
## Adding Surfaces
(before loop)

`test_surf = pygame.Surface((100,100)) # create a surface object (rectangle)`
`test_surf.fill('Red') # set color of test_surf to red`

(inside loop)

`screen.blit(test_surf,(100,50))`

## Adding Images to Surface

`sky_surf = pygame.image.load('Sky.png').convert() # create a surface object (before loop)`

`screen.blit(sky_surf,(0,0)) # adds the surface object to the screen (inside loop)`

`ground_surf = pygame.image.load('ground.png').convert() # create a surface object (before loop)`

`screen.blit(ground_surf, (0, 300))  # adds the surface object to the screen`

## Adding Text Surface

`test_font = pygame.font.Font(None,50) # use pygame default font (before loop)`

`score_surf = test_font.render(f'{score}', True, "Black") # adds the surface object to the screen'

