from collections import deque
from Queue import PriorityQueue


class Node(object):
    def __init__(self, value=None, visited=False, distance=float('inf')):
        self.value = value
        self.visited = visited
        self.distance = distance


class Edge(object):
    def __init__(self, n1=Node(), n2=Node(), weight=None):
        self.n1 = n1
        self.n2 = n2
        self.node_vals = (n1.value, n2.value)
        self.weight = weight


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

    def add_edge(self, n1, n2, weight=None):
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
        new_edge = Edge(node1, node2, weight)
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
            raise ValueError(u"Node does not exist in graph.")
        else:
            return [node.value for node in self._neighbors(n)]

    def _return_edge(self, n1, n2):
        """Returns edge object connecting n1 and n2"""
        return_edge = False
        if not self.has_node(n1):
            raise ValueError(u"Node does not exist in graph.")
        elif not self.has_node(n2):
            raise ValueError(u"Node does not exist in graph.")
        else:
            for edge in self.edges_list:
                if n1 in edge.node_vals and n2 in edge.node_vals:
                    return_edge = edge
        return return_edge

    def adjacent(self, n1, n2):
        """Returns True if edge connects two nodes, False if not"""
        return bool(self._return_edge(n1, n2))

    def _return_node(self, value):
        """Return node with specified value"""
        if self.has_node(value):
            # Find the node with the value
            i = 0
            start_node = self.nodes_list[0]
            while start_node.value != value:
                i += 1
                start_node = self.nodes_list[i]
            return start_node
        else:
            raise ValueError("Start node does not exist in graph.")

    def depth_first_traversal(self, start):
        """
        Return nodes that are viewed in the order of depth first traversal
        """
        start_node = self._return_node(start)
        # Initialize list
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

    def breadth_first_traversal(self, start):
        """
        Return nodes that are viewed in order of breadth first traversal
        """
        # Make sure the node exists
        start_node = self._return_node(start)
        # Initialize list and flip the start visited flag to True
        bft_list = []
        bft_queue = deque([start_node])
        while bft_queue:
            t = bft_queue.popleft()
            if not t.visited:
                t.visited = True
                bft_list.append(t.value)
                for neighb in self._neighbors(t.value):
                    bft_queue.append(neighb)
        return bft_list

    def weight_edge(self, n1, n2):
        """Return the weight of the edge connecting two nodes"""
        # Check that edge exists
        if self.adjacent(n1, n2):
            return self._return_edge(n1, n2).weight
        else:
            raise ValueError(u"Edge does not exist in graph.")

    # def dikstra(self, start):
    #     # Find the node with the start value:
    #     dpq = PriorityQueue()
    #     dpq.get()
    #     dpq.put((weight, value))
