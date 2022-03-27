#!/usr/bin/env python

import argparse
from PIL import Image, ImageDraw
from time import time
from searching_algorithms import *


def main(args: argparse.Namespace) -> None:
    img = Image.open(args.input).convert('RGB')
    pixel_matrix = np.array(img)

    start_time = time()
    path = BFS(tuple(args.start), tuple(args.goal), pixel_matrix)
    stop_time = time() - start_time

    print('Tiempo:\t{}s'.format(stop_time))
    print('Total de pasos:\t{}'.format(len(path)))

    path_pixels = np.array(img)

    if args.color == 'RED':
        color = RED
    elif args.color == 'GREEN':
        color = GREEN
    elif args.color == 'BLUE':
        color = BLUE

    if args.gif:
        frames = []
        for pos in path:
            path_pixels[pos] = color
            frame = Image.fromarray(path_pixels)
            ImageDraw.Draw(frame)
            frames.append(frame)
        frames[0].save(args.output+'.gif', format='GIF',
                       append_images=frames[1:], save_all=True, duration=20, loop=0)
    else:
        for pos in path:
            path_pixels[pos] = color

    solved_state = Image.fromarray(path_pixels)
    solved_state.save(args.output, format='PNG')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Un solucionador de laberintos')
    parser.add_argument(
        'input', help='nombre de la imagen con el laberinto a resolver')
    parser.add_argument(
        'output', help='imagen donde se guardará el laberinto resuelto')
    parser.add_argument(
        'start', nargs=2, help='posición del pixel de salida', type=int)
    parser.add_argument(
        'goal', nargs=2, help='posición del pixel objetivo', type=int)
    parser.add_argument('--alg', '-a', help='algoritmo de búsqueda',
                        choices=('bfs', 'dfs', 'iddfs'), default='bfs')
    parser.add_argument('--show', action='store_true',
                        help='muestra la imagen generada)')
    parser.add_argument('--color', '-c', help='color de la línea',
                        choices=('red', 'green', 'blue'), default='RED')
    parser.add_argument('--gif', '-g', action='store_true',
                        help='guardar gif del trayecto (usar con precaución)')
    args = parser.parse_args()
    main(args)
