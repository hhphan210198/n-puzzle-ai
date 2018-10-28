import sys
import math
import copy
import heapq


class State:
    def __init__(self, puzzle, cost):
        self.puzzle = puzzle
        self.parent = None
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


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

# print(initial_state.puzzle)


def uniform(initial_state):
    current_state = initial_state
    current_puzzle = current_state.puzzle
    count = 0
    expanded_number = 0
    max_frontier = 0
    if current_puzzle == goal_puzzle:
        print(to_board(current_state))
        print('Number of nodes added to the frontier is %d.' % (count))
        print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
        print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
        return
    # frontier and explored list
    frontier = []
    explored = []
    # dictionary to keep track of the costs in case states in frontier have a better f(n)
    cost_f = {}
    # solution to backtrack and print
    solution = []
    cost_f[current_state] = current_state.cost
    heapq.heappush(frontier, (current_state.cost, current_state))
    # print(current_state.puzzle)
    while frontier:
        current_tuple = heapq.heappop(frontier)
        #print(current_tuple)
        #print(current_tuple[0])
        #print(current_tuple[1].puzzle)
        current_state = current_tuple[1]
        explored.append(current_state)
        expanded_number += 1
        if current_state.puzzle == goal_puzzle:
            # print('SUCCESS!')
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
            return
        # print(current_state)
        # 100k limit
        if len(explored) > 100000:
            print("No solution (100,000 limit reached)")
            print('Number of nodes added to the frontier is %d.' % (count))
            print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
            print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier))
            return
        current_puzzle = current_state.puzzle
        for i in range(side):
            for j in range(side):
                if current_puzzle[i][j] == 0:
                    pos_row = i
                    pos_col = j
        if pos_col > 0:
            move_left = copy.deepcopy(current_puzzle)
            # print(move_left)
            temp = move_left[pos_row][pos_col]
            move_left[pos_row][pos_col] = move_left[pos_row][pos_col - 1]
            move_left[pos_row][pos_col - 1] = temp
            left = State(move_left, current_state.cost + 1)
            left.parent = current_state
            # print(left.puzzle)
            if left not in frontier and left not in explored:
                heapq.heappush(frontier, (left.cost, left))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1
            elif left in frontier and left.cost < cost_f[left]:
                cost_f[left] = left.cost
                heapq.heappush(frontier, (left.cost, left))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1

        if pos_row > 0:
            move_up = copy.deepcopy(current_puzzle)
            temp = move_up[pos_row][pos_col]
            move_up[pos_row][pos_col] = move_up[pos_row - 1][pos_col]
            move_up[pos_row - 1][pos_col] = temp
            up = State(move_up, current_state.cost + 1)
            up.parent = current_state
            # print(move_up)
            if up not in frontier and up not in explored:
                heapq.heappush(frontier, (up.cost, up))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1
            elif up in frontier and up.cost < cost_f[up]:
                cost_f[up] = up.cost
                heapq.heappush(frontier, (up.cost, up))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1

        if pos_col < (side - 1):
            move_right = copy.deepcopy(current_puzzle)
            temp = move_right[pos_row][pos_col]
            move_right[pos_row][pos_col] = move_right[pos_row][pos_col + 1]
            move_right[pos_row][pos_col + 1] = temp
            right = State(move_right, current_state.cost + 1)
            right.parent = current_state
            # print(move_right)
            if right not in frontier and right not in explored:
                heapq.heappush(frontier, (right.cost, right))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1
            elif right in frontier and right.cost < cost_f[right]:
                cost_f[right] = right.cost
                heapq.heappush(frontier, (right.cost, right))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1

        if pos_row < (side - 1):
            move_down = copy.deepcopy(current_puzzle)
            temp = move_down[pos_row][pos_col]
            move_down[pos_row][pos_col] = move_down[pos_row + 1][pos_col]
            move_down[pos_row + 1][pos_col] = temp
            down = State(move_down, current_state.cost + 1)
            down.parent = current_state
            # print(move_down)
            if down not in frontier and down not in explored:
                heapq.heappush(frontier, (down.cost, down))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1
            elif down in frontier and down.cost < cost_f[down]:
                cost_f[down] = down.cost
                heapq.heappush(frontier, (down.cost, down))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                count += 1
    """Frontier empty therefore return no solution"""
    print("No Solution")


uniform(initial_state)
