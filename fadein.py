from pygame import *

def fadein(image,screen):
    DONE = False

    alphaSurface = Surface((800,600)) # The custom-surface of the size of the screen.
    alphaSurface.blit(transform.scale(image,(800,600)),(0,0))
    alphaSurface.set_alpha(0) # Set alpha to 0 before the main-loop. 
    alph = 0 # The increment-variable.
    while not DONE:
        screen.fill((0,0,0)) # At each main-loop fill the whole screen with black.
        alph += 0.5 # Increment alpha by a really small value (To make it slower, try 0.01)
        alphaSurface.set_alpha(alph) # Set the incremented alpha-value to the custom surface.
        screen.blit(alphaSurface,(0,0)) # Blit it to the screen-surface (Make them separate)

        # Trivial pygame stuff.
        if key.get_pressed()[K_RETURN]:
            DONE = True
        for ev in event.get():
            if ev.type == QUIT:
                quit()
        display.flip() # Flip the whole screen at each frame.
