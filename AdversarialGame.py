

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import collections
import copy
import itertools
import random
import math
from queue import Queue
############################################################
# Section 1: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    b = [[False for i in range(cols)] for j in range(rows)]
    obj = DominoesGame(b)
    return obj

class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.r = len(board)
        self.c = len(board[0])

    def get_board(self):
        return self.board

    def reset(self):
        new_board  = [[False for j in range(self.c)] for i in range(self.r)]
        self.board = new_board


    def is_legal_move(self, row, col, vertical):
        if self.board[row][col]:
            return False
        if vertical:
            if row < self.r-1 and not self.board[row + 1][col]:
                return True
        else:
            if col < self.c-1 and not self.board[row][col + 1]:
                return True
        return False
                

    def legal_moves(self, vertical):        
        for i in range(self.r):
            for j in range(self.c):
                if self.is_legal_move( i, j, vertical):
                    yield (i,j)


    def perform_move(self, row, col, vertical):
        if self.is_legal_move(row, col, vertical):
            self.board[row][col] = True
            if vertical:
                self.board[row + 1][col] = True
            else:
                self.board[row][col + 1] = True
    def game_over(self, vertical):
        if len(list(self.legal_moves(vertical)))==0:
            return True 
        
        return False
    
    
    def copy(self):
        b = copy.deepcopy(self.board)
        obj = DominoesGame(b)
        return obj

    def successors(self, vertical):
        for m in self.legal_moves(vertical):
            copy_domino = self.copy()
            copy_domino.perform_move(m[0], m[1], vertical)
            yield m, copy_domino   

    def min_value(self, vertical, limit, alpha,beta):
        if limit ==0 or self.game_over(vertical):
            return (None, self.calculate_score(not vertical), 1)
        v = float('inf')
        num = 0
        optimal_move =None
        for new_move, new_puzzle in self.successors(vertical):
            sub_move, sub_score, sub_num = new_puzzle.max_value(not vertical, limit-1, alpha, beta)
            num = num+sub_num
            if sub_score <v:
                optimal_move = new_move
                v = sub_score
                beta = min(beta, v)
            if v<=alpha:
                return(optimal_move, v, num)
        return (optimal_move, v, num)
 
    def max_value(self, vertical, limit, alpha,beta):
        if limit ==0 or self.game_over(vertical):
            return (None, self.calculate_score(vertical), 1)
        v = -float('inf')
        num = 0
        optimal_move =None
        for new_move, new_puzzle in self.successors(vertical):
            sub_move, sub_score, sub_num = new_puzzle.min_value(not vertical, limit-1, alpha, beta)
            num = num+sub_num
            if sub_score >v:
                optimal_move = new_move
                v = sub_score
                alpha = max(alpha, v)
            if v>=beta:
                return(optimal_move, v, num)
        return (optimal_move, v, num)

    def get_random_move(self, vertical):
        pass
    def calculate_score(self,vertical):
        score = len(list(self.legal_moves(vertical))) -  len(list(self.legal_moves(not vertical)))
        return score
    def get_best_move(self, vertical, limit):
        alpha = -float('inf')
        beta = float('inf')
        return self.max_value(vertical, limit, alpha, beta)
    

