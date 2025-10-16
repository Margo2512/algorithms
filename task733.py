class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        start = image[sr][sc]
        stack = [(sr, sc)]
        r = len(image)
        c = len(image[0])
        while stack:
            x, y = stack.pop()
            # если покрашена - мы уже заходили
            if image[x][y] == color:
                continue
            # красим
            image[x][y] = color
            # добавляем соседей, если они нужного цвета
            neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for nx, ny in neighbours:
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if image[nx][ny] == start:
                    stack.append((nx, ny))
        return image