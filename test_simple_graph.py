import unittest
import simple_graph


class GraphTest(unittest.TestCase):

    def test_no_nodes(self):
        g = simple_graph.Graph()
        no_nodes = g.nodes()
        assert no_nodes == []

    def test_nodes(self):
        g = simple_graph.Graph()
        g.nodes_list = [simple_graph.Node(1), simple_graph.Node(2)]
        assert g.nodes() == [1, 2]

    def test_no_edges(self):
        g = simple_graph.Graph()
        no_edges = g.edges()
        assert no_edges == []

    def test_edges(self):
        g = simple_graph.Graph()
        node1 = simple_graph.Node(1)
        node2 = simple_graph.Node(2)
        node3 = simple_graph.Node(3)
        g.edges_list = [simple_graph.Edge(node1, node2),
                        simple_graph.Edge(node1, node3)]
        assert g.edges() == [(1, 2), (1, 3)]

    def test_add_node(self):
        g = simple_graph.Graph()
        g.add_node(1)
        assert g.nodes() == [1]

    def test_add_edge(self):
        g = simple_graph.Graph()
        new_node_val1 = 1
        new_node_val2 = 2
        g.add_edge(new_node_val1, new_node_val2)
        assert new_node_val1 in g.edges()[0]
        assert new_node_val2 in g.edges()[0]

    def test_add_edge_nodes(self):
        g = simple_graph.Graph()
        new_node_val1 = 1
        new_node_val2 = 2
        g.add_edge(new_node_val1, new_node_val2)
        assert new_node_val1 in g.nodes()
        assert new_node_val2 in g.nodes()
        new_node_val3 = 3
        g.add_edge(new_node_val1, new_node_val3)
        assert g.nodes().count(1) == 1

    def test_del_node_exists(self):
        g = simple_graph.Graph()
        new_node = 'hello'
        g.add_node(new_node)
        g.del_node(new_node)
        assert len(g.nodes()) == 0

    def test_del_node_not_exist(self):
        g = simple_graph.Graph()
        new_node1 = simple_graph.Node('hello')
        new_node2 = simple_graph.Node('goodbye')
        g.add_node(new_node1)
        with self.assertRaises(IndexError) as context:
            g.del_node(new_node2)
        self.assertEqual(context.exception.message,
                         u"Node does not exist in graph.")

    def test_del_node_deletes_edges(self):
        g = simple_graph.Graph()
        new_node1 = simple_graph.Node()
        new_node2 = simple_graph.Node()
        g.add_edge(new_node1, new_node2)
        g.del_node(new_node1)
        assert len(g.nodes()) == 1
        assert len(g.edges()) == 0

#     def test_del_edge_exists(self):
#         g = simple_graph.Graph()
#         new_node1 = simple_graph.Node()
#         new_node2 = simple_graph.Node()
#         g.add_edge(new_node1, new_node2)
#         g.del_edge(new_node2, new_node1)
#         assert len(g.edges()) == 0

#     def test_del_edge_not_exists(self):
#         g = simple_graph.Graph()
#         new_node1 = simple_graph.Node()
#         new_node2 = simple_graph.Node()
#         new_node3 = simple_graph.Node('nope')
#         g.add_edge(new_node1, new_node2)
#         with self.assertRaises(IndexError) as context:
#             g.del_edge(new_node1, new_node3)
#         self.assertEqual(context.exception.message, u"Edge does not exist \
# in graph.")
#         assert len(g.edges()) == 1

#     def test_has_node(self):
#         g = simple_graph.Graph()
#         new_node1 = simple_graph.Node('yes')
#         new_node2 = simple_graph.Node('no')
#         g.add_node(new_node1)
#         assert g.has_node(new_node1) is True
#         assert g.has_node(new_node2) is False

#     def test_neighbors(self):
#         n1 = simple_graph.Node('n1')
#         n2 = simple_graph.Node('n2')
#         n3 = simple_graph.Node('n3')
#         n4 = simple_graph.Node('n4')
#         g = simple_graph.Graph()
#         g.add_edge(n1, n2)
#         g.add_edge(n2, n4)
#         g.add_edge(n1, n4)
#         g.add_edge(n2, n3)
#         neighb = g.neighbors(n1)
#         assert n2 in neighb
#         assert n4 in neighb
#         assert n3 not in neighb

#     def test_neighb_no_node(self):
#         g = simple_graph.Graph()
#         node = simple_graph.Node('Nope')
#         with self.assertRaises(IndexError) as context:
#             g.neighbors(node)
#         self.assertEqual(context.exception.message, u"Node does not \
# exist in graph")

#     def test_adjacent(self):
#         n1 = simple_graph.Node('n1')
#         n2 = simple_graph.Node('n2')
#         n3 = simple_graph.Node('n3')
#         n4 = simple_graph.Node('n4')
#         g = simple_graph.Graph()
#         g.add_edge(n1, n2)
#         g.add_edge(n2, n4)
#         g.add_edge(n1, n4)
#         g.add_edge(n2, n3)
#         assert g.adjacent(n1, n2) is True
#         assert g.adjacent(n1, n3) is False

#     def test_adjacent_error(self):
#         g = simple_graph.Graph()
#         n1 = simple_graph.Node('n1')
#         n2 = simple_graph.Node('n2')
#         with self.assertRaises(IndexError) as context:
#             g.adjacent(n1, n2)
#         self.assertEqual(context.exception.message, u"Node does not exist \
# in graph")


if __name__ == '__main__':
    unittest.main()
