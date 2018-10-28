import sys
import math
import copy


class State:
    def __init__(self, puzzle, depth):
        self.puzzle = puzzle
        self.parent = None
        self.depth = depth


file = open(sys.argv[1], 'r')

init_numbers = file.read().split()

file.close()

# print(init_numbers)

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

initial_state = State(initial_puzzle, 0)
#print(initial_state.puzzle)

goal_puzzle = []
count = 0
for m in range(side):
    row = []
    for n in range(side):
        row.append(count)
        count += 1
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


def limited_dfs(initial_state, max_depth):
    count = 0
    current_state = initial_state
    current_puzzle = current_state.puzzle
    pos_row = 0
    pos_col = 0
    expanded_number = 0
    max_frontier = 0
    frontier = []
    frontier.append(current_state)
    max_frontier += 1
    count += 1
    visited = []
    solution = []
    while frontier:
        current_state = frontier.pop()
        expanded_number += 1
        # print(frontier)
        # print(current_state)
        visited.append(current_state)
        if current_state.puzzle == goal_puzzle:
            solution.append(current_state)
            while current_state != initial_state:
                current_state = current_state.parent
                solution.append(current_state)
            solution.reverse()
            for state in solution:
                print(to_board(state))
            print('Number of nodes added to the frontier is %d.' % (count))
            print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
            print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
            # print(max_depth)
            return 1
        # print(len(visited))
        if len(visited) > 100000:
            print("No solution (100,000 limit reached)")
            print('Number of nodes added to the frontier is %d.' % (count))
            print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
            print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
            return 0
        # print(visited)
        if current_state.depth == max_depth:
            continue
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
            left = State(move_left, current_state.depth +1)
            left.parent = current_state
            # print(left.puzzle)
            if left not in frontier and left not in visited:
                frontier.append(left)
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1

        if pos_row > 0:
            move_up = copy.deepcopy(current_puzzle)
            temp = move_up[pos_row][pos_col]
            move_up[pos_row][pos_col] = move_up[pos_row - 1][pos_col]
            move_up[pos_row - 1][pos_col] = temp
            up = State(move_up, current_state.depth + 1)
            up.parent = current_state
            # print(move_up)
            if up not in frontier and up not in visited:
                frontier.append(up)
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1

        if pos_col < (side - 1):
            move_right = copy.deepcopy(current_puzzle)
            temp = move_right[pos_row][pos_col]
            move_right[pos_row][pos_col] = move_right[pos_row][pos_col + 1]
            move_right[pos_row][pos_col + 1] = temp
            right = State(move_right, current_state.depth + 1)
            right.parent = current_state
            # print(move_right)
            if right not in frontier and right not in visited:
                frontier.append(right)
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1

        if pos_row < (side - 1):
            move_down = copy.deepcopy(current_puzzle)
            temp = move_down[pos_row][pos_col]
            move_down[pos_row][pos_col] = move_down[pos_row + 1][pos_col]
            move_down[pos_row + 1][pos_col] = temp
            down = State(move_down, current_state.depth + 1)
            down.parent = current_state
            # print(move_down)
            if down not in frontier and down not in visited:
                frontier.append(down)
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1
    return 0


def iterative_dfs(initial_state):
    current_depth = 0
    while 1:
        if limited_dfs(initial_state, current_depth) == 1:
            return
        current_depth += 1


iterative_dfs(initial_state)