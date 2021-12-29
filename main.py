import pygame
from Ball import Ball
from Screen import Screen


def run():
    pygame.init()
    Screen.create_screen((600, 600), (236, 229, 182))

    A = Ball(0, 600, 10, (255, 0, 0), 0, 0)
    A.draw()
    v = 50
    A.set_y_velocity(v)
    A.set_x_velocity(5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.key.key_code("a"):
                    A.set_y_velocity(v)
        A.draw()
        if A.get_y_velocity() == 0:
            v = v // 1.1
            A.set_y_velocity(v)

        pygame.display.update()

    pygame.display.quit()



if __name__ == '__main__':
    run()

