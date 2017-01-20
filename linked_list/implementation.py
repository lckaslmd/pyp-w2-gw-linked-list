from interface import AbstractLinkedList
from node import Node

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
            
    def __getitem__(self, index):
        if index < 0 or index > len(self) or self.start is None:
            raise IndexError('Index out of bounds')
        for ind, item in enumerate(self):
            if ind is index:
                return item.elem

    def __add__(self, other):
        new_list = LinkedList()
        for index, item in enumerate(self):
            new_list.append(item.elem)
            if index is len(self) - 1:
                new_list.end.next = other.start
        return new_list
    
    def __iadd__(self, other):
        if self.start is None:
            self.start = LinkedList()
            self.end = other.start
        self.end.next = other.start
        return self

    def __eq__(self, other):
        return all([items[0].elem is items[1].elem for items in zip(self, other)])

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
        return self.__len__()

    def pop(self, index = -1):
        if self.__len__() == 0:
            raise IndexError
        else:
            for elem in self.elements:
                if self.elements[elem] == self.elements[index]:
                    self.elements.next == None
                
        return self
