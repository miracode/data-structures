from collections import deque
from Queue import PriorityQueue


class Node(object):
    def __init__(self, value=None, visited=False):
        self.value = value
        self.visited = visited
        # for dikstra
        self.distance = float('inf')
        self.previous = None  # and a-star
        # for a-star
        # self.gscore = 0
        # self.fscore = 0


class Edge(object):
    def __init__(self, n1=Node(), n2=Node(), weight=None):
        self.n1 = n1
        self.n2 = n2
        self.weight = weight

    @property
    def node_vals(self):
        return (self.n1.value, self.n2.value)


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
        """Add new node value to the graph and return node"""
        if node_val in self.nodes():
            raise ValueError("Node already exists in graph")
        else:
            node = Node(node_val)
            self.nodes_list.append(node)
            return node

    def add_edge(self, n1, n2, weight=None):
        """Add new edge to graph with given node values"""
        # If node already exists in graph, use, otherwise create
        node1_filter = filter(lambda x: x.value == n1, self.nodes_list)
        node1 = node1_filter[0] if node1_filter else self.add_node(n1)
        node2_filter = filter(lambda x: x.value == n2, self.nodes_list)
        node2 = node2_filter[0] if node2_filter else self.add_node(n2)

        new_edge = Edge(node1, node2, weight)
        self.edges_list.append(new_edge)

    def _get_node(self, n):
        """Return node with specified value"""
        node = filter(lambda x: x.value == n, self.nodes_list)
        return node[0] if node else None

    def _get_edges_containing_node(self, n):
        return filter(lambda x: n in x.node_vals, self.edges_list)

    def _get_edge_containing_nodes(self, n1, n2):
        """Returns edge object connecting n1 and n2"""
        if not self.has_node(n1):
            raise ValueError(u"Node {} does not exist in graph.".format(n1))
        elif not self.has_node(n2):
            raise ValueError(u"Node {} does not exist in graph.".format(n2))
        else:
            edge = filter(lambda x: n1 in x.node_vals and
                          n2 in x.node_vals, self.edges_list)
        return edge[0] if edge else None

    def del_node(self, n):
        """Delete specified node from the graph"""

        node_to_delete = self._get_node(n)
        if node_to_delete:
            self.nodes_list.remove(node_to_delete)
        else:
            raise ValueError(u"Node does not exist in graph.")

        edges_to_delete = self._get_edges_containing_node(n)
        for edge in edges_to_delete:
            self.edges_list.remove(edge)

    def del_edge(self, n1, n2):
        """Delete edge connecting specified nodes"""
        edge_to_delete = self._get_edge_containing_nodes(n1, n2)
        if edge_to_delete:
            self.edges_list.remove(edge_to_delete)
        else:
            raise ValueError(u"Edge does not exist in graph.")

    def has_node(self, n):
        """Returns True if node is in the graph, otherwise False"""
        return n in self.nodes()

    def _neighbors(self, n):
        """Return list of node objects connected to given node"""
        neighb_edges = filter(lambda x: x.n1.value == n or x.n2.value == n,
                              self.edges_list)
        neighb = [edge.n1 if edge.n1.value != n else edge.n2
                  for edge in neighb_edges]
        return neighb

    def neighbors(self, n):
        """Returns list of node values connected to given node"""
        if not self.has_node(n):
            raise ValueError(u"Node does not exist in graph.")
        else:
            return [node.value for node in self._neighbors(n)]

    def adjacent(self, n1, n2):
        """Returns True if edge connects two nodes, False if not"""
        return bool(self._get_edge_containing_nodes(n1, n2))

    def depth_first_traversal(self, start):
        """
        Return nodes that are viewed in the order of depth first traversal
        """
        start_node = self._get_node(start)
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
        start_node = self._get_node(start)
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
        edge = self._get_edge_containing_nodes(n1, n2)
        if edge:
            return edge.weight
        else:
            raise ValueError(u"Edge does not exist in graph.")

    def dikstra(self, start):
        """Return shortest path according to Dikstra's algorithm"""
        # Find the node with the start value:
        start_node = self._get_node(start)
        start_node.distance = 0
        # Create priority queue
        dpq = PriorityQueue()
        dpq.put((start_node.distance, start_node))

        while dpq.qsize() > 0:
            curr = dpq.get()[1]
            curr.visited = True
            for neighb in self._neighbors(curr.value):
                if not neighb.visited:
                    alt = (curr.distance +
                           self.weight_edge(curr.value, neighb.value))
                    if alt < neighb.distance:
                        neighb.distance = alt
                        neighb.previous = curr
                        dpq.put((neighb.distance, neighb))
        # Create list of shortest path from start to final
        shortest = [start]
        while curr.value != start:
            shortest.insert(1, curr.value)
            curr = curr.previous
        return shortest

    def bellman_ford(self, start):
        """Returns weights and predecessors of following bellman ford path"""
        start_node = self._get_node(start)
        start_node.distance = 0
        weight = []
        previous = []
        # Relax edges repeatedly
        for i in range(len(self.nodes_list) - 1):
            for edge in self.edges_list:
                if edge.n1.distance + edge.weight < edge.n2.distance:
                    edge.n2.distance = edge.n1.distance + edge.weight
                    edge.n2.previous = edge.n1
                    weight.append(edge.n2.distance)
                    previous.append(edge.n2.previous.value)

        # Check for negative-weight cycle
        for edge in self.edges_list:
            if edge.n1.distance + edge.weight < edge.n2.distance:
                raise ValueError("Graph contains negative-weight cycle")

        return weight, previous

    # def _h_cost(self, start, finish):
    # """Return estimated heuristic cost from start to finish"""
    # cant figure one out

    # def a_star(self, start, finish):
    #     start_node = self._get_node(start)
    #     closedlist = []
    #     openlist = [start_node]
    #     camefrom = []

    #     while len(openlist) > 0:
    #         curr = min([node.fscore for node in openlist])
    #         if curr.value == finish:
    #             break

    #         openlist.remove(curr)
    #         closedlist.append(curr)
    #         for neighb in self._neighbors(curr.value):
    #             if neighb in closedlist:
    #                 tent_g_score = (curr.gscore +
    #                                 self.weight_edge(curr.value, neighb.value))
    #                 if neighb not in openlist or tent_g_score < neighb.gscore:
    #                     neighb.previous = curr
    #                     neighb.gscore = tent_g_score
    #                     neighb.fscore = (neighb.gscore +
    #                                      self._h_cost(neighb, finish))



