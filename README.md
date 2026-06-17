Sobre os resultados:

Professor, eu fiz o trabalho, porém ao executa-lo, o terminal exibia os resultados, mas todos eles vinham como solução não encontrada, como mostra a imagem que está no projeto, com o nome de "Resultado incorreto". Ao que pude entender, o problema estava com a ordem dos números para a criação do puzzle, ou seja, a ordem: 1, 2, 3, 4, 5, 6, 7, 8, 0 era o problema, pois com esta ordem, todas as vezes que repeti o código, sempre dava "solução não encontrada". Mas ao mudar a ordem para a seguinte: 3, 2, 1, 4, 5, 6, 7, 8, 0, o resultado apareceu e enfim os resultados foram encontrados, como mostra a imagem "Resultado correto". Não sei se tem outros erros, porém este foi o jeito que fiz para poder dar certo.

Atenciosamente,
Arthur Garcia Nonis

8-Puzzle — Busca em Espaço de Estados
O que implementar
puzzle/state.py
neighbors() — gera os estados filhos a partir do espaço vazio
path() — reconstrói a sequência de estados do inicial até este
actions() — retorna a sequência de ações usando path()
algorithms/bfs.py
BFS.search(initial) — Busca em Largura
algorithms/dfs.py
DFS.search(initial) — Busca em Profundidade
algorithms/a_star.py
AStar.heuristic(state) — função heurística admissível
AStar.search(initial) — Busca A*
Estrutura
├── puzzle/
│   ├── state.py        # State — IMPLEMENTAR neighbors, path, actions
│   ├── result.py       # SearchResult — não alterar
│   └── base_search.py  # Interface BaseSearch — não alterar
├── algorithms/
│   ├── bfs.py          ← IMPLEMENTAR
│   ├── dfs.py          ← IMPLEMENTAR
│   └── a_star.py       ← IMPLEMENTAR
└── main.py
