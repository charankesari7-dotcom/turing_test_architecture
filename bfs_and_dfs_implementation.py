from collections import deque

def is_valid(m, c):

    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and c > m:
        return False

    m_right = 3 - m
    c_right = 3 - c

    if m_right > 0 and c_right > m_right:
        return False

    return True

def successors(state):

    m, c, boat = state

    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    next_states = []

    for move in moves:

        if boat == 1:
            new_state = (m - move[0], c - move[1], 0)
        else:
            new_state = (m + move[0], c + move[1], 1)

        if is_valid(new_state[0], new_state[1]):
            next_states.append(new_state)

    return next_states

def bfs(start, goal):

    queue = deque([[start]])
    visited = set()

    while queue:

        path = queue.popleft()
        state = path[-1]

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for next_state in successors(state):

                new_path = list(path)
                new_path.append(next_state)
                queue.append(new_path)

    return None

def dfs(start, goal):

    stack = [[start]]
    visited = set()

    while stack:

        path = stack.pop()
        state = path[-1]

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for next_state in successors(state):

                new_path = list(path)
                new_path.append(next_state)
                stack.append(new_path)

    return None

def depth_limited_dfs(start, goal, limit):

    stack = [(start, [start], 0)]

    while stack:

        state, path, depth = stack.pop()

        if state == goal:
            return path

        if depth < limit:

            for next_state in successors(state):

                stack.append((next_state, path + [next_state], depth+1))

    return None

def iterative_deepening(start, goal):

    depth = 0

    while True:

        result = depth_limited_dfs(start, goal, depth)

        if result is not None:
            return result

        depth += 1


start = (3,3,1)
goal = (0,0,0)

print("BFS Solution")
print(bfs(start, goal))

print("\nDFS Solution")
print(dfs(start, goal))

print("\nIterative Deepening Solution")
print(iterative_deepening(start, goal))
