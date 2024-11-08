# přidat jablko

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


class Snake(pygame.sprite.Sprite):
    def __init__(self, rozmer, pozice):
        super().__init__()
        self.rozmer = rozmer
        self.smer_pohybu = [0, 0]
        self.pozice = pozice
        self.hlava_sprite = "./sprites/head_up.png"
        self.telo_sprite = "./sprites/body_vertical.png"
        self.ocas_sprite = "./sprites/tail_up.png"
        self.image = pygame.image.load(self.hlava_sprite)
        self.rect = self.image.get_rect()

    def zjisteni_smeru(self, stisknute_klavesy):
        if stisknute_klavesy[pygame.K_LEFT] and self.smer_pohybu[0] == 0:
            self.smer_pohybu[0] = -1
            self.smer_pohybu[1] = 0
            # rotate head sprite
            self.image = pygame.image.load(self.hlava_sprite)
            self.image = pygame.transform.rotate(self.image, 90)
        elif stisknute_klavesy[pygame.K_RIGHT] and self.smer_pohybu[0] == 0:
            self.smer_pohybu[0] = 1
            self.smer_pohybu[1] = 0
            self.image = pygame.image.load(self.hlava_sprite)
            self.image = pygame.transform.rotate(self.image, -90)

        if stisknute_klavesy[pygame.K_UP] and self.smer_pohybu[1] == 0:
            self.smer_pohybu[1] = -1
            self.smer_pohybu[0] = 0
            self.image = pygame.image.load(self.hlava_sprite)

        elif stisknute_klavesy[pygame.K_DOWN] and self.smer_pohybu[1] == 0:
            self.smer_pohybu[1] = 1
            self.smer_pohybu[0] = 0
            self.image = pygame.image.load(self.hlava_sprite)
            self.image = pygame.transform.rotate(self.image, 180)

    def pohyb(self):
        self.pozice[0] += self.smer_pohybu[0] * self.rozmer[0]
        self.pozice[1] += self.smer_pohybu[1] * self.rozmer[1]
        # nova_pozice = [
        #     self.segmenty[0][0] + self.smer_pohybu[0] * self.rozmer[0],
        #     self.segmenty[0][1] + self.smer_pohybu[1] * self.rozmer[1],
        # ]  # [50, 50] [[50, 50]]
        # [[0, 0], [50, 0], [100, 0]]
        # self.segmenty = [nova_pozice] + self.segmenty[:-1]

        self.rect.move_ip(
            self.smer_pohybu[0] * self.rozmer[0], self.smer_pohybu[1] * self.rozmer[1]
        )

    def update(self):
        self.pohyb()


okno = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

# Nastavení titulku okna
pygame.display.set_caption("Můj první program v Pygame")

H1 = Snake((50, 50), [100, 100])
snake_group = pygame.sprite.Group()
snake_group.add(H1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOVE_SNAKE_EVENT:
            snake_group.update()

    stisknute_klavesy = pygame.key.get_pressed()
    H1.zjisteni_smeru(stisknute_klavesy)

    okno.fill(BILA)
    # Obnovení okna
    snake_group.draw(okno)

    pygame.display.flip()
    hodiny.tick(FPS)
pygame.quit()
