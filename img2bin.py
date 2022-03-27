#!/usr/bin/env python

import argparse
import numpy as np
from PIL import Image

MAX_VAL = 255
THRESH = int(MAX_VAL / 1.25)
FORMAT = 'png'


def img2bin(img_path: str, img_output: str) -> None:
    img = Image.open(img_path)
    img = img.convert('L').convert('RGB')
    data = np.array(img)
    data_bool = data > THRESH
    data_bin = data_bool * MAX_VAL
    img_bw = Image.fromarray(np.uint8(data_bin))
    img_bw.save(img_output, format=FORMAT)

def main(args: argparse.Namespace) -> None:
    img2bin(args.input, args.output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Herramienta para formatear laberintos para poder ser resueltos')
    parser.add_argument(
        'input', help='nombre de la imagen a convertir')
    parser.add_argument(
        'output', help='nombre de la imagen convertida')
    
    args = parser.parse_args()
    main(args)