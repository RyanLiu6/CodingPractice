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
     void connect(TreeLinkNode *root)
     {
         TreeLinkNode* tempHead = new TreeLinkNode(0);
         TreeLinkNode* prev = tempHead;

         while (root != nullptr)
         {
             if (root->left != nullptr)
             {
                 prev->next = root->left;
                 prev = prev->next;
             }
             if (root->right != nullptr)
             {
                 prev->next = root->right;
                 prev = prev->next;
             }
             root = root->next;
             if (root == nullptr)
             {
                 prev = tempHead;
                 root = tempHead->next;
                 tempHead->next = nullptr;
             }
         }
     }
 };
