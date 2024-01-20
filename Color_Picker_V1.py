import pygame


'''
press a, q, z to change red value. press s, w, x to change green value. press d, e, c to change blue value. press f to reset color. 
press r to save a color and v to load the last saved color.
'''
pygame.init()

r, g, b = 0, 0, 0

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ChangeDetected = False
FavR = [100, 125, 123]
FavG =[20, 120, 53]
FavB = [20, 12, 23]
# The main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == pygame.KEYDOWN:
        ChangeDetected = True
        if event.key == pygame.K_a:
            r += 5
            if r > 255:
                r = 255
        if event.key == pygame.K_q:
            r -= 5
            if r < 0:
                r = 0
        if event.key == pygame.K_z:
            r = 0
        if event.key == pygame.K_s:
            g += 5
            if g > 255:
                g = 255
        if event.key == pygame.K_w:
            g -= 5
            if g < 0:
                g = 0
        if event.key == pygame.K_x:
            g = 0
        if event.key == pygame.K_d:
            b += 5
            if b > 255:
                b = 255
        if event.key == pygame.K_e:
            b -= 5
            if b < 0:
                b = 0
        if event.key == pygame.K_c:
            b = 0
        if event.key == pygame.K_f:
            r = 0
            g = 0
            b = 0
        if event.key == pygame.K_r:
            FavR.append(r)
            FavG.append(g)
            FavB.append(b)
        if event.key == pygame.K_v:
            r = FavR[-1]
            b = FavB[-1]
            g = FavG[-1]
    if ChangeDetected:
        ChangeDetected = False
        print(f" (r,g,b) = ({r}, {g}, {b})")
        print(FavB)
        BACKGROUND = (r, g, b)
        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        pygame.display.update()