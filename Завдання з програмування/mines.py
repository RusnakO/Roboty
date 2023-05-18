from tkinter import*
import random

GRID_SIZE = 50 #
SQUARE_SIZE = 30#
MINES_NUM = 100#

root = Tk()
root.title("Pythonicway Minesweep")
c = Canvas(root, width=GRID_SIZE*SQUARE_SIZE, heigh=GRID_SIZE*SQUARE_SIZE)
c.pack()

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        c.create_rectangle(i *SQUARE_SIZE, j * SQUARE_SIZE,
                           i * SQUARE_SIZE + SQUARE_SIZE,
                           j * SQUARE_SIZE + SQUARE_SIZE, fill = 'gray')
mines = set(random.sample(range(1, GRID_SIZE**2+1), MINES_NUM))
clicked = set()

def click(event):
    ids = c.find_withtag(CURRENT)[0]
    if ids in mines:
        c.itemconfig(CURRENT, fill="red")
    elif ids not in clicked:
        c.itemconfig(CURRENT, fill="green")
    c.update()

def mark_mine(event):
    ids = c.find_withtag(CURRENT)[0]
    if ids not in clicked:
        clicked.add(ids)
        x1, y2, x2, y2 = c.coords(ids)
        c.itemconfig(CURRENT, fill="yellow")
    else:
        clicked.remove(ids)
        c.itemconfig(CURRENT, fill="gray")
c.bind("<Button-1>",click)
c.bind("<Button-3>", mark_mine)
def generate_neighbors(square):
    """повертає клітинки, сусідні із          square"""
    if square == 1:
        data={GRID_SIZE + 1, 2, GRID_SIZE + 2}
    elif square == GRID_SIZE ** 2:
        data = {square - GRID_SIZE, square - 1, square - GRID_SIZE -1}
    elif square == GRID_SIZE:
            data = {GRID_SIZE - 1, GRID_SIZE * 2, GRID_SIZE*2 - 1}
    elif square == GRID_SIZE ** 2 - GRID_SIZE+1:
        data = {square+1, square-GRID_SIZE, square-GRID_SIZE+1}
    elif square < GRID_SIZE:
        data = {square + 1, square-1, square + GRID_SIZE,
                square+GRID_SIZE -1, square + GRID_SIZE+1}
    elif square > GRID_SIZE ** 2 - GRID_SIZE:
        data = {square + 1, square-1, square - GRID_SIZE,
                square-GRID_SIZE -1, square - GRID_SIZE+1}
    elif square % GRID_SIZE == 0:
        data = {square + GRID_SIZE, square -GRID_SIZE, square - 1,
                square + GRID_SIZE -1, square - GRID_SIZE - 1}
    elif square % GRID_SIZE == 1:
        data = {square + GRID_SIZE, square - GRID_SIZE, square + 1,
                square + GRID_SIZE +1, square - GRID_SIZE + 1}
    else:
        data = {square - 1, square + 1, square - GRID_SIZE, square + GRID_SIZE,
                square - GRID_SIZE - 1, square - GRID_SIZE +1,
                square + GRID_SIZE + 1, square + GRID_SIZE -1}
    return data
def check_mines(neighbors):
    return len(mines.intersection(neighbors))
def clearence(ids):
    clicked.add(ids)
    neighbors = generate_neighbors(ids)
    around = check_mines(neighbor)
    if around:
        x1, y1, x2, y2 = c.coords(ids)
        c.itemsconfig(ids, fill = "green")
        c.create_text(x1 + SQUARE_SIZE / 2,
                      y1 + SQUARE_SIZE / 2,
                      text= str(around), font="Arial{}".format(int(SQUARE_SIZE/2)), fill='yellow')
        
    else:
        for item in set(neghbors).difference(clicked):
            c.itemcofig(item, fill="green")
            clearance(item)
import sys
sys.setrecursionlimit(5000)
root.mainloop()


    
    
