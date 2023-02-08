import pygame as pg
import random

OKNO_SIRKA = 1000
OKNO_VYSKA = 800

CERNA = (0, 0, 0)
CERVENA = (255, 0, 0)
MODRA = (0, 0, 255)

GRAVITACE = 1
ODPOR = 1

zrychleni_x = 0

x = random.randint(100, 500)
y = random.randint(100, 500)
rychlost_x = 3
rychlost_y = 2


class Micek:
    def __init__(
        self, pozice: list, rychlost: list, hmotnost: int, odpor: int, barva: tuple
    ):
        self.pozice = pozice  # [x, y]
        self.rychlost = rychlost  # [r_x, r_y]
        self.hmotnost = hmotnost
        self.odpor = odpor
        self.barva = barva

    # v=a*t
    # x=1/2att
    def posun_se(self):

        self.rychlost[0] = self.rychlost[0] - abs(self.odpor)  # počítá rychlost na x
        self.rychlost[1] = self.rychlost[1] + (GRAVITACE * self.hmotnost * cas)

        self.pozice[0] = self.pozice[0] + self.rychlost[0]  # počítá pozici na x
        # self.pozice[1] = self.pozice[1] + (0.5 * GRAVITACE * self.hmotnost * cas**2)
        self.pozice[1] = self.pozice[1] + self.rychlost[1]
        # if self.rychlost[0] <= 0:
        #     self.rychlost[0] = 0
        # zastaví míček aby rychlost nebyla menší než 0

        if self.pozice[0] + 10 >= OKNO_SIRKA:
            self.rychlost[0] = -self.rychlost[0]
            # self.odpor = -self.odpor
            # odraží míček od stěny

        if self.pozice[0] - 10 <= 0:
            self.rychlost[0] = -self.rychlost[0]
            # self.odpor = -self.odpor
            # odráží míček od stěny

        if self.pozice[1] + 10 >= OKNO_VYSKA:
            self.rychlost[1] = -self.rychlost[1]
            # mění směr rychlosti na y, odráží míček od země

        self.odpor = self.odpor * 0.75

    def vykreli(self):
        int(self.pozice[0])
        pg.draw.circle(
            okno,
            self.barva,
            [int(self.pozice[0]), int(self.pozice[1])],
            10,
            2,
        )


pg.init()

hodiny = pg.time.Clock()
fps = 60
cas = 1 / fps

pg.display.set_caption("Fyzikální simualce - pygame")
okno = pg.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

okno.fill(CERNA)

micek = Micek([x, y], [rychlost_x, rychlost_y], 100, 1, CERVENA)
micek.vykreli()

micek2 = Micek([200, 500], [-2, 3], 50, 4, MODRA)
micek2.vykreli()

running = True
while running:
    klavesa = pg.key.get_pressed()  # {k_a: True, k_b: False ...}
    udalosti = pg.event.get()
    for event in udalosti:
        if event.type == pg.QUIT:
            running = False

        elif klavesa[pg.K_ESCAPE]:
            running = False

    okno.fill(CERNA)
    micek.posun_se()
    micek.vykreli()
    micek2.posun_se()
    micek2.vykreli()

    hodiny.tick(fps)
    pg.display.update()

pg.quit()
