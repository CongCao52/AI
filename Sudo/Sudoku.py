
############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import collections
import copy
import itertools
import random
import math

############################################################
# Sudoku Solver
############################################################

def sudoku_cells():
    sudoku =  [] 
    for i in range(9):
        for j in range(9):
            sudoku += [(i,j)]
    return sudoku

def sudoku_arcs():
    arcs = []
    cells = sudoku_cells()
    for c1 in cells:
        for c2 in cells:
            if c1 == c2:
                continue
            if c1[0] == c2[0] or c1[1] == c2[1]:
                arcs += [(c1,c2)]
            if (c1[0] // 3 == c2[0] // 3) and (c1[1] // 3 == c2[1] // 3):
                arcs += [(c1,c2)]
    return list(set(arcs))

def get_neighbors(arcs):
    neighbor_dict = dict()
    for arc in arcs:
        if arc[0] in neighbor_dict:
            neighbor_dict[arc[0]] += [arc[1]]
        else:
            neighbor_dict[arc[0]] = [arc[1]]
    return neighbor_dict



def read_board(path):
    file = open(path, "r")
    board = file.readlines()
    file.close()
    board_dict = dict()
    for i in range(9):
        for j in range(9):
            if board[i][j] == '*':
                board_dict[(i,j)] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                board_dict[(i,j)] = set([int(board[i][j])])
    return board_dict 

#b = read_board("medium1.txt")


class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()
    NEIGHBORS = get_neighbors(ARCS)

    def __init__(self, board):
        self.board = board

    def get_values(self, cell):
        return self.board[cell]

    def remove_inconsistent_values(self, cell1, cell2):
        c1 = self.get_values(cell1)
        c2 = self.get_values(cell2)
        if len(c2)==1 and len(c1)>1:
            c1.difference_update(c2)
            return True
        return False

    def infer_ac3(self):
        queue = collections.deque(Sudoku.ARCS)
        while len(queue) > 0:
            (cell1, cell2) = queue.popleft()
            if self.remove_inconsistent_values(cell1, cell2):
                
                for neighbor in self.NEIGHBORS[cell1]:
                    queue.append((neighbor,cell1))
        return 
    
    def is_solved(self):
        for c in Sudoku.CELLS:
            if len(self.board[c])>1:
                return False
            for n in Sudoku.NEIGHBORS[c]:
                if list(self.board[c])[0] in self.board[n]:
                    return False
        return True
        
        

    def infer_with_guessing(self):
        if self.is_solved():
            return 
        self.infer_improved()
        for c in Sudoku.CELLS:
            if len(self.board[c]) > 1:
                for v in self.board[c]:
                    copy_board = copy.deepcopy(self.board)
                    # guess
                    self.board[c] = set([v])
                    self.infer_with_guessing()
                    if self.is_solved():
                        break
                    else:
                        self.board = copy_board
                return           
    def infer_improved(self):
        
        result = True
        while result:
            self.infer_ac3()
            result = False

            for c in Sudoku.CELLS:
                if len(self.board[c]) > 1:
                    for v in self.board[c]:
                        unique_row = True
                        unique_col = True
                        unique_sub = True
                        for n in Sudoku.NEIGHBORS[c]:                        
                            if n[0] == c[0]:                        
                                if v in self.board[n]:
                                    unique_row = False                                
                            if n[1] == c[1]:                        
                                if v in self.board[n]:
                                    unique_col = False
                            else:
                                if v in self.board[n]:
                                    unique_sub = False                                
                        if unique_row or unique_col or unique_sub :
                            result = True
                            self.board[c] = set([v])
                            break
        return 
            

