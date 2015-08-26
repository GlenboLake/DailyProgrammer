screen = [line.rstrip('\n') for line in open('input/tiles.txt').readlines()]
tiles = []

tile_info = None
for y, row in enumerate(screen):
    for x, char in enumerate(row):
        if char == '.':
            if tile_info:
                tiles.append(tile_info)
                tile_info = None
            continue
        if not tile_info:
            if screen[y-1][x] == '.' and screen[y][x-1] == '.':
                # New tile!
                # Find tile height
                height = 0
                while screen[y+height][x] == char:
                    height += 1
                tile_info = [1, height, char, x, y]
        else:
            tile_info[0] += 1
for tile in sorted(tiles, key=lambda item: item[2]):
    print("{}x{} tile of character '{}' located at ({},{})".format(*tile))