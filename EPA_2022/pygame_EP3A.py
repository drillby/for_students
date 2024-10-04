import pygame

pygame.init()

OKNO_VYSKA = 600
OKNO_SIRKA = 800

BILA = (255, 255, 255)
MODRA = (0, 0, 255)
#                       x   y
souradnice_ctverec = [100, 100]
velikost_ctverec = [200, 200]

# Vytvoření okna
okno = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

# Nastavení titulku okna
pygame.display.set_caption("Můj první program v Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    stisknute_klavesy = pygame.key.get_pressed()

    if stisknute_klavesy[pygame.K_LEFT]:
        souradnice_ctverec[0] -= 1
    if stisknute_klavesy[pygame.K_RIGHT]:
        souradnice_ctverec[0] += 1
    if stisknute_klavesy[pygame.K_UP]:
        souradnice_ctverec[1] -= 1
    if stisknute_klavesy[pygame.K_DOWN]:
        souradnice_ctverec[1] += 1

    okno.fill(BILA)
    pygame.draw.rect(
        okno,
        MODRA,
        (
            # souradnice_ctverec[0],
            # souradnice_ctverec[1],
            # velikost_ctverec[0],
            # velikost_ctverec[1],
            *souradnice_ctverec,
            *velikost_ctverec,
        ),
    )
    # Obnovení okna
    pygame.display.flip()
