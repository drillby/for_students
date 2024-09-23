# TODO: Přidat eventy pro změnu barvy mince, hráče, pozadí
# TODO: Mince bude textura
# TODO: Restart button

import random
import math
import pygame as pg

pg.init()

OKNO_SIRKA = 800
OKNO_VYSKA = 600

CERNA = (0, 0, 0)
BILA = (255, 255, 255)
ZLUTA = (255, 255, 0)

VELIKOST_MINCE = 10

POCET_MINCI_START = 3
MAX_POCET_MINCI = 10


clock = pg.time.Clock()
FPS = 60

GAME_OVER_SEC = 20
GAME_OVER_EVENT = pg.USEREVENT + 1
pg.time.set_timer(GAME_OVER_EVENT, GAME_OVER_SEC * 1000)

SPAWN_COIN_SEC = 1
SPAWN_COIN_EVENT = pg.USEREVENT + 2
pg.time.set_timer(SPAWN_COIN_EVENT, SPAWN_COIN_SEC * 1000)

# TODO: dodělat event na změnu barvy pozadí po sebrání mince
CHANGE_BG_EVENT = pg.USEREVENT + 3
change_bg_event = pg.event.Event(CHANGE_BG_EVENT)
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pg.font.Font('freesansbold.ttf', 32)
font_game_over = pg.font.Font('freesansbold.ttf', 64)
# create a text surface object,
# on which text is drawn on it.
pocet_minci = 0


class GameObject:
    def __init__(self, souradnice, barva):
        self.__x = souradnice[0]
        self.__y = souradnice[1]
        self.barva = barva


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


class Hrac(GameObject):
    def __init__(self, souradnice, rozmer, barva, rychlost=5):
        super().__init__(souradnice, barva)
        self.velikost_x = rozmer[0]
        self.velikost_y = rozmer[1]
        self.rychlost = rychlost

    def pohyb(self, stisknute_klavesy):
        move_x = 0
        move_y = 0
        if stisknute_klavesy[pg.K_LEFT]:
            move_x = -self.rychlost
        if stisknute_klavesy[pg.K_RIGHT]:
            move_x = self.rychlost
        if stisknute_klavesy[pg.K_UP]:
            move_y = -self.rychlost
        if stisknute_klavesy[pg.K_DOWN]:
            move_y = self.rychlost

        direction = [move_x, move_y]
        if (abs(direction[0]) == self.rychlost and abs(direction[1]) == self.rychlost):
            direction[0] *= 1 / math.sqrt(2)
            direction[1] *= 1 / math.sqrt(2)

        self.x += direction[0]
        self.y += direction[1]


    def vykresli(self, okno):
        pg.draw.rect(
            okno, self.barva, (self.x, self.y, self.velikost_x, self.velikost_y)
        )


class Coin(GameObject):
    def __init__(self, souradnice, velikost, barva):
        super().__init__(souradnice, barva)
        self.velikost = velikost

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


def vypis(napis, barva_textu, barva_pozadi, font, origin_point, pozice):
    text = font.render(napis, True, barva_textu, barva_pozadi)
    textRect = text.get_rect()
    if origin_point == "topleft":
        textRect.topleft == pozice
    elif origin_point == "center":
        textRect.center == pozice
    else:
        raise ValueError("Nesprávná hodnota origin_poin")

    return text, textRect


H1 = Hrac((100, 100), (50, 50), BILA)
mince = []

for _ in range(POCET_MINCI_START):
    x = random.randint(0, OKNO_SIRKA - (2 * VELIKOST_MINCE))
    y = random.randint(0, OKNO_SIRKA - (2 * VELIKOST_MINCE))
    mince.append(
        Coin((x, y), VELIKOST_MINCE, ZLUTA)
    )


okno = pg.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

pg.display.set_caption("Muj prvni program v Pygame")

muze_hybat = True
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == GAME_OVER_EVENT:
            muze_hybat = False
        if event.type == SPAWN_COIN_EVENT:
            if len(mince) < MAX_POCET_MINCI:
                x = random.randint(0, OKNO_SIRKA - (2 * VELIKOST_MINCE))
                y = random.randint(0, OKNO_VYSKA - (2 * VELIKOST_MINCE))
                mince.append(
                    Coin((x, y), VELIKOST_MINCE, ZLUTA)
                )

    stisknute_klavesy = pg.key.get_pressed()

    if muze_hybat:
        H1.pohyb(stisknute_klavesy)
        napis = 'Počet mincí: {pocet_minci}'.format(pocet_minci=pocet_minci)
        text, textRect = vypis(napis, BILA, CERNA, font, "topleft", (10, 10))

    for idx, coin in enumerate(mince):
        if kolize(H1, coin):
            mince.pop(idx)
            pocet_minci += 1

    okno.fill(CERNA)


    # vykresleni ctverce
    if muze_hybat:
        for coin in mince:
            coin.vykresli(okno)
        H1.vykresli(okno)

    if not muze_hybat:
        napis = 'KONEC HRY! Počet mincí: {pocet_minci}'.format(pocet_minci=pocet_minci)
        text, textRect = vypis(napis, BILA, CERNA, font_game_over, "center", (OKNO_SIRKA // 2, OKNO_VYSKA // 2))

    okno.blit(text, textRect)

    pg.display.flip()
    clock.tick(FPS)