import pygame
import os
import Pokemon

pygame.init()
sc_w, sc_h = 800, 600
x, y = 0, 0
FPS = 25
clock = pygame.time.Clock()
ospath = os.path.dirname(__file__)
split_gif = os.path.join("images", "sprite_pokemon", "front", "split_gif")

screen = pygame.display.set_mode((sc_w, sc_h))

...
frames = [] # to store the different images of the GIF
for i in range(41):
    if i < 10:
        frames.append(pygame.image.load(f"images\\sprite_pokemon\\front\split_gif\\frame_0{i}_delay-0.03s.gif").convert_alpha())
        "Pokemon.resizeImage(frames[i], 200, 200)"
    else:
        frames.append(pygame.image.load(f"images\\sprite_pokemon\\front\split_gif\\frame_{i}_delay-0.03s.gif").convert_alpha())
        """Pokemon.resizeImage(frames[i], 200, 200)"""

running = True
current_frame = 0 # keep an index of what frame we're currently looking at
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
    
    
    screen.blit(frames[current_frame], (x,y)) # draw the current frame to the screen
    current_frame += 1 # go to the next frame
    current_frame %= len(frames) # loop back around if you reached the end
    pygame.display.flip()
    clock.tick(FPS)

