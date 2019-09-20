import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack



class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # Insert the given value into the tree
  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  # Return True if the tree contains the value
  # False if it does not
  # Can stop at the first instance of the value
  # If we get to an ending node we know the value is not present
  def contains(self, target):
    if self.value == target:
      return True
    else:
      if target < self.value:
        if not self.left:
          return False
        else:
          return self.left.contains(target)
      else:
        if not self.right:
          return False
        else:
          return self.right.contains(target)

  # Return the maximum value found in the tree
  def get_max(self):
    if not self.right:
      return self.value
    return self.right.get_max()
    

  # Call the function `cb` on the value of each node
  # You may use a recursive or iterative approach

  # Once the binary search tree has been created, 
  # its elements can be retrieved in-order by 
  # recursively traversing the left subtree of the root node, 
  # accessing the node itself, then recursively traversing the 
  # right subtree of the node, continuing this pattern with each 
  # node in the tree as it's recursively accessed
  def r_for_each(self, cb):
    # I am going to use pre-order traversal
    cb(self.value)
    if self.left:
      self.left.r_for_each(cb)
    if self.right:
      self.right.r_for_each(cb)

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print():
    pass

  # Print the value of every node, starting with the given node,
  # in a breadth first traversal
  def bft_print(node):
    pass

  # Print the value of every node, starting with the given node,
  # in a depth first traversal
  def dft_print(node):
    pass


  ########Stretch Goals#########
  # Note: Research may be required

  # Print In-order DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order DFT
  def post_order_dft(self, node):
    pass
  