class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self.children:
            self._children.append(node)
            if node.parent != self:
                node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None

    @parent.setter
    def parent(self, parent):

        if parent:
            if self._parent != None:
                self._parent.remove_child(self)
                self._parent = None
            self._parent = parent
            parent.add_child(self)

        else:
            self._parent.remove_child(self)
            self._parent = None

    def depth_search(self, target):

        if self.value == target:
            return self

        for child in self.children:
            node = child.depth_search(target)
            if node:
                return node

    def breadth_first(self, target):
        queue = [self]

        while(queue):
            top = queue.pop(0)
            if top.value == target:
                return top
            for child in top.children:
                queue.append(child)


# node1 = Node("root")
# node2 = Node("child")
# node3 = Node("child2")
# node4 = Node('child3')

# node1.add_child(node2)
# node2.add_child(node3)
# node2.add_child(node4)

# print(node1.breadth_first('root'))
