class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mx = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # Считаем площадь острова в этой координате
                mx = max(mx, self.area(grid, x, y))
        return mx

    def area(self, grid, x, y):
        if grid[x][y] == 0:
            # здесь нет острова
            return 0
        res = 1
        stack = [(x, y)]
        # меняем сушу на воду, чтобы не посчитать одну клетку дважды
        grid[x][y] = 0
        r = len(grid)
        c = len(grid[0])
        while stack:
            x, y = stack.pop()
            neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for nx, ny in neighbours:
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                # если на соседней клетке суша, то это продолжение того же острова
                if grid[nx][ny] == 1:
                    res += 1
                    stack.append((nx, ny))
                    grid[nx][ny] = 0
        return res