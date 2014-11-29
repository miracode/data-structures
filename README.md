data-structures
===============


# Binary Heap
## Implementation of a min or max binary heap (default is max)

BinaryHeap([iterable=(), btype='max' or 'min'])

Functions:
* insert(val) - Insert a value to add to the heap which places it in the correct location
* pop() - Return and remove the top-most value of the heap

# Binary Search Tree
## Implementation of a recursive binary search tree where each node is also a binary search tree

BinarySearchTree([value=None])

Functions:
* insert(val) - Insert a value into the BST, creating a new BST node and placing it in the correct location.
* contains(val) - Return True or False whether val is contained in the BST
* size() - Return size (or number of nodes) in the BST
* depth() - Return depth/height of the BST
* balance() - Return integer indicating balance of BST: 0 for balanced, negatives for left-leaning, positive for right-leaning
* delete(val) - Remove specified value from BST if it exists

# Doubly Linked List
## Create a doubly linked list with nodes pointing forward and backward

DoublyLinkedList()

Functions:
* insert(val) - Add a node to the beginning of the DLL
* append(val) - Add a node do the end of the DLL
* pop() - Remove and return first node of the list
* shift() - Remove and return the last node of the list
* remove(val) - Remove and return the first node in the list with the specified value


# Hash Table
## Create a hash table with specified size using a hash algorithm based off the ordinal character number, the inded of the list, and the size of the list

HashTable(size)

Functions:
* get(key) - return hashed value associated with key
* set(key, val) - set a value to a key by adding it to a hashed list

# Insertion Sort
## Sort an array by comparing with preceding ordered element

insertion_sort(array) - Returns sorted array

# Linked List
## Create a singly linked list with a node pointing to the next value

Linked_list([*args]) - initial list optional

Functions:
* pop() - Remove first node of linked list
* insert(data) - insert data to head of linked list
* size() - Return size of linked list
* search(data) - Return node containing data in linked list if exists, otherwise None
* remove(node) - Remove specified node from list
* print_tuple() - Print entire linked list as a tuple literal





merge_sort.py	added merge sort	11 days ago
parentheses.py	parenthetics tests passed	2 months ago


priorityq.py	use peep in pop	a month ago
queue.py	cleaned queue	a month ago

queue.py  
create a queue data structure with functions:
- enqueue(value) - add value to the queue
- dequeue() - removes and returns first value in queue
- size() - returns the size of the queue
- 
quick_sort.py	in place sort	9 days ago
radix_sort.py	added another factor of n by finding the max number of digits	8 days ago
simple_graph.py	kind of confused about what bellman ford should return	20 days ago
stack.py	cleaned linked list and stack

linked_list.py  
create a linked list data structure


stack.py  
create a stack data structure








binary_heap.py  
create a max or min binary heap with functions:  
- insert(value) - add a value to the binary heap
- pop() - remove and return root value of binary heap
  - (Pop algorithm logic from [Wikipedia - Binary Heap - Max-Heapify](http://en.wikipedia.org/wiki/Binary_heap#Delete))

priorityq.py  
create a priority queue where lowest number has highest priority  
- insert(value, priority) - add value to queue
- pop() - returns and removes highest priority value in queue
- peek() - returns highest priority value without removing

bst.py  
create a binary search tree  
numbers added to the tree are placed to left if lower or to the right if higher
