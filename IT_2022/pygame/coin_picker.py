# TODO: Vypsat skore na obrazovku
# TODO: Mince se smaže a objeví se nová na jiném místě (ne jednom přemístění)
# TODO: Přidat eventy pro změnu barvy mince, hráče, pozadí
# TODO: Mince bude textura
# TODO: Časový limit (?)

import random

import pygame as pg

pg.init()

OKNO_SIRKA = 800
OKNO_VYSKA = 600

CERNA = (0, 0, 0)
BILA = (255, 255, 255)


clock = pg.time.Clock()
FPS = 60

pocet_minci = 0


class Hrac:
    def __init__(self, souradnice, rozmer, barva, rychlost=5):
        self.__x = souradnice[0]
        self.__y = souradnice[1]
        self.velikost_x = rozmer[0]
        self.velikost_y = rozmer[1]
        self.barva = barva
        self.rychlost = rychlost

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, hodnota):
        if hodnota < 0:
            self.__x = 0
        elif hodnota > OKNO_SIRKA - self.velikost_x:
            self.__x = OKNO_SIRKA - self.velikost_x
        else:
            self.__x = hodnota

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, hodnota):
        if hodnota < 0:
            self.__y = 0
        elif hodnota > OKNO_VYSKA - self.velikost_y:
            self.__y = OKNO_VYSKA - self.velikost_y
        else:
            self.__y = hodnota

    def pohyb(self, stisknute_klavesy):
        if stisknute_klavesy[pg.K_LEFT]:
            self.x -= self.rychlost
        if stisknute_klavesy[pg.K_RIGHT]:
            self.x += self.rychlost
        if stisknute_klavesy[pg.K_UP]:
            self.y -= self.rychlost
        if stisknute_klavesy[pg.K_DOWN]:
            self.y += self.rychlost

    def vykresli(self, okno):
        pg.draw.rect(
            okno, self.barva, (self.x, self.y, self.velikost_x, self.velikost_y)
        )


class Coin:
    def __init__(self, souradnice, velikost, barva):
        self.x = souradnice[0]
        self.y = souradnice[1]
        self.velikost = velikost
        self.barva = barva

    def vykresli(self, okno):
        pg.draw.circle(okno, self.barva, (self.x, self.y), self.velikost)


def kolize(objekt1, objekt2):
    # objekt1 je hrac
    # objekt2 je mince
    hrac_x1 = objekt1.x
    hrac_x2 = objekt1.x + objekt1.velikost_x

    hrac_y1 = objekt1.y
    hrac_y2 = objekt1.y + objekt1.velikost_y

    mince_x1 = objekt2.x - objekt2.velikost
    mince_x2 = objekt2.x + objekt2.velikost

    mince_y1 = objekt2.y - objekt2.velikost
    mince_y2 = objekt2.y + objekt2.velikost

    if hrac_x1 < mince_x2 and hrac_x2 > mince_x1:
        if hrac_y1 < mince_y2 and hrac_y2 > mince_y1:
            return True
    return False


H1 = Hrac((100, 100), (50, 50), BILA)
C1 = Coin((200, 200), 10, (255, 255, 0))


okno = pg.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

pg.display.set_caption("Muj prvni program v Pygame")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    stisknute_klavesy = pg.key.get_pressed()

    H1.pohyb(stisknute_klavesy)

    if kolize(H1, C1):
        C1.x = random.randint(0, OKNO_SIRKA - C1.velikost)
        C1.y = random.randint(0, OKNO_VYSKA - C1.velikost)
        pocet_minci += 1
        print(f"Kolize! Pocet minci: {pocet_minci}")

    okno.fill(CERNA)
    # vykresleni ctverce
    C1.vykresli(okno)
    H1.vykresli(okno)

    pg.display.flip()
    clock.tick(FPS)
