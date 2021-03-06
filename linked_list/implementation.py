from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=[]):
        self.start, self.end = None, None
        
        for elem in elements:
            self.append(elem)

    def __str__(self):
        return '[' + ", ".join([ str(item.elem) for item in self ]) + ']'

    def __len__(self):
        return len([ item for item in self ])

    def __iter__(self):
        self.current = self.start
        while self.current is not None:
            yield self.current
            self.current = self.current.next
    
    def __getitem__(self, index):
        index = (len(self) + index) if index < 0 else index
        if index < 0 or index >= len(self) or self.start is None:
            raise IndexError('Index out of bounds')
        for ind, item in enumerate(self):
            if ind is index:
                return item.elem
        
    def __add__(self, other):
        return LinkedList().__iadd__(self).__iadd__(other)
    
    def __iadd__(self, other):
        for item in other:
            self.append(item.elem)
        return self

    def __eq__(self, other):
        return isinstance(self, LinkedList) and isinstance(other, LinkedList) and \
               len(self) is len(other)                                        and \
               all(items[0].elem == items[1].elem for items in zip(self, other))

    def __ne__(self, other):
        return not (self == other)
        
    def append(self, elem):
        if self.end is None:
            self.start = Node(elem)
            self.start.next = None
            self.end = self.start
        else:            
            self.end.next = Node(elem)
            self.end = self.end.next

    def count(self):
        return len(self)

    def pop(self, index = -1):
        index = (len(self) + index) if index < 0 else index
        current_node, last_node = self.start, None
        
        if index < 0 or index >= len(self) or self.start is None:
            raise IndexError('Index out of bounds')
        else:
            if index is 0:
                self.start = self.start.next
            else:
                for _ in range(index, 0, -1):
                    last_node = current_node
                    current_node = last_node.next
                last_node.next = current_node.next
        return current_node.elem
