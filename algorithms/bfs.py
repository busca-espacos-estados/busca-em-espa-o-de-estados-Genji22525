from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        if initial.is_goal:
            return SearchResult(solution=initial, depth=0, nodes_expanded=0, nodes_generated=1, max_frontier_size=1)

        frontier: deque[State] = deque([initial])
        visited: set[State] = {initial}

        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while frontier:
            max_frontier_size = max(max_frontier_size, len(frontier))
            node = frontier.popleft()
            nodes_expanded += 1

            for child in node.neighbors():
                nodes_generated += 1
                if child in visited:
                    continue

                if child.is_goal:
                    depth = child.cost  
                    return SearchResult(
                        solution=child,
                        nodes_expanded=nodes_expanded,
                        nodes_generated=nodes_generated,
                        max_frontier_size=max_frontier_size,
                        depth=depth,
                    )

                visited.add(child)
                frontier.append(child)

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
            depth=0,
        )

