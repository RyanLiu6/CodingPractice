/*
// Definition for a Node.
class Node {
public:
    int val = NULL;
    Node* prev = NULL;
    Node* next = NULL;
    Node* child = NULL;

    Node() {}

    Node(int _val, Node* _prev, Node* _next, Node* _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
    }
};
*/
class Solution {
public:
    Node* flatten(Node* head)
    {
        return flatHelper(head);
    }

    Node* flatHelper(Node* head)
    {
        if (head == nullptr) return head;

        Node* curr = head;
        Node* nextCont = nullptr;

        while (curr->next != nullptr)
        {
            if (curr->child == nullptr)
            {
                cout << curr->val << " ";
                curr = curr->next;
            }
            else
            {
                cout << curr->val << " ";
                nextCont = curr->next;
                cout << "continue is " << nextCont->val << " ";
                Node* childStart = flatHelper(curr->child);

                curr->next = childStart;
                childStart->prev = curr;
                curr->child = nullptr;

                Node* childEnd = curr;
                while (childEnd->next != nullptr)
                {
                    childEnd = childEnd->next;
                }

                childEnd->next = nextCont;
                nextCont->prev = childEnd;

                curr = nextCont;
            }
        }
        return head;
    }
};
