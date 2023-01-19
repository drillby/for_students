import random

import pygame

pygame.init()

herni_okno = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Event Handling")

running = True

while running:
    for event in pygame.event.get():  # For Loop
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Zmáčkl jsi pravou šipku")
            elif event.key == pygame.K_LEFT:
                print("Zmáčkl jsi levou šipku")

        elif event.type == pygame.MOUSEMOTION:
            print(f"Hýbeš myší, je na pozici {pygame.mouse.get_pos()}")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Levé tlačítko")
            elif event.button == 2:
                print("Kolečko")
            elif event.button == 3:
                print("Pravé tlačítko")

    # stav_klaves = pygame.key.get_pressed()  # {K_a:True, K_b:False, K_c:True, .....}
    # if stav_klaves[pygame.K_UP]:
    #     print(random.randint(0, 100))
    # if stav_klaves[pygame.K_UP]:
    #     print(random.randint(101, 200))
