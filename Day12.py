"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a
decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area
from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter,
where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best
signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has
elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step,
you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear,
the elevation of the destination square can be at most one higher than the elevation of your current square; that is,
if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the
elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right,
but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<),
or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
--- Part Two ---

As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't
very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the
square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So,
you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at
elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get
the best signal?
"""


# import numpy as np
# import re


def create_graph_from_input():
    vertices = set()
    edges = set()
    grid = []
    with open('inputs/input_day12', 'r') as file:
        for i, line in enumerate(file):
            line = list(line[:-1])
            if 'S' in line:
                start = (i, line.index('S'))
                line[line.index('S')] = 'a'
            if 'E' in line:
                end = (i, line.index('E'))
                line[line.index('E')] = 'z'
            line = [ord(height) for height in line]
            grid.append(line)

    for i, line in enumerate(grid):
        for j, height in enumerate(line):
            vertex = (i, j)
            vertices.add(vertex)
            if i < len(grid) - 1 and grid[i + 1][j] - height <= 1:
                edge = (vertex, (i + 1, j))
                edges.add(edge)
            if j < len(line) - 1 and grid[i][j + 1] - height <= 1:
                edge = (vertex, (i, j + 1))
                edges.add(edge)
            if i > 0 and grid[i - 1][j] - height <= 1:
                edge = (vertex, (i - 1, j))
                edges.add(edge)
            if j > 0 and grid[i][j - 1] - height <= 1:
                edge = (vertex, (i, j - 1))
                edges.add(edge)

    return start, end, vertices, edges, grid


def part1(startlist=None):
    start, end, vertices, edges, _ = create_graph_from_input()
    if startlist is None:
        startlist = [start]
    queue = startlist
    new_queue = []
    seen = set(startlist)
    steps = 0
    # modifizierte Breitensuche
    while end not in seen:
        steps += 1
        while queue:
            node = queue.pop(0)
            for vertex in vertices:
                if vertex not in seen and (node, vertex) in edges:
                    new_queue.append(vertex)
                    seen.add(vertex)
        queue = new_queue
        new_queue = []

    return steps


def part2():
    _, _, vertices, _, grid = create_graph_from_input()
    startlist = list()
    for vertex in vertices:
        i, j = vertex
        if grid[i][j] == 97:
            startlist.append(vertex)
    return part1(startlist)


if __name__ == "__main__":
    print(part2())
