import sys
import math
import copy
import heapq
from queue import PriorityQueue


class State:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.parent = None



file = open(sys.argv[1], 'r')

init_numbers = file.read().split()

file.close()

side = (int)(math.sqrt(len(init_numbers)))

# print(side)

for i in range(len(init_numbers)):
    if init_numbers[i] == '.':
        init_numbers[i] = '0'
    init_numbers[i] = (int)(init_numbers[i])

# print(init_numbers)

index = 0
initial_puzzle = []
for i in range(side):
    row = []
    for j in range(side):
        row.append(init_numbers[index])
        index += 1
    initial_puzzle.append(row)

initial_state = State(initial_puzzle)
#print(initial_state.puzzle)

goal_puzzle = []
c = 0
for m in range(side):
    row = []
    for n in range(side):
        row.append(c)
        c += 1
    goal_puzzle.append(row)

# print(goal_puzzle)
# print(len(goal_puzzle))


def to_board(state):
    puzzle = state.puzzle
    length = len(puzzle)
    dup = copy.deepcopy(puzzle)
    num = ""
    for i in range(length):
        for j in range(length):
            if dup[i][j] == 0:
                dup[i][j] = '.'
            dup[i][j] = (str)(dup[i][j])

    for k in range(length):
        num += " ".join(dup[k])
        num += "\n"
    return num

# print(to_board(goal_puzzle))


def bfs(initial_state):
    count = 0
    current_state = initial_state
    current_puzzle = current_state.puzzle
    pos_row = 0
    pos_col = 0
    expanded_number = 0
    max_frontier = 0
    if current_puzzle == goal_puzzle:
        print(to_board(current_state))
        print('Number of nodes added to the frontier is %d.' % (count))
        print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
        print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
        return
    frontier = []
    frontier.append(current_state)
    max_frontier += 1
    count += 1
    # print(frontier)
    explored = []
    solution = []
    while frontier:
        current_state = frontier.pop(0)
        expanded_number += 1
        # print(frontier)
        # print(current_state)
        explored.append(current_state)
        # print(len(explored))
        if len(explored) > 100000:
            print("No solution (100,000 limit reached)")
            print('Number of nodes added to the frontier is %d.' % (count))
            print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
            print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
            return
        #print(explored)
        current_puzzle = current_state.puzzle
        # getting index of the blank tile
        for i in range(side):
            for j in range(side):
                if current_puzzle[i][j] == 0:
                    pos_row = i
                    pos_col = j
        # print(pos_row+1)
        # print(pos_col+1)
        # print(current_puzzle)
        if pos_col > 0:
            move_left = copy.deepcopy(current_puzzle)
            # print(move_left)
            temp = move_left[pos_row][pos_col]
            move_left[pos_row][pos_col] = move_left[pos_row][pos_col - 1]
            move_left[pos_row][pos_col - 1] = temp
            left = State(move_left)
            left.parent = current_state
            # print(left.puzzle)
            if left not in frontier and left not in explored:
                if left.puzzle == goal_puzzle:
                    solution.append(left)
                    while left != initial_state:
                        left = left.parent
                        solution.append(left)
                    solution.reverse()
                    for state in solution:
                        print(to_board(state))
                    print('Number of nodes added to the frontier is %d.' %(count))
                    print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
                    print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
                    return
                else:
                    frontier.append(left)
                    if len(frontier) > max_frontier:
                        max_frontier = len(frontier)
                    count += 1

        if pos_row > 0:
            move_up = copy.deepcopy(current_puzzle)
            temp = move_up[pos_row][pos_col]
            move_up[pos_row][pos_col] = move_up[pos_row - 1][pos_col]
            move_up[pos_row - 1][pos_col] = temp
            up = State(move_up)
            up.parent = current_state
            # print(move_up)
            if up not in frontier and up not in explored:
                if up.puzzle == goal_puzzle:
                    solution.append(up)
                    while up != initial_state:
                        up = up.parent
                        solution.append(up)
                    solution.reverse()
                    for state in solution:
                        print(to_board(state))
                    print('Number of nodes added to the frontier is %d.' % (count))
                    print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
                    print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
                    return
                else:
                    frontier.append(up)
                    if len(frontier) > max_frontier:
                        max_frontier = len(frontier)
                    count += 1

        if pos_col < (side - 1):
            move_right = copy.deepcopy(current_puzzle)
            temp = move_right[pos_row][pos_col]
            move_right[pos_row][pos_col] = move_right[pos_row][pos_col + 1]
            move_right[pos_row][pos_col + 1] = temp
            right = State(move_right)
            right.parent = current_state
            # print(move_right)
            if right not in frontier and right not in explored:
                if right.puzzle == goal_puzzle:
                    solution.append(right)
                    while right != initial_state:
                        right = right.parent
                        solution.append(right)
                    solution.reverse()
                    for state in solution:
                        print(to_board(state))
                    print('Number of nodes added to the frontier is %d.' % (count))
                    print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
                    print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
                    return
                else:
                    frontier.append(right)
                    if len(frontier) > max_frontier:
                        max_frontier = len(frontier)
                    count += 1

        if pos_row < (side - 1):
            move_down = copy.deepcopy(current_puzzle)
            temp = move_down[pos_row][pos_col]
            move_down[pos_row][pos_col] = move_down[pos_row + 1][pos_col]
            move_down[pos_row + 1][pos_col] = temp
            down = State(move_down)
            down.parent = current_state
            # print(move_down)
            if down not in frontier and down not in explored:
                if down.puzzle == goal_puzzle:
                    solution.append(down)
                    while down != initial_state:
                        down = down.parent
                        solution.append(down)
                    solution.reverse()
                    for state in solution:
                        print(to_board(state))
                    print('Number of nodes added to the frontier is %d.' % (count))
                    print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
                    print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
                    return
                else:
                    frontier.append( down)
                    if len(frontier) > max_frontier:
                        max_frontier = len(frontier)
                    count += 1
        # print(len(frontier))
        # print(frontier)
    print("No Solution")

bfs(initial_state)
