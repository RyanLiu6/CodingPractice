class BasicSoln:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)

        if root.val > val:
            return self.searchBST(root.left, val)

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val < val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)

        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)

        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            inSucc = self.findSucc(root.right)
            root.val = inSucc.val
            root.right = self.deleteNode(root.right, root.val)

        return root


    def findSucc(self, root):
        while root.left:
            root = root.left;

        return root
