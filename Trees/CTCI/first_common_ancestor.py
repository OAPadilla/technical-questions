

# 4.8 FIRST COMMON ANCESTOR
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_common_ancestor(root, p, q):
    # Error check that nodes p, q exist on tree
    if not covers(root, p) or not covers(root, q):
        return None
    return ancestor_helper(root, p, q)


def ancestor_helper(root, p, q):
    # If node is found
    if root is None or root == p or root == q:
        return root

    # Checks if nodes in same subtree, if not we found the ancestor node
    p_on_left = covers(root.left, p)
    q_on_left = covers(root.left, q)
    if p_on_left != q_on_left:
        return root

    # Child root node for subtree with p, q nodes
    child_side = TreeNode(root.left if p_on_left else root.right)
    return ancestor_helper(child_side, p, q)


def covers(root, p):
    if root is None:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)
