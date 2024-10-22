class Node:
    def __init__(self, node_type, left=None, right=None):
        self.type = node_type  # "operator" (AND/OR) or "operand" (condition)
        self.left = left       # Reference to left child (another Node or None)
        self.right = right     # Reference to right child (another Node or None)

    def __repr__(self):
        return f"Node(type={self.type}, left={self.left}, right={self.right})"

    def to_dict(self):
        """Convert the Node to a dictionary for JSON serialization."""
        return {
            "node_type": self.type,
            "left": self.left.to_dict() if isinstance(self.left, Node) else self.left,
            "right": self.right.to_dict() if isinstance(self.right, Node) else self.right
        }
