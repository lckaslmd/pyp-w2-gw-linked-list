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
        if isinstance(self.elem, collections.Iterable) and isinstance(other.elem, collections.Iterable):
            return len(self.elem) is len(other.elem) and \
                   all(items[0] is items[1] for items in zip(self.elem, other.elem))
        else:
            return self.elem is other.elem

    def __repr__(self):
        return str(self)
