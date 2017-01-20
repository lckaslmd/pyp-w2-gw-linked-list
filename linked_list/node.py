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
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False
        return self.elem == other.elem and self.next == other.next
        
    def __repr__(self):
        return str(self)
