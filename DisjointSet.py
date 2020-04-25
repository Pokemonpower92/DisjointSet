# This is a basic Disjoint set implemented with
# Union by size with path compression.

class Node:
    ''' Every disjoint set holds a list of node objects.
        These are those objects. '''

    def __init__(self, data):
        self.data = str(data)
        self.link = None
        self.size = 1

    def clear(self):
        self.link = None
        self.size = 1

class DisjointSet:
    ''' This is a union by size with path compression implementation. '''

    def __init__(self, verticies):
        self.verticies = verticies
        self.size = len(verticies)
        self.components = self.size

    def print(self):
        for v in self.verticies:
            print(v.data + ':', v.link)

links = []

for x in range(10):
    n = Node(x)
    links.append(n)

set = DisjointSet(links)

set.print()
