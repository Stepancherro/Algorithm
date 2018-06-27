#include <iostream>
#include <vector>

using namespace std;

class BSTNode
{
public:
  int m_nValue;
  BSTNode *m_pLeft;
  BSTNode *m_pRight;
  BSTNode *m_pParent;

public:
    BSTNode();
    BSTNode(int value);
    ~BSTNode();
};

BSTNode::BSTNode()
{
    m_nValue = 0;
    m_pLeft = m_pRight = m_pParent = NULL;
}

BSTNode::BSTNode(int value)
{
    m_nValue = value;
    m_pLeft = m_pRight = m_pParent = NULL;
}

BSTNode::~BSTNode()
{
}

void BST_Insert(BSTNode *pRoot, int value)
{
    BSTNode *y = NULL;
    BSTNode *x = pRoot;
    BSTNode *z = new BSTNode();
    z->m_nValue = value;
    z->m_pLeft = z->m_pRight = NULL;
    while(x != NULL)
    {
        y = x;
        if(z->m_nValue < x->m_nValue)
            x = x->m_pLeft;
        else
            x = x->m_pRight;
    }
    z->m_pParent = y;
    if(y == NULL)
        pRoot = z;
    else if(z->m_nValue < y->m_nValue)
        y->m_pLeft = z;
    else
        y->m_pRight = z;
}

void Inorder_Tree_walk(BSTNode* pRoot)
{
    if(pRoot != NULL)
    {
        Inorder_Tree_walk(pRoot->m_pLeft);
        cout << pRoot->m_nValue << " ";
        Inorder_Tree_walk(pRoot->m_pRight);
    }
}

BSTNode* Tree_Search(BSTNode* pRoot, int k)
{
    if(pRoot == NULL || k == pRoot->m_nValue)
        return pRoot;
    if(k < pRoot->m_nValue)
        return Tree_Search(pRoot->m_pLeft, k);
    else
        return Tree_Search(pRoot->m_pRight, k);
}

BSTNode* Tree_Minimum(BSTNode* x)
{
    while(x->m_pLeft != NULL)
        x = x->m_pLeft;
    return x;
}

BSTNode* Tree_Maximum(BSTNode* x)
{
    while(x->m_pRight != NULL)
        x = x->m_pRight;
    return x;
}

BSTNode* Tree_Successor(BSTNode* x)
{
    if(x->m_pRight != NULL)
        return Tree_Minimum(x->m_pRight);
    BSTNode *y = x->m_pParent;
    while(y != NULL && x == y->m_pRight)
    {
        x = y;
        y = y->m_pParent;
    }
    return y;
}

BSTNode* Tree_Predecessor(BSTNode* x)
{
    if(x->m_pLeft != NULL)
        return Tree_Maximum(x->m_pLeft);
    BSTNode *y = x->m_pParent;
    while(y != NULL && x == y->m_pLeft)
    {
        x = y;
        y = y->m_pParent;
    }
    return y;
}

void Transplant(BSTNode* pRoot, BSTNode* u, BSTNode* v)
{
    if(u->m_pParent == NULL)
        pRoot = v;
    else if(u == u->m_pParent->m_pLeft)
        u->m_pParent->m_pLeft = v;
    else
        u->m_pParent->m_pRight = v;
    if(v != NULL)
        v->m_pParent = u->m_pParent;
}

void Tree_Delete(BSTNode* pRoot, BSTNode* z)
{
    if(z->m_pLeft == NULL)
        Transplant(pRoot, z, z->m_pRight);
    else if(z->m_pRight == NULL)
        Transplant(pRoot, z, z->m_pLeft);
    else
    {
        BSTNode *y = Tree_Minimum(z->m_pRight);
        if(y->m_pParent != z)
        {
            Transplant(pRoot, y, y->m_pRight);
            y->m_pRight = z->m_pRight;
            y->m_pRight->m_pParent = y;
        }
        Transplant(pRoot, z, y);
        y->m_pLeft = z->m_pLeft;
        y->m_pLeft->m_pParent = y;
    }
}

int main()
{
    int n;
    cin >> n;
    BSTNode* pRoot = new BSTNode(15);
    for (int i = 0; i < n; ++i)
    {
        int temp;
        cin >> temp;
        BST_Insert(pRoot, temp);
    }
    Inorder_Tree_walk(pRoot);
    return 0;
}
