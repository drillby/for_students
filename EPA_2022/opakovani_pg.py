import math

import pygame as pg

pg.init()

OKNO_SIRKA = 800
OKNO_VYSKA = 600

BILA = (255, 255, 255)
CERNA = (0, 0, 0)

okno = pg.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))
pg.display.set_caption("Truhla")

hodiny = pg.time.Clock()
FPS = 60


class GameObject(pg.sprite.Sprite):
    def __init__(self, x, y, obrazek, scale=1):
        super().__init__()
        self.image = pg.image.load(obrazek)
        self.image = pg.transform.scale(
            self.image,
            (int(self.image.get_width() * scale), int(self.image.get_height() * scale)),
        )
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


class Hrac(GameObject):
    def __init__(self, x, y, rychlost, obrazek, scale):
        super().__init__(x, y, obrazek, scale)
        self.rychlost = rychlost
        self.skore = 0

    def update(self):
        self.pohyb()
        self.zkontroluj_hranice()

    def pohyb(self):
        keys = pg.key.get_pressed()
        move_x = 0
        move_y = 0

        if keys[pg.K_LEFT]:
            move_x = -self.rychlost
        if keys[pg.K_RIGHT]:
            move_x = self.rychlost
        if keys[pg.K_UP]:
            move_y = -self.rychlost
        if keys[pg.K_DOWN]:
            move_y = self.rychlost

        direction = [move_x, move_y]
        if abs(direction[0]) == self.rychlost and abs(direction[1]) == self.rychlost:
            direction[0] *= 1 / math.sqrt(2)
            direction[1] *= 1 / math.sqrt(2)

        self.rect.x += direction[0]
        self.rect.y += direction[1]

    def zkontroluj_hranice(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > OKNO_SIRKA - self.rect.width:
            self.rect.x = OKNO_SIRKA - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > OKNO_VYSKA - self.rect.height:
            self.rect.y = OKNO_VYSKA - self.rect.height


H1 = Hrac(OKNO_SIRKA // 2, OKNO_VYSKA // 2, 5, "sprites/truhla.png", 1)
hrac_group = pg.sprite.Group()
hrac_group.add(H1)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    hrac_group.update()

    """
    if pg.sprite.spritecollide(H1, mince_group, True):
        H1.skore += 1
        print("Mince sebrána!")
    """

    okno.fill(BILA)
    hrac_group.draw(okno)

    pg.display.flip()
    hodiny.tick(FPS)
pg.quit()
