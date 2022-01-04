import pygame
from Ball import Ball
from Block import Block
from Screen import Screen


def run():
    pygame.init()
    Screen.create_screen((600, 400), (236, 229, 182))

    ball_radius = 10
    ball_color = (255, 0, 0)
    A = Ball(ball_radius, ball_color,
             Screen.get_left() + ball_radius,
             Screen.get_bottom() - ball_radius,
             0, 0)
    jump_velocity = -40
    run_velocity = 0.08

    B = Block(345, 355, 200, 250, ball_color, A)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.key.get_pressed()[pygame.K_UP]:
            A.ball_jump(jump_velocity)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            A.ball_move(run_velocity)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            A.ball_move(-run_velocity)

        A.draw(Screen.get_color())
        A.calculate_pos_velo(0.01)
        Screen.update_ball(0.01, A)
        B.update_ball(0.01, A)
        A.update_pos_velo()
        A.draw(A.get_color())
        B.draw()
        pygame.draw.line(Screen.get_screen(), (0, 0, 0), (200, 0), (200, 400))
        pygame.draw.line(Screen.get_screen(), (0, 0, 0), (250, 0), (250, 400))
        pygame.draw.line(Screen.get_screen(), (0, 0, 0), (0, 345), (600, 345))
        pygame.draw.line(Screen.get_screen(), (0, 0, 0), (0, 355), (600, 355))
        pygame.display.update()

    pygame.display.quit()


if __name__ == '__main__':
    run()

