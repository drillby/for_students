import random
from os import PathLike
from typing import Tuple

import pygame


class Zamerovac(pygame.sprite.Sprite):
    def __init__(self, obrazek_cesta: PathLike):
        super().__init__()
        self.image = pygame.image.load(obrazek_cesta)
        self.rect = self.image.get_rect()
        self.zvuk = pygame.mixer.Sound("vystrel.wav")

    def vystrel(self):
        self.zvuk.play()
        pygame.sprite.spritecollide(zamerovac, cil_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Cil(pygame.sprite.Sprite):
    def __init__(self, obrazek_cesta: PathLike, poz_x: int, poz_y: int):
        super().__init__()
        self.image = pygame.image.load(obrazek_cesta)
        self.rect = self.image.get_rect()
        self.rect.center = [poz_x, poz_y]

    def update(self):
        pocet_cilu = len(cil_group)
        if pocet_cilu < MAX_CILU:
            for _ in range(MAX_CILU - pocet_cilu):
                cil = Cil(
                    "cil.png",
                    random.randrange(0, rozmery_okna[0]),
                    random.randrange(0, rozmery_okna[1]),
                )
                cil_group.add(cil)


pygame.init()

hodiny = pygame.time.Clock()
fps = 60

MODRA = (0, 0, 255)

MAX_CILU = 10

rozmery_okna = (800, 600)
okno = pygame.display.set_mode(rozmery_okna)
pygame.mouse.set_visible(False)

zamerovac = Zamerovac("zamerovac.png")
zamerovac_group = pygame.sprite.Group()
zamerovac_group.add(zamerovac)

cil_group = pygame.sprite.Group()
for _ in range(MAX_CILU):
    novy_cil = Cil(
        "cil.png",
        random.randrange(0, rozmery_okna[0]),
        random.randrange(0, rozmery_okna[1]),
    )
    cil_group.add(novy_cil)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            zamerovac.vystrel()

    okno.fill(MODRA)
    cil_group.draw(okno)
    zamerovac_group.draw(okno)
    zamerovac_group.update()
    cil_group.update()

    pygame.display.flip()
    hodiny.tick(fps)
