class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def demonstrate_tree_construction():
    print("\n=== TREE CONSTRUCTION ===")
    leaderboard = BST()
    scores = [5000, 3000, 8000, 1000, 4000, 7000, 9000]
    for score in scores:
        leaderboard.insert(score)
    print(f"Inserted high scores in this order: {scores}")
    return leaderboard


def demonstrate_inorder_traversal(leaderboard):
    print("\n=== IN-ORDER TRAVERSAL ===")
    ranked_scores = leaderboard.inorder()
    print(f"Leaderboard sorted lowest to highest: {ranked_scores}")


def demonstrate_search(leaderboard):
    print("\n=== SEARCH TESTS ===")
    print(f"Is 8000 on the leaderboard? {leaderboard.search(8000)}")
    print(f"Is 1000 on the leaderboard? {leaderboard.search(1000)}")
    print(f"Is 6000 on the leaderboard? {leaderboard.search(6000)}")
    print(f"Is 2500 on the leaderboard? {leaderboard.search(2500)}")


def demonstrate_edge_cases():
    print("\n=== EDGE CASES ===")

    empty_board = BST()
    print(f"Traversing an empty leaderboard: {empty_board.inorder()}")
    print(f"Searching an empty leaderboard for 5000: {empty_board.search(5000)}")

    single_board = BST()
    single_board.insert(5000)
    print(f"Leaderboard with a single score: {single_board.inorder()}")
    print(f"Searching a single-score leaderboard for 5000: {single_board.search(5000)}")
    print(f"Searching a single-score leaderboard for 9000: {single_board.search(9000)}")

    duplicate_board = BST()
    duplicate_board.insert(5000)
    duplicate_board.insert(5000)
    print(f"Inserting the same score (5000) twice: {duplicate_board.inorder()}")


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    leaderboard = demonstrate_tree_construction()
    demonstrate_inorder_traversal(leaderboard)
    demonstrate_search(leaderboard)
    demonstrate_edge_cases()


if __name__ == "__main__":
    main()
