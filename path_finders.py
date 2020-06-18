from tree import Node

# base_node = Node((2, 0))


class KnightPathFinder:
    def __init__(self, root=Node(tuple((2, 0)))):
        self._root = root
        self._considered_positions = set((root.value))

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
        # print(attempted_moves)
        valid_moves = [(x, y) for (x, y) in attempted_moves
                       if x >= 0 and x <= 7 and y >= 0 and y <= 7]
        return valid_moves

    def new_moves_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        new_moves = set(valid_moves) - set(self.considered_positions)
        for move in new_moves:
            self.considered_positions.add(move)
        return new_moves

    def build_move_tree(self):
        moves = self.new_moves_positions(self.root.value)
        base = self.root
        for move in moves:
            child = Node(move)
            self.root.add_child(child)
        queue = self.root.children

        while(queue):
            base = queue.pop(0)
            moves = self.new_moves_positions(base.value)
            for move in moves:
                child = Node(move)
                base.add_child(child)
                queue += base.children

        
knight = KnightPathFinder()

knight.build_move_tree()

print(knight.considered_positions)
