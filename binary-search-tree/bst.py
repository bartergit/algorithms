from binarytree import tree, bst, Node

class Tree_Node(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.len_left = 0
        self.len_right = 0

    def add_left(self, val):
        self.len_left += 1
        child = Tree_Node(val)
        self.left = child
        return child

    def add_right(self, val):
        self.len_right += 1
        child = Tree_Node(val)
        self.right = child
        return child

    def insert(self, val):
        current_node = self
        while True:
            if val < current_node.val:
                if current_node.left is not None:
                    current_node.len_left += 1
                    current_node = current_node.left
                else:
                    current_node.add_left(val)
                    break
            else:
                if current_node.right is not None:
                    current_node.len_right += 1
                    current_node = current_node.right
                else:
                    current_node.add_right(val)
                    break


def create_bst(seq):
    seq = list(set(seq))
    root = Tree_Node(seq[0])
    for value in seq[1:]:
        root.insert(value)
    return root


def inorder(node: Tree_Node, func):
    if node is not None:
        inorder(node.left, func)
        func(node.val)
        inorder(node.right, func)


def reverse_order(node: Tree_Node, func):
    if node is not None:
        reverse_order(node.right, func)
        func(node.val)
        reverse_order(node.left, func)


def postorder(node: Tree_Node, func):
    if node is not None:
        func(node.val)
        postorder(node.left, func)
        postorder(node.right, func)


def rotate_right(root):  # pivot - new parent node
    pivot = root.left
    root.left = pivot.right
    pivot.right = root
    root.len_left -= pivot.len_left
    pivot.len_right = root.len_left + root.len_right + 1
    return pivot


def rotate_left(root):  # pivot - new parent node
    pivot = root.right
    root.right = pivot.left
    pivot.left = root
    root.len_right -= pivot.len_right
    pivot.len_left = root.len_left + root.len_right + 1
    return pivot


def find(node, value, path):
    if node is None:
        return
    path.append(node)
    if node.value == value:
        return
    elif value < node.value:
        find(node.left, value, path)
    else:
        find(node.right, value, path)


def depth_search(node: Tree_Node, res):
    if node is not None:
        depth_search(node.left, res)
        res.append(node)
        depth_search(node.right, res)


def find_min(node, k, start=0):
    if k == node.len_left + start:
        return node
    if k + start < node.len_left:
        return find_min(node.left, k, start)
    if node.len_left + start < k <= start + node.len_right + node.len_left:
        return find_min(node.right, k, start + node.len_left + 1)
    if k > start + node.len_right + node.len_left:
        return None


def rebalance(tree):
    if tree is None:
        return
    len_tree = tree.len_left + tree.len_right
    minimal = find_min(tree, len_tree // 2)
    path = []
    find(tree, minimal.val, path)
    path.pop()
    temp = None
    for node in reversed(path):
        if temp is not None:
            if temp.val < node.val:
                node.left = temp
            else:
                node.right = temp
        if minimal.val < node.val:
            temp = rotate_right(node)
        else:
            temp = rotate_left(node)
    minimal.left = rebalance(minimal.left)
    minimal.right = rebalance(minimal.right)
    return minimal


def depth_search_by_k(node: Tree_Node, res, k):
    if node is not None:
        depth_search(node.left, res)
        if len(res) <= k:
            res.append(node)
        else:
            return
        depth_search(node.right, res)


def find_k_minimal(root, k):
    res = []
    depth_search_by_k(root, res, k)
    return res[k].value


if __name__ == "__main__":
    a = [2, 1, 3]
    root = create_bst(a)
    print(find_min(root, 2))
