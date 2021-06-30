import random
from sys import maxsize
import time
import pygame
import merge_sort_pygame_graphics as graphics

"""
MERGE SORT VISUALIZED WITH PYGAME
bennyBoy_JP 2021 - https://twitter.com/Bennyboy_JP

Merge sort, a divide and conquer recursive algorithm:
https://en.wikipedia.org/wiki/Merge_sort#Algorithm

**NOTE** You will need pygame library installed for this:
pygame installation: https://www.pygame.org/wiki/GettingStarted

Download "Arcade-R.TTF" font from: https://www.ffonts.net/Arcade-R.font

Thanks for your interest!
"""
# --------------------
# USER PARAMETERS:
# the range of the amount of circles per round
circle_lowest_range, circle_highest_range = 10, 100

# the range of random numbers
range_of_randomized_numbers = 1000

# frame-rate of pygame animation
speed = 15

# the duration before starting a new round (seconds)
time_between_rounds = 1

# decreases the size of pygame's screen (higher = smaller screen)
margin = 100
# --------------------

pygame.init()
display_info_object = pygame.display.Info()
screen_width, screen_height = display_info_object.current_w - margin, display_info_object.current_h - (margin * 2)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("merge sort visualization")


def start():

    while True:

        for event in pygame.event.get():  # able to quit by closing window
            if event.type == pygame.QUIT:
                quit()

        # begin Merge Sort algorithm
        def merge_sort_engine(A):

            def merge_sort(arr, first, last):

                def merge(current_a, f, m, l):
                    L = current_a[f:m + 1] + [maxsize]
                    R = current_a[m + 1:l + 1] + [maxsize]

                    i = j = 0
                    for current_idx in range(f, l + 1):
                        if L[i] <= R[j]:
                            current_a[current_idx] = L[i]
                            i += 1
                        else:
                            current_a[current_idx] = R[j]
                            j += 1
                    return current_a

                if first < last:
                    middle = (first + last) // 2
                    merge_sort(arr, first, middle)
                    merge_sort(arr, middle + 1, last)
                    merge(arr, first, middle, last)

                    # current state of list is passed to the graphics engine for rendering
                    graphics.graphics_engine(
                        screen, screen_width, screen_height, screen_gutter_size, color_kv, arr, speed)

                return arr

            return merge_sort(A, 0, len(A) - 1)

        num_of_circles_per_round = random.randint(circle_lowest_range, circle_highest_range)
        randomized_numbers = [num for num in random.sample(
            range(range_of_randomized_numbers), num_of_circles_per_round)]

        total_width_circles = sum(randomized_numbers)

        # circle_size_scaler is determined to fit screen (1.05 is used to give a small cushion on x-axis)
        circle_size_scaler = screen_width / (total_width_circles * 1.05)

        # will adjust each number using circle_size_scaler to fit the screen
        randomized_numbers_scaled = list(map(lambda random_num: random_num * circle_size_scaler, randomized_numbers))

        # will center all circles to center of screen
        screen_gutter_size = (screen_width - sum(randomized_numbers_scaled)) // 2

        # assigns each number and color random color to a key/value pear (color_kv)
        color_kv = {}
        for random_number in randomized_numbers_scaled:
            colorR = random.randint(100, 255)
            colorG = random.randint(100, 255)
            colorB = random.randint(100, 255)

            color_kv[random_number] = (colorR, colorG, colorB)

        merge_sort_engine(randomized_numbers_scaled)

        time.sleep(time_between_rounds)


if __name__ == "__main__":
    start()
