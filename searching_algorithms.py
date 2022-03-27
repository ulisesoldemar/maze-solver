#!/usr/bin/env python

import numpy as np
from queue import Queue

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def check_pixel_color(value: np.ndarray, color: tuple) -> bool:
    return np.array_equal(value, color)


def adjacent(pos: tuple, limits: tuple) -> tuple:
    row, col = pos
    y, x = limits
    up, down, left, right = row-1, row+1, col-1, col+1
    valid_moves = []
    if up >= 0:
        valid_moves.append((up, col))  # UP
    if down < y:
        valid_moves.append((down, col))  # DOWN
    if left >= 0:
        valid_moves.append((row, left))  # LEFT
    if right < x:
        valid_moves.append((row, right))  # RIGHT
    if up >= 0 and left >= 0:
        valid_moves.append((up, left))  # UP-LEFT
    if up >= 0 and right < x:
        valid_moves.append((up, right))  # UP-RIGHT
    if down < y and left >= 0:
        valid_moves.append((down, left))  # DOWN-LEFT
    if down < y and right < x:
        valid_moves.append((down, right))  # DOWN-RIGHT
    return tuple(valid_moves)


def BFS(start: tuple, end: tuple, pixels: np.ndarray) -> list:
    if pixels[start] == 0:
        raise IndexError('posición de inicio invalida {}'.format(start))
    if pixels[end] == 0:
        raise IndexError('posición objetivo invalida {}'.format(start))

    if start == end:
        return [start]

    queue = Queue()
    queue.put([start])
    while queue:
        path = queue.get()
        pixel = path[-1]
        if pixel == end:
            return path
        for adj in adjacent(pixel, pixels.shape):
            if pixels[adj] > 0:
                pixels[adj] = 0
                new_path = list(path)
                new_path.append(adj)
                queue.put(new_path)


def DFS(start: tuple, end: tuple, pixels: np.ndarray) -> list:
    if pixels[start] == 0:
        raise IndexError('posición de inicio invalida {}'.format(start))

    if pixels[end] == 0:
        raise IndexError('posición objetivo invalida {}'.format(start))

    if start == end:
        return [start]

    stack = [[start]]
    while stack:
        path = stack.pop()
        pixel = path[-1]
        if pixel == end:
            return path

        for adj in adjacent(pixel, pixels.shape):
            if pixels[adj] > 0:
                pixels[adj] = 0
                new_path = list(path)
                new_path.append(adj)
                stack.append(new_path)


def IDDFS(start: tuple, end: tuple, pixels: np.ndarray, max_depth: int) -> tuple:
    if pixels[start] == 0:
        raise IndexError('posición de inicio invalida {}'.format(start))

    if pixels[end] == 0:
        raise IndexError('posición objetivo invalida {}'.format(start))

    if start == end:
        return [start], 0

    stack = [[start]]
    depth_stack = [max_depth]
    while stack:
        path = stack.pop()
        pixel = path[-1]
        if pixels[pixel] == 0:
            continue

        depth = depth_stack.pop()
        if depth >= 0:
            pixels[pixel] = 0
            for adj in adjacent(pixel, pixels.shape):
                depth_stack.append(depth - 1)
                if adj == end:
                    return path, max_depth - depth
                new_path = list(path)
                new_path.append(adj)
                stack.append(new_path)
    raise ValueError('meta no alcanzada con profundidad {}'.format(max_depth))
