class topoSort:
    def ts(graph):
        stack = []
        visited = []

        for vertex in graph.getAllVertices():
            if vertex in visited:
                continue
            else:
                self.tsUtil(vertex, stack, visited)

        retArr = []
        for i in range(len(stack)):
            retArr.append(stack.pop())

        return retArr

    def tsUtil(vertex, stack, visited):
        visited.append(vertex);

        for child in vertex.adjacentVertices():
            if child in visited:
                continue
            else:
                self.tsUtil(child, stack, visited)

        stack.append(vertex)
