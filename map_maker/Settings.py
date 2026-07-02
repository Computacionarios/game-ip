type rgb_type = tuple[int, int, int]
type pos_type = tuple[int, int]
type size_type = tuple[int, int]

screen_colors = {
  "bg_color": (30, 30, 30,0),
  "tile_color": (50, 50, 50,0),
}

pallet_colors = {  # cores presentes na paleta
  "red": (200, 0, 0, 9),
  "green": (0, 200, 0, 9),
  "blue": (0, 0, 200, 9),
  "black": (0, 0, 0, 9),
  "white": (200, 200, 200, 9),
}

# global props
BORDER = 5

# cnavas props
CANVAS_GAP = 1
TILE_SIZE = 10
CANVAS_SIZE = (1200, 800)
PALLET_WIDTH = 50

print(CANVAS_SIZE[0] / TILE_SIZE)
print(CANVAS_SIZE[1] / TILE_SIZE)
