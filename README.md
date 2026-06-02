# python-dsa

Personal notes + runnable examples on data structures and algorithms, with a focus on
**how each one is actually implemented in CPython under the hood**.

Each topic is a self-contained Jupyter notebook following the same shape:
**concept → CPython internals → demos that *prove* the claims → when-to-use → complexity cheat-sheet.**

The directories and files are numbered as a learning path — read them in order:
**foundations → data structures → algorithms → patterns.**

## Layout

```
0-foundations/
  01-big-o.ipynb
  02-python-idioms-for-dsa.ipynb

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

2-algorithms/
  01-sorting.ipynb
  02-searching.ipynb
  03-recursion-and-backtracking.ipynb
  04-dynamic-programming.ipynb
  05-graph-algorithms.ipynb
  06-string-algorithms.ipynb
  07-bit-manipulation.ipynb

3-patterns/
  01-two-pointers.ipynb
  02-sliding-window.ipynb
  03-prefix-sums-and-difference-arrays.ipynb
  04-monotonic-stack-and-queue.ipynb
  05-top-k-and-k-way-merge.ipynb
  06-cyclic-sort.ipynb
  07-combinatorial-generation.ipynb
  08-coordinate-compression.ipynb
  …                         (more patterns planned — see the table below)

templates/
  notebook-template.ipynb   ← copy this to start a new topic
```

## Notebooks

### Foundations

| Topic | Status | Covers |
|---|:---:|---|
| [Big-O & complexity](0-foundations/01-big-o.ipynb) | ✅ | growth rates, reading complexity off code, amortized analysis, best/avg/worst & space |
| [Python idioms for DSA](0-foundations/02-python-idioms-for-dsa.ipynb) | ✅ | slicing, comprehensions/generators, the data model (dunders), unpacking, stdlib toolkit, gotchas |

### Data structures

| Topic | Status | Covers |
|---|:---:|---|
| [arrays](1-data-structures/01-arrays.ipynb) | ✅ | `list`, `tuple`, `array`, `numpy`, `deque`; growth strategy; the `[[0]*n]*m` aliasing gotcha |
| [strings](1-data-structures/02-strings.ipynb) | ✅ | `str`, PEP 393 char-width, interning, the `+=` trap, `bytes`/`bytearray` |
| [dict & set](1-data-structures/03-dictionaries-and-sets.ipynb) | ✅ | hash tables, open addressing, compact-dict layout, resizing, hashing |
| [heaps](1-data-structures/04-heaps.ipynb) | ✅ | `heapq` binary heap, sift up/down, `heapify` is O(n) |
| [linked lists](1-data-structures/05-linked-lists.ipynb) | ✅ | singly/doubly from scratch; reversal & Floyd's cycle detection; why CPython avoids them; `deque`/`OrderedDict` |
| [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb) | ✅ | LIFO/FIFO; the `list`-as-queue O(n²) trap; `deque(maxlen)`; `queue` module |
| [trees](1-data-structures/07-trees.ipynb) | ✅ | BST from scratch (insert/search/**delete**), DFS/BFS traversals, the balance problem, `bisect` |
| [tries](1-data-structures/08-tries.ipynb) | ✅ | prefix tree from scratch, autocomplete, node sharing, when a `set` wins |
| [graphs](1-data-structures/09-graphs.ipynb) | ✅ | adjacency list vs matrix, BFS/DFS, topological sort, Dijkstra |

### Algorithms

| Topic | Status | Covers |
|---|:---:|---|
| [sorting](2-algorithms/01-sorting.ipynb) | ✅ | Timsort internals (runs, galloping, adaptive, stable); `key=`/DSU; bubble→radix implemented & raced; counting sort beats Timsort |
| [searching](2-algorithms/02-searching.ipynb) | ✅ | linear vs binary; binary search from scratch; `bisect` (left/right, `key=`, pred/succ); binary search on the answer |
| [recursion & backtracking](2-algorithms/03-recursion-and-backtracking.ipynb) | ✅ | call stack, no tail-call optimization, recursion limit; memoization (`functools.cache`); permutations/subsets/N-queens |
| [dynamic programming](2-algorithms/04-dynamic-programming.ipynb) | ✅ | top-down memo vs bottom-up table; coin change, LCS, edit distance, knapsack + 1D rolling |
| [graph algorithms](2-algorithms/05-graph-algorithms.ipynb) | ✅ | Dijkstra, Bellman-Ford, A\*, union-find, MST (Kruskal/Prim) |
| [string algorithms](2-algorithms/06-string-algorithms.ipynb) | ✅ | naive/KMP/Rabin-Karp; CPython `fastsearch` (BMH + two-way); built-in vs pure-Python |
| [bit manipulation](2-algorithms/07-bit-manipulation.ipynb) | ✅ | arbitrary-precision `int` (`PyLong`, 30-bit digits); bit tricks; masking; bitmask sets |

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
| meet in the middle | 📋 | split the search space, combine halves |
| sweep line | 📋 | events sorted along an axis |

## Running

Uses [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run jupyter lab                     # interactive editing

# execute a notebook in place (refresh its saved outputs):
uv run jupyter nbconvert --to notebook --execute --inplace 1-data-structures/01-arrays.ipynb
```

## Testing

Every notebook is executed end-to-end on each push via [`nbmake`](https://github.com/treebeardtech/nbmake), so committed notebooks never go stale or broken. Run the same check locally:

```bash
uv run pytest                 # runs nbmake over the foundations / data-structures / algorithms notebooks
```

This executes notebooks in memory (it does **not** overwrite their saved outputs) and fails on any cell error. CI runs it via `.github/workflows/notebooks.yml`.

## House style

- Every nontrivial claim gets a **runnable demo that proves it** (`sys.getsizeof`, `id`, timing).
- Each notebook ends with a **when-to-use table** and a **Big-O cheat-sheet**.
- Start new topics from `templates/notebook-template.ipynb` to keep the structure consistent.
