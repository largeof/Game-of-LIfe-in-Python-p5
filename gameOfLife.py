# Game of life in p5 
#
# Author: Austin Merrick

from p5 import *

tiles = 25
tile_size = 25
background_color = Color(24)
actual_color = Color(200)

#this initializes 2d arrow with 0's 
grid = [[0 for i in range(tiles)] for j in range(tiles)]

grid[5][5]=1


def setup():
    size(tile_size * tiles, tile_size * tiles)
    title("Game of life")

    no_stroke()

def draw():
    #for every tile, if 1, print color, else dont
    background(Color(24))

    for x in range(tiles):
        for y in range(tiles):
            if grid[x][y] == 1:
                fill(actual_color)
                square((x*tile_size, y*tile_size), tile_size)



def getNeighbors(xcord, ycord):
    #give this function x and y, and it will give a list of tuples as neighbors
    #it should wrap around honestly.. that'd be cooler than things just going off screen
    neighbors = []
    return neighbors

def mouse_pressed(event):
    gridsx=event.x//tile_size
    gridsy=event.y//tile_size

    if grid[gridsx][gridsy]==1:
        grid[gridsx][gridsy]=0
    else:
        grid[gridsx][gridsy]=1


def key_pressed(event):
    #make 

    return

if __name__ == '__main__':
    run(frame_rate=15)