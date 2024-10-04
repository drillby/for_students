import math

import pygame

pygame.init()

OKNO_VYSKA = 600
OKNO_SIRKA = 800

BILA = (255, 255, 255)
MODRA = (0, 0, 255)

hodiny = pygame.time.Clock()
FPS = 60


class Hrac:
    def __init__(self, rozmer, pozice, barva, rychlost=5):
        self.rozmer = rozmer
        self.pozice = pozice
        self.barva = barva
        self.rychlost = rychlost

    def vykresli(self, okno):
        pygame.draw.rect(okno, self.barva, (*self.pozice, *self.rozmer))
        # pygame.draw.rect(okno, self.barva, (self.pozice[0], self.pozice[1], self.rozmer[0], self.rozmer[1]))

    def pohyb(self, stisknute_klavesy):
        move_x = 0
        move_y = 0
        if stisknute_klavesy[pygame.K_LEFT]:
            move_x = -self.rychlost
        if stisknute_klavesy[pygame.K_RIGHT]:
            move_x = self.rychlost
        if stisknute_klavesy[pygame.K_UP]:
            move_y = -self.rychlost
        if stisknute_klavesy[pygame.K_DOWN]:
            move_y = self.rychlost

        direction = [move_x, move_y]
        if abs(direction[0]) == self.rychlost and abs(direction[1]) == self.rychlost:
            direction[0] *= 1 / math.sqrt(2)
            direction[1] *= 1 / math.sqrt(2)

        self.pozice[0] += direction[0]
        self.pozice[1] += direction[1]

    def zkontroluj_hranice(self):
        if self.pozice[0] < 0:
            self.pozice[0] = 0
        if self.pozice[1] < 0:
            self.pozice[1] = 0
        if self.pozice[0] > OKNO_SIRKA - self.rozmer[0]:
            self.pozice[0] = OKNO_SIRKA - self.rozmer[0]
        if self.pozice[1] > OKNO_VYSKA - self.rozmer[1]:
            self.pozice[1] = OKNO_VYSKA - self.rozmer[1]


# Vytvoření okna
okno = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

# Nastavení titulku okna
pygame.display.set_caption("Můj první program v Pygame")

H1 = Hrac((50, 50), [100, 100], MODRA)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    stisknute_klavesy = pygame.key.get_pressed()

    H1.pohyb(stisknute_klavesy)
    H1.zkontroluj_hranice()

    okno.fill(BILA)
    # Obnovení okna
    H1.vykresli(okno)
    pygame.display.flip()
    hodiny.tick(FPS)
