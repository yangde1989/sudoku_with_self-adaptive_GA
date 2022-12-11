import random
import numpy as np
from copy import deepcopy

easy_sudoku =  np.array([[3,1,5,6,0,0,0,0,4],
                    [0,9,0,0,0,0,2,0,0],
                    [2,0,0,5,9,0,0,1,3],
                    [0,6,0,1,7,5,0,0,0],
                    [1,8,0,3,0,0,7,0,0],
                    [5,3,0,0,4,0,0,9,6],
                    [0,2,9,0,5,1,0,7,8],
                    [0,0,0,0,3,0,0,2,0],
                    [7,4,3,0,0,2,5,0,0]])

medium_sudoku =  np.array([[0,0,8,9,0,0,3,4,5],
                    [0,4,3,8,5,0,7,0,6],
                    [6,0,2,4,0,0,0,0,0],
                    [0,6,0,2,0,0,0,0,0],
                    [0,0,0,0,8,0,0,0,8],
                    [0,0,0,7,0,4,1,0,2],
                    [0,0,0,0,9,0,0,0,0],
                    [5,0,0,0,0,2,0,8,0],
                    [7,0,0,0,6,0,0,1,3]])

hard_sudoku =  np.array([[1,7,8,9,0,0,3,4,6],
                    [0,4,0,1,0,6,0,0,0],
                    [0,0,0,0,0,5,2,0,8],
                    [4,0,0,0,7,8,0,0,0],
                    [0,0,6,0,0,0,0,0,5],
                    [0,0,0,0,0,1,3,0,0],
                    [0,2,0,9,0,4,5,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [8,1,0,0,0,0,6,4,9]])

evil_sudoku =  np.array([[0,4,0,0,0,9,0,0,0],
                    [0,7,0,0,0,0,2,0,0],
                    [0,0,6,3,4,0,0,0,5],
                    [0,0,9,0,0,5,0,0,0],
                    [0,0,0,0,0,8,0,0,1],
                    [0,6,0,1,9,0,0,7,0],
                    [0,0,0,8,0,0,0,0,0],
                    [3,0,0,0,0,0,0,5,0],
                    [0,0,4,6,1,0,0,0,3]])

def convert_sudoku(sudoku):
    flat_sudoku = [[] for _ in range(len(sudoku))]
    row = 0
    col = 0
    counter = 0
    step = int((len(sudoku)**0.5))
    for a in range(step):
        col = 0
        for b in range(step):
            for i in range(row, row+step):
                for j in range(col, col+step):
                    flat_sudoku[counter].append(sudoku[i][j])
            counter+=1
            col+=3
        row+=3
    pos = deepcopy(flat_sudoku)
    for i in range(len(pos)):
        for j in range(len(pos[i])):
            if pos[i][j]!=0:
                pos[i][j]=1
    return flat_sudoku, pos
flatsudoku, pos = convert_sudoku(sudoku1)
# print(flatsudoku)
# print(pos)

# sudoku = [[] for i in range(9)]
# print(sudoku)

def population(sudoku, pop_num):
    flatsudoku, pos = convert_sudoku(sudoku)
    total_pop = []
    for _ in range(pop_num):
        flat = deepcopy(flatsudoku)
        for i in range(len(flat)):
            rand_list = []
            rand = random.sample(range(1, len(flat)+1), len(flat))
            for j in rand:
                if j not in flat[i]:
                    rand_list.append(j)
            while 0 in flat[i]:
                for k in rand_list:
                    flat[i][flat[i].index(0)]=k
        mut_rates = []
        for i in range(len(flat)):
            rand = random.random()
            mut_rates.append(rand)
        # mut_rates = [initial_mut_rate] * len(flat)
        flat += mut_rates
        total_pop.append(flat)
    return total_pop, pos

total, pos = population(flatsudoku, 5)
total1, pos = population(flatsudoku, 5)
# print(total)
# print('sigma', total[0][9:])

def convert_back(flatsudoku):
    filled_sudoku = np.zeros([int(len(flatsudoku)/2), int(len(flatsudoku)/2)])
    for i in range(9):
        index1 = i//int(np.sqrt(len(flatsudoku)/2))
        index2 = i%int(np.sqrt(len(flatsudoku)/2))
        for j in range(int(np.sqrt(len(flatsudoku)/2))):
            filled_sudoku[index1*3+j][3*index2:3*(index2+1)]= flatsudoku[i][3*j:3*(j+1)]
    return filled_sudoku

# converted_sudoku =convert_back(total[0])
# print(converted_sudoku)

def valid_solution(individual):
    for i in individual:
        set_i = set(i)
        if len(i) != len(set_i):
            return 'Invalid'
    return 'Valid'

