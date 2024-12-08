from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_from_list(lst):
    if not lst:  # Handle empty list case
        return None

    root = TreeNode(lst[0])  # The first element is the root
    queue = deque([root])  # Queue to hold nodes for level-order construction
    i = 1  # Pointer for list elements

    while queue and i < len(lst):
        current = queue.popleft()  # Get the current node to attach children
        if current:  # Ensure current node is not None
            # Attach left child
            if i < len(lst) and lst[i] is not None:
                current.left = TreeNode(lst[i])
                queue.append(current.left)
            i += 1

            # Attach right child
            if i < len(lst) and lst[i] is not None:
                current.right = TreeNode(lst[i])
                queue.append(current.right)
            i += 1

    return root


def print_tree(root):
    if not root:
        return "Empty Tree"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Clean up trailing Nones for display
    while result and result[-1] is None:
        result.pop()
    print(result)
