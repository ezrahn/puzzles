# https://www.youtube.com/watch?v=7HgsS8bRvjo&t=313s

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
      
      
def count_unival(subRoot, parent_value = None):
    if subRoot == None:
        return 0, None
    
    # leaf nodes is always a unival.
    if subRoot.left == None and subRoot.right == None:
        return 1, True
        
    isUnival = False    
    left_count, left_unival = count_unival(subRoot.left, subRoot.value)
    right_count, right_unival = count_unival(subRoot.right, subRoot.value)
    subtree_count = left_count + right_count
    if subRoot.left and subRoot.right and subRoot.left.value == subRoot.right.value and subRoot.left.value == subRoot.value:
        subtree_count += 1
        isUnival = True
        
    return subtree_count, isUnival
    
a = Node(1, None, None)
print count_unival(a)

b = Node(1, a, a)
print count_unival(b)

c = Node(0, b, a)
print count_unival(c)

d = Node(1, b, a)
print count_unival(d)

e = Node(1, a, None)
print count_unival(e)

f = Node(1, None, a)
print count_unival(f)
assert count_unival(f) == (1, False)

right_sample = Node(3, None, b)
sample = Node(3, a, right_sample)
print count_unival(sample)

line = Node(1, None, a)
line2 = Node(1, None, line)
line3 = Node(1, None, line2)
print count_unival(line3)