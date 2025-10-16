class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        self.isConnected = isConnected
        res = 0
        for c in range(len(isConnected)):
            if c not in self.visited:
                # город еще не был посещен, посетим его и все соединенные с ним
                res += 1
                self.visit(c)
        return res

    def visit(self, c):
        # отмечаем посещенными город c и все города, в которые можно попасть из него
        self.visited.add(c)
        stack = [c]
        while stack:
            c = stack.pop()
            for nxt, cnct in enumerate(self.isConnected[c]):
                if not cnct or nxt in self.visited:
                    continue
                self.visited.add(nxt)
                stack.append(nxt)