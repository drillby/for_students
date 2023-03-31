from typing import List, Tuple
import pygame


class GameObject:
    def __init__(
        self, pozice: List[int], rozmery: Tuple[int, int], barva: Tuple[int, int, int]
    ) -> None:
        self.pozice = pozice
        self.rozmery = rozmery
        self.barva = barva

    def vykresli(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.barva, (*self.pozice, *self.rozmery), 0)


class Player(GameObject):
    def __init__(
        self,
        pozice: List[int],
        rozmery: Tuple[int, int],
        barva: Tuple[int, int, int],
        rychlost_pohybu: int,
    ) -> None:
        super().__init__(pozice, rozmery, barva)
        self.rychlost_pohybu = rychlost_pohybu

    def pohni_se(self, surface_y_rozmer: int, nahoru: bool):
        if self.pozice[1] > surface_y_rozmer - self.rozmery[1]:
            self.pozice[1] = surface_y_rozmer - self.rozmery[1]
            return
        if self.pozice[1] < 0:
            self.pozice[1] = 0
            return

        if nahoru:
            self.pozice[1] -= self.rychlost_pohybu
        else:
            self.pozice[1] += self.rychlost_pohybu


class Micek(GameObject):
    def __init__(
        self,
        pozice: List[int],
        rozmery: Tuple[int, int],
        barva: Tuple[int, int, int],
        rychlost: List[int],
    ) -> None:
        super().__init__(pozice, rozmery, barva)
        self.rychlost = rychlost

    def odraz_od_steny_y(self, surface_y_rozmer: int):
        if self.pozice[1] < 0:
            self.rychlost[1] *= -1
        elif self.pozice[1] > surface_y_rozmer - self.rozmery[1]:
            self.rychlost[1] *= -1
            # self.rychlost[1] = -self.rychlost[1]
        return

    def konec_kola(self, surface_x_rozmer: int):
        if self.pozice[0] < 0:
            SKORE[1] += 1
            return True
        elif self.pozice[0] > surface_x_rozmer - self.rozmery[0]:
            SKORE[0] += 1
            return True
        return False

    def odraz_od_hrace(self, hrac_1: Player, hrac_2: Player):
        # hrac_1 => vlevo
        # hrac_2 => vpravo
        if self.pozice[0] <= hrac_1.pozice[0] + hrac_1.rozmery[0] and self.pozice[
            1
        ] in range(hrac_1.pozice[1], hrac_1.pozice[1] + hrac_1.rozmery[1]):
            # self.pozice[1] >= hrac_1.pozice[1] or self.pozice[1] <= hrac_1.pozice[1] + hrac_1.rozmery[1]
            self.rychlost[0] *= -1

        if self.pozice[0] + self.rozmery[0] >= hrac_2.pozice[0] and self.pozice[
            1
        ] in range(hrac_2.pozice[1], hrac_2.pozice[1] + hrac_2.rozmery[1]):
            # self.pozice[1] >= hrac_1.pozice[1] or self.pozice[1] <= hrac_1.pozice[1] + hrac_1.rozmery[1]
            self.rychlost[0] *= -1

    def pohni_se(self):
        self.pozice[0] += self.rychlost[0]
        self.pozice[1] += self.rychlost[1]


def nove_kolo(micek: Micek, hraci: Tuple[Player, Player]):
    micek.pozice = [
        velikost_okna[0] // 2 - velikost_micku[0] // 2,
        velikost_okna[1] // 2 + velikost_micku[1] // 2,
    ]
    for hrac in hraci:
        hrac.pozice[1] = velikost_okna[1] // 2 + velikost_hrace[1] // 2


pygame.init()
# Vytvoř okno pro hru
velikost_okna = (800, 480)
okno = pygame.display.set_mode(velikost_okna)

BILA = (255, 255, 255)
CERNA = (0, 0, 0)

SKORE = [0, 0]

MAX_BODY = 10

# Nastav název okna
pygame.display.set_caption("Ping-Pong")

# vytvoření objektu pro úpravu obnovovací frekvence
hodiny = pygame.time.Clock()
fps = 60

velikost_hrace = (20, 100)
pocatecni_pozice_1 = [100, velikost_okna[1] // 2 + velikost_hrace[1] // 2]
pocatecni_pozice_2 = [700, velikost_okna[1] // 2 + velikost_hrace[1] // 2]
rychlost_pohybu = 5

velikost_micku = (20, 20)
pocatecni_pozice_micek = [
    velikost_okna[0] // 2 - velikost_micku[0] // 2,
    velikost_okna[1] // 2 + velikost_micku[1] // 2,
]
puvodni_rychlost = [-3, 3]

hrac_1 = Player(pocatecni_pozice_1, velikost_hrace, BILA, rychlost_pohybu)
hrac_2 = Player(pocatecni_pozice_2, velikost_hrace, BILA, rychlost_pohybu)

micek = Micek(pocatecni_pozice_micek, velikost_micku, BILA, puvodni_rychlost)

font = pygame.font.SysFont("calibri", 40)

# Nastav počáteční stav hry
running = True
# Hlavní herní smyčka
while running:
    # Zpracuj události
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    klavesa = pygame.key.get_pressed()  # {pygame.A: True, pygame.B = False, ...}

    if klavesa[pygame.K_w]:
        hrac_1.pohni_se(velikost_okna[1], True)
    elif klavesa[pygame.K_s]:
        hrac_1.pohni_se(velikost_okna[1], False)

    if klavesa[pygame.K_UP]:
        hrac_2.pohni_se(velikost_okna[1], True)
    elif klavesa[pygame.K_DOWN]:
        hrac_2.pohni_se(velikost_okna[1], False)

    micek.odraz_od_hrace(hrac_1, hrac_2)
    micek.odraz_od_steny_y(velikost_okna[1])
    micek.pohni_se()
    if micek.konec_kola(velikost_okna[0]):
        nove_kolo(micek, (hrac_1, hrac_2))

    if MAX_BODY in SKORE:
        print("Konec hry\n")
        if SKORE[0] == MAX_BODY:
            print("Vyhrál hráč 2")
        else:
            print("Vyhrál hráč 1")
        pygame.quit()

    score1 = font.render(f"{SKORE[0]} : {SKORE[1]}", True, BILA)

    okno.fill(CERNA)
    hrac_1.vykresli(okno)
    hrac_2.vykresli(okno)
    micek.vykresli(okno)
    okno.blit(score1, (velikost_okna[0] // 3.0, velikost_okna[1] // 3.0))
    hodiny.tick(fps)
    pygame.display.flip()

    # Ukonči PyGame
pygame.quit()
