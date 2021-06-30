import pygame


def graphics_engine(screen, screen_width, screen_height, screen_gutter_size, color_kv, sort_status, fps):

    # background color
    DARKBLUE = (0, 0, 20)

    # text color
    LIGHTGREY = (200, 200, 200)

    # text
    font = pygame.font.Font("./merge_sort_pygame/ARCADE_R.TTF", 24)
    text_surface = font.render(str("merge sort"), True, LIGHTGREY)
    text_rect = text_surface.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 4)

    # speed
    clock = pygame.time.Clock()

    def draw_screen():

        screen.fill(DARKBLUE)
        screen.blit(text_surface, text_rect)

        x_adjust = 0  # will keep circles stacked on x-axis neatly
        for circle_size in sort_status:

            pygame.draw.circle(
                screen,
                (color_kv[circle_size][0], color_kv[circle_size][1], color_kv[circle_size][2]),
                (screen_gutter_size + x_adjust + circle_size // 2, screen_height // 2),
                circle_size // 2
            )

            x_adjust += circle_size

            for event in pygame.event.get():  # able to quit by closing window
                if event.type == pygame.QUIT:
                    quit()

        clock.tick(fps)
        pygame.display.update()

    draw_screen()
