# python-dsa

[![notebooks](https://github.com/jakeryderv/python-dsa/actions/workflows/notebooks.yml/badge.svg)](https://github.com/jakeryderv/python-dsa/actions/workflows/notebooks.yml)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jakeryderv/python-dsa)
[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jakeryderv/python-dsa/main?urlpath=lab)
[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)

Personal notes + runnable examples on data structures and algorithms, with a focus on
**how each one is actually implemented in CPython under the hood**.

Each topic is a self-contained Jupyter notebook following the same shape:
**concept → CPython internals → demos that *prove* the claims → when-to-use → complexity cheat-sheet.**

The directories and files are numbered as a learning path — read them in order:
**foundations → data structures → algorithms → patterns.**

📋 **[CHEATSHEET.md](CHEATSHEET.md)** — the whole series at a glance: aggregated complexity tables, a
*"which structure / algorithm / pattern do I reach for?"* decision guide, and practice problems by topic.

## Layout

```
0-foundations/
  01-big-o.ipynb
  02-python-idioms-for-dsa.ipynb
  03-cpython-cost-model.ipynb

1-data-structures/
  01-arrays.ipynb
  02-strings.ipynb
  03-dictionaries-and-sets.ipynb
  04-heaps.ipynb
  05-linked-lists.ipynb
  06-stacks-and-queues.ipynb
  07-trees.ipynb
  08-tries.ipynb
  09-graphs.ipynb
  10-fenwick-and-segment-trees.ipynb
  11-lru-cache.ipynb
  12-probabilistic-structures.ipynb

2-algorithms/
  01-sorting.ipynb
  02-searching.ipynb
  03-selection.ipynb
  04-recursion-and-backtracking.ipynb
  05-dynamic-programming.ipynb
  06-graph-algorithms.ipynb
  07-advanced-graph-algorithms.ipynb
  08-string-algorithms.ipynb
  09-suffix-structures.ipynb
  10-bit-manipulation.ipynb
  11-greedy.ipynb
  12-number-theory.ipynb
  13-computational-geometry.ipynb

3-patterns/
  01-two-pointers.ipynb
  02-sliding-window.ipynb
  03-prefix-sums-and-difference-arrays.ipynb
  04-monotonic-stack-and-queue.ipynb
  05-top-k-and-k-way-merge.ipynb
  06-cyclic-sort.ipynb
  07-combinatorial-generation.ipynb
  08-coordinate-compression.ipynb
  09-meet-in-the-middle.ipynb
  10-sweep-line.ipynb
  11-grid-and-matrix-traversal.ipynb

templates/
  notebook-template.ipynb   ← copy this to start a new topic
```

## Notebooks

### Foundations

| Topic | Status | Covers |
|---|:---:|---|
| [Big-O & complexity](0-foundations/01-big-o.ipynb) | ✅ | growth rates, reading complexity off code, amortized analysis, best/avg/worst & space |
| [Python idioms for DSA](0-foundations/02-python-idioms-for-dsa.ipynb) | ✅ | slicing, comprehensions/generators, the data model (dunders), unpacking, stdlib toolkit, gotchas |
| [The CPython cost model](0-foundations/03-cpython-cost-model.ipynb) | ✅ | why Big-O hides huge constants: bytecode dispatch, call & attribute/global lookup overhead, the GIL, when numpy/builtins win |

### Data structures

| Topic | Status | Covers |
|---|:---:|---|
| [arrays](1-data-structures/01-arrays.ipynb) | ✅ | `list`, `tuple`, `array`, `numpy`, `deque`; growth strategy; the `[[0]*n]*m` aliasing gotcha |
| [strings](1-data-structures/02-strings.ipynb) | ✅ | `str`, PEP 393 char-width, interning, the `+=` trap, `bytes`/`bytearray` |
| [dict & set](1-data-structures/03-dictionaries-and-sets.ipynb) | ✅ | hash tables, open addressing, compact-dict layout, resizing, hashing |
| [heaps](1-data-structures/04-heaps.ipynb) | ✅ | `heapq` binary heap, sift up/down, `heapify` is O(n) |
| [linked lists](1-data-structures/05-linked-lists.ipynb) | ✅ | singly/doubly from scratch; reversal & Floyd's cycle detection; why CPython avoids them; `deque`/`OrderedDict` |
| [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb) | ✅ | LIFO/FIFO; the `list`-as-queue O(n²) trap; `deque(maxlen)`; `queue` module |
| [trees](1-data-structures/07-trees.ipynb) | ✅ | BST from scratch (insert/search/**delete**), DFS/BFS, **AVL self-balancing with rotations**, the balance problem, `bisect`, `sortedcontainers` |
| [tries](1-data-structures/08-tries.ipynb) | ✅ | prefix tree from scratch, autocomplete, node sharing, when a `set` wins |
| [graphs](1-data-structures/09-graphs.ipynb) | ✅ | adjacency list vs matrix, BFS/DFS, topological sort, Dijkstra |
| [Fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) | ✅ | dynamic range queries: Fenwick (BIT) + segment tree + **lazy propagation** for range updates, O(log n) |
| [LRU cache](1-data-structures/11-lru-cache.ipynb) | ✅ | hash map + doubly linked list for O(1) get/put; `OrderedDict` & `functools.lru_cache` |
| [probabilistic structures](1-data-structures/12-probabilistic-structures.ipynb) | ✅ | Bloom filter, skip list, count-min sketch — approximate structures with measured error rates vs theory |

### Algorithms

| Topic | Status | Covers |
|---|:---:|---|
| [sorting](2-algorithms/01-sorting.ipynb) | ✅ | Timsort internals (runs, galloping, adaptive, stable); `key=`/DSU; bubble→radix implemented & raced; counting sort beats Timsort |
| [searching](2-algorithms/02-searching.ipynb) | ✅ | linear vs binary; binary search from scratch; `bisect` (left/right, `key=`, pred/succ); binary search on the answer |
| [selection](2-algorithms/03-selection.ipynb) | ✅ | k-th element / median: quickselect (avg O(n)), median-of-medians (guaranteed O(n)), `heapq.nlargest`, `statistics.median` |
| [recursion & backtracking](2-algorithms/04-recursion-and-backtracking.ipynb) | ✅ | call stack, no tail-call optimization, recursion limit; memoization (`functools.cache`); permutations/subsets/N-queens |
| [dynamic programming](2-algorithms/05-dynamic-programming.ipynb) | ✅ | top-down memo vs bottom-up table; coin change, LCS, edit distance, knapsack + 1D rolling |
| [graph algorithms](2-algorithms/06-graph-algorithms.ipynb) | ✅ | Dijkstra, Bellman-Ford, A\*, **Floyd-Warshall (all-pairs)**, union-find, MST (Kruskal/Prim) |
| [advanced graph algorithms](2-algorithms/07-advanced-graph-algorithms.ipynb) | ✅ | SCC (Tarjan/Kosaraju), bridges & articulation points, max-flow/min-cut (Edmonds-Karp), bipartite matching |
| [string algorithms](2-algorithms/08-string-algorithms.ipynb) | ✅ | naive/KMP/Rabin-Karp; CPython `fastsearch` (BMH + two-way); built-in vs pure-Python |
| [suffix structures](2-algorithms/09-suffix-structures.ipynb) | ✅ | Z-algorithm, suffix array + LCP (Kasai), Aho-Corasick multi-pattern matching |
| [bit manipulation](2-algorithms/10-bit-manipulation.ipynb) | ✅ | arbitrary-precision `int` (`PyLong`, 30-bit digits); bit tricks; masking; bitmask sets |
| [greedy](2-algorithms/11-greedy.ipynb) | ✅ | greedy-choice property; activity selection, fractional knapsack, jump game; when greedy fails (→ DP) |
| [number theory](2-algorithms/12-number-theory.ipynb) | ✅ | GCD/Euclid, sieve of Eratosthenes, **Miller-Rabin primality**, modular exponentiation & inverse, combinatorics |
| [computational geometry](2-algorithms/13-computational-geometry.ipynb) | ✅ | cross-product orientation, segment intersection, convex hull (monotone chain), point-in-polygon; integer-exact arithmetic |

### Patterns

Problem-solving templates that combine the structures & algorithms above. These read as **signal → template → worked examples → toolkit** (the internals slot doesn't apply).

| Topic | Status | Covers |
|---|:---:|---|
| [two pointers](3-patterns/01-two-pointers.ipynb) | ✅ | converging, read/write, fast & slow (Floyd's); two-sum, dedupe, happy number |
| [sliding window](3-patterns/02-sliding-window.ipynb) | ✅ | fixed & variable windows; max-sum-k, longest-unique-substring, min-subarray |
| [prefix sums & difference arrays](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) | ✅ | O(1) range-sum/update; subarray-sum-k with negatives; 2D prefix sums |
| [monotonic stack & queue](3-patterns/04-monotonic-stack-and-queue.ipynb) | ✅ | next-greater-element, daily temperatures, largest rectangle, sliding-window-max |
| [top-K & K-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb) | ✅ | size-k heap (O(n log k)), top-k-frequent, frontier-heap merge, `heapq.merge` |
| [cyclic sort](3-patterns/06-cyclic-sort.ipynb) | ✅ | in-place sort for `1..n` ranges; find missing/duplicate numbers in O(n)/O(1) |
| [combinatorial generation](3-patterns/07-combinatorial-generation.ipynb) | ✅ | subsets/permutations/combinations (backtracking + bitmask); `itertools` |
| [coordinate compression](3-patterns/08-coordinate-compression.ipynb) | ✅ | map sparse/huge values to dense `0..k-1` ranks; index a size-k array by value |
| [meet in the middle](3-patterns/09-meet-in-the-middle.ipynb) | ✅ | split 2ⁿ → 2·2^(n/2); subset-sum/closest-sum for n≈40, combine with set or `bisect` |
| [sweep line](3-patterns/10-sweep-line.ipynb) | ✅ | events sorted along an axis; merge intervals, min-meeting-rooms (events + heap) |
| [grid & matrix traversal](3-patterns/11-grid-and-matrix-traversal.ipynb) | ✅ | flood fill (DFS/BFS), multi-source BFS, in-place rotate/transpose/spiral; the grid-as-graph view |

## Running

Uses [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run jupyter lab                     # interactive editing

# execute a notebook in place (refresh its saved outputs):
uv run jupyter nbconvert --to notebook --execute --inplace 1-data-structures/01-arrays.ipynb
```

Or open any notebook in the browser with the **Colab** / **Binder** badges above — no local setup.

## Testing & quality gates

CI runs three checks on every push (`.github/workflows/notebooks.yml`):

```bash
uv run pytest                              # nbmake: execute every notebook, fail on any cell error
uv run ruff check .                        # lint (notebook-aware; config in pyproject.toml)
uv run python scripts/check_outputs_fresh.py   # re-execute & confirm saved outputs aren't stale
```

`pytest` (nbmake) executes notebooks **in memory** and does **not** overwrite saved outputs, so it can't
tell whether the committed outputs match the current code — that's what the freshness check adds, diffing a
fresh run against the saved outputs with numbers/addresses normalised (so `timeit` jitter isn't a false alarm).

Optional local hook (`.pre-commit-config.yaml`): `uv run pre-commit install` runs ruff + nbmake on staged notebooks before each commit.

## House style

- Every nontrivial claim gets a **runnable demo that proves it** (`sys.getsizeof`, `id`, timing).
- Each notebook ends with a **when-to-use table** and a **Big-O cheat-sheet** (all rolled up in [CHEATSHEET.md](CHEATSHEET.md)).
- Start new topics from `templates/notebook-template.ipynb` to keep the structure consistent.
