def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if not min_val < node.data < max_val:
        return False

    return is_bst(node.left, min_val, node.data) and is_bst(node.right, node.data, max_val)

def check_binary_search_tree_(root):
    return is_bst(root)