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



GAME_OVER_SEC = 10
GAME_OVER_EVENT = pg.USEREVENT + 1
pg.time.set_timer(GAME_OVER_EVENT, GAME_OVER_SEC * 1000)

SPAWN_COIN_SEC = 1
SPAWN_COIN_EVENT = pg.USEREVENT + 2
pg.time.set_timer(SPAWN_COIN_EVENT, SPAWN_COIN_SEC * 1000)

RESTART_GAME_EVENT = pg.USEREVENT + 3
restart_game_event = pg.event.Event(RESTART_GAME_EVENT)



MINCE_START = 3

MAX_MINCE = 10

game_over = False

pocet_minci = 0


class GameObject(Sprite):
    def __init__(self, x, y, obrazek, scale=1):
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


def spawn_mince(mince_group, hrac):
    while True:
        x = random.randint(0, OKNO_SIRKA - 50)
        y = random.randint(0, OKNO_VYSKA - 50)
        nova_mince = Mince(x, y, "sprites/mince.png", scale=0.1)

        if nova_mince.rect.colliderect(hrac.rect):
            continue

        koliduje = False
        for mince in mince_group:
            if nova_mince.rect.colliderect(mince.rect):
                koliduje = True
                break

        if not koliduje:
            mince_group.add(nova_mince)
            break



H1 = Hrac(OKNO_SIRKA // 2, OKNO_VYSKA // 2, "sprites/truhla.png", 5)
hrac_group = Group()
hrac_group.add(H1)

mince_group = Group()

for _ in range(MINCE_START):
    spawn_mince(mince_group, H1)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == GAME_OVER_EVENT:
            game_over = True

        if event.type == SPAWN_COIN_EVENT\
                and not game_over\
                and len(mince_group) <= MAX_MINCE:
            spawn_mince(mince_group, H1)



        if event.type == pg.MOUSEBUTTONDOWN\
                and event.button == 1\
                and game_over\
                and text_restart_game_rect.collidepoint(event.pos):
            pg.event.post(restart_game_event)

        if event.type == RESTART_GAME_EVENT:
            game_over = False

            for _ in range(MINCE_START):
                spawn_mince(mince_group, H1)

            H1.rect.x = OKNO_SIRKA // 2
            H1.rect.y = OKNO_VYSKA // 2
            hrac_group.add(H1)

            pocet_minci = 0

    hrac_group.update()

    if pg.sprite.spritecollide(H1, mince_group, True):
        pocet_minci += 1


    okno.fill(BILA)
    hrac_group.draw(okno)
    mince_group.draw(okno)


    text_skore = skore_font.render(f"Skóre: {pocet_minci}", True, CERNA, BILA)
    okno.blit(text_skore, (10, 10))



    if game_over:
        mince_group.empty()
        hrac_group.empty()

        okno.fill(CERNA)
        text_game_over = game_over_font.render(f"KONEC HRY! Skóre: {pocet_minci}", True, BILA, CERNA)
        text_game_over_rect = text_game_over.get_rect()
        text_game_over_rect.center = (OKNO_SIRKA // 2, OKNO_VYSKA // 2)
        okno.blit(text_game_over, text_game_over_rect)

        text_restart_game = skore_font.render("Stiskni pro restart hry!", True, BILA, CERNA)
        text_restart_game_rect = text_restart_game.get_rect()
        text_restart_game_rect.center = (OKNO_SIRKA // 2, OKNO_VYSKA // 2 + text_game_over_rect.height)
        okno.blit(text_restart_game, text_restart_game_rect)


    pg.display.flip()
    clock.tick(FPS)
