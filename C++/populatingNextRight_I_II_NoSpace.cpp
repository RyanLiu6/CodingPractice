/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == nullptr) {
            return;
        }

        queue<TreeLinkNode*> q;
        q.push(root);

        levHelper(q);
    }

    void levHelper(queue<TreeLinkNode*> q) {
        if (q.empty()) {
            return;
        }

        int n = q.size();

        vector<TreeLinkNode*> levArr;

        for (int i = 0; i < n; i++) {
            TreeLinkNode* node = q.front();
            q.pop();
            levArr.push_back(node);

            if (node->left != nullptr) {
                q.push(node->left);
            }
            if (node->right != nullptr) {
                q.push(node->right);
            }
        }

        for (int i = 0; i < levArr.size() - 1; i++) {
            levArr[i]->next = levArr[i + 1];
        }
        levArr[levArr.size() - 1]->next = nullptr;

        levHelper(q);
    }
};
