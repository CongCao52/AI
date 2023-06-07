
############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math 
import random 
from collections import deque
import copy



############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    n1 = math.factorial(n*n)
    n2 = math.factorial(n*n-n)
    n3 = math.factorial(n)
    return n1/n2/n3
    

def num_placements_one_per_row(n):
    return n**n

def n_queens_valid(board):
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i]==board[j]:
                return False
            if abs(board[i]-board[j])==abs(i-j):
                return False
    return True
            
                  
def n_queens_helper(x,n):
    return [x+[i] for i in range(n)]


def n_queens_solutions(n):
    lst = n_queens_helper([],n)
    result = []
    while len(lst)>=1:
        x=lst.pop()
        if(n_queens_valid(x)==True):
            if(len(x)==n):
                result.append(x)
            else:
                lst.extend(n_queens_helper(x,n))
    return result
                

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.mat = board

    def get_board(self):
        return self.mat

    def perform_move(self, row, col):
        self.mat[row][col] = not self.mat[row][col]
        if row-1 >=0:
            self.mat[row-1][col] = not self.mat[row-1][col]
        if col-1>=0:
            self.mat[row][col-1] = not self.mat[row][col-1]
        if row+2-len(self.mat)<=0:
            self.mat[row+1][col] = not self.mat[row+1][col]
        if col+2-len(self.mat[0])<=0:
            self.mat[row][col+1] = not self.mat[row][col+1]
        

    def scramble(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                index =  random.randint(1,2)
                if index == 1:
                    self.perform_move(i,j)



    def is_solved(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if self.mat[i][j]==True:
                    return False
        return True
    
    def copy(self):
        p_copy = []
        for i in range(len(self.mat)):
            r = []
            for j in range(len(self.mat[0])):
                r = r+[self.mat[i][j]]
            p_copy =p_copy+[r]
        obj = LightsOutPuzzle(p_copy)
        return obj
        

    def successors(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                p_copy1 = self.copy()
                p_copy1.perform_move(i,j)
                yield (i,j), p_copy1


###***
    def ChangetoTuple(self):
        return tuple([tuple(row) for row in self.mat])
    
    def find_solution(self):
        s = []
        if self.is_solved()==True:
            return s
        front = deque([([],self)])
        front_board  = [self.get_board()]
        exp = set()
        
        exp.add(self.ChangetoTuple())
        while(len(front)!=0):
            move, p=front.popleft()
            exp.add(p.ChangetoTuple())
            for new_move, new_p in p.successors():
                s = move+[new_move]
                if new_p.is_solved():
                    return s 
                state=(s,new_p)
                new_board = new_p.ChangetoTuple()
                if new_board not in exp and new_p not in front:
                    front.append(state)
                    front_board.append(new_p.get_board())
        return None

def create_puzzle(rows, cols):
    p = []
    for i in range (rows):
        r = []
        for j in range(cols):
            r = r+[False]
        p = p + [r]
    obj = LightsOutPuzzle(p)
    return obj    
#################################################################################


############################################################
#test
############################################################
# Section 3: Linear Disk Movement
############################################################


class LinearDisk(object):

    def __init__(self, length, num, disks):
        self.length = length
        self.num =num
        self.disks = disks
        

    def get_information(self):
        return self.length, self.num, self.disks

    def perform_move(self, old, new):
         self.disks[old],self.disks[new] = self.disks[new],self.disks[old]
        
        

    def is_solved(self):
        result = self.disks ==[0 if i<(self.length-self.num) else 1 for i in range(self.length)]
        return result
        
       
    
    def copy(self):
        c = copy.deepcopy(self.disks)
        obj = LinearDisk(self.length, self.num, c)
        return obj
        

    def successors(self):
        for i in range(self.length):
            if self.disks[i] !=0:
                if i<self.length-1 and self.disks[i+1]==0:
                    disk_copy = self.copy()
                    disk_copy.perform_move(i,i+1)
                    yield (i,i+1), disk_copy
                if i<self.length-2 and self.disks[i+1]!=0 and self.disks[i+2]==0:
                    disk_copy = self.copy()
                    disk_copy.perform_move(i,i+2)
                    yield (i,i+2), disk_copy
    
    
    
    
    
    def is_solved_distinct(self):
        result = self.disks ==[0 if i<(self.length-self.num) else self.length -i for i in range(self.length)]
        return result

    
    def successors_distinct(self):
        for i in range(self.length):
            if self.disks[i] !=0:
                
                if  i<self.length-1 and self.disks[i+1]==0:
                    disk_copy = self.copy()
                    disk_copy.perform_move(i,i+1)
                    yield (i,i+1), disk_copy
                    
                if self.length-2>i and self.disks[i+2]==0 and self.disks[i+1]!=0:
                    disk_copy = self.copy()
                    disk_copy.perform_move(i,i+2)
                    yield (i,i+2), disk_copy
                
                if  i>=1 and self.disks[i-1]==0:
                    disk_copy= self.copy()
                    disk_copy.perform_move(i,i-1)
                    yield (i,i-1), disk_copy
                
                if  i>=2 and self.disks[i-2]==0 and self.disks[i-1]!=0:
                    disk_copy = self.copy()
                    disk_copy.perform_move(i,i-2)
                    yield (i,i-2), disk_copy






def solve_identical_disks(length, n):
    x = [ 1 if i < n else 0 for i in range(length)]
    d = LinearDisk(length, n,x)

    result = []
    if d.is_solved():
        return result
    
    front = deque([([], d)])
    front_config = [tuple(d.disks)]
    
    exp = set()
    exp.add(tuple(d.disks))
    
    
    while (len(front) != 0):
        move, p = front.popleft()
        exp.add(tuple(p.disks))
        
        for new_move,new_p in p.successors():
            
            result = move + [new_move]
            if new_p.is_solved():

                return result
              
            state = (result, new_p)

            
            if tuple(new_p.disks) not in (exp or front_config):
                front.append(state)
                front_config.append(tuple(new_p.disks))
    return None    
    
    
 
    
    
def solve_distinct_disks(length, n):
    x = [ i+1 if i < n else 0 for i in range(length)]
    d = LinearDisk(length, n,x)
    
    result = []

    if d.is_solved_distinct():
        return result
    
    front = deque([([], d)])
    front_config = [tuple(d.disks)]
    
    exp = set()
    exp.add(tuple(d.disks))
    
    
    while (len(front) != 0):
        move, p = front.popleft()
        exp.add(tuple(p.disks))
        
        for new_move,new_p in p.successors_distinct():
            
            result = move + [new_move]
            if new_p.is_solved_distinct():

                return result
              
            state = (result, new_p)

            
            if tuple(new_p.disks) not in (exp or front_config):
                front.append(state)
                front_config.append(tuple(new_p.disks))

    return None
