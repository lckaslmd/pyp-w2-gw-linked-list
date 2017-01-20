from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=[]):
        self.elements = elements
        self.start = None
        self.end = self.start
        last = self.start

        if len(elements) is 1:
            self.start = Node(elements[0])
            self.start.next = None
            self.end = self.start
        else:
            for index, item in enumerate(elements):
                if index is 0:
                    self.start = Node(item)
                    last = self.start
                else:
                    last.next = Node(item)
                    last = last.next
                    if index is len(elements) - 1:
                        self.end = last

    def __str__(self):
        return '[' + ", ".join([str(item.elem) for item in self]) + ']'

    def __len__(self):
        return len([item for item in self if item is not None])

    def __iter__(self):
        self.current = self.start
        return self

    def next(self):
        if self.current is None:
            raise StopIteration()
        else:
            to_be_returned = self.current
            self.current = self.current.next
            return to_be_returned
            
    __next__ = next
    
    def __getitem__(self, index):
        index = (len(self) + index) if index < 0 else index
        if index < 0 or index >= len(self) or self.start is None:
            raise IndexError('Index out of bounds')
        for ind, item in enumerate(self):
            if ind is index:
                return item.elem

    def __add__(self, other):
        new_list = LinkedList()
        if self.start is not None:
            for item in self:
                new_list.append(item.elem)
        for item in other:
                new_list.append(item.elem)
        return new_list
    
    def __iadd__(self, other):
        if self.end is not None:
            self.end.next = other.start
        else:
            if other.start is not None:
                self.start = other.start
                self.end = other.end
        return self

    def __eq__(self, other):
        return isinstance(self, LinkedList) and isinstance(other, LinkedList) and \
               len(self) is len(other)                                        and \
               all([items[0].elem is items[1].elem for items in zip(self, other)])

    def __ne__(self, other):
        return self is not other
        
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
        counter = index
        current_node = self.start
        last_node = None
        save = 0
        
        if index < 0 or index >= len(self) or self.start is None:
            raise IndexError('Index out of bounds')
        else:
            
            if index is 0:
                save = self.start.elem
                self.start = self.start.next
            else:
                while counter > 0:
                    last_node = current_node
                    current_node = last_node.next
                    counter -= 1
                save = current_node.elem
                last_node.next = current_node.next
        return save
