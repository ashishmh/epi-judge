import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# (lca_node, num_nodes)
def lca_inner(tree, node0, node1):
    if not tree:
        return None, 0

    lca_l, num_l = lca_inner(tree.left, node0, node1)
    if num_l == 2:
        assert lca_l is not None
        return lca_l, num_l
    lca_r, num_r = lca_inner(tree.right, node0, node1)
    if num_r == 2:
        assert lca_r is not None
        return lca_r, num_r

    x = int(tree in (node0, node1))
    result_num_nodes = x + num_l + num_r
    result_lca_node = tree if result_num_nodes == 2 else None
    return result_lca_node, result_num_nodes


def lca(tree, node0, node1):
    result, _ = lca_inner(tree, node0, node1)
    return result


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
