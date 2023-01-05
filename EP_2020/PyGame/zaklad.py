import pygame

# Inicializuj PyGame
pygame.init()

# Vytvoř okno pro hru
velikost_okna = (800, 480)
okno = pygame.display.set_mode(velikost_okna)

# velokost_ctverce = (20, 20)
# pozice_ctverce = (200, 200)

# cervena = (255, 0, 0)

obrazek_auto = pygame.image.load("./auto.png")
pozice_auta = (200, 200)

# Nastav název okna
pygame.display.set_caption("Název hry")

# Nastav počáteční stav hry
running = True

# Hlavní herní smyčka
# TODO: automatický pohyb čtverce, pohyb pomocí klávesnoce, detekce okrajů obrazovky
while running:
    # Zpracuj události
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # pygame.draw.rect(
    #     okno, cervena, pozice_ctverce, 0
    # )  # kam, barva, velikost, šířka okraje (0 = vyplňeno)

    # vykteslí obrázek auta na okno na zadanou pozici
    # okno.blit(obrazek_auto, pozice_auta)

    # Aktualizuj okno
    pygame.display.flip()

# Ukonči PyGame
pygame.quit()
