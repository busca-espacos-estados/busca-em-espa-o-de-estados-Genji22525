import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        goal_pos = {v: i for i, v in enumerate((1, 2, 3, 4, 5, 6, 7, 8, 0))}
        h = 0
        for i, v in enumerate(state.tiles):
            if v == 0:
                continue
            gi = goal_pos[v]
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(gi, 3)
            h += abs(r1 - r2) + abs(c1 - c2)
        return h

    def search(self, initial: State) -> SearchResult:
        if initial.is_goal:
            return SearchResult(solution=initial, depth=0, nodes_expanded=0, nodes_generated=1, max_frontier_size=1)

        
        counter = 0
        frontier: list[tuple[int, int, int, State]] = []
        g0 = initial.cost
        counter += 1
        heapq.heappush(frontier, (g0 + self.heuristic(initial), g0, counter, initial))

        best_g: dict[tuple[int, ...], int] = {initial.tiles: g0}

        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while frontier:
            max_frontier_size = max(max_frontier_size, len(frontier))
            _, g, _, node = heapq.heappop(frontier)

            # Se este nó não corresponde ao melhor g conhecido, ignore.
            if g != best_g.get(node.tiles, g):
                continue

            nodes_expanded += 1

            if node.is_goal:
                return SearchResult(
                    solution=node,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=node.cost,
                )

            for child in node.neighbors():
                nodes_generated += 1
                tentative_g = child.cost
                prev_g = best_g.get(child.tiles)
                if prev_g is None or tentative_g < prev_g:
                    best_g[child.tiles] = tentative_g
                    counter += 1
                    f = tentative_g + self.heuristic(child)
                    heapq.heappush(frontier, (f, tentative_g, counter, child))

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
            depth=0,
        )

