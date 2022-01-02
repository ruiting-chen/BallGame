import pygame
from Ball import Ball
from Block import Block
from Screen import Screen


def run():
    pygame.init()
    Screen.create_screen((600, 400), (236, 229, 182))

    ball_radius = 10
    ball_color = (255, 0, 0)
    A = Ball(Screen.get_left() + ball_radius,
             Screen.get_bottom() - ball_radius,
             ball_radius, ball_color, 0, 0)
    jump_velocity = -40
    run_velocity = 10

    B = Block(345, 355, 200, 250, ball_color, A)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.key.get_pressed()[pygame.K_UP]:
            A.ball_jump(jump_velocity)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            A.set_x_velocity(run_velocity)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            A.set_x_velocity(-run_velocity)

        A.draw(Screen.get_color())
        Screen.update_ball_pos(0.01, A)
        B.update_ball_pos(0.01, A)
        A.draw(A.get_color())
        B.draw()
        pygame.display.update()

    pygame.display.quit()


if __name__ == '__main__':
    run()

