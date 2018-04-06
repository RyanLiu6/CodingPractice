'''
i.e. The tree is like:
         0
      /     \
     0        1
   /  \      /  \
  1    0    1    1
 /\   / \   /
1  1 1   0 1

Since it's complete binary tree, it is
[0,
0,1,
1,0,1,1,
1,1,1,0,1]

(Breath First Search)
'''


def set_bit(tree, pos, length):
    return


def clear_bit(tree, pos, length):
    if not tree or pos < 0 or length <= 0:
        return

    n = len(tree) - 1

    # Set self to 0
