# implement a function to print a list from tail to head.

# either a stack or recursive.

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next = next_node

def create_linked_list():
  x = Node('x')
  y = Node('y')
  z = Node('z')
  x.next = y
  y.next = z
  return x

def recursive_print_node(node):
  if node is not None:
    if node.next is not None:
      recursive_print_node(node.next)
    print node.value

recursive_print_node(create_linked_list())
