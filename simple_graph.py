
class Node(object):
    pass


class Edge(object):
    pass


class Graph(object):

    def __init__(self):
        self.nodes_list = []
        self.edges_list = []

    def nodes(self):
        """Return list of all nodes in graph"""
        return self.nodes_list

    def edges(self):
        """Return list of all edges in graph"""
        return self.edges_list

    def add_node(self, node):
        """Add new node to the graph"""
        self.nodes_list.append(node)
