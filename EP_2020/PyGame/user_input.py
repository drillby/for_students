import pygame

# Inicializuj PyGame
pygame.init()

# Vytvoř okno pro hru
velikost_okna = (800, 480)
okno = pygame.display.set_mode(velikost_okna)

velikost_ctverce = (20, 20)
pozice_ctverce = [200, 200] # pole kvůli změně pozice
rychlost_ctverce_x = 10
rychlost_ctverce_y = 10

cervena = (255, 0, 0)

# vytvoření objektu pro úpravu obnovovací frekvence
hodiny = pygame.time.Clock()
fps = 60

# Nastav název okna
pygame.display.set_caption("Název hry")

# Nastav počáteční stav hry
running = True

# Hlavní herní smyčka
while running:
    # Zpracuj události
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
            # při stisknutí klávesy změna souřadnice čtverce
            if event.key == pygame.K_d:
                pozice_ctverce[0] += rychlost_ctverce_x
            if event.key == pygame.K_w:
                pozice_ctverce[1] -= rychlost_ctverce_y
            if event.key == pygame.K_s:
                pozice_ctverce[1] += rychlost_ctverce_y
            if event.key == pygame.K_a:
                pozice_ctverce[0] -= rychlost_ctverce_x

    # kolize na pravé straně okna (+ velikost_crverec kvůli vykompenzování souřadnic)
    if pozice_ctverce[0] + velikost_ctverce[0] > velikost_okna[0]:
        # pozice = [maximální povolená pozice x, y neměním]
        pozice_ctverce = [velikost_okna[0] - velikost_ctverce[0], pozice_ctverce[1]]

    elif pozice_ctverce[0] < 0:
        # pozice = [maximální povolená pozice x, y neměním]
        pozice_ctverce = [0, pozice_ctverce[1]]
    
    # stejný princip jako u x souřadnice
    if pozice_ctverce[1] + velikost_ctverce[1] > velikost_okna[1]: 
        pozice_ctverce = [pozice_ctverce[0], velikost_okna[1] - velikost_ctverce[1]]

    elif pozice_ctverce[1] < 0:
        pozice_ctverce = [pozice_ctverce[0], 0]

    pygame.draw.rect(
        okno, cervena, (*pozice_ctverce, *velikost_ctverce), 0
    )  # kam, barva, velikost, šířka okraje (0 = vyplňeno)

    # omezení omezovací frekvence na 60fps
    hodiny.tick(fps)
    # Aktualizuj okno
    pygame.display.flip()
    okno.fill((0, 0, 0))

# Ukonči PyGame
pygame.quit()