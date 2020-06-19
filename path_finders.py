from tree import Node


class KnightPathFinder:
    def __init__(self, root=(2, 0)):
        self._root = Node(root)
        self._considered_positions = {root}

    @property
    def root(self):
        return self._root

    @property
    def considered_positions(self):
        return self._considered_positions

    def get_valid_moves(self, pos):
        potential_moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2),
                           (2, 1), (2, -1), (-1, -2), (1, -2)]
        attempted_moves = [(pos[0]+x, pos[1]+y) for (x, y) in potential_moves]
        valid_moves = [(x, y) for (x, y) in attempted_moves
                       if x >= 0 and x <= 7 and y >= 0 and y <= 7]
        return valid_moves

    def new_moves_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        new_moves = set(valid_moves) - self.considered_positions
        for move in new_moves:
            self.considered_positions.add(move)
        return new_moves

    def build_move_tree(self):
        base = self.root
        queue = [self.root]
        while(queue):
            base = queue.pop(0)
            moves = self.new_moves_positions(base.value)
            for move in moves:
                child = Node(move)
                base.add_child(child)
                queue.append(child)

    def find_path(self, end_pos):
        end_node = self.root.breadth_first(end_pos)
        path = self.trace_path_to_root(end_node)
        return path

    def trace_path_to_root(self, end_node):
        current_node = end_node
        node_path = []
        while(current_node):
            node_path.insert(0, current_node)
            current_node = current_node.parent

        coord_path = [node.value for node in node_path]
        return coord_path


# knight = KnightPathFinder()
# # knight.build_move_tree()
# # print(knight.considered_positions)
# finder = KnightPathFinder((0, 0))
# # print(finder.new_moves_positions((0, 0)))
# finder.build_move_tree()

# end = finder.find_path((7, 5))
# end_parent = end.parent
# end_grandparent = end_parent.parent
# end_great_grandparent = end_grandparent.parent
# end_great_great_grandparent = end_great_grandparent.parent
# print(f'{end}\'s parent is {end_parent} and its grandparent is {end_grandparent}. Its great grandparent is {end_great_grandparent}. Finally its greatest grandparent is {end_great_great_grandparent}')

# print(finder._root.value)

# print(finder._root.children[0].children[2].children)

finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1)))  # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
# => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
print(finder.find_path((7, 6)))
