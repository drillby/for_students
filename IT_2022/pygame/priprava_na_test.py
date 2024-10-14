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

BILA = (255, 255, 255)
CERNA = (0, 0, 0)

skore_font = pg.font.Font('freesansbold.ttf', 32)
game_over_font = pg.font.Font('freesansbold.ttf', 46)


GAME_OVER_EVENT = pg.USEREVENT + 1
game_over_event = pg.event.Event(GAME_OVER_EVENT)


SPAWN_STRELA_SEC = 1
SPAWN_STRELA_EVENT = pg.USEREVENT + 2
pg.time.set_timer(SPAWN_STRELA_EVENT, SPAWN_STRELA_SEC * 1000)


RESTART_GAME_EVENT = pg.USEREVENT + 3
restart_game_event = pg.event.Event(RESTART_GAME_EVENT)

ULTIMATE_CHARGE_SEC = 3
ULTIMATE_CHARGE_EVENT = pg.USEREVENT + 4
pg.time.set_timer(ULTIMATE_CHARGE_EVENT, ULTIMATE_CHARGE_SEC * 1000)

pocet_bodu = 0


game_over = False
can_use_u = False

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
        if stisknute_klavesy[pg.K_UP]:
            self.rect.y -= self.rychlost
        if stisknute_klavesy[pg.K_DOWN]:
            self.rect.y += self.rychlost

    def zkontroluj_hranice(self):
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > OKNO_VYSKA - self.rect.height:
            self.rect.y = OKNO_VYSKA - self.rect.height

    def update(self):
        self.pohyb()

        self.zkontroluj_hranice()

class Strela(GameObject):
    def __init__(self, x, y, obrazek, rychlost, scale=1):
        super().__init__(x, y, obrazek, scale)
        self.rychlost = rychlost

    def update(self):
        self.rect.x -= self.rychlost

        if self.rect.x < 0:
            self.rect.x = OKNO_SIRKA
            # self.kill()
            global pocet_bodu
            pocet_bodu += 1


def spawn_strela(strely_group):
    if len(strely_group) < 1:
        y = random.randint(0, OKNO_VYSKA - 50)
        nova_strela = Strela(OKNO_SIRKA, y, "sprites/mince.png", 5, scale=0.1)
        strely_group.add(nova_strela)
        return

    while True:
        y = random.randint(0, OKNO_VYSKA - 50)
        nova_strela = Strela(OKNO_SIRKA, y, "sprites/mince.png",5, scale=0.1)

        koliduje = False
        for mince in strely_group:
            if nova_strela.rect.colliderect(mince.rect):
                koliduje = True
                break

        if not koliduje:
            strely_group.add(nova_strela)
            break



H1 = Hrac(20, OKNO_VYSKA // 2, "sprites/truhla.png", 5)
hrac_group = Group()
hrac_group.add(H1)

strely_group = Group()



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == GAME_OVER_EVENT:
            game_over = True

        if event.type == SPAWN_STRELA_EVENT\
                and not game_over:
            spawn_strela(strely_group)
            # strela = Strela(OKNO_SIRKA, random.randint(0, OKNO_VYSKA), "sprites/mince.png", 5, 0.1)
            # strely_group.add(strela)


        if event.type == pg.MOUSEBUTTONDOWN\
                and event.button == 1\
                and game_over\
                and text_restart_game_rect.collidepoint(event.pos):
            pg.event.post(restart_game_event)

        if event.type == RESTART_GAME_EVENT:
            game_over = False

            H1.rect.x = 20
            H1.rect.y = OKNO_VYSKA // 2
            hrac_group.add(H1)

            pocet_bodu = 0

            pg.time.set_timer(ULTIMATE_CHARGE_EVENT, ULTIMATE_CHARGE_SEC * 1000)

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and can_use_u:
            pocet_strel = len(strely_group)
            pocet_bodu += pocet_strel
            strely_group.empty()
            can_use_u = False
            pg.time.set_timer(ULTIMATE_CHARGE_EVENT, ULTIMATE_CHARGE_SEC * 1000)

        if event.type == ULTIMATE_CHARGE_EVENT:
            can_use_u = True

    hrac_group.update()
    strely_group.update()

    if pg.sprite.spritecollide(H1, strely_group, True):
        pg.event.post(game_over_event)


    okno.fill(BILA)
    hrac_group.draw(okno)
    strely_group.draw(okno)


    text_skore = skore_font.render(f"Skóre: {pocet_bodu}", True, CERNA, BILA)
    okno.blit(text_skore, (10, 10))


    text_skore = skore_font.render("U" if can_use_u else "N", True, CERNA, BILA)
    okno.blit(text_skore, (OKNO_SIRKA - 30, 10))


    if game_over:
        strely_group.empty()
        hrac_group.empty()

        okno.fill(CERNA)
        text_game_over = game_over_font.render(f"KONEC HRY! Skóre: {pocet_bodu}", True, BILA, CERNA)
        text_game_over_rect = text_game_over.get_rect()
        text_game_over_rect.center = (OKNO_SIRKA // 2, OKNO_VYSKA // 2)
        okno.blit(text_game_over, text_game_over_rect)

        text_restart_game = skore_font.render("Stiskni pro restart hry!", True, BILA, CERNA)
        text_restart_game_rect = text_restart_game.get_rect()
        text_restart_game_rect.center = (OKNO_SIRKA // 2, OKNO_VYSKA // 2 + text_game_over_rect.height)
        okno.blit(text_restart_game, text_restart_game_rect)


    pg.display.flip()
    clock.tick(FPS)
