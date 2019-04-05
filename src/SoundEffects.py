import pygame

pygame.init()

sc = pygame.display.set_mode((400, 300))

pygame.mixer.music.load('../assets/S47-85_Mantis_Lords.wav')
pygame.mixer.music.play(-1)
# sound1 = pygame.mixer.Sound('boom.wav')
# sound2 = pygame.mixer.Sound('one.ogg')

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                pygame.mixer.music.pause()
                # pygame.mixer.music.stop()
            elif i.key == pygame.K_UP:
                pygame.mixer.music.unpause()
            elif i.key == pygame.K_DOWN:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)
            elif i.key == pygame.K_RIGHT:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
        # elif i.type == pygame.MOUSEBUTTONUP:
        #     if i.button == 1:
        #         sound1.play()
        #     elif i.button == 3:
        #         sound2.play()
    pygame.time.delay(20)