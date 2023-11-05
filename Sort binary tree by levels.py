class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

r=[]

def tree_by_levels(node):
    if node:
        if node.value == None:
            return []
    
    levels = []
    queue = [node]  # Initialize the queue with the root node
    
    while queue:  # While there are nodes to process
        current_node = queue.pop(0)  # Pop the first node in the queue
        if node:
            levels.append(current_node.value)
        
        if current_node.left:  # If the left child exists, add it to the queue
            queue.append(current_node.left)
        if current_node.right:  # If the right child exists, add it to the queue
            queue.append(current_node.right)
    
    return levels


sample = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
print(tree_by_levels(sample))