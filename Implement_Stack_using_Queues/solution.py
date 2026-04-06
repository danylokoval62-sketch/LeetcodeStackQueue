"""
Stack implementation using queues.

This module provides a Stack data structure implemented using two queues,
enabling LIFO (Last-In-First-Out) operations with O(n) push complexity.
"""

class Node:
    """Represents a single node in a linked list."""
    def __init__(self, data, next=None):
        """
        Initialize a node.
        
        Args:
            data: The data to store in the node.
            next: Reference to the next node (default: None).
        """
        self.data = data
        self.next = next


class Queue:
    """FIFO queue implementation using a linked list."""
    def __init__(self):
        """Initialize an empty queue with head and tail pointers."""
        self.head = None
        self.tail = None

    def push(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to enqueue.
        """
        new_node = Node(item)

        if self.is_empty():
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        """
        Remove and return the item from the front of the queue.
        
        Returns:
            The item at the front of the queue, or None if empty.
        """
        if self.is_empty():
            return None

        popped_data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return popped_data

    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        
        Returns:
            The item at the front, or None if empty.
        """
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.head is None


class MyStack:
    """Stack implementation using two queues for LIFO operations."""

    def __init__(self):
        """Initialize an empty stack with two auxiliary queues."""
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        """
        Add an element to the top of the stack.
        
        Args:
            x: The integer value to add to the stack.
        """
        self.q2.push(x)

        while not self.q1.is_empty():
           item = self.q1.pop()
           self.q2.push(item)

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Remove and return the element from the top of the stack.
        
        Returns:
            The integer value at the top of the stack.
        """
        return self.q1.pop()

    def top(self) -> int:
        """
        Return the element at the top of the stack without removing it.
        
        Returns:
            The integer value at the top of the stack.
        """
        return self.q1.peek()

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.q1.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
