from rpg.button import *


def test_button_class():

    pygame.init()
    SIZE = (800, 600)
    screen = pygame.display.set_mode(SIZE)

    button = Button(100, 100, 100, 60,
                    (0xff, 0x80, 0x00),
                    (0xff, 0xff, 0x00),
                    (0x00, 0xff, 0x00))
    assert type(button.image_default) == pygame.Surface
    assert type(button.image_hover) == pygame.Surface
    assert type(button.image_click) == pygame.Surface

    def click_function():
        # move button a pseudorandom position and flip the dimensions
        button.width, button.height = button.height, button.width
        button.pos_x = (6789*button.pos_x+1234) % (SIZE[0]-button.width-2) + 1
        button.pos_y = (4321*button.pos_y+9876) % (SIZE[1]-button.height-2) + 1

    button.add_onclick(lambda: print("Button clicked"))
    button.add_onclick(click_function)
    assert len(button.onclicks) == 2

    running = True
    while running:
        events = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button.mouse_click(mouse_pos[0], mouse_pos[1])
            elif event.type == pygame.MOUSEMOTION:
                button.mouse_move(mouse_pos[0], mouse_pos[1])

        screen.fill((255, 255, 255))
        button.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
