import pygame
from pygame.locals import *
import time

def DrawScreen(grid, screen, myfont):
    width = 40
    height = 40
    margin = 5

    white = (255, 255, 255)
    ypos = margin
    for x in range(0,9):
        xpos = margin
        for y in range(0,9):
            pygame.draw.rect(screen,white,(xpos,ypos,width,height))
            if(grid[x][y] != 0):
                label = myfont.render(str(grid[x][y]), 1, (0,0,0))
                screen.blit(label, (xpos + margin,ypos))
            if((y+1)%3==0):
                xpos += margin*1.5 + width
            else:
                xpos += margin + width      
        if((x+1)%3==0):
            ypos += margin*1.5 + width 
        else:
            ypos += margin + width
    pygame.display.update()

def Find_vals(grid, pos):
    poss_vals = [1,2,3,4,5,6,7,8,9]
    Check_vals(grid,pos,poss_vals)
    if(len(poss_vals) == 1):
        grid[pos[0]][pos[1]] = poss_vals[0]

def Check_vals(grid, pos, poss_vals):
    #Check row
    for x in range(0,9):
        if(grid[pos[0]][x] in poss_vals):
            poss_vals.remove(grid[pos[0]][x])
    #Check col
    for y in range(0,9):
        if(grid[y][pos[1]] in poss_vals):
            poss_vals.remove(grid[y][pos[1]])
    box_y = pos[0] // 3
    box_x = pos[1] // 3
    for x in range(box_y*3, box_y*3 + 3):
        for y in range(box_x*3, box_x*3 + 3):
            if(grid[x][y] in poss_vals):
                poss_vals.remove(grid[x][y])
    return poss_vals

def Solve(grid, screen, myfont):
    solved = False
    while not solved:
        flag = 0
        for x in range(0,9):
            for y in range(0,9):
                if(grid[x][y] == 0):
                    pos = x,y
                    Find_vals(grid,pos)
                    time.sleep(0.01)
                    DrawScreen(grid, screen, myfont)
        for x in range(0,9):
            if (0 in grid[x]):
                flag = 1
        if flag == 0:
            solved = True
    
def main():
    grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((420,420))
    myfont = pygame.font.SysFont("monospace",40)

    DrawScreen(grid, screen, myfont)
    Solve(grid, screen, myfont)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()