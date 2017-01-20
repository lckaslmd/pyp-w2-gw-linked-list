import collections

class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return 'Node({})'.format(self.elem) + ' > ' +                 \
              ('Node({})'.format(self.next.elem) if self.next else '/')

    def __eq__(self, other):
        def compare_elems(elem1, elem2):
            if (isinstance(elem1, collections.Iterable) and \
                isinstance(elem2, collections.Iterable)):
                return len(elem1) is len(elem2) and \
                       all(items[0] is items[1] for items in zip(elem1, elem2))
            else:
                return self.elem is other.elem
                
        def compare_nodes(self, other):
            if self is None and other is None:
                return True
            elif self is None or other is None:
                return False
            else:
                return compare_elems(self.elem, other.elem) and \
                       compare_nodes(self.next, other.next)
        
        return compare_nodes(self, other)
        
    def __repr__(self):
        return str(self)
