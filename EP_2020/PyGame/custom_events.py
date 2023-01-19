# Python program to add Custom Events
import pygame

pygame.init()

# Setting up the screen and timer
okno = pygame.display.set_mode((500, 500))
hodiny = pygame.time.Clock()

# set title
pygame.display.set_caption("Custom Events")

# defining colours
BILA = (255, 255, 255)
CERVENA = (255, 0, 0)
ZELENA = (0, 255, 0)
MODRA = (0, 0, 255)

# Keep a track of active variable
barva_pozadi = BILA
okno.fill(BILA)

# námi vytvořený event na změnu barvy
ZMEN_BARVU = pygame.USEREVENT + 1

# vytvořený event pro změnu velikosti čtverce
NA_CTVERCI = pygame.USEREVENT + 2

ctverec = pygame.Rect((225, 225, 50, 50))
roste = True

# nastavení eventu na změnu barvy každých 500ms
# stav můžeme sledovat v pygame.event.get() cylku
pygame.time.set_timer(ZMEN_BARVU, 500)

fps = 60
running = True
while running:

    for event in pygame.event.get():

        # každých 500ms změníme barvu
        if event.type == ZMEN_BARVU:
            if barva_pozadi == ZELENA:
                okno.fill(ZELENA)
                barva_pozadi = BILA
            elif barva_pozadi == BILA:
                okno.fill(BILA)
                barva_pozadi = ZELENA

        if event.type == NA_CTVERCI:

            # zvětšení čtverce
            if roste:
                ctverec.inflate_ip(3, 3)
                roste = ctverec.width < 75
            else:
                ctverec.inflate_ip(-3, -3)
                roste = ctverec.width < 50

        if event.type == pygame.QUIT:
            running = False

    # zaregistrování eventu pro další frame
    # stav můžeme sledovat v pygame.event.get() cylku
    if ctverec.collidepoint(pygame.mouse.get_pos()):
        pygame.event.post(pygame.event.Event(NA_CTVERCI))

    pygame.draw.rect(okno, CERVENA, ctverec)
    pygame.display.update()
    hodiny.tick(fps)

pygame.quit()
