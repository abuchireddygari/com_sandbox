from logging.config import valid_ident


class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.left_child=None
        self.right_child=None

    def insert_left(self,val):
        if self.left_child==None:
            self.left_child=BinaryTree(val)
        else:
            temp=BinaryTree(val)
            temp.left_child=self.left_child
            self.left_child=temp

    def insert_right(self,val):
        if self.right_child==None:
            self.right_child=BinaryTree(val)
        else:
            temp=BinaryTree(val)
            temp.right_child=self.right_child
            self.right_child=temp
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child

    def set_root_val(self,val):
        self.val=val

    def get_root_val(self):
        return self.val


tree=BinaryTree("a")
print(tree.get_root_val())
print(tree.get_left_child())
print(tree.get_right_child())
tree.insert_left("b")
tree.insert_left("c")
print(tree.get_left_child().get_root_val())
print(tree.get_left_child().get_left_child().get_root_val())
tree.insert_right("d")
tree.insert_right("e")
print(tree.get_right_child().get_root_val())
print(tree.get_right_child().get_right_child().get_root_val())
