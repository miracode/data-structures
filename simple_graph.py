
class Node(object):
    def __init__(self, value=None, visited=False):
        self.value = value
        self.visited = visited


class Edge(object):
    def __init__(self, n1=Node(), n2=Node()):
        self.n1 = n1
        self.n2 = n2
        self.node_vals = (n1.value, n2.value)


class Graph(object):

    def __init__(self):
        self.nodes_list = []
        self.edges_list = []

    def nodes(self):
        """Return list of all node values in graph"""
        return [node.value for node in self.nodes_list]

    def edges(self):
        """Return list of all edge tuples in graph"""
        return [edge.node_vals for edge in self.edges_list]

    def add_node(self, node_val):
        """Add new node value to the graph"""
        if node_val in self.nodes():
            raise ValueError("Node already exists in graph")
        else:
            node = Node(node_val)
            self.nodes_list.append(node)

    def add_edge(self, n1, n2):
        """Add new edge to graph with given node values"""
        # If node already exists in graph, use, otherwise create
        try:
            spot1 = self.nodes().index(n1)
            node1 = self.nodes_list[spot1]
        except ValueError:
            self.add_node(n1)
            node1 = self.nodes_list[-1]
        try:
            spot2 = self.nodes().index(n2)
            node2 = self.nodes_list[spot2]
        except ValueError:
            self.add_node(n2)
            node2 = self.nodes_list[-1]
        new_edge = Edge(node1, node2)
        self.edges_list.append(new_edge)

    def del_node(self, n):
        """Delete specified node from the graph"""

        # If node exists in list of nodes, remove. Else raise error
        node_in_graph = False
        for node in self.nodes_list:
            if n == node.value:
                self.nodes_list.remove(node)
                node_in_graph = True

        # Determine if node exists in edges & remove
        if node_in_graph:
            for edge in self.edges_list:
                if n in edge.node_vals:
                    self.edges_list.remove(edge)

        else:
            raise ValueError(u"Node does not exist in graph.")

    def del_edge(self, n1, n2):
        """Delete edge connecting specified nodes"""
        edge_in_graph = False
        for edge in self.edges_list:
            if n1 in edge.node_vals and n2 in edge.node_vals:
                self.edges_list.remove(edge)
                edge_in_graph = True

        if not edge_in_graph:
            raise ValueError(u"Edge does not exist in graph.")

    def has_node(self, n):
        """Returns True if node is in the graph, otherwise False"""
        if n in self.nodes():
            return True
        else:
            return False

    def _neighbors(self, n):
        """Return list of node objects connected to given node"""
        neighb = []
        for edge in self.edges_list:
            if edge.n1.value == n:
                neighb.append(edge.n2)
            if edge.n2.value == n:
                neighb.append(edge.n1)
        return neighb

    def neighbors(self, n):
        """Returns list of node values connected to given node"""
        if not self.has_node(n):
            raise ValueError(u"Node does not exist in graph")
        else:
            return [node.value for node in self._neighbors(n)]

    def adjacent(self, n1, n2):
        """Returns True if edge connects two nodes, False if not"""
        if not self.has_node(n1):
            raise ValueError(u"Node does not exist in graph")
        elif not self.has_node(n2):
            raise ValueError(u"Node does not exist in graph")
        else:
            edge_in_graph = False
            for edge in self.edges():
                if n1 in edge and n2 in edge:
                    edge_in_graph = True
            return edge_in_graph

    def depth_first_traversal(self, start):
        # Make sure the node exists
        if self.has_node(start):
            # Find the node with the start value
            i = 0
            start_node = self.nodes_list[0]
            while start_node.value != start:
                i += 1
                start_node = self.nodes_list[i]
            # Initialize list and flip the start visited flag to True
            dft_list = []
            dft_stack = [start_node]
            while dft_stack:
                v = dft_stack.pop()
                if not v.visited:
                    v.visited = True
                    dft_list.append(v.value)
                    for neighb in self._neighbors(v.value):
                        dft_stack.append(neighb)
            return dft_list

        else:
            raise ValueError(u"Node does not exist in graph")

