import sys
import math
import copy
import heapq


class State_A:
    def __init__(self, puzzle, g):
        self.puzzle = puzzle
        self.parent = None
        self.g = g

    def __lt__(self, other):
        return self.g < other.g


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

initial_state = State_A(initial_puzzle, 0)
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


def manhattan_heu(puzzle_1):
    h2 = 0;
    for i in range(side):
        for j in range(side):
            if puzzle_1[i][j] != 0:
                value = puzzle_1[i][j]
                # Find the coordinates of that value in the goal state
                row = (int)(value / side)
                col = value % side
                manhattan = abs(i - row) + abs(j - col)
                h2 += manhattan
    return h2

# print(initial_state.puzzle)


def a_star(initial_state):
    current_state = initial_state
    current_puzzle = current_state.puzzle
    count = 0
    expanded_number = 0
    max_frontier_q = 0
    if current_puzzle == goal_puzzle:
        print(to_board(current_state))
        print('Number of nodes added to the frontier_q is %d.' % (count))
        print('Number of nodes selected from the frontier_q for expansion is %d.' % (expanded_number))
        print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier_q))
        return
    # frontier and explored list
    frontier_q = []
    explored_q = []
    # dictionary to keep track of the costs in case states in frontier have a better f(n)
    cost_f = {}
    # solution to backtrack and print
    solution_q = []
    cost_f[current_state] = current_state.g + manhattan_heu(current_state.puzzle)
    heapq.heappush(frontier_q, (current_state.g + manhattan_heu(current_state.puzzle), current_state))
    # print(current_state.puzzle)
    while frontier_q:
        current_tuple = heapq.heappop(frontier_q)
        #print(current_tuple)
        #print(current_tuple[0])
        #print(current_tuple[1].puzzle)
        current_state = current_tuple[1]
        explored_q.append(current_state)
        expanded_number += 1
        if current_state.puzzle == goal_puzzle:
            # print('SUCCESS!')
            solution_q.append(current_state)
            while current_state != initial_state:
                current_state = current_state.parent
                solution_q.append(current_state)
            solution_q.reverse()
            for state in solution_q:
                print(to_board(state))
            print('Number of nodes added to the frontier is %d.' % (count))
            print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
            print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier_q))
            return
        # print(current_state)
        # 100k limit
        if len(explored_q) > 100000:
            print("No solution (100,000 limit reached)")
            print('Number of nodes added to the frontier is %d.' % (count))
            print('Number of nodes selected from the frontier for expansion is %d.' % (expanded_number))
            print('Maximum size of search queue at any given time of the search is %d.' % (max_frontier_q))
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
            left = State_A(move_left, current_state.g + 1)
            left.parent = current_state
            # print(left.puzzle)
            if left not in frontier_q and left not in explored_q:
                heapq.heappush(frontier_q, (left.g + manhattan_heu(left.puzzle), left))
                if len(frontier_q) > max_frontier_q:
                    max_frontier_q = len(frontier_q)
                count += 1
            elif left in frontier_q and left.g + manhattan_heu(left.puzzle) < cost_f[left]:
                cost_f[left] = left.g + manhattan_heu(left.puzzle)
                heapq.heappush(frontier_q, (left.g + manhattan_heu(left.puzzle), left))
                if len(frontier_q) > max_frontier_q:
                    max_frontier_q = len(frontier_q)
                count += 1

        if pos_row > 0:
            move_up = copy.deepcopy(current_puzzle)
            temp = move_up[pos_row][pos_col]
            move_up[pos_row][pos_col] = move_up[pos_row - 1][pos_col]
            move_up[pos_row - 1][pos_col] = temp
            up = State_A(move_up, current_state.g + 1)
            up.parent = current_state
            # print(move_up)
            if up not in frontier_q and up not in explored_q:
                heapq.heappush(frontier_q, (up.g + manhattan_heu(up.puzzle), up))
                if len(frontier_q) > max_frontier_q:
                    max_frontier_q = len(frontier_q)
                count += 1
            elif up in frontier_q and up.g + manhattan_heu(up.puzzle) < cost_f[up]:
                cost_f[up] = up.g + manhattan_heu(up.puzzle)
                heapq.heappush(frontier_q, (up.g + manhattan_heu(up.puzzle), up))
                if len(frontier_q) > max_frontier_q:
                    max_frontier_q = len(frontier_q)
                count += 1

        if pos_col < (side - 1):
            move_right = copy.deepcopy(current_puzzle)
            temp = move_right[pos_row][pos_col]
            move_right[pos_row][pos_col] = move_right[pos_row][pos_col + 1]
            move_right[pos_row][pos_col + 1] = temp
            right = State_A(move_right, current_state.g + 1)
            right.parent = current_state
            # print(move_right)
            if right not in frontier_q and right not in explored_q:
                heapq.heappush(frontier_q, (right.g + manhattan_heu(right.puzzle), right))
                if len(frontier_q) > max_frontier_q:
                    max_frontier_q = len(frontier_q)
                count += 1
            elif right in frontier_q and right.g + manhattan_heu(right.puzzle) < cost_f[right]:
                cost_f[right] = right.g + manhattan_heu(right.puzzle)
                heapq.heappush(frontier_q, (right.g + manhattan_heu(right.puzzle), right))
                if len(frontier_q) > max_frontier_q:
                    max_frontier_q = len(frontier_q)
                count += 1

        if pos_row < (side - 1):
            move_down = copy.deepcopy(current_puzzle)
            temp = move_down[pos_row][pos_col]
            move_down[pos_row][pos_col] = move_down[pos_row + 1][pos_col]
            move_down[pos_row + 1][pos_col] = temp
            down = State_A(move_down, current_state.g + 1)
            down.parent = current_state
            # print(move_down)
            if down not in frontier_q and down not in explored_q:
                heapq.heappush(frontier_q, (down.g + manhattan_heu(down.puzzle), down))
                if len(frontier_q) > max_frontier_q:
                    max_frontier_q = len(frontier_q)
                count += 1
            elif down in frontier_q and down.g + manhattan_heu(down.puzzle) < cost_f[down]:
                cost_f[down] = down.g + manhattan_heu(down.puzzle)
                heapq.heappush(frontier_q, (down.g + manhattan_heu(down.puzzle), down))
                if len(frontier_q) > max_frontier_q:
                    max_frontier_q = len(frontier_q)
                count += 1
    """Frontier empty therefore return no solution"""
    print("No Solution")


a_star(initial_state)
