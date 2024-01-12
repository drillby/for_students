import random

import pygame

VELIKOST_OKNA = (800, 480)

GRAVITACE = 1

class Micek:
    def __init__(self, pozice, rychlost, hmotnost, barva, polomer):
        self.pozice = pozice
        self.rychlost = rychlost
        self.hmotnost = hmotnost
        self.barva = barva
        self.polomer = polomer

    def posun_se(self):
        self.pozice[1] = self.pozice[1] + self.rychlost[1]
        self.pozice[0] = self.pozice[0] + self.rychlost[0]

        return self

    def vypocti_rychlost(self):
        self.rychlost[1] = self.rychlost[1] + GRAVITACE

        return self

    def zkontoruj_odrazy(self):
        if self.pozice[1] > VELIKOST_OKNA[1] - self.polomer:
            self.rychlost[1] *= -1

        if self.pozice[0] < 0 + self.polomer:
            self.rychlost[0] *= -1

        if self.pozice[0] > VELIKOST_OKNA[0] - self.polomer:
            self.rychlost[0] *= -1

        return self

    def vykresli(self, okno):
        self.pozice = [int(self.pozice[0]), int(self.pozice[1])]
        pygame.draw.circle(okno, self.barva, self.pozice, self.polomer, 2)

        return self


pozice = [random.randint(20,VELIKOST_OKNA[0]-20), random.randint(20,VELIKOST_OKNA[1]-20)]
rychlost = [-1, 1]
hmotnost = 1
cervena = (255, 0, 0)
prumer = 10

pozice2 = [600, 300]
rychlost2 = [1, -1]
hmotnost2 = 2
modra = (0, 0, 255)
prumer2 = 20

micek1 = Micek(pozice, rychlost, hmotnost, cervena, prumer)
micek2 = Micek(pozice2, rychlost2, hmotnost2, modra, prumer2)

# Inicializuj PyGame
pygame.init()

# Vytvoř okno pro hru
velikost_okna = (800, 480)
okno = pygame.display.set_mode(velikost_okna)


fps = 60
hodiny = pygame. time.Clock()

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

    okno.fill((0, 0, 0))
    micek1.zkontoruj_odrazy().vypocti_rychlost().posun_se().vykresli(okno)

    micek2.zkontoruj_odrazy()
    micek2.vypocti_rychlost()
    micek2.posun_se()




    micek2.vykresli(okno)

    # Aktualizuj okno
    hodiny.tick(fps)
    pygame.display.flip()


# Ukonči PyGame
pygame.quit()
