# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:15:45 2020

@author: franc
"""
from random import randint

from os import system
from sys import exit

printgrid = lambda grid: [print(i) for i in grid]

def printgame(grid):
    out = "   "
    for i in range(len(grid)):
        
        if i + 1 < 10:
            
            out += " " + str(i + 1) + " "
            
        else:
            out += str(i + 1) + " "
    out += "\n"
    for i in range(len(grid)):
        if i + 1 < 10:
            
            out += " " + str(i + 1) + " "
        else:
            out +=  str(i + 1) + " "
       
        for j in grid[i]:
            if j == "O":
                out +=  "███"
            else:
                a = " " + j + " "
                out += a
        out += "\n"
    print(out)
            

def clear(): 
  system("cls")

class Minefield:
    def __init__(self, size):
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.gameview = [["O" for i in range(size)] for j in range(size)]
        self.counter = size**2
    def mine_in(self, number, x, y):
        self.counter -= number
        for i in range(number):
            a = True
            while a:
                b = (randint(0,len(self.board) - 1), randint(0,len(self.board) - 1))
                if self.board[b[0]][b[1]] != "M" and (b[0] != y or b[1] != x):
                    self.board[b[0]][b[1]] = "M"
                    for j in matrix(b[0],b[1]):
                        try:
                            if self.board[j[0]][j[1]] != "M" and j[0] >= 0 and j[1] >= 0:
                                self.board[j[0]][j[1]] += 1
                        except:
                            "a"
                    a = False
    
    def clear(self, x, y):
        if self.gameview[y][x] == "O":
            
            if self.board[y][x] == "M":
                self.gameview[y][x] = "X"
                return True
            elif self.board[y][x] > 0:
                self.gameview[y][x] = str(self.board[y][x])
                self.counter -= 1
            elif self.board[y][x] == 0:
                
                pos = [matrix(y,x)]
                a = 1
                start = 0
                while a > 0:
                    
                    pos = pos[start:]
                    start = len(pos)
                    for i in pos:
                        
                        for j in i:
                            try:
                                #print("j = " + str(j))
                                if self.board[j[0]][j[1]] == 0 and self.gameview[j[0]][j[1]] == "O" and j[0] >= 0 and j[1] >= 0:
                                    self.gameview[j[0]][j[1]] = " "
                                    self.counter -= 1
                                    pos.append(matrix(j[0],j[1]))
                                
                                    
                                elif self.board[j[0]][j[1]] > 0 and self.gameview[j[0]][j[1]] == "O" and j[0] >= 0 and j[1] >= 0:
                                    self.gameview[j[0]][j[1]] = str(self.board[j[0]][j[1]])
                                    self.counter -= 1
                                    
                                    
                            except:
                                 
                                 "a"
                    a = len(pos)
                         

        elif self.gameview[y][x] in " 123456789":
            print("Tile Already Cleared")
        else:
            print("Can't Clear Flagged Tile")
                                
                                
                    
    def flag(self, x, y):
        if self.gameview[y][x] == "O":
            self.gameview[y][x] = "F"
        elif self.gameview[y][x] == "F":
            self.gameview[y][x] = "O"
        elif not self.gameview[y][x] in "OF":
            print("Can't flag; tile cleared")
        
                    
def matrix(y,x):
    """takes a 2 dimenstional position coordinate and generates a 3x3 matrix 
    around that point
    """
    return [[y-1,x-1],[y-1,x],[y-1,x+1],[y, x-1],[y, x+1],[y+1, x-1],[y+1,x],[y+1, x+1]]

  

def rungame():
    clear()
    minefield = Minefield(int(input("Board size ")))
    number = int(input("Number of Mines "))
    printgame(minefield.gameview)
    x = int(input("X ")) - 1
    y = int(input("Y ")) - 1
    minefield.mine_in(number, x, y)
    minefield.clear(x, y)
    print(minefield.counter)
    clear()
    printgame(minefield.gameview)
    if minefield.counter == 0:
        print("All Mines Located ")
        if input("Press Enter to Play Again, X to exit ").upper() == "X":
            exit()
            
        rungame()
    
    while True:
        if input("Type f to flag ").upper() == "F":
            minefield.flag(int(input("X "))-1, int(input("Y "))-1)
        else:       
            if minefield.clear(int(input("X "))-1, int(input("Y "))-1) == True:
                clear()
                printgame(minefield.gameview)
                print("BOOM")
                if input("Press Enter to Play Again, X to exit ").upper() == "X":
                    exit()
                rungame()
            elif minefield.counter == 0:
                clear()
                printgame(minefield.gameview)
                print("All Mines Located ")
                
                if input("Press Enter to Play Again, X to exit ").upper() == "X":                    
                    exit()
                rungame()
        clear()
        printgame(minefield.gameview)
        
rungame()


