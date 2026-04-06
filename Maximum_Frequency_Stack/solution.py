"""
Maximum Frequency Stack implementation.

This module provides a FreqStack data structure that supports pushing and popping
the most frequently used element in O(1) amortized time complexity.
"""

from collections import defaultdict

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

class FreqStack:
    """Stack that returns the most frequently pushed element when popped."""

    def __init__(self):
        """
        Initialize the frequency stack with tracking structures.
        
        Maintains frequency count for each value and stacks grouped by frequency.
        """
        self.freq = defaultdict(int)
        self.group = defaultdict(Stack)
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        Push a value onto the stack and update its frequency.
        
        Args:
            val: The integer value to push.
        """
        self.freq[val] += 1

        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f

        self.group[f].push(val)


    def pop(self) -> int:
        """
        Remove and return the most frequently pushed element.
        
        Returns:
            The integer value with the highest frequency.
        """
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if self.group[self.max_freq].is_empty():
            self.max_freq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
