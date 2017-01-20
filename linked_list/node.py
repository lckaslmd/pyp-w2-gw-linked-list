import collections

class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return 'Node({})'.format(self.elem) + ' > ' + ('Node({})'.format(self.next.elem) if self.next else '/')

    def __eq__(self, other):
        def compare_elems(elem1, elem2):
            if isinstance(elem1, collections.Iterable) and isinstance(elem2, collections.Iterable):
                return len(elem1) is len(elem2) and \
                       all(items[0] is items[1] for items in zip(elem1, elem2))
            else:
                return self.elem is other.elem
                
        flg_equal = True
        current_self, current_other = self, other
        while current_self is not None and current_other is not None:
            flg_equal = flg_equal and compare_elems(current_self.elem, current_other.elem)
            current_self = current_self.next
            current_other = current_other.next
        if current_self is None and current_other is not None or \
           current_self is not None and current_other is None:
            return False
        else:
            return flg_equal
            
    def __repr__(self):
        return str(self)
        