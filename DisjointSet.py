# This is a basic Disjoint set implemented with
# Union by size with path compression.

class Node:
    ''' Every disjoint set holds a dictionary of node objects.
        These are those objects. '''

    def __init__(self, data):
        self.data = str(data)
        self.link = self
        self.size = 1

    def clear(self):
        self.link = self
        self.size = 1

class DisjointSet:
    ''' This is a union by size with path compression implementation. '''
    ''' Verticies are stored as a dictionary of nodes keyed on their data. '''

    def __init__(self, lst):
        self.verticies = {}
        self.size = len(lst)
        self.components = self.size

        for l in lst:
            n = Node(l)
            self.verticies[str(l)] = n

    # Simply prints the set for bug testing.
    def print(self):
        for v in self.verticies.values():
            print(v.data + ':', v.link.data)

        print("Number of connected components:", self.components)

    # Finds the root of the node with the given data.
    def find(self, data):
        try:
            node = self.verticies[str(data)]
            path = []

            while node.link != node:
                path.append(node)
                node = self.verticies[str(node.link.data)]

            for v in path:
                v.link = node

            return str(node.data)

        except KeyError:
            print('Invalid Key')
            return None

    # Performs union by size on two nodes given by keys a and b
    def union(self, a, b):

        try:
            rootA = self.verticies[self.find(a)]
            rootB = self.verticies[self.find(b)]

            # In the case of components of the same size,
            # The root will default to a
            if rootA.size >= rootB.size:
                rootB.link = rootA
                rootA.size+= rootB.size

            else:
                rootA.link = rootB
                rootB.size+= rootA.size

            # Modify the number of connected components.
            self.components-=1

        except KeyError:
            print('Invalid Key')
            return

    # Returns the number of connected nodes in node data's
    # connected component.
    def number(self, data):
        try:
            return self.verticies[self.find(data)].size
        except KeyError:
            print('Invalid Key')
            return 0
