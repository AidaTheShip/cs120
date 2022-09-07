#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)

def calculate_sizes(v):
    # Base case for recursion: When we are at the leaf vertices, their "left" and "right" pointers will point to None
    if v.left == v.right == None: 
        v.size = 1
        return v.size # returns the size to add up
    else:
        # the size of the earlier node is equal to the size of its children + 1 (the 1 for its own size)
        if v.left == None:
            size = calculate_sizes(v.right) + 1
        elif v.right == None: 
            size = calculate_sizes(v.left) + 1
        else: 
            size = calculate_sizes(v.left) + calculate_sizes(v.right) + 1
        v.size = size
        return size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)

# go with n/2 > 
    
# General logic for this: write a helper function that returns the potential if you remove a certain vertex
def find_vertex(r):
    if not r: 
        return 0
    elif calculate_potential(r) <= r.size/2:
        return r
    else:
        return find_vertex(r.left) or find_vertex(r.right)

## takes in the vertex, that will be removed - gives back the potential

def calculate_size(r):
    if r == None or r.size == None:
        return 0
    else:
        return r.size

def calculate_potential(r):
    if r == None:
        return 0
    s1 = calculate_size(r.parent)
    s2 = calculate_size(r.left)
    s3 = calculate_size(r.right)
    print(s1, s2,s3)
    if s1 <= s2 and s3 <= s2: 
        return s2
    elif s2 <= s1 and s3 <= s1: 
        return s1
    elif s1 <= s3 and s2 <= s3: 
        return s3
    else:
        return 0
         
# # takes in the vertex, that will be removed
# def calculate_potential(r):
#     # first of all let's check what exists and what doesn't exis
#     a = r.parent
#     b = r.left
#     c = r.right
    
#     if a == None:
#         a = 0
#     elif b == None: 
#         b = 0
#     else:
#         c = 0
    
#     if a == 0 and (b == c)!= 0:
#         s1 = r.left.size
#         s2 = r.right.size
#         s3 = 0
#     elif b == 0 and (a == c) != 0:
#         s1 = 0
#         s2 = r.right.size
#         s3 = r.parent.size
#     elif c == 0 and (a == b) != 0:
#         s1 = r.left.size
#         s2 = 0
#         s3 = r.parent.size
#     else:
#         s1 = 0
#         s2 = 0
#         s3 = 0
#     if s1 <= s2 and s3 <= s2: 
#         return s2
#     elif s2 <= s1 and s3 <= s1: 
#         return s1
#     elif s1 <= s3 and s2 <= s3: 
#         return s3
#     else:
#         return 0