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
**foundations → data structures → algorithms → patterns.** The later algorithms notebooks
push into advanced / competitive-programming territory (flows, FFT, suffix automata, tree
decompositions); every nontrivial claim is still proven by a runnable cell.

📋 **[CHEATSHEET.md](CHEATSHEET.md)** — the whole series at a glance: aggregated complexity tables, a
*"which structure / algorithm / pattern do I reach for?"* decision guide, and practice problems by topic.

## Layout

```
0-foundations/      3 notebooks  — Big-O, Python idioms, the CPython cost model
1-data-structures/  14 notebooks — arrays → systems structures (B-tree / LSM)
2-algorithms/       25 notebooks — sorting → randomized (core + an advanced/CP block)
3-patterns/         11 notebooks — reusable problem-solving templates
templates/          notebook-template.ipynb — copy to start a new topic
```

Every notebook is linked with a one-line summary in the tables below.

## Notebooks

### Foundations

| Topic | Status | Covers |
|---|:---:|---|
| [Big-O & complexity](0-foundations/01-big-o.ipynb) | ✅ | growth rates, reading complexity off code, amortized analysis, best/avg/worst & space, **P vs NP / NP-completeness** |
| [Python idioms for DSA](0-foundations/02-python-idioms-for-dsa.ipynb) | ✅ | slicing, comprehensions/generators, the data model (dunders), unpacking, stdlib toolkit, gotchas |
| [The CPython cost model](0-foundations/03-cpython-cost-model.ipynb) | ✅ | why Big-O hides huge constants: bytecode dispatch, call & attribute/global lookup overhead, the GIL, when numpy/builtins win |

### Data structures

| Topic | Status | Covers |
|---|:---:|---|
| [arrays](1-data-structures/01-arrays.ipynb) | ✅ | `list`, `tuple`, `array`, `numpy`, `deque`; growth strategy; the `[[0]*n]*m` aliasing gotcha |
| [strings](1-data-structures/02-strings.ipynb) | ✅ | `str`, PEP 393 char-width, interning, the `+=` trap, `bytes`/`bytearray` |
| [dict & set](1-data-structures/03-dictionaries-and-sets.ipynb) | ✅ | hash tables, open addressing, compact-dict layout, resizing, hashing |
| [heaps](1-data-structures/04-heaps.ipynb) | ✅ | `heapq` binary heap, sift up/down, `heapify` is O(n), **two-heaps running median** |
| [linked lists](1-data-structures/05-linked-lists.ipynb) | ✅ | singly/doubly from scratch; reversal & Floyd's cycle detection; why CPython avoids them; `deque`/`OrderedDict` |
| [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb) | ✅ | LIFO/FIFO; the `list`-as-queue O(n²) trap; `deque(maxlen)`; `queue` module |
| [trees](1-data-structures/07-trees.ipynb) | ✅ | BST from scratch (insert/search/delete), DFS/BFS + **Morris** (O(1) space), **AVL** rotations, the balance problem, `bisect`, `sortedcontainers` |
| [tries](1-data-structures/08-tries.ipynb) | ✅ | prefix tree from scratch, autocomplete, node sharing, **binary/XOR trie** (max-XOR), when a `set` wins |
| [graphs](1-data-structures/09-graphs.ipynb) | ✅ | adjacency list vs matrix, BFS/DFS, topological sort, Dijkstra |
| [Fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) | ✅ | Fenwick (BIT) + segment tree + **lazy propagation** + **sparse table** (static O(1) RMQ) |
| [spatial & persistent structures](1-data-structures/11-spatial-and-persistent-structures.ipynb) | ✅ | interval tree, k-d tree (nearest-neighbour + range), persistent segment tree (path-copying versions) |
| [LRU cache](1-data-structures/12-lru-cache.ipynb) | ✅ | hash map + doubly linked list for O(1) get/put; `OrderedDict` & `functools.lru_cache` |
| [probabilistic structures](1-data-structures/13-probabilistic-structures.ipynb) | ✅ | Bloom filter, skip list, count-min sketch — approximate structures with measured error rates vs theory |
| [systems data structures](1-data-structures/14-systems-data-structures.ipynb) | ✅ | B-tree / B+ tree (high fan-out, on-disk), LSM tree (memtable + sorted runs + compaction); read vs write amplification |

### Algorithms

Core (01–04, 06, 11–12, 14–15, 17–19, 23) plus an **advanced / competitive-programming block** woven in by topic.

| Topic | Status | Covers |
|---|:---:|---|
| [sorting](2-algorithms/01-sorting.ipynb) | ✅ | Timsort internals; `key=`/DSU; bubble→radix implemented & raced; counting sort beats Timsort; **bucket sort** |
| [searching](2-algorithms/02-searching.ipynb) | ✅ | linear vs binary; binary search from scratch; `bisect`; binary search on the answer; **ternary search** (unimodal) |
| [selection](2-algorithms/03-selection.ipynb) | ✅ | k-th element / median: quickselect (avg O(n)), median-of-medians (guaranteed O(n)), `heapq.nlargest`, `statistics.median` |
| [recursion & backtracking](2-algorithms/04-recursion-and-backtracking.ipynb) | ✅ | call stack, no TCO, recursion limit; memoization; permutations/subsets/N-queens, **Sudoku & grid word search** |
| [divide & conquer](2-algorithms/05-divide-and-conquer.ipynb) | ✅ | the Master Theorem, Karatsuba multiplication, counting inversions, max-subarray |
| [dynamic programming](2-algorithms/06-dynamic-programming.ipynb) | ✅ | top-down memo vs bottom-up; coin change, LCS, edit distance, knapsack + 1D rolling; **LIS, subset sum, partition** |
| [advanced dynamic programming](2-algorithms/07-advanced-dynamic-programming.ipynb) | ✅ | interval, bitmask (TSP), tree, digit, state-machine, expected-value DP |
| [DP optimizations](2-algorithms/08-dp-optimizations.ipynb) | ✅ | monotonic-deque DP, convex hull trick, divide-and-conquer DP, Knuth's optimization |
| [tree algorithms](2-algorithms/09-tree-algorithms.ipynb) | ✅ | LCA (binary lifting + Euler/RMQ), tree diameter, rerooting (all-roots DP) |
| [advanced tree decompositions](2-algorithms/10-advanced-tree-decompositions.ipynb) | ✅ | centroid decomposition, heavy-light decomposition (path queries via segment tree) |
| [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) | ✅ | Dijkstra, Bellman-Ford, A\*, Floyd-Warshall (all-pairs), union-find, MST (Kruskal/Prim) |
| [advanced graph algorithms](2-algorithms/12-advanced-graph-algorithms.ipynb) | ✅ | SCC (Tarjan/Kosaraju), bridges & articulation points, max-flow/min-cut (Edmonds-Karp), bipartite matching |
| [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb) | ✅ | Dinic, min-cost max flow, Hopcroft-Karp, Hungarian (assignment), Eulerian (Hierholzer), König |
| [string algorithms](2-algorithms/14-string-algorithms.ipynb) | ✅ | naive/KMP/Rabin-Karp; CPython `fastsearch`; **Manacher's** (longest palindrome in O(n)) |
| [suffix structures](2-algorithms/15-suffix-structures.ipynb) | ✅ | Z-algorithm, suffix array + LCP (Kasai), Aho-Corasick multi-pattern matching |
| [suffix automaton & tree](2-algorithms/16-suffix-automaton-and-tree.ipynb) | ✅ | suffix automaton (online O(n)): distinct substrings, longest common substring; suffix tree |
| [bit manipulation](2-algorithms/17-bit-manipulation.ipynb) | ✅ | arbitrary-precision `int` (`PyLong`, 30-bit digits); bit tricks; masking; bitmask sets |
| [greedy](2-algorithms/18-greedy.ipynb) | ✅ | greedy-choice property; activity selection, fractional knapsack, jump game, **Huffman coding**; when greedy fails (→ DP) |
| [number theory](2-algorithms/19-number-theory.ipynb) | ✅ | GCD/Euclid, sieve, Miller-Rabin, modexp & inverse; **prime factorization, Euler totient, CRT**; combinatorics |
| [combinatorics](2-algorithms/20-combinatorics.ipynb) | ✅ | Pascal's triangle, Catalan, nCr mod p (Lucas), inclusion-exclusion, stars-and-bars |
| [advanced number theory](2-algorithms/21-advanced-number-theory.ipynb) | ✅ | matrix exponentiation (fast Fibonacci), game theory (Nim / Sprague-Grundy), discrete log (BSGS) |
| [FFT & polynomials](2-algorithms/22-fft-and-polynomials.ipynb) | ✅ | FFT (Cooley-Tukey) + inverse, NTT (exact integer convolution), polynomial & big-int multiply |
| [computational geometry](2-algorithms/23-computational-geometry.ipynb) | ✅ | orientation, segment intersection, convex hull (monotone chain + **Graham**), point-in-polygon, **closest pair** (D&C) |
| [sqrt decomposition & offline](2-algorithms/24-sqrt-decomposition-and-offline.ipynb) | ✅ | sqrt decomposition (block ops), Mo's algorithm, offline query processing |
| [randomized algorithms](2-algorithms/25-randomized-algorithms.ipynb) | ✅ | Las Vegas vs Monte Carlo, reservoir sampling, Fisher-Yates, Freivalds' verification |

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

- Every nontrivial claim gets a **runnable demo that proves it** (`sys.getsizeof`, `id`, timing, or an assert vs a brute-force oracle).
- Each notebook ends with a **when-to-use table** and a **Big-O cheat-sheet** (all rolled up in [CHEATSHEET.md](CHEATSHEET.md)).
- Start new topics from `templates/notebook-template.ipynb` to keep the structure consistent.
