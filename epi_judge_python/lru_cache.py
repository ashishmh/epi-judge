from test_framework import generic_test
from test_framework.test_failure import TestFailure


class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = dict()
        self.dll = DoublyLinkedList()
        return

    def lookup(self, isbn):
        if isbn not in self.data:
            return -1
            # return False, None

        price, node = self.data[isbn]
        self.dll.delete_node(node)
        new_node = self.dll.insert_at_back(isbn)
        self.data[isbn] = price, new_node
        return price
        # return True, price

    def insert(self, isbn, price):
        if isbn in self.data:
            old_price, node = self.data[isbn]
            self.dll.delete_node(node)
            new_node = self.dll.insert_at_back(isbn)
            self.data[isbn] = (old_price, new_node)
        else:
            size = len(self.data)
            if size == self.capacity:
                node = self.dll.remove_from_front()
                del self.data[node.val]
            node = self.dll.insert_at_back(isbn)
            self.data[isbn] = (price, node)
        return

    def erase(self, isbn):
        if isbn not in self.data:
            return False

        _, node = self.data[isbn]
        del self.data[isbn]
        self.dll.delete_node(node)
        return True


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # inserts new node at front, returns ref
    def insert_at_front(self, val):
        self.size += 1
        if self.head is not None:
            new_node = Node(val, None, self.head)
            self.head.left = new_node
        else:
            new_node = Node(val, None, None)
            self.tail = new_node
        self.head = new_node
        return new_node

    # removes node from front, returns ref
    def remove_from_front(self):
        if self.size == 0:
            return None

        self.size -= 1
        old_head = self.head
        self.head = self.head.right
        if self.head:
            self.head.left = None
        else:
            self.tail = None
        return old_head

    # inserts node at back, returns ref
    def insert_at_back(self, val):
        self.size += 1
        new_node = Node(val, None, None)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.right = new_node
            new_node.left = self.tail
        self.tail = new_node
        return new_node

    # removes node from back, returns ref
    def remove_from_back(self):
        if self.size == 0:
            return None

        self.size -= 1
        old_tail = self.tail
        self.tail = self.tail.left
        if self.tail:
            self.tail.right = None
        else:
            self.head = None
        return old_tail

    # deletes nodes at specified ref
    def delete_node(self, node_addr):
        if self.size == 0:
            return

        if node_addr is self.head:
            self.remove_from_front()
        elif node_addr is self.tail:
            self.remove_from_back()
        else:
            node_addr.left.right = node_addr.right
            node_addr.right.left = node_addr.left
            self.size -= 1

    def print_list(self):
        ptr = self.head
        output = []
        while ptr:
            output.append(ptr.val)
            ptr = ptr.right
        print('List: ', output)
        return


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
