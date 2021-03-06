# Maze Solver
Solucionador de laberintos mediante los algoritmo BFS, DFS y IDDFS.

## Uso
Abrir una línea de comandos y ejecutar:
```main.py [-h] [--alg {bfs,dfs,iddfs}] [--depth DEPTH] [--show] [--color {red,green,blue}] [--gif]input output start_y start_x goal_y goal_x```

Es necesario conocer las coordenadas del píxel de inicio y píxel final para utilizar el programa.
Cualquier programa de edición de imágenes te puede ayudar para saberlo.

Se encuentran 3 laberintos de ejemplo en la carpeta `examples`. Sus coordenadas son:
1. `maze1.png`: Inicio = (201, 17), Meta = (15, 340)
2. `maze2.png`: Inicio = (896, 283), Meta = (32, 575)
3. `maze3.png`: Inicio = (983, 405), Meta = (21, 397)

### Ejemplo
* Con Python instalado
    ```
    python main.py examples/maze1.png examples/maze1_solved 201 17 15 340 --alg=bfs --show
    ```
* Sin Python instalado (para Windows)
    ```
    main.exe examples/maze1.png examples/maze1_solved 201 17 15 340 --alg=bfs --show
    ```
---
# img2bin
Herramienta de formato para imágenes de laberinto.

## Uso
Abrir una línea de comandos y ejecutar: `python img2bin.py input output`

## Ejemplo
* Con Python instalado
    ```
    python img2bin.py examples/maze3.png examples/maze3_formated.png
    ```
* Sin Python instalado (para Windows)
    ```
    img2bin.exe examples/maze3.png examples/maze3_formated.png
    ```