from __future__ import annotations
from typing import List, Optional, Tuple


GOAL_STATE = (3, 2, 1, 4, 5, 6, 7, 8, 0)


class State:
    """Representa um estado do 8-puzzle como tupla imutável de 9 inteiros (0 = espaço vazio)."""

    def __init__(self, tiles: Tuple[int, ...], parent: Optional["State"] = None, action: Optional[str] = None, cost: int = 0):
        if len(tiles) != 9 or set(tiles) != set(range(9)):
            raise ValueError("Estado inválido: deve conter exatamente os valores 0-8.")
        self.tiles = tiles
        self.parent = parent
        self.action = action
        self.cost = cost

    @property
    def is_goal(self) -> bool:
        return self.tiles == GOAL_STATE

    @property
    def blank_index(self) -> int:
        return self.tiles.index(0)

    def neighbors(self) -> List["State"]:
        """Retorna os estados filhos válidos a partir deste estado."""
        # Representação em matriz 3x3
        r, c = divmod(self.blank_index, 3)

        # Ação descreve o movimento do espaço vazio.
        candidates: list[tuple[str, tuple[int, int]]] = []
        if r > 0:
            candidates.append(("UP", (r - 1, c)))
        if r < 2:
            candidates.append(("DOWN", (r + 1, c)))
        if c > 0:
            candidates.append(("LEFT", (r, c - 1)))
        if c < 2:
            candidates.append(("RIGHT", (r, c + 1)))

        neighbors: list[State] = []
        for action, (nr, nc) in candidates:
            n_blank = nr * 3 + nc
            tiles_list = list(self.tiles)
            tiles_list[self.blank_index], tiles_list[n_blank] = tiles_list[n_blank], tiles_list[self.blank_index]
            new_tiles = tuple(tiles_list)
            neighbors.append(
                State(
                    new_tiles,
                    parent=self,
                    action=action,
                    cost=self.cost + 1,
                )
            )

        return neighbors

    def path(self) -> List["State"]:
        """Retorna a sequência de estados do estado inicial até este."""
        out: list[State] = []
        cur: State | None = self
        while cur is not None:
            out.append(cur)
            cur = cur.parent
        out.reverse()
        return out

    def actions(self) -> List[str]:
        """Retorna a sequência de ações do estado inicial até este."""
        return [st.action for st in self.path()[1:] if st.action is not None]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, State) and self.tiles == other.tiles

    def __hash__(self) -> int:
        return hash(self.tiles)

    def __lt__(self, other: "State") -> bool:
        return self.cost < other.cost

    def __repr__(self) -> str:
        t = self.tiles
        return (
            f"+-------+\n"
            f"| {t[0]} {t[1]} {t[2]} |\n"
            f"| {t[3]} {t[4]} {t[5]} |\n"
            f"| {t[6]} {t[7]} {t[8]} |\n"
            f"+-------+"
        ).replace("0", " ")
