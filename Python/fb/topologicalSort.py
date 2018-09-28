class tsSolution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = self.createGraph(numCourses, prerequisites)
        visited = [0 for _ in range(numCourses)]

        for i in range(numCourses):
            if not self.tsUtil(i, graph, visited):
                return False
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = self.createGraph(numCourses, prerequisites)
        visited = [0 for _ in range(numCourses)]
        stack = []

        for i in range(numCourses):
            if not self.tsUtil_Order(i, graph, visited, stack):
                return []
        return stack[::-1]

    def createGraph(self, numCourses, preReq):
        graph = [set() for _ in range(numCourses)]

        for x, y in preReq:
            graph[y].add(x)

        return graph

    def tsUtil(self, vertex, graph, visited):
        """
        visited[vertex] = -1 when vertex is current vertex
        visited[vertex] = 0 when not yet visited
        visited[vertex] = 1 when visited previously and had no cycle
        """
        if visited[vertex] == -1:
            return False
        elif visited[vertex] == 1:
            return True
        else:
            visited[vertex] = -1

            for child in graph[vertex]:
                if not self.tsUtil(child, graph, visited):
                    return False

            visited[vertex] = 1
            return True

    def tsUtil_Order(self, vertex, graph, visited, stack):
        """
        visited[vertex] = -1 when vertex is current vertex
        visited[vertex] = 0 when not yet visited
        visited[vertex] = 1 when visited previously and had no cycle
        """
        if visited[vertex] == -1:
            return False
        elif visited[vertex] == 1:
            return True
        else:
            visited[vertex] = -1

            for child in graph[vertex]:
                if not self.tsUtil_Order(child, graph, visited, stack):
                    return False

            visited[vertex] = 1
            stack.append(vertex)
            return True

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """


    def createGraph_Words(self, words):
        graph = {}

        for word in words:
            for c in word:
