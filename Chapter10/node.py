class Node:
    def __init__(self, val=None, next_node=None):
        self._val = val
        self._next = next_node

    def get_val(self):
        return self._val

    def get_next(self):
        return self._next

    def set_val(self, val):
        self._val = val

    def set_next(self, next_node):
        self._next = next_node


class DictNode:
    def __init__(self, key=None, val=None, next_node=None):
        self._key = key
        self._val = val
        self._next = next_node

    def get_key(self):
        return self._key

    def get_val(self):
        return self._val

    def get_next(self):
        return self._next

    def set_key(self, key):
        self._key = key

    def set_val(self, val):
        self._val = val

    def set_next(self, next_node):
        self._next = next_node
