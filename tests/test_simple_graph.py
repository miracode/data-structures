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
        with self.assertRaises(ValueError) as context:
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

    def test_del_edge_exists(self):
        g = simple_graph.Graph()
        new_node1 = 1
        new_node2 = 1
        g.add_edge(new_node1, new_node2)
        g.del_edge(new_node2, new_node1)
        assert len(g.edges()) == 0

    def test_del_edge_not_exists(self):
        g = simple_graph.Graph()
        new_node1 = 1
        new_node2 = 2
        new_node3 = simple_graph.Node('nope')
        g.add_edge(new_node1, new_node2)
        g.add_node(new_node3)
        with self.assertRaises(ValueError) as context:
            g.del_edge(new_node1, new_node3)
        self.assertEqual(context.exception.message, u"Edge does not exist \
in graph.")
        assert len(g.edges()) == 1

    def test_has_node(self):
        g = simple_graph.Graph()
        new_node1 = 'yes'
        new_node2 = 'no'
        g.add_node(new_node1)
        assert g.has_node(new_node1) is True
        assert g.has_node(new_node2) is False

    def test_neighbors(self):
        n1 = 'n1'
        n2 = 'n2'
        n3 = 'n3'
        n4 = 'n4'
        g = simple_graph.Graph()
        g.add_edge(n1, n2)
        g.add_edge(n2, n4)
        g.add_edge(n1, n4)
        g.add_edge(n2, n3)
        neighb = g.neighbors(n1)
        assert n2 in neighb
        assert n4 in neighb
        assert n3 not in neighb

    def test_neighb_no_node(self):
        g = simple_graph.Graph()
        node = 'Nope'
        with self.assertRaises(ValueError) as context:
            g.neighbors(node)
        self.assertEqual(context.exception.message, u"Node does not \
exist in graph.")

    def test_adjacent(self):
        n1 = 'n1'
        n2 = 'n2'
        n3 = 'n3'
        n4 = 'n4'
        g = simple_graph.Graph()
        g.add_edge(n1, n2)
        g.add_edge(n2, n4)
        g.add_edge(n1, n4)
        g.add_edge(n2, n3)
        assert g.adjacent(n1, n2) is True
        assert g.adjacent(n1, n3) is False

    def test_adjacent_error(self):
        g = simple_graph.Graph()
        n1 = 'n1'
        n2 = 'n2'
        with self.assertRaises(ValueError) as context:
            g.adjacent(n1, n2)
        self.assertEqual(context.exception.message, u"Node n1 does not exist \
in graph.")

    def test_dft(self):
        # 1 - 2 - 3
        #   \ |
        #     4
        n1 = 1
        n2 = 2
        n3 = 3
        n4 = 4
        g = simple_graph.Graph()
        g.add_edge(n1, n2)
        g.add_edge(n2, n4)
        g.add_edge(n1, n4)
        g.add_edge(n2, n3)
        actual = g.depth_first_traversal(n1)
        expected = [1, 2, 4, 3]
        assert actual == expected

    def test_bft(self):
        n1 = 1
        n2 = 2
        n3 = 3
        n4 = 4
        n5 = 5
        g = simple_graph.Graph()
        g.add_edge(n1, n2)
        g.add_edge(n2, n4)
        g.add_edge(n1, n4)
        g.add_edge(n2, n3)
        g.add_edge(n3, n5)
        actual = g.breadth_first_traversal(n1)
        expected = [1, 2, 4, 3, 5]
        assert actual == expected

    def test_weight(self):
        g = simple_graph.Graph()
        g.add_edge(1, 2, 3)
        assert g.weight_edge(1, 2) == 3
        with self.assertRaises(ValueError) as context:
            g.weight_edge(1, 5)
        self.assertEqual(context.exception.message, u"Node 5 does not exist \
in graph.")
        g.add_node(5)
        with self.assertRaises(ValueError) as context:
            g.weight_edge(1, 5)
        self.assertEqual(context.exception.message, u"Edge does not exist \
in graph.")

    def test_dikstra(self):
        g = simple_graph.Graph()
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 2)
        g.add_edge(3, 4, 5)
        g.add_edge(2, 4, 2)
        actual = g.dikstra(1)
        expected = [1, 2, 4]
        assert actual == expected

    def test_dikstra2(self):
        g = simple_graph.Graph()
        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 6, 2)
        g.add_edge(1, 4, 2)
        g.add_edge(4, 5, 2)
        g.add_edge(5, 3, 2)
        g.add_edge(1, 6, 5)
        actual = g.dikstra(1)
        expected = [1, 2, 3, 6]
        assert actual == expected

    def test_bf(self):
        g = simple_graph.Graph()
        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 6, 2)
        g.add_edge(1, 4, 2)
        g.add_edge(4, 5, 2)
        g.add_edge(5, 3, 2)
        g.add_edge(1, 6, 5)
        actual = g.bellman_ford(1)[1]
        expected = [1, 2, 3, 1, 4]
        assert actual == expected


if __name__ == '__main__':
    unittest.main()
