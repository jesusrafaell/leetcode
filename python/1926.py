# Nearest Exit from Entrance in Maze
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        d = ((0, 1), (1, 0), (0, -1), (-1, 0))

        x, y = entrance
        # maze[x][y] = "x"
        q = collections.deque([(x, y)])
        seen = {(x, y)}

        p = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in d:
                    x = i + dx
                    y = j + dy
                    if (x < 0 or x == m or y < 0 or y == n) or (
                        (x, y) in seen or maze[x][y] == "+"
                    ):
                        continue
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return p
                    q.append((x, y))
                    seen.add((x, y))
            p += 1

        return -1
