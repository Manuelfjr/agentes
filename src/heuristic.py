import heapq
import copy


class AStarSolver:
    def __init__(self, initial_state, goal_state, moves, heuristic=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.moves = moves
        self.heuristic = heuristic or self.manhattan_distance

    class Node:
        def __init__(self, state, parent=None, move=None, g=0, heuristic_fn=None):
            self.state = state
            self.parent = parent
            self.move = move
            self.g = g
            self.h = heuristic_fn(state) if heuristic_fn else 0
            self.f = self.g + self.h

        def __lt__(self, other):
            return self.f < other.f

    def find_zero(self, state):
        for i, row in enumerate(state):
            if 0 in row:
                return (i, row.index(0))
        return None

    def manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                val = state[i][j]
                if val != 0:
                    goal_i, goal_j = divmod(val - 1, 3)
                    distance += abs(goal_i - i) + abs(goal_j - j)
        return distance

    def is_goal(self, state):
        return state == self.goal_state

    def generate_children(self, state):
        children = []
        x, y = self.find_zero(state)
        for move, (dx, dy) in self.moves.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = copy.deepcopy(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                children.append((move, new_state))
        return children

    def print_state(self, state):
        for row in state:
            print(row)
        print()

    def node_name(self, state):
        flat = [str(num) for row in state for num in row]
        return ''.join(flat)

    def reconstruct_path(self, node):
        path = []
        while node:
            path.append((node.move, node.state))
            node = node.parent
        return list(reversed(path))[1:]

    def solve(self):
        start_node = self.Node(self.initial_state, heuristic_fn=self.heuristic)
        frontier = []
        heapq.heappush(frontier, start_node)
        explored = set()
        step = 0

        while frontier:
            print("-" * 30)
            print(f"F{step} =", end=" {")
            print(', '.join([
                f"{self.node_name(n.state)}_{n.f}" for n in frontier
            ]), end="}\n")

            current = heapq.heappop(frontier)

            print("\nNó selecionado (menor f):")
            self.print_state(current.state)
            print(f"f = {current.f} (g = {current.g}, h = {current.h})")

            if self.is_goal(current.state):
                print("✅ Objetivo alcançado!")
                return self.reconstruct_path(current), current.g

            explored.add(str(current.state))
            children = self.generate_children(current.state)

            print("-" * 30)
            print("\nExpandindo nós:")
            for move, child_state in children:
                if str(child_state) not in explored:
                    child_node = self.Node(child_state, parent=current, move=move, g=current.g + 1, heuristic_fn=self.heuristic)
                    heapq.heappush(frontier, child_node)
                    print(f"Movimento: {move}")
                    self.print_state(child_state)
                    print(f"f = {child_node.f} (g = {child_node.g}, h = {child_node.h})")

            print("-" * 30 + "\n")
            step += 1

        print("❌ Nenhuma solução encontrada.")
        return None, None
