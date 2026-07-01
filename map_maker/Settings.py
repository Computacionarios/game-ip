type rgb_type = tuple[int, int, int]
type pos_type = tuple[int, int]
type size_type = tuple[int, int]

screen_colors = {
  "bg_color": (30, 30, 30),
  "tile_color": (50,50,50),
}

pallet_colors = {  # cores presentes na paleta
  "red": (200, 0, 0),
  "green": (0, 200, 0),
  "blue": (0, 0, 200),
  "black": (0, 0, 0),
  "white": (200, 200, 200),
}

# global props
BORDER = 5

# cnavas props
CANVAS_GAP = 1
TILE_SIZE = 16
TILES_AMOUNT = 32
