class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.val)
            self._inorder_traversal(root.right, result)
        return result

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, root, result):
        if root:
            result.append(root.val)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)
        return result

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, root, result):
        if root:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.val)
        return result

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

def bst_menu():
    bst = BST()
    while True:
        print("\n--- BST Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. In-order Traversal")
        print("4. Pre-order Traversal")
        print("5. Post-order Traversal")
        print("6. Search")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key to insert: "))
            bst.insert(key)
        elif choice == 2:
            key = int(input("Enter key to delete: "))
            bst.delete(key)
        elif choice == 3:
            print("In-order traversal:", bst.inorder_traversal())
        elif choice == 4:
            print("Pre-order traversal:", bst.preorder_traversal())
        elif choice == 5:
            print("Post-order traversal:", bst.postorder_traversal())
        elif choice == 6:
            key = int(input("Enter key to search: "))
            result = bst.search(key)
            if result:
                print("Found node with key", key)
            else:
                print("Node with key", key, "not found")
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    bst_menu()
