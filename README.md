# python-dsa

Personal notes + runnable examples on data structures and algorithms, with a focus on
**how each one is actually implemented in CPython under the hood**.

Each topic is a self-contained Jupyter notebook following the same shape:
**concept → CPython internals → demos that *prove* the claims → when-to-use → complexity cheat-sheet.**

## Layout

```
data-structures/
  _template.ipynb   ← copy this to start a new topic
  arrays.ipynb
  strings.ipynb
  dictionaries-and-sets.ipynb
  heaps.ipynb
  linked-lists.ipynb
  stacks-and-queues.ipynb
  trees.ipynb
  tries.ipynb
  graphs.ipynb

algorithms/
  sorting.ipynb
  searching.ipynb
  recursion-and-backtracking.ipynb
  dynamic-programming.ipynb
  graph-algorithms.ipynb
```

> The `algorithms/` track has begun; more topics (searching, recursion/DP, graph algorithms) to follow.

## Notebooks

### Data structures

| Topic | Status | Covers |
|---|:---:|---|
| [arrays](data-structures/arrays.ipynb) | ✅ | `list`, `tuple`, `array`, `numpy`, `deque`; growth strategy; the `[[0]*n]*m` aliasing gotcha |
| [strings](data-structures/strings.ipynb) | ✅ | `str`, PEP 393 char-width, interning, the `+=` trap, `bytes`/`bytearray` |
| [dict & set](data-structures/dictionaries-and-sets.ipynb) | ✅ | hash tables, open addressing, compact-dict layout, resizing, hashing |
| [heaps](data-structures/heaps.ipynb) | ✅ | `heapq` binary heap, sift up/down, `heapify` is O(n) |
| [linked lists](data-structures/linked-lists.ipynb) | ✅ | singly/doubly from scratch; reversal & Floyd's cycle detection; why CPython avoids them; `deque`/`OrderedDict` |
| [stacks & queues](data-structures/stacks-and-queues.ipynb) | ✅ | LIFO/FIFO; the `list`-as-queue O(n²) trap; `deque(maxlen)`; `queue` module |
| [trees](data-structures/trees.ipynb) | ✅ | BST from scratch (insert/search/**delete**), DFS/BFS traversals, the balance problem, `bisect` |
| [tries](data-structures/tries.ipynb) | ✅ | prefix tree from scratch, autocomplete, node sharing, when a `set` wins |
| [graphs](data-structures/graphs.ipynb) | ✅ | adjacency list vs matrix, BFS/DFS, topological sort, Dijkstra |

### Algorithms

| Topic | Status | Covers |
|---|:---:|---|
| [sorting](algorithms/sorting.ipynb) | ✅ | Timsort internals (runs, galloping, adaptive, stable); `key=`/DSU; bubble→radix implemented & raced; counting sort beats Timsort |
| [searching](algorithms/searching.ipynb) | ✅ | linear vs binary; binary search from scratch; `bisect` (left/right, `key=`, pred/succ); binary search on the answer |
| [recursion & backtracking](algorithms/recursion-and-backtracking.ipynb) | ✅ | call stack, no tail-call optimization, recursion limit; memoization (`functools.cache`); permutations/subsets/N-queens |
| [dynamic programming](algorithms/dynamic-programming.ipynb) | ✅ | top-down memo vs bottom-up table; coin change, LCS, edit distance, knapsack + 1D rolling |
| [graph algorithms](algorithms/graph-algorithms.ipynb) | ✅ | Dijkstra, Bellman-Ford, A\*, union-find, MST (Kruskal/Prim) |
| string algorithms | 📋 | the two-way algorithm `str.find` uses, KMP, Rabin-Karp |
| bit manipulation | 📋 | arbitrary-precision `int` (`PyLong`, 30-bit digits); bitwise tricks |

## Running

Uses [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run jupyter lab                     # interactive editing

# execute a notebook in place (refresh its saved outputs):
uv run jupyter nbconvert --to notebook --execute --inplace data-structures/<name>.ipynb
```

## Testing

Every notebook is executed end-to-end on each push via [`nbmake`](https://github.com/treebeardtech/nbmake), so committed notebooks never go stale or broken. Run the same check locally:

```bash
uv run pytest                 # runs nbmake over data-structures/ and algorithms/
```

This executes notebooks in memory (it does **not** overwrite their saved outputs) and fails on any cell error. CI runs it via `.github/workflows/notebooks.yml`.

## House style

- Every nontrivial claim gets a **runnable demo that proves it** (`sys.getsizeof`, `id`, timing).
- Each notebook ends with a **when-to-use table** and a **Big-O cheat-sheet**.
- Start new topics from `_template.ipynb` to keep the structure consistent.
