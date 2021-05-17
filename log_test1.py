def shortestPathBinaryMatrix(grid):
    # 2:20 5/12/21

    from collections import deque
    n = len(grid)
    step = 1
    visited = set([(0, 0)])
    dq = deque([(0, 0)])
    target = (n - 1, n - 1)

    if grid[0][0]:
        return -1

    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    while dq:
        n = len(dq)
        for i in range(n):
            top = dq.popleft()
            # if top == target:
            if top[0] == target[0] and top[1] == target[1]:
                return step

            for r, c in dirs:
                row, col = top[0] + r, top[1] + c
                if 0 <= row < n and 0 <= col < n:
                    if grid[row][col] == 0 and (row, col) not in visited:
                        visited.add((row, col))
                        dq.append((row, col))
        step += 1

    return -1

grid = [[0,1],[1,0]]

print(shortestPathBinaryMatrix(grid))

print(len(grid), len(grid[0]))