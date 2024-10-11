# TODO: zrychlit pohyb hada když skore%10 == 0
# TODO: vypsat skore na obrazovku

import random

import pygame

pygame.init()

OKNO_VYSKA = 600
OKNO_SIRKA = 800

BILA = (255, 255, 255)
MODRA = (0, 0, 255)
CERVENA = (255, 0, 0)

hodiny = pygame.time.Clock()
FPS = 60

MOVE_SNAKE_SEC = 0.5
MOVE_SNAKE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE_EVENT, int(MOVE_SNAKE_SEC * 1000))

skore = 0


class GameObject:
    def __init__(self, rozmer, pozice, barva):
        self.rozmer = rozmer
        self.pozice = pozice
        self.barva = barva

    def vykresli(self, okno):
        pygame.draw.rect(okno, self.barva, (*self.pozice, *self.rozmer))


class Apple(GameObject):
    def __init__(self, rozmer, pozice, barva):
        super().__init__(rozmer, pozice, barva)

    def zkontroluj_kolizi(self, hrac):
        return hrac.pozice == self.pozice


class Snake(GameObject):
    def __init__(self, rozmer, pozice, barva):
        super().__init__(rozmer, pozice, barva)
        self.smer_pohybu = [0, 0]  # [x, y]

    def zjisteni_smeru(self, stisknute_klavesy):
        if stisknute_klavesy[pygame.K_LEFT]:
            self.smer_pohybu[0] = -1
            self.smer_pohybu[1] = 0
        elif stisknute_klavesy[pygame.K_RIGHT]:
            self.smer_pohybu[0] = 1
            self.smer_pohybu[1] = 0

        if stisknute_klavesy[pygame.K_UP]:
            self.smer_pohybu[1] = -1
            self.smer_pohybu[0] = 0
        elif stisknute_klavesy[pygame.K_DOWN]:
            self.smer_pohybu[1] = 1
            self.smer_pohybu[0] = 0

    def pohyb(self):
        self.pozice[0] += self.smer_pohybu[0] * self.rozmer[0]
        self.pozice[1] += self.smer_pohybu[1] * self.rozmer[1]

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

H1 = Snake((50, 50), [100, 100], MODRA)
A1 = Apple((50, 50), [200, 200], CERVENA)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOVE_SNAKE_EVENT:
            H1.pohyb()
            H1.zkontroluj_hranice()

    stisknute_klavesy = pygame.key.get_pressed()

    H1.zjisteni_smeru(stisknute_klavesy)

    if A1.zkontroluj_kolizi(H1):
        skore += 1
        seznam_x = [i for i in range(0, OKNO_SIRKA, A1.rozmer[0])]
        seznam_y = list(range(0, OKNO_VYSKA, A1.rozmer[1]))
        A1.pozice = [random.choice(seznam_x), random.choice(seznam_y)]

    okno.fill(BILA)
    # Obnovení okna
    H1.vykresli(okno)
    A1.vykresli(okno)
    pygame.display.flip()
    hodiny.tick(FPS)
