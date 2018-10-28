Name: Hieu Phan

Fun fact: I have a Scottish fold cat.

Uninformed Search: Breadth First Search

Heuristic for A*: the sum of Manhattan distances of the tiles from their goal positions.

Based on the metrics results from different test cases, I can see the pattern that the number of nodes added to the
frontier, selected to expand, and the maximum size of the search queue of breadth first search are a lot larger than
those of A*. It is because while A* expand the 'best' node in the search queue, BFS expands each layer of nodes in the
queue. Therefore, if the solution has a high depth, BFS will take much longer to reach the goal state that A* does.

Running instruction:
- Breadth-First-Search:
python bfs.py text_file
Sample: python bfs.py /Users/hieuphan/Documents/Test_1.txt
- A Star:
python a_star.py text_file
Sample: python bfs.py /Users/hieuphan/Documents/Test_1.txt

Note:
- Both search methods are able to solve almost all of the 3x3 cases with variety from easy to hard, some simple versions
of 4x4 and 5x5 puzzles. They do return no solution when 100k limit is reached, even though it will take a while to reach
100k explored states.
- I use the number of explored nodes (from the frontier), not the number of nodes generated and added to the frontier,
to decide if the 100,000k limit has been reached.

Extra Credit Search:
I also implemented Iterative Deepening DFS, Uniform Cost Search
Running Instruction:
- Iterative Deepening DFS:
python iterative_dfs.py text_file
Sample: python iterative_dfs.py /Users/hieuphan/Documents/Test_1.txt

- Uniform Cost Search:
python uniform.py text_file
Sample: python uniform.py /Users/hieuphan/Documents/Test_1.txt
