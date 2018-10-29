For this project, I implemented different search algorithms to solve the n-puzzle problem, including:
- BFS
- Uniform cost search (which do not differ from BFS because step costs are constant)
- Iterative Deepening DFS
- A* (Manhattan Heuristic)
Based on the testing metrics on different boards of different sizes, A* is the most efficient algorithm as expect.
Boards can be fed as .txt file. Example: 
1 2 .
3 4 5
6 7 8

The result will include the solution and its metrics. Example for the board above using a_star:
1 2 .
3 4 5
6 7 8

1 . 2
3 4 5
6 7 8

. 1 2
3 4 5
6 7 8

Number of nodes added to the frontier is 5.
Number of nodes selected from the frontier for expansion is 3.
Maximum size of search queue at any given time of the search is 4.

(Note: The algorithms will terminate when it reaches 100,000 explored nodes from the frontier and return no solution) 
