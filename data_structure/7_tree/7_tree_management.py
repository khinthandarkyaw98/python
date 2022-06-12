class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
        spaces = "  " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if show ==  "both":
            print(f"{prefix}{self.name}  ({self.designation})")
        elif show == "name":
            print(f"{prefix}{self.name}")
        elif show == "designation":
            print(f"{prefix}{self.designation}")
        if self.children:  # len(self.children) >0
            for child in self.children:
                child.print_tree(show)


def build_management_tree():
    ceo = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")

    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy

"""
output 
Nilupul
      |__Chinmay
            |__Vishwa
                  |__Dhaval
                  |__Abhijit
            |__Aamir
      |__Gels
            |__Peter
            |__Waqas
CEO
      |__CTO
            |__Infrastructure Head
                  |__Cloud Manager
                  |__App Manager
            |__Application Head
      |__HR Head
            |__Recruitment Manager
            |__Policy Manager
Nilupul  (CEO)
      |__Chinmay  (CTO)
            |__Vishwa  (Infrastructure Head)
                  |__Dhaval  (Cloud Manager)
                  |__Abhijit  (App Manager)
            |__Aamir  (Application Head)
      |__Gels  (HR Head)
            |__Peter  (Recruitment Manager)
            |__Waqas  (Policy Manager)
"""