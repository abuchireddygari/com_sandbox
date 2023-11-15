class TreeNode:
    
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level=0
        while self.parent:
            level += 1
            self = self.parent
        return level

    def print_tree(self):
        spaces = 2 * ' ' * self.get_level()
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_prod_tree():
    root = TreeNode("electronics")

    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("lenovo"))
    laptop.add_child(TreeNode("apple"))
    laptop.add_child(TreeNode("hp"))
    
    mobile = TreeNode("mobile")
    mobile.add_child(TreeNode("apple"))
    mobile.add_child(TreeNode("samsung"))
    mobile.add_child(TreeNode("nokia"))
    mobile.add_child(TreeNode("blackberry"))

    tv = TreeNode("tv")
    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("sony"))
    tv.add_child(TreeNode("lg"))
    tv.add_child(TreeNode("visio"))
    tv.add_child(TreeNode("sharp"))
    
    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)


    return root


if __name__=="__main__":
    root = build_prod_tree()
    root.print_tree()
