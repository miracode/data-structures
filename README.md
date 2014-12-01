data-structures
===============


# Binary Heap
### Implementation of a min or max binary heap (default is max)
Resources: [Wikipedia - Binary Heap - Max-Heapify Pop Algorithm](http://en.wikipedia.org/wiki/Binary_heap#Delete)

BinaryHeap([iterable=(), btype='max' or 'min'])

Functions:
* insert(val) - Insert a value to add to the heap which places it in the correct location
* pop() - Return and remove the top-most value of the heap


# Binary Search Tree
### Implementation of a recursive AVL binary search tree where each node is also a binary search tree.
#### Insertions and deletions will cause the tree to check whether it is currently balanced and rotate if necessary to rebalance.
Resources: [Interactive Python](http://interactivepython.org/courselib/static/pythonds/Trees/balanced.html), [Wikipedia](http://en.wikipedia.org/wiki/AVL_tree)

BinarySearchTree([value=None])

Functions:
* insert(val) - Insert a value into the BST, creating a new BST node and placing it in the correct location.  If the tree becomes imbalanced, tree will rotate until it becomes balanced.
* contains(val) - Return True or False whether val is contained in the BST
* size() - Return size (or number of nodes) in the BST
* depth() - Return depth/height of the BST
* balance() - Return integer indicating balance of BST: 0 for balanced, negatives for left-leaning, positive for right-leaning
* delete(val) - Remove specified value from BST if it exists.  If the tree becomes imbalanced, tree will rotate until it becomes balanced.

# Doubly Linked List
### Create a doubly linked list with nodes pointing forward and backward

DoublyLinkedList()

Functions:
* insert(val) - Add a node to the beginning of the DLL
* append(val) - Add a node do the end of the DLL
* pop() - Remove and return first node of the list
* shift() - Remove and return the last node of the list
* remove(val) - Remove and return the first node in the list with the specified value


# Hash Table
### Create a hash table with specified size using a hash algorithm based off the ordinal character number, the inded of the list, and the size of the list

HashTable(size)

Functions:
* get(key) - return hashed value associated with key
* set(key, val) - set a value to a key by adding it to a hashed list

# Insertion Sort
### Sort an array by comparing with preceding ordered element

insertion_sort(array) - Returns sorted array

# Linked List
### Create a singly linked list with a node pointing to the next value

Linked_list([*args]) - initial list optional

Functions:
* pop() - Remove first node of linked list
* insert(data) - insert data to head of linked list
* size() - Return size of linked list
* search(data) - Return node containing data in linked list if exists, otherwise None
* remove(node) - Remove specified node from list
* print_tuple() - Print entire linked list as a tuple literal


# Merge Sort
### Return a sorted list by merging already sorted sub-lists

merge_sort(array)


# Parentheses
### Return integer which signifies whether parentheses are properly closed

parentheses(text)
-    1 - if input text has open parentheses (more are open than closed)
-    0 - if input text has closed parentheses (there are an equal number)
-    -1 - if the input text has broken parentheses (there are more closed than open)

# Priority Queue
### Create a queue of values where lowest number has highest priority

PriorityQ()

Functions:
* insert(priority, value) - Insert a value with specified priority into the queue
* peek() - Return highest priority value without removing from the queue
* pop() - Return and remove the highest priority valuue from the queue


# Queue
### Queue data structure - First in, first out

Functions:
- enqueue(value) - add value to the end of the queue
- dequeue() - removes and returns first value in queue
- size() - returns the size of the queue

# Quick Sort
### Sort array by partitioning the array and sorting one either side of pivot

quick_sort(array)

# Radix Sort
### Sort array of numbers using numbers 0-9 as buckets for a least significant digit algorithm.

radix_sort(array)

# Simple Graph
### Make a simple graph with nodes and edges connecting two nodes
Resources: [Bellman-Ford](http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm#Algorithm), [Dikstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm)

Graph()

Functions:
* nodes() - Return list of all node values in graph
* edges() - Return list of all edges' node values as tuples
* add_node(node_val) - Add a new node value to the graph if it does not yet exist
* add_edge(n1, n2[, weight=None]) - add an edge with given node vals and optional weight
* del_node(n) - Remove node with given value from graph
* del(edge(n1, n2) - Remove edge connecting two node values
* has_node(n) - Return True or False whether graph contains node with specified value
* neighbors(n) - Return values of nodes connected to given node
* adjacent(n1, n2) - Return True or Faulse whether nodes are connected or not
* depth_first_traversal(start) - Returns traversal path from start to finish by searching depth first
* breadth_first_traversal(start) - Return traversal path from start to finish by searching breadth first
* weight_edge(n1, n2) - Return the weight of the edge connecting given nodes
* dikstra(start) - Return shortest path by following Dikstra's algorithm
* bellman_ford(start) - Return weight and predecessors of following a Bellman-Ford path

# Stack
### Create a stack - last on, first off

Stack()

Functions:
* push(data) - Add data to the stack
* pop() - Remove top item from the stack
