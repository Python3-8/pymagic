"""PyMagic"""
import sys
import math
import pygame
import pygame.gfxdraw
import pymsgbox


def main():
    # welcome
    option = pymsgbox.confirm(
        "Welcome to PyMagic! Click 'Instructions' to learn how to use PyMagic, or 'Skip' to skip to the program.", 'Welcome', ('Instructions', 'Skip'))
    if option is None:
        sys.exit()
    if option == 'Instructions':
        if not pymsgbox.confirm('''\
    The different controls are provided below. Press these keys to perform the actions associated with them.
    Q/Left mouse button press - Pen/eraser down/up
    C - Clear board
    X - Make board white/black
    R - Set pen color to red
    O - Orange
    Y - Yellow
    G - Green
    B - Blue
    V - Purple
    P - Pink
    W - White
    Z - Black
    Left Shift - Toggle tool (pen/eraser)
    Up Arrow - Increase tool thickness
    Down Arrow - Decrease tool thickness\
    ''', 'Instructions', ('OK',)):
            sys.exit()

    # setting constants
    class Colors:
        red = (248, 81, 86)
        orange = (255, 153, 79)
        yellow = (255, 210, 88)
        green = (0, 194, 136)
        blue = (29, 147, 232)
        purple = (108, 77, 241)
        pink = (179, 96, 210)
        white = (221, 221, 221)
        black = (34, 34, 34)

    def get_win_width(win_height):
        return round((1+math.sqrt(5))/2 * win_height)

    # initalization
    pygame.init()
    win_height = 15/16 * pygame.display.Info().current_h
    win_width = get_win_width(win_height)  # golden ratio
    win = pygame.display.set_mode((win_width, 750), pygame.RESIZABLE)
    pygame.display.set_caption('PyMagic')

    # loop
    run = True
    tool_down = False
    marked_points = []
    points = []
    pen = True  # False for eraser
    tool_color = Colors.white
    tool_thickness = 3
    board_color = Colors.black
    hover_color = (128, 128, 128, 128)
    hover_shadow_offset = 3
    while run:
        # register events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    tool_down = not tool_down
                elif event.key == pygame.K_c:
                    marked_points.clear()
                elif event.key == pygame.K_r:
                    tool_color = Colors.red
                elif event.key == pygame.K_o:
                    tool_color = Colors.orange
                elif event.key == pygame.K_y:
                    tool_color = Colors.yellow
                elif event.key == pygame.K_g:
                    tool_color = Colors.green
                elif event.key == pygame.K_b:
                    tool_color = Colors.blue
                elif event.key == pygame.K_v:
                    tool_color = Colors.purple
                elif event.key == pygame.K_p:
                    tool_color = Colors.pink
                elif event.key == pygame.K_w:
                    tool_color = Colors.white
                elif event.key == pygame.K_z:
                    tool_color = Colors.black
                elif event.key == pygame.K_x:
                    board_color = Colors.white if board_color == Colors.black else Colors.black
                elif event.key == pygame.K_UP:
                    tool_thickness += 1
                elif event.key == pygame.K_DOWN:
                    tool_thickness -= 1
                    if tool_thickness <= 0:
                        tool_thickness = 1
                elif event.key == pygame.K_LSHIFT:
                    pen = not pen
                marked_points.append([])
            elif event.type == pygame.MOUSEBUTTONUP:
                tool_down = not tool_down
                marked_points.append([])
            elif event.type == pygame.VIDEORESIZE:
                win = pygame.display.set_mode(
                    (get_win_width(event.h), event.h), pygame.RESIZABLE)
        # main stuff
        win.fill(board_color)
        for points in marked_points:
            last_point = None
            for point in points:
                draw_color = board_color if point[1] == 'eraser' else point[1]
                pygame.gfxdraw.filled_circle(
                    win, *point[0], point[2], draw_color)
                if last_point:
                    pygame.draw.line(
                        win, draw_color, last_point[0], point[0], last_point[2] * 2)
                last_point = point
        cursor_pos = pygame.mouse.get_pos()
        if tool_down:
            if pen:
                marked_points[-1].append((cursor_pos,
                                         tool_color, tool_thickness))
            else:
                marked_points[-1].append((cursor_pos,
                                         'eraser', tool_thickness))
        pygame.gfxdraw.circle(win, *cursor_pos, tool_thickness, hover_color)
        # update display
        pygame.display.update()


if __name__ == '__main__':
    main()
