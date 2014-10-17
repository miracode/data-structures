data-structures
===============

linked_list.py  
create a linked list data structure


stack.py  
create a stack data structure


queue.py  
create a queue data structure with functions:
- enqueue(value) - add value to the queue
- dequeue() - removes and returns first value in queue
- size() - returns the size of the queue


parentheses.py  
parentheses(text) will return  
-    1 - if input text has open parentheses (more are open than closed)
-    0 - if input text has closed parentheses (there are an equal number)
-    -1 - if the input text has broken parentheses (there are more closed than open)


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