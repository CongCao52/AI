############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import random
import copy
from queue import Queue
from queue import PriorityQueue



############################################################
# Section 1: Tile Puzzle
############################################################

def create_tile_puzzle(rows, cols):
    number =0
    m = []
    for i in range(rows):
        r = []
        for j in range(cols):
            number = number+1
            if number == rows * cols: 
                number=0
            r =r + [number]
        m = m + [r]
    return TilePuzzle(m)
    
#create_tile_puzzle(2,3)
    

class TilePuzzle(object):
    
    # Required
    def __init__(self, board):
        self.board = board

    def get_board(self):
        return self.board
    def perform_move(self, direction):
        # get the 0 
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]==0:
                    break
            if self.board[row][col]==0:
                break

        if direction =='up':
            if row <1:
                return False
            else:
                self.board[row][col],self.board[row - 1][col] =self.board[row - 1][col],self.board[row][col]

                return True
        elif direction == 'down':
            if row+1 >=len(self.board):
                return False
            else:
                self.board[row][col],self.board[row + 1][col] = self.board[row + 1][col],self.board[row][col]
                return True
        elif direction == 'left':
            if col <1:
                return False
            else:
                self.board[row][col],self.board[row][col - 1] = self.board[row][col - 1],self.board[row][col]
                return True
        elif direction =='right':
            if col+1>=len(self.board[0]):
                return False
            else:
                self.board[row][col],self.board[row][col + 1] = self.board[row][col + 1],self.board[row][col]
                return True
        return False 

    def scramble(self, num_moves):
        for i in range(num_moves):
            n = random.randint(1,4)
            if n==1:
                self.perform_move('up')
            elif n==2:
                self.perform_move('down')
            elif n==3:
                self.perform_move('left')
            else:
                self.perform_move('right')

    def is_solved(self):
        x = len(self.board)
        y = len(self.board[0])
        #solved_matrix = create_tile_puzzle(x,y)
        #### create initial matrix
        number =0
        m = []
        for i in range(x):
            r = []
            for j in range(y):
                number = number+1
                if number == x * y: 
                    number=0
                r =r + [number]
            m = m + [r]
        
        if self.board == m:
            return True 
        else:
            return False

    def copy(self):
        thecopy = copy.deepcopy(self.board)
        return TilePuzzle(thecopy)


    def successors(self):
        m = ['up','down','left','right']
        for move in m:
            copys = self.copy()
            if copys.perform_move(move):
                yield move, copys
        

    # Required
    def iddfs_helper(self, limit, moves):
        if limit == len(moves):
            return 
        else:
            for move, new_puzzle in self.successors():
                if new_puzzle.is_solved():
                    yield moves + [move]
                else:
                    yield from new_puzzle.iddfs_helper(limit,moves+[move])
    
    def find_solutions_iddfs(self):
        if self.is_solved():
            yield []
        else:
            index = 1
            lst = list(self.iddfs_helper(index,[]))
            while len(lst)==0:
                index = index+1
                lst = list(self.iddfs_helper(index,[]))
            yield from self.iddfs_helper(index, [])
            
    def manhattan_distance(self):
        r = len(self.board)
        c = len(self.board[0])
        
        distance = 0
        for i in range(r):
            for j in range(c):
                elem = self.board[i][j]
                if elem !=0:
                    new_r = (elem-1)//c
                    new_c = (elem-1)%c
                    distance +=abs(new_r-i) +abs(new_c-j)
        return distance
                    
    
    def MatrixToTuple(self):
        return tuple([tuple(r) for r in self.board])
            
    # Required
    def find_solution_a_star(self):
        frontier = PriorityQueue()
        frontier.put((0,([],self)))
        
        came_from = set()
        came_from.add(self.MatrixToTuple())
        
        while not frontier.empty():
            current_move, current_puzzle = frontier.get()[1]
            if current_puzzle.is_solved():
                return current_move
            else:
                for new_move, new_puzzle in current_puzzle.successors():
                    if new_puzzle.is_solved():
                        return current_move + [new_move]
                    else:
                        new_puzzle_totuple = new_puzzle.MatrixToTuple()
                        if new_puzzle_totuple not in (came_from ):
                            next_moves = current_move+[new_move]
                            priority = len(next_moves) +new_puzzle.manhattan_distance()
                            frontier.put((priority,(next_moves, new_puzzle)))
                            came_from.add(new_puzzle_totuple)
        return None
                            

############################################################
# Section 2: Grid Navigation
############################################################

class Grid(object):

    def __init__(self, start, goal, scene):
        # self.start = start
        self.position = start
        self.goal = goal
        self.board = scene

    def get_position(self):
        return self.position
    
    def perform_move(self, direction):
        r = self.position[0]
        c = self.position[1]
        if direction =='up':
            if r<1:
                return False
            else:
                new_r = r-1
                new_c = c
                return True
        elif direction=='down':
            if r >= len(self.board)-1:
                return False
            else:
                new_r = r+1
                new_c = c
        elif direction == 'left':
            if c<1:
                return False
            else:
                new_r = r 
                new_c = c-1
        elif direction == 'right':
            if c+1>=len(self.board[0]):
                return False
            else:
                new_r = r
                new_c = c+1
        elif direction =='up-left':
            if r<1 and c<1:
                return False
            else:
                new_r = r-1
                new_c = c-1
        elif direction == 'up-right':
            if r<1 or c>=len(self.board[0])-1:
                return False 
            else:
                new_r = r-1
                new_c =c+1
        elif direction =='down-left':
            if r >= len(self.board)-1 or c<1:
                return False
            else:
                new_r = r+1
                new_c = c-1
        elif direction =='down-right':
            if r>=len(self.board)-1 or c>=len(self.board[0])-1:
                return False
            else:
                new_r = r+1
                new_c = c+1
        try:
            if not self.board[new_r][new_c]:
                self.position = (new_r,new_c)
                return True
        except:
            return False
        return False

    def is_solved(self):
        return self.position==self.goal 

    def copy(self):
        copys = (self.position[0], self.position[1])
        return Grid(copys, self.goal,self.board)
        
        
    def successors(self):
        
        m = ['up','down','left','right','up-left','up-right','down-left','down-right']
        for move in m:
            copys = self.copy()
            if copys.perform_move(move):
                yield copys.position,copys
                
    def heuristic(self):
        diff = pow((self.position[0]-self.goal[0]),2)+pow((self.position[1]-self.position[1]),2)
        return math.sqrt(diff)

    def find_solution_a_star(self):
        current_r = self.position[0]
        current_c = self.position[1]
        goal_r = self.goal[0]
        goal_c = self.goal[1]
        
        if self.board[current_r][current_c] or self.board[goal_r][goal_c]:
            return None
       
        step = 0
        
        frontier = PriorityQueue()
        frontier.put((self.heuristic(),([self.position],self)))
        
        came_from = dict()
        came_from[self.position] = None
        
        cost  = dict()
        cost[self.position] = step
        
        while not frontier.empty():

            positions, current_puzzle = frontier.get()[1]
            current_position = positions[-1]
            
            if current_puzzle.is_solved():
                return positions 
            

            for new_pos, new_puzzle in current_puzzle.successors():
                
                diff = pow((current_position[0]-new_pos[0]),2)+pow((current_position[1]-new_pos[1]),2)

                new_step_cost = cost[current_position] + 3* math.sqrt(diff)
                
   
                if new_pos not in (came_from ):
                    if new_pos not in cost or new_step_cost < cost[new_pos]:
                        new_positions =  positions + [new_pos]
                        
                        cost[new_pos] = new_step_cost
                        priority = new_step_cost + new_puzzle.heuristic()
                        frontier.put((priority,(new_positions,new_puzzle)))
                        
                        came_from[new_pos] = current_position
        return None

def find_path(start, goal, scene):
    grid = Grid(start, goal, scene)
    
    return grid.find_solution_a_star()

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################
class LinearDisk(object):

    def __init__(self, length, n, disks):
        self.length = length
        self.num =n
        self.disks = disks
        self.goal = [0 if i < (self.length- self.num) else self.length-i for i in range(self.length)]
        

    def get_information(self):
        return self.disks, self.length, self.num

    def perform_move(self, old, new):
         self.disks[old],self.disks[new] = self.disks[new],self.disks[old]
        
    
        
       
    
    def copy(self):
        c = copy.deepcopy(self.disks)
        obj = LinearDisk(self.length, self.num, c)
        return obj
    
    def is_solved_distinct(self):
        result = self.disks ==self.goal
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
    
    def heuristic_distance(self):
        distance = sum([ (abs(len(self.disks) - elements - i))/2 + abs( (len(self.disks) - elements - i)) % 2 for (i, elements) in enumerate(self.disks) if elements > 0])
        return distance  

def solve_distinct_disks(length, n):
    d1 = LinearDisk(length,n, [ i+1 if i < n else 0 for i in range(length)])
    result = []
    if d1.is_solved_distinct():
        return result
    step = 0
    current = d1
    frontier = PriorityQueue()
    cost  = dict()
    came_from = dict()
    cost[tuple(current.disks)] = step
    frontier.put((current.heuristic_distance(),([],current)))
    came_from[tuple(current.disks)] = None
    while not frontier.empty():
        m, puzzle = frontier.get()[1]        
        for new_m,new_p in puzzle.successors_distinct():
            
            result = m + [new_m]
            
            new_step = cost[tuple(puzzle.disks)] + 1
            
            if new_p.is_solved_distinct():

                return result
              
            state = (result, new_p)

            if tuple(new_p.disks) not in (came_from ):
                if tuple(new_p.disks) not in cost or new_step < cost[tuple(new_p.disks)]:
                    
                        cost[tuple(new_p.disks)] = new_step
                        
                        p= new_step + new_p.heuristic_distance()
                        
                        frontier.put((p,state))
                        came_from[tuple(new_p.disks)] = tuple(puzzle.disks)
    return None

