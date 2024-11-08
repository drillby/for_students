# spawn jablka do hada
# restart hry
# zkažená jablka

import random

import pygame

pygame.init()

OKNO_VYSKA = 600
OKNO_SIRKA = 800

BILA = (255, 255, 255)
MODRA = (0, 0, 255)
CERVENA = (255, 0, 0)
CERNA = (0, 0, 0)

ZRYCHLENI_KAZDYCH_X = 10
MIN_INTERVAL_SEC = 0.1
ZMENA_INTERVALU = 0.05

score_font = pygame.font.Font("freesansbold.ttf", 32)

hodiny = pygame.time.Clock()
FPS = 60

MOVE_SNAKE_SEC = 0.5
MOVE_SNAKE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE_EVENT, int(MOVE_SNAKE_SEC * 1000))

skore = 0

game_over = False


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
        return hrac.segmenty[0] == self.pozice


class Snake(GameObject):
    def __init__(self, rozmer, pozice, barva, barva_hlavy):
        super().__init__(rozmer, pozice, barva)
        self.smer_pohybu = [0, 0]  # [x, y]
        self.segmenty = [self.pozice]
        self.barva_hlavy = barva_hlavy

    def zveceni(self):
        self.segmenty.append(self.segmenty[-1])

    def zjisteni_smeru(self, stisknute_klavesy):
        if stisknute_klavesy[pygame.K_LEFT] and self.smer_pohybu[0] == 0:
            self.smer_pohybu[0] = -1
            self.smer_pohybu[1] = 0
        elif stisknute_klavesy[pygame.K_RIGHT] and self.smer_pohybu[0] == 0:
            self.smer_pohybu[0] = 1
            self.smer_pohybu[1] = 0

        if stisknute_klavesy[pygame.K_UP] and self.smer_pohybu[1] == 0:
            self.smer_pohybu[1] = -1
            self.smer_pohybu[0] = 0
        elif stisknute_klavesy[pygame.K_DOWN] and self.smer_pohybu[1] == 0:
            self.smer_pohybu[1] = 1
            self.smer_pohybu[0] = 0

    def pohyb(self):
        # self.pozice[0] += self.smer_pohybu[0] * self.rozmer[0]
        # self.pozice[1] += self.smer_pohybu[1] * self.rozmer[1]
        nova_pozice = [
            self.segmenty[0][0] + self.smer_pohybu[0] * self.rozmer[0],
            self.segmenty[0][1] + self.smer_pohybu[1] * self.rozmer[1],
        ]  # [50, 50] [[50, 50]]
        # [[0, 0], [50, 0], [100, 0]]
        self.segmenty = [nova_pozice] + self.segmenty[:-1]

    def zkontroluj_hranice(self):
        global game_over
        if self.segmenty[0][0] < 0:
            game_over = True
        if self.segmenty[0][1] < 0:
            game_over = True
        if self.segmenty[0][0] > OKNO_SIRKA - self.rozmer[0]:
            game_over = True
        if self.segmenty[0][1] > OKNO_VYSKA - self.rozmer[1]:
            game_over = True

    def zkontroluj_kolizi(self):
        for segment in self.segmenty[1:]:
            if self.segmenty[0] == segment:
                return True
        return False

    def vykresli(self, okno):
        for idx, segment in enumerate(self.segmenty):
            if idx == 0:
                pygame.draw.rect(okno, self.barva_hlavy, (*segment, *self.rozmer))
            else:
                pygame.draw.rect(okno, self.barva, (*segment, *self.rozmer))


# Vytvoření okna
okno = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

# Nastavení titulku okna
pygame.display.set_caption("Můj první program v Pygame")

H1 = Snake((50, 50), [100, 100], MODRA, CERNA)
A1 = Apple((50, 50), [200, 200], CERVENA)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOVE_SNAKE_EVENT:
            H1.pohyb()
            H1.zkontroluj_hranice()
            if H1.zkontroluj_kolizi():
                game_over = True
        elif (
            event.type == pygame.MOUSEBUTTONDOWN
            and game_over
            and pygame.mouse.get_pressed()[0]
            and text_restart_rect.collidepoint(event.pos)
        ):
            game_over = False
            skore = 0
            seznam_x = [i for i in range(0, OKNO_SIRKA, A1.rozmer[0])]
            seznam_y = list(range(0, OKNO_VYSKA, A1.rozmer[1]))
            H1 = Snake(
                (50, 50),
                [random.choice(seznam_x), random.choice(seznam_y)],
                MODRA,
                CERNA,
            )
            A1 = Apple(
                (50, 50), [random.choice(seznam_x), random.choice(seznam_y)], CERVENA
            )

    stisknute_klavesy = pygame.key.get_pressed()

    H1.zjisteni_smeru(stisknute_klavesy)

    if A1.zkontroluj_kolizi(H1):
        skore += 1
        seznam_x = [i for i in range(0, OKNO_SIRKA, A1.rozmer[0])]
        seznam_y = list(range(0, OKNO_VYSKA, A1.rozmer[1]))
        A1.pozice = [random.choice(seznam_x), random.choice(seznam_y)]
        H1.zveceni()

        if (
            skore % ZRYCHLENI_KAZDYCH_X == 0
            and skore != 0
            and MOVE_SNAKE_SEC > MIN_INTERVAL_SEC
        ):
            MOVE_SNAKE_SEC -= ZMENA_INTERVALU
            pygame.time.set_timer(MOVE_SNAKE_EVENT, int(MOVE_SNAKE_SEC * 1000))

    okno.fill(BILA)
    # Obnovení okna
    H1.vykresli(okno)
    A1.vykresli(okno)
    text = score_font.render(f"Score: {skore}", True, CERNA)
    okno.blit(text, (10, 10))

    if game_over:
        H1.smer_pohybu = [0, 0]
        okno.fill(CERNA)
        text = score_font.render(f"Score: {skore}", True, BILA)
        text_rect = text.get_rect(center=(OKNO_SIRKA // 2, OKNO_VYSKA // 2))
        okno.blit(text, text_rect)
        text_restart = score_font.render("Stiskni pro restart", True, BILA)
        text_restart_rect = text_restart.get_rect(
            center=(OKNO_SIRKA // 2, OKNO_VYSKA // 2 + text_rect.height)
        )
        okno.blit(text_restart, text_restart_rect)
    pygame.display.flip()
    hodiny.tick(FPS)
