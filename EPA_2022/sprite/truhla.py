import pygame as pg

pg.init()

OKNO_SIRKA = 800
OKNO_VYSKA = 600

BILA = (255, 255, 255)

okno = pg.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))
pg.display.set_caption("Truhla")


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


class Mince(GameObject):
    def __init__(self, x, y, obrazek, scale):
        super().__init__(x, y, obrazek, scale)


H1 = Hrac(100, 100, 5, "sprites/truhla.png", 1)

M1 = Mince(200, 200, "sprites/mince.png", 0.1)
M2 = Mince(300, 300, "sprites/mince.png", 0.1)
M3 = Mince(400, 400, "sprites/mince.png", 0.1)

mince_group = pg.sprite.Group()
hrac_group = pg.sprite.Group()
hrac_group.add(H1)

mince_group.add(M1)
mince_group.add(M2)
mince_group.add(M3)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    okno.fill(BILA)
    hrac_group.draw(okno)
    mince_group.draw(okno)
    pg.display.flip()
pg.quit()
