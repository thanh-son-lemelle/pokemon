import pygame
import os

def resizeImage(image, multiplier):
    originalWidth, originalHeight = image.get_size()
    newHeight = int(multiplier * originalHeight)
    newWidth = int(multiplier * originalWidth)
    image = pygame.transform.scale(image, (newWidth, newHeight))
    return image

pygame.init()
sc_w, sc_h = 800, 400
x, y = 0, 0
FPS = 30
clock = pygame.time.Clock()
ospath = os.path.dirname(__file__)
split_gif = os.path.join("images", "sprite_pokemon", "front", "split_gif")

screen = pygame.display.set_mode((sc_w, sc_h))
...
frames = [] # to store the different images of the GIF
for i in range(105):
    if i < 10:
        frame = (pygame.image.load(f"images\\sprite_pokemon\\front\\split_gif\\4\\frame_00{i}_delay-0.05s.gif").convert_alpha())
        
    elif i < 100:
        frame = (pygame.image.load(f"images\\sprite_pokemon\\front\split_gif\\4\\frame_0{i}_delay-0.05s.gif").convert_alpha())
    else:
        frame = (pygame.image.load(f"images\\sprite_pokemon\\front\split_gif\\4\\frame_{i}_delay-0.05s.gif").convert_alpha())

    frameresized = resizeImage(frame, 1.5)
    frames.append(frameresized)

framesbis = []
for i in range (41):
    if i < 10:
        frame = (pygame.image.load(f"images\\sprite_pokemon\\front\\split_gif\\4bis\\frame_0{i}_delay-0.03s.gif").convert_alpha())
    else:
        frame = (pygame.image.load(f"images\\sprite_pokemon\\front\\split_gif\\4bis\\frame_{i}_delay-0.03s.gif").convert_alpha())
    frameresized = resizeImage(frame, 1.5)
    framesbis.append(frameresized)
        

running = True
current_frame = 0 # keep an index of what frame we're currently looking at
current_framebis = 0
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
    bg = pygame.image.load("images\\background\combat\sprite_combat_background02.png")
    bg = pygame.transform.scale(bg, (sc_w, sc_h))
    screen.fill((255,255,255))
    screen.blit(bg, (0,0))
    screen.blit(frames[current_frame], (x,y)) # draw the current frame to the screen
    current_frame += 1 # go to the next frame
    current_frame %= len(frames) # loop back around if you reached the end
    
    screen.blit(framesbis[current_framebis], (sc_w/2,sc_h/2)) # draw the current frame to the screen
    current_framebis += 1 # go to the next frame
    current_framebis %= len(framesbis) # loop back around if you reached the end
    pygame.display.flip()
    clock.tick(FPS)

