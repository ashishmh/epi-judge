import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode():
    def __init__(self, num, left, right):
        self.left = left
        self.right = right
        self.num = num


def generate_all_binary_trees(num_nodes):
    if num_nodes == 0:
        return [None]
    if num_nodes == 1:
        return [BinaryTreeNode(0, None, None)]

    result = []
    for k in range(num_nodes):
        left_subtrees = generate_all_binary_trees(k)  # binary trees of k nodes
        right_subtrees = generate_all_binary_trees(num_nodes - k - 1) # binary trees of num_nodes - k - 1 nodes
        for ltree in left_subtrees:
            for rtree in right_subtrees:
                result.append(BinaryTreeNode(0, ltree, rtree))
    return result


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_trees.py",
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
