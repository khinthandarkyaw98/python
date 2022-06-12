class TreeNode:
    def __init__(self, location):
        self.location = location
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, show):
        spaces = "  " * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        if show == self.get_level() or show > self.get_level()-1:
            print(prefix + self.location)
        if self.children:
            for child in self.children:
                child.print_tree(show)

def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francsico"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == "__main__":
    root_node = build_location_tree()
    print("root_node.print_tree(1)")
    root_node.print_tree(1)
    print("\nroot_node.print_tree(2)")
    root_node.print_tree(2)
    print("\nroot_node.print_tree(3)")
    root_node.print_tree(3)

"""
output 
root_node.print_tree(1)
Global
    |__India
    |__USA

root_node.print_tree(2)
Global
    |__India
        |__Gujarat
        |__Karnataka
    |__USA
        |__New Jersey
        |__California

root_node.print_tree(3)
Global
    |__India
        |__Gujarat
            |__Ahmedabad
            |__Baroda
        |__Karnataka
            |__Bangluru
            |__Mysore
    |__USA
        |__New Jersey
            |__Princeton
            |__Trenton
        |__California
            |__San Francsico
            |__Mountain View
            |__Palo Alto
"""