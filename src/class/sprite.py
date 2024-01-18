import pygame

pygame.init()
sc_w, sc_h = 800, 600
x, y = 0, 0
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((sc_w, sc_h))

...

frames = [] # to store the different images of the GIF
for i in range(4):
    frames.append(pygame.image.load(f"idle/idle ({i+1}).jpg").convert_alpha())

running = True
current_frame = 0 # keep an index of what frame we're currently looking at
while running:
    for ev in pygame.event.get():
        ...
    
    ...

    screen.blit(frames[current_frame], (x,y)) # draw the current frame to the screen
    current_frame += 1 # go to the next frame
    current_frame %= len(frames) # loop back around if you reached the end
    pygame.display.flip()
    clock.tick(FPS)

