from collections import namedtuple

Node = namedtuple('Node', ['val', 'left', 'right'])


# recursive

def flatten(bst):
    if bst is None:
        return []
    return flatten(bst.left) + [bst.val] + flatten(bst.right)


# Write iterative version from scratch
def flatten_iter(bst):
    result = []
    parents = []

    def descend_left(node):
        while node is not None:
            parents.append(node)
            node = node.left

    descend_left(bst)
    # parents contains path from root to left-most leaf

    while parents:
        p = parents.pop()
        result.append(p.val)
        descend_left(p.right)

    return result


# Test

tree0 = None  # empty tree
tree1 = Node(5, None, None)
tree2 = Node(7, tree1, None)
tree3 = Node(7, tree1, Node(9, None, None))
tree4 = Node(2, None, tree3)
tree5 = Node(2, Node(1, None, None), tree3)


def check_flatten(f):
    assert f(tree0) == []
    assert f(tree1) == [5]
    assert f(tree2) == [5, 7]
    assert f(tree3) == [5, 7, 9]
    assert f(tree4) == [2, 5, 7, 9]
    assert f(tree5) == [1, 2, 5, 7, 9]
    print('ok')


check_flatten(flatten_iter)
