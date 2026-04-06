"""
Queue implementation using stacks.

This module provides a Queue data structure implemented using two stacks,
where operations are optimized for amortized O(1) time complexity.
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


class Stack:
    """LIFO stack implementation using a linked list."""
    def __init__(self):
        """Initialize an empty stack."""
        self.head = None

    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to push onto the stack.
        """
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        """
        Remove and return the item from the top of the stack.
        
        Returns:
            The item at the top of the stack.
        """
        dat = self.head.data
        self.head = self.head.next

        return dat

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        
        Returns:
            The item at the top of the stack.
        """
        return self.head.data

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.head is None


class MyQueue:
    """Queue implementation using two stacks for efficient operations."""

    def __init__(self):
        """Initialize an empty queue with two auxiliary stacks."""
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        """
        Add an element to the rear of the queue.
        
        Args:
            x: The integer value to add to the queue.
        """
        self.stack_in.push(x)

    def pop(self) -> int:
        """
        Remove and return the element from the front of the queue.
        
        Returns:
            The integer value at the front of the queue.
        """
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                item = self.stack_in.pop()
                self.stack_out.push(item)
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Return the element at the front of the queue without removing it.
        
        Returns:
            The integer value at the front of the queue.
        """
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                item = self.stack_in.pop()
                self.stack_out.push(item)
        return self.stack_out.peek()

    def empty(self) -> bool:
        """
        Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.stack_in.is_empty() and self.stack_out.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
