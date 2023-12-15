import pygame

# Inicializuj PyGame
pygame.init()

# Vytvoř okno pro hru
velikost_okna = (800, 480)
okno = pygame.display.set_mode(velikost_okna)

velikost_ctverce = (20, 60)
pozice_ctverce = [50, velikost_okna[1]//2-velikost_ctverce[1]//2]  # pole kvůli změně pozice
rychlost_ctverce = 2

rychlost_micku_x = 2
rychlost_micku_y = -2

velikost_micku = (20,20)

cervena = (255, 0, 0)

fps = 60
hodiny = pygame. time.Clock()

class Hrac:
    def __init__(self, pozice, barva, velikost_ctverce):
        self.pozice = pozice
        self.barva = barva
        self.velikost_ctverce = velikost_ctverce

    def vykresli(self, kam):
        pygame.draw.rect(kam, self.barva, (*self.pozice, *self.velikost_ctverce), 0)


h1 = Hrac([50, velikost_okna[1]//2-velikost_ctverce[1]//2], cervena, velikost_ctverce)
h2 = Hrac([750, velikost_okna[1]//2-velikost_ctverce[1]//2], cervena, velikost_ctverce)
micek = Hrac([velikost_okna[0]//2-velikost_micku[0]//2, velikost_okna[1]//2-velikost_micku[1]//2], cervena, velikost_micku)

# Nastav název okna
pygame.display.set_caption("Název hry")
pygame.key.set_repeat(0, 1)

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

    klavesy = pygame.key.get_pressed()
    if klavesy[pygame.K_w]:
        h1.pozice[1] -= rychlost_ctverce
    if klavesy[pygame.K_s]:
        h1.pozice[1] += rychlost_ctverce

    if klavesy[pygame.K_UP]:
        h2.pozice[1] -= rychlost_ctverce
    if klavesy[pygame.K_DOWN]:
        h2.pozice[1] += rychlost_ctverce

    micek.pozice[0] += rychlost_micku_x
    micek.pozice[1] += rychlost_micku_y

    if micek.pozice[1] < 0:
        rychlost_micku_y *= -1

    if micek.pozice[1] > velikost_okna[1] - micek.velikost_ctverce[1]:
        rychlost_micku_y *= -1

    if micek.pozice[1] in range(h2.pozice[1], h2.pozice[1]+h2.velikost_ctverce[1])\
            and micek.pozice[0]+micek.velikost_ctverce[0]== h2.pozice[0]:
        rychlost_micku_x *= -1

    if micek.pozice[1] in range(h1.pozice[1], h1.pozice[1]+h1.velikost_ctverce[1])\
            and micek.pozice[0]-micek.velikost_ctverce[0]== h1.pozice[0]:
        rychlost_micku_x *= -1


    if micek.pozice[0] < 0 or micek.pozice[0] > velikost_okna[0]:
        micek.pozice = [velikost_okna[0]//2-velikost_micku[0]//2, velikost_okna[1]//2-velikost_micku[1]//2]


    if h1.pozice[1] < 0:
        h1.pozice[1] = 0

    if h1.pozice[1] > velikost_okna[1]-h1.velikost_ctverce[1]:
        h1.pozice[1] = velikost_okna[1]-h1.velikost_ctverce[1]

    if h2.pozice[1] < 0:
        h2.pozice[1] = 0

    if h2.pozice[1] > velikost_okna[1]-h2.velikost_ctverce[1]:
        h2.pozice[1] = velikost_okna[1]-h2.velikost_ctverce[1]


    h1.vykresli(okno)
    h2.vykresli(okno)
    micek.vykresli(okno)

    # Aktualizuj okno
    hodiny.tick(fps)
    pygame.display.flip()
    okno.fill((0, 0, 0))

# Ukonči PyGame
pygame.quit()