


class Node:
    def __init__(self, data):
        self.data = data  
        self.left = None 
        self.right = None 


def order_traversal(root):
    if root:  
        order_traversal(root.left)  
        print(root.data, end=' ') 
        order_traversal(root.right)  


def preorder_traversal(root):
    if root:  
        print(root.data, end=' ') 
        preorder_traversal(root.left)  
        preorder_traversal(root.right)  

def postorder_traversal(root):
    if root:  
        postorder_traversal(root.left)  
        postorder_traversal(root.right)  
        print(root.data, end=' ') 


root = Node(50)


root.left = Node(30)
root.left.left = Node(40)
root.left.right = Node(20)


root.right = Node(70)
root.right.left = Node(60)
root.right.right = Node(80)


#Task 1 
print("In-order:")
order_traversal(root)  
print()  

#Task 2 
print("Pre-order:")
preorder_traversal(root) 
print()  

#Task 3 
print("Post-order:")
postorder_traversal(root) 
print() 
