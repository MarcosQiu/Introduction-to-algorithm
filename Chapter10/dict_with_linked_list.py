from node import DictNode


class Dictionary:
    def __init__(self):
        self.head = DictNode()
        self.head.set_next(self.head)

    def insert(self, key, val):
        new_node = DictNode(key, val, self.head.get_next())
        self.head.set_next(new_node)

    def delete(self, key):
        prev = self.head
        cur = self.head.get_next()
        while cur.get_val() is not None and cur.get_key() != key:
            prev, cur = cur, cur.get_next()

        if cur.get_val() is not None:
            prev.set_next(cur.get_next())
        return cur.get_val()

    def search(self, key):
        cur = self.head.get_next()
        while cur.get_val() is not None and cur.get_key() != key:
            cur = cur.get_next()

        return cur.get_val()


if __name__ == '__main__':
    d = Dictionary()
    print(d.search(1))
    d.insert(2, 5)
    d.insert(3, 7)
    print(d.search(2))
    d.delete(2)
    print(d.search(3))

