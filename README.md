# Welcome to Tech Friday - Pygame Demonstration
#### https://github.com/UM-Flint-CSC/Tech_Friday
***
This presentation for Tech Friday is a very brief introduction to using the Python game engine Pygame. 
To get a full indepth tutorial on this subject I recommend that you watch ["The ultimate introduction to Pygame"](https://youtu.be/AY9MnQ4x3zk?si=eHUOPduFXs4LrxJO)
***
## Adding Surfaces
(before loop)

```python
test_surf = pygame.Surface((100,100)) # create a surface object (rectangle)
test_surf.fill('Red') # set color of test_surf to red
```

(inside loop)

```python
screen.blit(test_surf,(100,50))
```

## Adding Images to Surface

```python
sky_surf = pygame.image.load('Sky.png').convert() # create a surface object (before loop)
ground_surf = pygame.image.load('ground.png').convert() # create a surface object (before loop)
```
```python
screen.blit(sky_surf,(0,0)) # adds the surface object to the screen (inside loop)
screen.blit(ground_surf, (0, 300))  # adds the surface object to the screen (inside loop)
```

## Adding Text Surface

```python
test_font = pygame.font.Font(None,50) # use pygame default font (before loop)
score_surf = test_font.render(f'Score:', True, "Black") # adds the surface object to the screen (before loop)
```
```python
screen.blit(score_surf,(400,50)) # adds the surface object to the screen (inside loop)
```

## Adding An Image Surface to a Rectangle Object

```python
snail_surf = pygame.image.load('snail/snail1.png').convert_alpha() # create a surface object (before loop)
snail_rect = snail_surf.get_rect(bottomleft = (800,300)) # create a rectangle object (before loop)
```
```python
screen.blit(snail_surf,snail_rect) # adds the rectangle object to the screen (inside loop)
```

## Animating a Rectangle Object

```python
snail_rect.left -= 4
if snail_rect.right <= 0: 
    snail_rect.left = 800
```

## Adding the Player Character and Detecting Collisions

```python
player_surf = pygame.image.load('Player/player_walk_1.png').convert_alpha() # (before loop)
player_rect = player_surf.get_rect(midbottom = (80,300)) # create a rectangle object (before loop)
```

```python
screen.blit(player_surf,player_rect) # adds the rectangle object to the screen (inside loop)
```
```python
if player_rect.colliderect(snail_rect):
    print('collision') # just for testing
```

## Animate the Player Jumping

```python
player_gravity = 0 # create a variable to gravity value - Step 1 to create a gravity effect (before loop)
```

```python
player_gravity += 1 # increment gravity value by 1 each frame (inside loop)
player_rect.y += player_gravity # add the increasing gravity value to the play recangle y (vertical) position (inside loop)
```

## Space Key User Input To Jump

```python
# add event to detect space key pressed inside the event for loop
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        player_gravity = -20
```

## Providing a Floor for the Player Character

```python
and player_rect.bottom == 300 # combined with space key down condition
```

```python
if player_rect.bottom >= 300:
    player_rect.bottom = 300 # add detection of player on floor
```

## End Game if the Snail Touches the Player

```python
game_active = True # create variable to game state (before loop)
```
```python
    if player_rect.colliderect(snail_rect):
        game_active = False
```
```python
if game_active:
    # current game code
else:
    # draw game over screen
```


