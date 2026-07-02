import pygame
import tkinter as tk

# Initialize tkinter
root = tk.Tk()
# Hide the main window container
root.withdraw()

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

type rgb_type = tuple[int, int, int]
type pos_type = tuple[int, int]
type size_type = tuple[int, int]

screen_colors = {
  "bg_color": (30, 30, 30, 0),
  "tile_color": (50, 50, 50, 0),
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
TILE_SIZE = 3
PALLET_WIDTH = 50

CANVAS_SIZE = (screen_width, screen_height)

proportion = 100
CANVAS_SIZE = (CANVAS_SIZE[0] - proportion, CANVAS_SIZE[1] - proportion)

print(CANVAS_SIZE[0] / TILE_SIZE)
print(CANVAS_SIZE[1] / TILE_SIZE)
