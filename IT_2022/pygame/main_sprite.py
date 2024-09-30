import pygame as pg
from pygame.sprite import Sprite, Group
import math
import random

pg.init()

OKNO_SIRKA = 800
OKNO_VYSKA = 600

okno = pg.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

pg.display.set_caption("Coin Picker")

FPS = 60
clock = pg.time.Clock()

CERNA = (0, 0, 0)
BILA = (255, 255, 255)

MINCE_START = 3

class GameObject(Sprite):
    def __init__(self, x, y, obrazek, scale=1):
        super().__init__()
        self.image = pg.image.load(obrazek)
        self.image = pg.transform.scale(
            self.image,
            (int(self.image.get_width() * scale), int(self.image.get_height() * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Hrac(GameObject):
    def __init__(self, x, y, obrazek, rychlost, scale=1):
        super().__init__(x, y, obrazek, scale)
        self.rychlost = rychlost

    def pohyb(self):
        stisknute_klavesy = pg.key.get_pressed()
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

        self.rect.x += direction[0]
        self.rect.y += direction[1]

    def zkontroluj_hranice(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > OKNO_SIRKA - self.rect.width:
            self.rect.x = OKNO_SIRKA - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > OKNO_VYSKA - self.rect.height:
            self.rect.y = OKNO_VYSKA - self.rect.height

    def update(self):
        self.pohyb()

        self.zkontroluj_hranice()

class Mince(GameObject):
    def __init__(self, x, y, obrazek, scale=1):
        super().__init__(x, y, obrazek, scale)



H1 = Hrac(OKNO_SIRKA // 2, OKNO_VYSKA // 2, "sprites/truhla.png", 5)
hrac_group = Group()
hrac_group.add(H1)

mince_group = Group()

for _ in range(MINCE_START):
    x = random.randint(0, OKNO_SIRKA - 50)
    y = random.randint(0, OKNO_SIRKA - 50)
    mince_group.add(
        Mince(x, y, "sprites/mince.png", scale=0.1)
    )


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    hrac_group.update()

    pg.sprite.spritecollide(H1, mince_group, True)


    okno.fill(BILA)
    hrac_group.draw(okno)
    mince_group.draw(okno)

    pg.display.flip()
    clock.tick(FPS)