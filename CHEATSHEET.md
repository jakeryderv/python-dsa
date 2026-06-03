# DSA Cheat-Sheet — The Whole Series at a Glance

A single navigable reference and study plan for the **53-notebook** Python DSA series (with a CPython-internals angle). It rolls up the per-notebook *"When to use what"* and *"Complexity cheat-sheet"* cells into one place: a decision guide for *"I have problem X, what do I reach for?"*, master complexity tables, a pattern quick-reference, a study plan of canonical practice problems, and a Python stdlib toolkit.

Every complexity below is taken straight from the per-notebook tables — each row links back to its source notebook, so use this to skim and jump in. Notation throughout: `n` = element count, `V`/`E` = vertices/edges, `m` = pattern/query length, `L` = key length, `k` = a small bound (top-k, prefix matches, piles), `W` = numeric capacity, `q` = number of queries, `Σ` = alphabet size. Entries are **worst case** unless marked *avg* / *amortized* / *expected*.

**The meta-rule (from [cpython-cost-model](0-foundations/03-cpython-cost-model.ipynb)):** pick the algorithm *class* with [big-o](0-foundations/01-big-o.ipynb) first, then shrink the constant with the cost model. The less time your data spends as per-element Python objects in an interpreted loop, the faster you go.

---

## Series map

| Tier | Notebooks |
|---|---|
| **0 — Foundations** (3) | [big-o](0-foundations/01-big-o.ipynb) · [python-idioms](0-foundations/02-python-idioms-for-dsa.ipynb) · [cpython-cost-model](0-foundations/03-cpython-cost-model.ipynb) |
| **1 — Data structures** (14) | [arrays](1-data-structures/01-arrays.ipynb) · [strings](1-data-structures/02-strings.ipynb) · [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) · [heaps](1-data-structures/04-heaps.ipynb) · [linked lists](1-data-structures/05-linked-lists.ipynb) · [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb) · [trees](1-data-structures/07-trees.ipynb) · [tries](1-data-structures/08-tries.ipynb) · [graphs](1-data-structures/09-graphs.ipynb) · [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) · [spatial & persistent](1-data-structures/11-spatial-and-persistent-structures.ipynb) · [lru cache](1-data-structures/12-lru-cache.ipynb) · [probabilistic structures](1-data-structures/13-probabilistic-structures.ipynb) · [systems structures](1-data-structures/14-systems-data-structures.ipynb) |
| **2 — Algorithms** (25) | [sorting](2-algorithms/01-sorting.ipynb) · [searching](2-algorithms/02-searching.ipynb) · [selection](2-algorithms/03-selection.ipynb) · [recursion & backtracking](2-algorithms/04-recursion-and-backtracking.ipynb) · [divide & conquer](2-algorithms/05-divide-and-conquer.ipynb) · [dynamic programming](2-algorithms/06-dynamic-programming.ipynb) · [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb) · [DP optimizations](2-algorithms/08-dp-optimizations.ipynb) · [tree algorithms](2-algorithms/09-tree-algorithms.ipynb) · [advanced tree decompositions](2-algorithms/10-advanced-tree-decompositions.ipynb) · [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) · [advanced graph algorithms](2-algorithms/12-advanced-graph-algorithms.ipynb) · [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb) · [string algorithms](2-algorithms/14-string-algorithms.ipynb) · [suffix structures](2-algorithms/15-suffix-structures.ipynb) · [suffix automaton & tree](2-algorithms/16-suffix-automaton-and-tree.ipynb) · [bit manipulation](2-algorithms/17-bit-manipulation.ipynb) · [greedy](2-algorithms/18-greedy.ipynb) · [number theory](2-algorithms/19-number-theory.ipynb) · [combinatorics](2-algorithms/20-combinatorics.ipynb) · [advanced number theory](2-algorithms/21-advanced-number-theory.ipynb) · [fft & polynomials](2-algorithms/22-fft-and-polynomials.ipynb) · [computational geometry](2-algorithms/23-computational-geometry.ipynb) · [sqrt decomposition & offline](2-algorithms/24-sqrt-decomposition-and-offline.ipynb) · [randomized algorithms](2-algorithms/25-randomized-algorithms.ipynb) |
| **3 — Patterns** (11) | [two pointers](3-patterns/01-two-pointers.ipynb) · [sliding window](3-patterns/02-sliding-window.ipynb) · [prefix sums & diff arrays](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) · [monotonic stack/queue](3-patterns/04-monotonic-stack-and-queue.ipynb) · [top-k & k-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb) · [cyclic sort](3-patterns/06-cyclic-sort.ipynb) · [combinatorial generation](3-patterns/07-combinatorial-generation.ipynb) · [coordinate compression](3-patterns/08-coordinate-compression.ipynb) · [meet in the middle](3-patterns/09-meet-in-the-middle.ipynb) · [sweep line](3-patterns/10-sweep-line.ipynb) · [grid & matrix traversal](3-patterns/11-grid-and-matrix-traversal.ipynb) |

---

## 1. Which do I reach for? — the decision guide

The highest-value part: keyed by **goal**, not by structure name.

### Storing & looking things up

| I want… | Reach for | Notebook |
|---|---|---|
| Membership / de-dup, order doesn't matter | `set` (O(1) avg `in`) | [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) |
| Key → value mapping | `dict` (O(1) avg, insertion-ordered) | [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) |
| A hashable key/member that's itself a collection | `frozenset` / `tuple` | [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) · [arrays](1-data-structures/01-arrays.ipynb) |
| Count occurrences | `collections.Counter` | [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) |
| Sorted data, lookup-heavy (few inserts) | sorted `list` + `bisect` | [trees](1-data-structures/07-trees.ipynb) · [searching](2-algorithms/02-searching.ipynb) |
| **Ordered data with fast lookup *and* insert** | `sortedcontainers` / balanced tree (CPython has none built in) | [trees](1-data-structures/07-trees.ipynb) |
| Compact storage of many numbers | `array` / `numpy.ndarray` | [arrays](1-data-structures/01-arrays.ipynb) |
| Fast push/pop at both ends | `collections.deque` | [arrays](1-data-structures/01-arrays.ipynb) · [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb) |
| Autocomplete / "all keys with prefix X" / longest-prefix match | trie (radix for tight memory) | [tries](1-data-structures/08-tries.ipynb) |
| **Maximum XOR of a value against a set** | binary trie (bit-by-bit greedy) | [tries](1-data-structures/08-tries.ipynb) |
| Bounded LRU cache of function results | `functools.lru_cache` / `OrderedDict` | [lru cache](1-data-structures/12-lru-cache.ipynb) |
| **On-disk ordered index, read-heavy** | B+ tree (high fan-out, few seeks) | [systems structures](1-data-structures/14-systems-data-structures.ipynb) |
| **Write-/ingest-heavy on-disk store** | LSM tree (sequential writes, low write amp) | [systems structures](1-data-structures/14-systems-data-structures.ipynb) |

### Priorities, order statistics, ranges

| I want… | Reach for | Notebook |
|---|---|---|
| Repeatedly pull the min/max while inserting | `heapq` on a `list` (O(log n) push/pop) | [heaps](1-data-structures/04-heaps.ipynb) |
| A priority queue (Dijkstra, scheduling) | `heapq` with `(priority, count, item)` tuples | [heaps](1-data-structures/04-heaps.ipynb) |
| **A running median over a stream** | two heaps (max-heap + min-heap, O(log n) insert) | [heaps](1-data-structures/04-heaps.ipynb) |
| **k-th smallest / median (single rank)** | quickselect (O(n) avg); `statistics.median` for clarity | [selection](2-algorithms/03-selection.ipynb) |
| **The k smallest/largest items, k ≪ n** | `heapq.nsmallest` / `nlargest` (O(n log k)) | [selection](2-algorithms/03-selection.ipynb) · [top-k](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| Worst-case O(n) selection guarantee | median-of-medians (BFPRT) | [selection](2-algorithms/03-selection.ipynb) |
| Merge k sorted lists/streams lazily | `heapq.merge` (frontier heap, O(N log k)) | [top-k & k-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| **Many range-sum queries, static array** | prefix sums (O(1) query) | [prefix sums](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) |
| Many range-updates, read once | difference array (O(1) per update) | [prefix sums](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) |
| **Point update + range sum, interleaved** | Fenwick / BIT (O(log n) both) | [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) |
| Point update + range min/max/gcd | segment tree (any associative op) | [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) |
| **Range update + range query** | segment tree **+ lazy propagation** | [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) |
| **Immutable array, range min/max/gcd in O(1)** | sparse table (idempotent op, no updates) | [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) |
| A range aggregate that **isn't easily associative** (distinct count, mode, k-th) | sqrt decomposition (O(√n), tiny constant) | [sqrt decomposition & offline](2-algorithms/24-sqrt-decomposition-and-offline.ipynb) |
| **All queries known up front, weird aggregate** | Mo's algorithm (O((n+q)√n) by reordering) | [sqrt decomposition & offline](2-algorithms/24-sqrt-decomposition-and-offline.ipynb) |
| Query an array **as it was at version k** | persistent segment tree (path copying) | [spatial & persistent](1-data-structures/11-spatial-and-persistent-structures.ipynb) |

### Searching & sorting

| I want… | Reach for | Notebook |
|---|---|---|
| Sort anything | `sorted()` / `list.sort()` (Timsort, stable, O(n log n)) | [sorting](2-algorithms/01-sorting.ipynb) |
| Sort bounded-range integers, fastest | counting / radix sort (O(n), beats the comparison floor) | [sorting](2-algorithms/01-sorting.ipynb) |
| Sort uniformly distributed floats | bucket sort (O(n) expected) | [sorting](2-algorithms/01-sorting.ipynb) |
| Find / count in sorted data | `bisect` (O(log n)) | [searching](2-algorithms/02-searching.ipynb) |
| Boundary of a monotonic condition | binary search **on the answer** | [searching](2-algorithms/02-searching.ipynb) |
| **Argmax/argmin of a unimodal function** | ternary search (O(log R)) | [searching](2-algorithms/02-searching.ipynb) |
| Keep a list sorted as you insert | `bisect.insort` (O(log n) find, O(n) shift) | [sorting](2-algorithms/01-sorting.ipynb) |
| **Split / combine into smaller independent halves** | divide & conquer (read complexity off the Master Theorem) | [divide & conquer](2-algorithms/05-divide-and-conquer.ipynb) |

### Strings & substring search

| I want… | Reach for | Notebook |
|---|---|---|
| Just `pattern in text` in Python | built-in `in` / `.find` (C `fastsearch`) | [string algorithms](2-algorithms/14-string-algorithms.ipynb) |
| **One pattern, understood from scratch** | KMP (O(n+m), prefix function) | [string algorithms](2-algorithms/14-string-algorithms.ipynb) |
| Rolling hash / fingerprinting / 2D | Rabin-Karp | [string algorithms](2-algorithms/14-string-algorithms.ipynb) |
| **Every palindromic substring in O(n)** | Manacher's algorithm | [string algorithms](2-algorithms/14-string-algorithms.ipynb) |
| **Many substring queries on a fixed text** | suffix array (+ LCP for repeats) | [suffix structures](2-algorithms/15-suffix-structures.ipynb) |
| **Many patterns, one scan** | Aho-Corasick (O(\|T\| + matches)) | [suffix structures](2-algorithms/15-suffix-structures.ipynb) |
| Linear prefix-match primitive / string periods | Z-algorithm | [suffix structures](2-algorithms/15-suffix-structures.ipynb) |
| **Count distinct substrings / LCS of two strings / online build** | suffix automaton (minimal DFA, O(n)) | [suffix automaton & tree](2-algorithms/16-suffix-automaton-and-tree.ipynb) |
| Build a big string from pieces | `list` + `"".join` (never the `+=` cliff) | [strings](1-data-structures/02-strings.ipynb) |
| A mutable byte buffer | `bytearray` | [strings](1-data-structures/02-strings.ipynb) |

### Graphs, trees & flows

| Shortest path with… | Use | Cost | Notebook |
|---|---|:---:|---|
| **No weights** | BFS | O(V+E) | [graphs](1-data-structures/09-graphs.ipynb) |
| **Non-negative weights** | Dijkstra (`heapq`) | O((V+E) log V) | [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) |
| **Negative weights** | Bellman-Ford | O(V·E) | [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) |
| **All pairs** | Floyd-Warshall | O(V³) | [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) |
| **One goal + a heuristic** | A\* | O((V+E) log V), fewer nodes | [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) |

| Graph / tree goal | Use | Notebook |
|---|---|---|
| Order tasks with dependencies | topological sort (Kahn / DFS) | [graphs](1-data-structures/09-graphs.ipynb) |
| "Same component?" / incremental connectivity | Union-Find (~O(1) amortized) | [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) |
| Minimum spanning tree | Kruskal (sparse) / Prim (dense) | [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) |
| SCC / 2-SAT / cycle in a digraph | Kosaraju or Tarjan | [advanced graph algorithms](2-algorithms/12-advanced-graph-algorithms.ipynb) |
| Single points of failure (links/routers) | bridges / articulation points | [advanced graph algorithms](2-algorithms/12-advanced-graph-algorithms.ipynb) |
| Throughput / min cut, simplest correct | Edmonds-Karp max-flow | [advanced graph algorithms](2-algorithms/12-advanced-graph-algorithms.ipynb) |
| **Max throughput, dense / large capacities** | Dinic (O(V²E)) | [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb) |
| **Flow that also minimizes a price** | min-cost max flow | [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb) |
| **Cheapest perfect assignment (n×n costs)** | Hungarian algorithm (O(n³)) | [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb) |
| Largest bipartite matching, large graph | Hopcroft-Karp (O(E√V)) | [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb) |
| **A route using every edge once** | Eulerian path (Hierholzer) | [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb) |
| **LCA / distance between nodes, many queries** | binary lifting (sparse table of ancestors) | [tree algorithms](2-algorithms/09-tree-algorithms.ipynb) |
| **Longest path / tree diameter** | two-pass BFS, or single-DFS DP | [tree algorithms](2-algorithms/09-tree-algorithms.ipynb) |
| **An aggregate for *every* root** | rerooting (all-roots DP, O(n)) | [tree algorithms](2-algorithms/09-tree-algorithms.ipynb) |
| **Path sum/max with point updates** | heavy-light decomposition + segment tree | [advanced tree decompositions](2-algorithms/10-advanced-tree-decompositions.ipynb) |
| **Count / aggregate over all paths by property** | centroid decomposition | [advanced tree decompositions](2-algorithms/10-advanced-tree-decompositions.ipynb) |
| Subtree aggregate + point update | Euler tour + Fenwick / segment tree | [advanced tree decompositions](2-algorithms/10-advanced-tree-decompositions.ipynb) |

### DP — which flavor is it?

| The state looks like… | It's | Notebook |
|---|---|---|
| Index / pair of positions, overlapping subproblems | classic DP (coin change, LCS, edit dist, knapsack, LIS) | [dynamic programming](2-algorithms/06-dynamic-programming.ipynb) |
| A contiguous **interval** `(i,j)` with a split inside | interval DP (matrix-chain) | [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb) |
| A **subset** packed in a bitmask, small n ≤ ~20 | bitmask DP (Held-Karp TSP) | [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb) |
| A node depending on its subtrees | tree DP (max-weight independent set) | [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb) |
| Counting numbers in `[0,N]` by a digit rule | digit DP | [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb) |
| A sequence of steps with a few legal modes | state-machine DP (stock w/ cooldown) | [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb) |
| An expected value over random outcomes | probability DP (absorbing Markov chain) | [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb) |
| A correct recurrence that's just **too slow** | DP optimization (deque / CHT / D&C DP / Knuth) | [DP optimizations](2-algorithms/08-dp-optimizations.ipynb) |

### Math, counting & geometry

| I want… | Reach for | Notebook |
|---|---|---|
| GCD / primes / modular inverse / CRT | `math.gcd`, sieve, `pow(a,-1,m)`, Miller-Rabin | [number theory](2-algorithms/19-number-theory.ipynb) |
| **Count arrangements / nCk mod p / Catalan / inclusion-exclusion** | combinatorics toolkit | [combinatorics](2-algorithms/20-combinatorics.ipynb) |
| **n-th term of a linear recurrence, huge n** | matrix exponentiation (O(log n)) | [advanced number theory](2-algorithms/21-advanced-number-theory.ipynb) |
| **Who wins an impartial game** | Sprague-Grundy + mex (nim-sum XOR) | [advanced number theory](2-algorithms/21-advanced-number-theory.ipynb) |
| **Solve `a^x ≡ b (mod m)`, moderate m** | baby-step giant-step (O(√m)) | [advanced number theory](2-algorithms/21-advanced-number-theory.ipynb) |
| **Convolve two sequences / multiply polynomials** | FFT (float) / NTT (exact integer), O(n log n) | [fft & polynomials](2-algorithms/22-fft-and-polynomials.ipynb) |
| Orientation / segment crossing / convex hull / point-in-polygon | the cross-product geometry toolkit | [computational geometry](2-algorithms/23-computational-geometry.ipynb) |
| **Closest pair of points** | divide & conquer / sweep, O(n log n) | [computational geometry](2-algorithms/23-computational-geometry.ipynb) |
| Optimal prefix code / compression | Huffman coding (greedy) | [greedy](2-algorithms/18-greedy.ipynb) |
| A small fixed universe needing raw speed | `int` bitmask as a set | [bit manipulation](2-algorithms/17-bit-manipulation.ipynb) |

### "Is this input actually too slow?" & scale tricks

| Situation | Reach for | Notebook |
|---|---|---|
| **"Is this big input actually O(n²)?"** | the cost model — measure, hoist lookups, drop to C/numpy | [cpython-cost-model](0-foundations/03-cpython-cost-model.ipynb) |
| **P vs NP intuition — tractable or not?** | the P / NP / NP-complete framing | [big-o](0-foundations/01-big-o.ipynb) |
| Web-scale "have I seen this?" with rare false-yes OK | Bloom filter | [probabilistic structures](1-data-structures/13-probabilistic-structures.ipynb) |
| Distinct count over a huge stream | HyperLogLog | [probabilistic structures](1-data-structures/13-probabilistic-structures.ipynb) |
| Approximate heavy-hitters / top-K | count-min sketch | [probabilistic structures](1-data-structures/13-probabilistic-structures.ipynb) |
| **Which intervals cover a point / nearest 2-D point** | interval tree / k-d tree | [spatial & persistent](1-data-structures/11-spatial-and-persistent-structures.ipynb) |
| **Uniform sample from a stream of unknown length** | reservoir sampling (one pass, O(k) space) | [randomized algorithms](2-algorithms/25-randomized-algorithms.ipynb) |
| **Verify a costly computation cheaply** | Monte-Carlo / Freivalds (one-sided error) | [randomized algorithms](2-algorithms/25-randomized-algorithms.ipynb) |
| Values up to 10⁹ but only k distinct | coordinate compression → index by value | [coordinate compression](3-patterns/08-coordinate-compression.ipynb) |
| Exponential search, n ≈ 30–45 | meet in the middle (2ⁿ → 2·2^(n/2)) | [meet in the middle](3-patterns/09-meet-in-the-middle.ipynb) |
| Overlapping subproblems + optimal substructure | dynamic programming | [dynamic programming](2-algorithms/06-dynamic-programming.ipynb) |
| Locally-best choice + provable greedy property | greedy (sort + one pass) | [greedy](2-algorithms/18-greedy.ipynb) |

---

## 2. Data structures — complexity table

Worst case unless noted. Links go to each structure's notebook.

### Linear structures ([arrays](1-data-structures/01-arrays.ipynb), [linked lists](1-data-structures/05-linked-lists.ipynb), [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb))

| Structure | Index | Search | Insert/del front | Insert/del end | Insert/del middle | Memory/elem |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `list` | O(1) | O(n) | O(n) | O(1) amort. | O(n) | high (ptr+obj) |
| `tuple` (immutable) | O(1) | O(n) | — | — | — | high (ptr+obj) |
| `array` | O(1) | O(n) | O(n) | O(1) amort. | O(n) | low (C type) |
| `numpy.ndarray` | O(1) | O(n) | O(n) | O(n) (realloc) | O(n) | low (C type) |
| `deque` | O(n) | O(n) | O(1) | O(1) | O(n) | low-ish (blocked) |
| Singly linked list | O(n) | O(n) | O(1) | O(n)† | O(n)‡ | high (node obj) |
| Doubly linked list | O(n) | O(n) | O(1) | O(1) | O(1) given a node | higher (2 ptrs) |

<sub>† O(1) with a tail pointer · ‡ singly LL needs the predecessor to relink.</sub>

### Hash structures ([dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb))

| Structure | Lookup/membership | Insert | Delete | Iterate | Memory |
|---|:---:|:---:|:---:|:---:|:---:|
| `dict` | O(1) avg, O(n) worst | O(1) avg† | O(1) avg | O(n) | high |
| `set` | O(1) avg, O(n) worst | O(1) avg† | O(1) avg | O(n) | high |
| `frozenset` | O(1) avg, O(n) worst | — (immutable) | — | O(n) | high |

<sub>† amortized — occasional O(n) resize past ~2/3 full. Worst case is pathological collisions only.</sub>

### Ordered & range structures ([heaps](1-data-structures/04-heaps.ipynb), [trees](1-data-structures/07-trees.ipynb), [tries](1-data-structures/08-tries.ipynb), [fenwick](1-data-structures/10-fenwick-and-segment-trees.ipynb))

| Structure | Search/lookup | Insert | Delete | Min/max | Range query | Build |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Binary heap (`heapq`) | O(n) | O(log n) | O(log n) | O(1) peek | — | O(n) `heapify` |
| Two heaps (running median) | — | O(log n) | O(log n) | O(1) median | — | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(log n + k) | — |
| BST (degenerate) | O(n) | O(n) | O(n) | O(n) | O(n) | — |
| Sorted list + `bisect` | O(log n) | O(n)† | O(n) | O(1) at ends | O(log n + k) | O(n log n) |
| Trie | O(L) | O(L) | O(L) | — | prefix O(L+k) | — |
| Binary trie (max-XOR) | O(W) | O(W) | O(W) | — | max-XOR O(W) | — |
| Prefix sum (static) | — | O(n) rebuild | — | — | O(1) | O(n) |
| Fenwick tree | — | O(log n) | — | — | O(log n) | O(n log n) |
| Segment tree | — | O(log n) | — | — | O(log n) | O(n) |
| Segment tree + lazy | — | O(log n) range | — | — | O(log n) | O(n) |
| Sparse table | — | — (immutable) | — | — | **O(1)** idempotent | O(n log n) |

<sub>† O(log n) to find the spot, O(n) to shift. L = key length, k = matches, W = bit-width of the value.</sub>

### Spatial & persistent structures ([spatial & persistent](1-data-structures/11-spatial-and-persistent-structures.ipynb))

| Structure | Build | Query | Update | Extra memory |
|---|:---:|:---:|:---:|:---:|
| Interval tree | O(n log n) | O(log n + k) | — (static) | O(n) |
| k-d tree (2-D) | O(n log n) | O(log n + k) avg* | O(log n) amortized† | O(n) |
| Persistent segment tree | O(n) | O(log n) per version | O(log n) **new nodes** | O(log n) per version |

<sub>*k-d nearest/range is O(√n + k) worst case in 2-D and degrades toward O(n) in high dimensions. † k-d trees rebalance poorly under churn — rebuild periodically. Path copying makes each persistent update allocate only ~⌈log₂ n⌉ new nodes; *m* updates cost O(m log n) total memory.</sub>

### Probabilistic structures ([probabilistic structures](1-data-structures/13-probabilistic-structures.ipynb))

| Structure | Space | add | query | Error direction |
|---|:---:|:---:|:---:|---|
| Bloom filter | m bits (~1.44·log₂(1/p)·n) | O(k) | O(k) | false positives only; **no false negatives** |
| Skip list | O(n) (~2 ptrs/node) | O(log n) exp | O(log n) exp | **exact** (randomized balance) |
| Count-min sketch | w·d counters | O(d) | O(d) | overestimates only; **never undercounts** |
| HyperLogLog | M registers (~M bytes) | O(1) | O(M) | ±1.04/√M relative |

### Systems (on-disk) structures ([systems structures](1-data-structures/14-systems-data-structures.ipynb))

Cost is measured in **disk I/O** (seeks / block rewrites), not comparisons. n = keys, m = fan-out, B = block size, R = LSM runs.

| Operation | B-tree / B+ tree | LSM tree |
|---|:---:|:---:|
| Point lookup | O(log_m n) I/O | O(R) runs, ~O(1) with Bloom filters |
| Range scan | O(log_m n + k/B) (linked leaves) | O(R · scan) — merge across runs |
| Insert / update | O(log_m n), **in place** | O(1) amortized (append) |
| Delete | O(log_m n), in place | O(1) (tombstone) |
| Write amplification | **high** (rewrite a block per write) | **low** (sequential, batched) |
| Read amplification | **low** (one descent) | **higher** (check R runs) |

<sub>Read-heavy ⇒ B-tree (wide, shallow, update in place — the index under every SQL DB). Write-heavy ⇒ LSM tree (buffer, flush sorted runs, merge lazily, skip runs with Bloom filters).</sub>

### LRU cache ([lru cache](1-data-structures/12-lru-cache.ipynb))

| Op | `dict`+DLL / `OrderedDict` / `lru_cache` |
|---|:---:|
| `get`, `put`, evict LRU | O(1) each (memory O(capacity)) |

---

## 3. Algorithms — complexity table

### Sorting ([sorting](2-algorithms/01-sorting.ipynb))

| Algorithm | Best | Average | Worst | Space | Stable | In-place |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Timsort** (`sorted`) | O(n) | O(n log n) | O(n log n) | O(n) | ✅ | ✗ |
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ✗ | ✅ |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Shell | O(n log n) | ~O(n^1.3) | O(n²) | O(1) | ✗ | ✅ |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ✗ |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | ✗ | ✅ |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | ✗ | ✅ |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(n+k) | ✅ | ✗ |
| Radix | O(d·n) | O(d·n) | O(d·n) | O(n+b) | ✅ | ✗ |
| Bucket | O(n+k) | O(n) | O(n²) | O(n) | ✅ | ✗ |

<sub>k = value range, d = digits, b = radix base. Bucket is O(n) expected on uniform input.</sub>

### Searching & selection ([searching](2-algorithms/02-searching.ipynb), [selection](2-algorithms/03-selection.ipynb))

| Method | Best | Average | Worst | Space | Precondition |
|---|:---:|:---:|:---:|:---:|---|
| Linear search (`in`, `.index`) | — | O(n) | O(n) | O(1) | none |
| Binary search / `bisect` | — | O(log n) | O(log n) | O(1) | sorted |
| Hash lookup (`set`/`dict`) | — | O(1) avg | O(n) | — | hashable keys |
| Binary search on the answer | — | O(log R · P) | O(log R · P) | — | monotonic predicate |
| Ternary search | — | O(log R · F) | O(log R · F) | O(1) | unimodal function |
| `min` / `max` | O(n) | O(n) | O(n) | O(1) | — |
| Quickselect (random pivot) | O(n) | O(n) | O(n²) | O(1) | — |
| Median-of-medians (BFPRT) | O(n) | O(n) | O(n) | O(n) | — |
| `heapq.nsmallest`/`nlargest(k)` | O(n) | O(n log k) | O(n log k) | O(k) | — |
| `statistics.median` | O(n log n) | O(n log n) | O(n log n) | O(n) | — |
| `sorted(xs)[k]` | O(n) | O(n log n) | O(n log n) | O(n) | — |

<sub>R = range size, P = predicate cost, F = function-eval cost.</sub>

### Divide & conquer ([divide & conquer](2-algorithms/05-divide-and-conquer.ipynb))

`T(n) = a·T(n/b) + f(n)` — read complexity off the Master Theorem.

| Problem | Algorithm | Recurrence | Result |
|---|---|:---:|:---:|
| Sort a sequence | merge sort | `2T(n/2)+O(n)` | O(n log n) |
| Search a sorted sequence | binary search | `T(n/2)+O(1)` | O(log n) |
| k-th smallest, no full sort | quickselect | `T(n)+O(n)` avg | O(n) avg |
| Multiply huge integers | Karatsuba | `3T(n/2)+O(n)` | O(n^1.585) |
| Count out-of-order pairs | merge-and-count | `2T(n/2)+O(n)` | O(n log n) |
| Best contiguous-sum slice | max-subarray combine | `2T(n/2)+O(n)` | O(n log n) |
| Closest pair of points | strip combine | `2T(n/2)+O(n)` | O(n log n) |

<sub>Master Theorem cases: (1) leaf-heavy `Θ(n^(log_b a))`; (2) balanced `Θ(n^(log_b a)·log n)`; (3) root-heavy `Θ(f(n))`. **Overlapping** subproblems ⇒ use DP, not D&C.</sub>

### Dynamic programming ([dynamic programming](2-algorithms/06-dynamic-programming.ipynb), [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb), [DP optimizations](2-algorithms/08-dp-optimizations.ipynb))

**Classic grid DPs:**

| Problem | State | Time | Space (naive → rolled) |
|---|---|:---:|:---:|
| Fibonacci | `n` | O(n) | O(n) → O(1) |
| Coin change | amount | O(amount × #coins) | O(amount) |
| Longest common subsequence | `(i, j)` | O(m·n) | O(m·n) → O(min(m,n)) |
| Edit distance | `(i, j)` | O(m·n) | O(m·n) → O(min(m,n)) |
| 0/1 knapsack | `(item, cap)` | O(n·W) | O(n·W) → O(W) |
| Longest increasing subseq. | `i` / patience | O(n²) or O(n log n) | O(n) |

**Advanced DP families** (the state is no longer a simple index):

| Category | Canonical problem | State | Time |
|---|---|---|:---:|
| Interval | matrix-chain mult. | `(i, j)` | O(n³) |
| Bitmask | TSP (Held-Karp) | `(mask, i)` | O(2ⁿ · n²) |
| Tree | max-weight indep. set | node + take/skip | O(n) |
| Digit | count in `[0, N]` | `(pos, tight, started, …)` | O(len · feat · 10) |
| State-machine | stock w/ cooldown | `(day, mode)` | O(n · modes) |
| Probability | absorbing Markov chain | transient state | O(t³) solve |

**DP optimizations** (the recurrence is already correct — only the speed changes):

| Optimization | From | To | Precondition |
|---|:---:|:---:|---|
| Sliding-window deque | O(nk) | **O(n)** | min/max over a fixed-width window of states |
| Convex Hull Trick (monotone) | O(n²) | **O(n)** | linear transition; slopes & queries monotone |
| Convex Hull Trick (general) | O(n²) | **O(n log n)** | linear transition; arbitrary slopes/queries |
| Divide-and-conquer DP | O(kn²) | **O(kn log n)** | `opt(i)` non-decreasing in `i` |
| Knuth's optimization | O(n³) | **O(n²)** | interval cost satisfies the quadrangle inequality |

<sub>W = capacity (knapsack is pseudo-polynomial — scales with the numeric W).</sub>

### Tree algorithms ([tree algorithms](2-algorithms/09-tree-algorithms.ipynb), [advanced tree decompositions](2-algorithms/10-advanced-tree-decompositions.ipynb))

| Algorithm | Build / preprocess | Query | Notes |
|---|:---:|:---:|---|
| Root the tree (parent/depth/size) | O(n) | — | one iterative DFS |
| LCA — binary lifting | O(n log n) | O(log n) | sparse table `up[k][v]` |
| LCA — Euler tour + sparse-table RMQ | O(n log n) | O(1) | RMQ over the Euler tour |
| Tree distance (via LCA) | O(n log n) | O(log n) | `du + dv − 2·d_lca` |
| Diameter — two-pass BFS | O(n) | — | unweighted endpoint lemma |
| Diameter — single-DFS DP | O(n) | — | `h1 + h2` bend; extends to weights |
| Rerooting (all-roots DP) | O(n) | O(1) per root | down pass + ±1 reroot pass |
| Euler tour + segment tree | O(n) | O(log n) | subtree aggregates + point update |
| Centroid decomposition | O(n log n) | O(log² n) | all-paths counting |
| Heavy-light decomposition | O(n) | O(log² n) | online path queries + point/range update |

### Graph algorithms ([graph algorithms](2-algorithms/11-graph-algorithms.ipynb), [advanced](2-algorithms/12-advanced-graph-algorithms.ipynb), [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb))

| Algorithm | Solves | Time | Space |
|---|---|:---:|:---:|
| BFS / DFS | traverse / unweighted shortest path | O(V+E) | O(V) |
| Topological sort | order a DAG | O(V+E) | O(V) |
| Dijkstra | non-negative shortest path | O((V+E) log V) | O(V) |
| Bellman-Ford | negative-weight shortest path | O(V·E) | O(V) |
| A\* | single-goal shortest path + heuristic | O((V+E) log V) | O(V) |
| Floyd-Warshall | all-pairs shortest paths | O(V³) | O(V²) |
| Union-Find | incremental connectivity | ~O(1) amortized | O(V) |
| Kruskal | MST (sparse / edge list) | O(E log E) | O(V) |
| Prim | MST (dense / adjacency) | O(E log V) | O(V) |
| Kosaraju / Tarjan SCC | strongly connected components | O(V+E) | O(V+E) / O(V) |
| Bridges / articulation | edges/vertices that disconnect | O(V+E) | O(V) |
| Edmonds-Karp | max-flow / min-cut (simplest) | O(V·E²) | O(V+E) |
| **Dinic** | max-flow / min-cut (default fast) | O(V²·E), O(E√V) unit-cap | O(V+E) |
| **Min-cost max flow** (SPFA) | cheapest max flow | O(V·E·flow) worst | O(V+E) |
| **Kuhn** | max bipartite matching (simplest) | O(V·E) | O(V+E) |
| **Hopcroft-Karp** | max bipartite matching (fast) | O(E·√V) | O(V+E) |
| **Hungarian** | min-cost perfect assignment | O(n³) | O(n²) |
| **Bipartite check** | 2-colorability / odd cycle | O(V+E) | O(V) |
| **Hierholzer** | Eulerian path / circuit | O(E) | O(V+E) |

### String, suffix & automaton algorithms ([string algorithms](2-algorithms/14-string-algorithms.ipynb), [suffix structures](2-algorithms/15-suffix-structures.ipynb), [suffix automaton & tree](2-algorithms/16-suffix-automaton-and-tree.ipynb))

| Algorithm | Preprocess / build | Search / query | Space |
|---|:---:|:---:|:---:|
| Naive search | — | O(n·m) | O(1) |
| KMP | O(m) | O(n) | O(m) |
| Rabin-Karp | O(m) | O(n) avg, O(n·m) worst | O(1) |
| Manacher | O(n) | O(1) per center | O(n) |
| CPython `fastsearch` | O(m) | O(n) | O(1) |
| Z-array | O(n) | O(n) per `P+sep+T` | O(n) |
| Suffix array (prefix-doubling) | O(n log² n) | O(m log n) | O(n) |
| Suffix array (SA-IS, named) | O(n) | O(m log n) | O(n) |
| LCP array (Kasai) | O(n) given SA | O(1) lookup | O(n) |
| Aho-Corasick | O(M) | O(n + z) scan | O(M·Σ) |
| **Suffix automaton (SAM)** | **O(n) online** | O(m) accept; O(\|t\|) LCS | O(n·Σ) |
| · count distinct substrings | — | **O(n)** total | — |
| Suffix tree (Ukkonen, named) | O(n) | O(m) | O(n·Σ) |

<sub>M = total pattern length, z = matches, Σ = alphabet size. SAM has ≤ 2n−1 states, ≤ 3n−4 edges.</sub>

### Number theory, combinatorics & advanced ([number theory](2-algorithms/19-number-theory.ipynb), [combinatorics](2-algorithms/20-combinatorics.ipynb), [advanced number theory](2-algorithms/21-advanced-number-theory.ipynb), [fft](2-algorithms/22-fft-and-polynomials.ipynb))

| Task | Algorithm | Complexity | Builtin |
|---|---|:---:|---|
| GCD / LCM | Euclid | O(log n) | `math.gcd` / `math.lcm` |
| All primes ≤ n | sieve of Eratosthenes | O(n log log n) | — |
| Single primality | trial division / Miller-Rabin | O(√n) / prob. | — |
| base^exp mod m | binary exponentiation | O(log exp) | `pow(b, e, m)` |
| Modular inverse | extended Euclid / Fermat | O(log m) | `pow(a, -1, m)` |
| Prime factorization | trial div / SPF sieve / Pollard's rho | O(√n) / O(log n) / O(n¼) | — |
| Euler's totient φ(n) | product formula over prime factors | O(√n) | — |
| CRT: solve x ≡ rᵢ (mod mᵢ) | Chinese Remainder Theorem | O(k log M) | `pow(Mᵢ,-1,mᵢ)` |
| nCk, nPk, n! | — | exact | `math.comb`/`perm`/`factorial` |
| nCk mod prime p (n < p) | factorials + Fermat inverse | O(n) prep, O(1)/query | `pow(a,-1,p)` |
| nCk mod small prime, huge n | Lucas' theorem | O(log_p n) | — |
| Catalan Cₙ | `C(2n,n)/(n+1)` | O(n) | `math.comb` |
| Inclusion–exclusion | alternate +/− over subsets | O(2^m) | — |
| Stars & bars | `C(n+k−1, k−1)` | O(k) | `math.comb` |
| n-th term of a linear recurrence | matrix exponentiation | O(k³ log n) | — |
| Impartial game winner | Sprague-Grundy + mex (nim-sum) | O(states·moves) | — |
| Discrete log `a^x ≡ b (mod m)` | baby-step giant-step | O(√m) | — |
| Convolution / polynomial multiply | FFT (float) / NTT (exact int) | O(n log n) | `numpy.convolve` / `numpy.fft` |
| Big-integer multiply (N digits) | Karatsuba / FFT | O(N^1.585) / O(N log N) | CPython `int` |

### Geometry ([computational geometry](2-algorithms/23-computational-geometry.ipynb))

| Task | Algorithm | Complexity | Exact on ints? |
|---|---|:---:|:---:|
| Orientation of 3 points | sign of cross product | O(1) | ✅ |
| Segment intersection (yes/no) | four-orientation rule | O(1) | ✅ |
| Convex hull | Andrew's monotone chain | O(n log n) | ✅ |
| Point in polygon | ray casting (even-odd) | O(n) | ⚠️ division for x_cross |
| Polygon area / orientation | shoelace formula | O(n) | ✅ |
| Closest pair of points | divide & conquer / sweep | O(n log n) | ✅ via squared distances |

<sub>One primitive: `cross(o,a,b)`. Keep coordinates **integer**, compare **squared** distances, and avoid division until the final coordinate.</sub>

### Range-query middle ground ([sqrt decomposition & offline](2-algorithms/24-sqrt-decomposition-and-offline.ipynb))

| Technique | Build | Range query | Point update | Range update |
|---|:---:|:---:|:---:|:---:|
| Prefix sums | O(n) | O(1) | O(n) rebuild | — |
| **Sqrt decomposition** | O(n) | **O(√n)** | O(1) | O(√n) (block lazy) |
| Fenwick tree | O(n) | O(log n) | O(log n) | — |
| Segment tree (+ lazy) | O(n) | O(log n) | O(log n) | O(log n) |
| **Mo's algorithm** | O(q log q) sort | **O((n+q)√n)** total, offline | — | — |

<sub>Sqrt decomposition is the simple, flexible middle: worse than O(log n) but tiny constant, and it computes aggregates a tree can't (distinct count, mode, k-th). Mo's reuses the √n idea *on the queries*.</sub>

### Randomized algorithms ([randomized algorithms](2-algorithms/25-randomized-algorithms.ipynb))

| Algorithm | Time | Space | Flavor | Guarantee |
|---|:---:|:---:|---|---|
| Reservoir sampling | O(n) one pass | O(k) | Las Vegas | each element selected w.p. k/n |
| Fisher-Yates shuffle | O(n) | O(1) in-place | Las Vegas | all n! orderings equally likely |
| Monte Carlo estimation (π) | O(N) | O(1) | Monte Carlo | error ~1/√N |
| Freivalds' check | O(t·n²) | O(n) | Monte Carlo, one-sided | miss rate ≤ 2⁻ᵗ |
| Randomized quickselect | O(n) expected | O(1) | Las Vegas | always correct |

<sub>**Las Vegas** = always correct, random runtime (analyze *expected time*). **Monte Carlo** = fixed runtime, bounded — ideally one-sided — error (amplify by repetition). Always seed the RNG and measure.</sub>

---

## 4. Patterns — quick reference

The 11 problem-solving patterns: how to **recognize** each, the technique, and the payoff.

| Pattern | Signal — when you recognize it | Technique | Complexity | Notebook |
|---|---|---|:---:|---|
| **Two pointers** | sorted array → pair/triplet by sum; in-place compact/dedupe; cycle/midpoint | converging / read-write / fast-slow pointers | O(n) time, O(1) space (from O(n²)) | [two pointers](3-patterns/01-two-pointers.ipynb) |
| **Sliding window** | optimum/count over a **contiguous** run | grow/shrink a window, update a running summary | O(n) (from O(n·k) or O(n²)) | [sliding window](3-patterns/02-sliding-window.ipynb) |
| **Prefix sums & diff arrays** | many range-sum queries (static); many range-updates | precompute running sums / inverse difference array | build O(n), query O(1) | [prefix sums](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) |
| **Monotonic stack/queue** | nearest greater/smaller; max/min in every window | discard elements that can never be the answer | O(n) (from O(n²)/O(n·k)) | [monotonic stack/queue](3-patterns/04-monotonic-stack-and-queue.ipynb) |
| **Top-K & k-way merge** | k largest/smallest/most-frequent; merge k sorted | size-k heap / heap of frontiers | O(n log k) / O(N log k) | [top-k & k-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| **Cyclic sort** | array values are a permutation of `1..n` / `0..n-1` | swap each value to its home index | O(n) time, O(1) space | [cyclic sort](3-patterns/06-cyclic-sort.ipynb) |
| **Combinatorial generation** | enumerate subsets / permutations / combinations | backtracking / bitmask / `itertools` | 2ⁿ subsets, n! perms (prune!) | [combinatorial generation](3-patterns/07-combinatorial-generation.ipynb) |
| **Coordinate compression** | values sparse/huge but only relative order matters | remap to dense ranks `0..k-1` | build O(n log n), map O(1)/O(log k) | [coordinate compression](3-patterns/08-coordinate-compression.ipynb) |
| **Meet in the middle** | exponential search, n ≈ 30–45 | split in halves, combine with set / `bisect` | 2·2^(n/2) (from 2ⁿ) | [meet in the middle](3-patterns/09-meet-in-the-middle.ipynb) |
| **Sweep line** | interval / geometry events along an axis | sort events, maintain active state | O(n log n) | [sweep line](3-patterns/10-sweep-line.ipynb) |
| **Grid & matrix traversal** | a 2D grid is a graph in disguise | BFS/DFS on implicit graph; multi-source BFS | O(R·C) | [grid & matrix](3-patterns/11-grid-and-matrix-traversal.ipynb) |

---

## 5. Practice problems by pattern / topic — the study plan

Canonical interview/LeetCode problems grouped by the technique that cracks them. Work each group right after its notebook.

### Two pointers — [two pointers](3-patterns/01-two-pointers.ipynb)
- Two Sum II (sorted input)
- 3Sum / 3Sum Closest
- Container With Most Water
- Trapping Rain Water
- Remove Duplicates from Sorted Array
- Valid Palindrome

### Sliding window — [sliding window](3-patterns/02-sliding-window.ipynb)
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Longest Repeating Character Replacement
- Permutation in String
- Maximum Average Subarray I (fixed window)
- Fruit Into Baskets

### Prefix sums & difference arrays — [prefix sums](3-patterns/03-prefix-sums-and-difference-arrays.ipynb)
- Subarray Sum Equals K (prefix + hashmap)
- Range Sum Query — Immutable / 2D Immutable
- Product of Array Except Self
- Contiguous Array (equal 0s and 1s)
- Car Pooling / Corporate Flight Bookings (difference array)

### Monotonic stack & queue — [monotonic stack/queue](3-patterns/04-monotonic-stack-and-queue.ipynb)
- Daily Temperatures
- Next Greater Element I / II
- Largest Rectangle in Histogram
- Trapping Rain Water (stack variant)
- Sliding Window Maximum (monotonic deque)

### Top-K & k-way merge — [top-k & k-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb)
- Kth Largest Element in an Array
- Top K Frequent Elements
- Merge k Sorted Lists
- Find K Pairs with Smallest Sums
- Kth Smallest Element in a Sorted Matrix

### Cyclic sort — [cyclic sort](3-patterns/06-cyclic-sort.ipynb)
- Missing Number
- Find All Numbers Disappeared in an Array
- Find All Duplicates in an Array
- First Missing Positive
- Set Mismatch (the corrupt pair)

### Combinatorial generation / backtracking — [combinatorial generation](3-patterns/07-combinatorial-generation.ipynb) · [recursion & backtracking](2-algorithms/04-recursion-and-backtracking.ipynb)
- Subsets / Subsets II
- Permutations / Permutations II
- Combination Sum
- Generate Parentheses
- N-Queens
- Word Search
- Sudoku Solver

### Coordinate compression — [coordinate compression](3-patterns/08-coordinate-compression.ipynb)
- Count of Smaller Numbers After Self
- Reverse Pairs
- The Skyline Problem
- Rectangle Area II
- Number of Longest Increasing Subsequence (with a BIT)

### Meet in the middle — [meet in the middle](3-patterns/09-meet-in-the-middle.ipynb)
- Partition to K Equal Sum Subsets
- Closest Subsequence Sum
- Split Array With Same Average
- 4Sum (and 4Sum II)

### Sweep line — [sweep line](3-patterns/10-sweep-line.ipynb)
- Merge Intervals
- Insert Interval
- Meeting Rooms II (min rooms)
- My Calendar I / II / III
- The Skyline Problem

### Grid & matrix traversal — [grid & matrix](3-patterns/11-grid-and-matrix-traversal.ipynb)
- Number of Islands
- Rotting Oranges (multi-source BFS)
- Flood Fill
- Word Ladder (BFS on implicit graph)
- Walls and Gates
- Rotate Image / Spiral Matrix

### Divide & conquer — [divide & conquer](2-algorithms/05-divide-and-conquer.ipynb)
- Sort an Array (merge sort)
- Count of Smaller Numbers After Self (merge-and-count inversions)
- Maximum Subarray (D&C combine)
- Different Ways to Add Parentheses
- Beautiful Array

### Dynamic programming — [dynamic programming](2-algorithms/06-dynamic-programming.ipynb)
- Coin Change / Coin Change II
- Longest Common Subsequence
- Edit Distance
- 0/1 Knapsack (Partition Equal Subset Sum)
- Longest Increasing Subsequence
- House Robber
- Word Break
- Unique Paths

### Advanced DP & DP optimizations — [advanced DP](2-algorithms/07-advanced-dynamic-programming.ipynb) · [DP optimizations](2-algorithms/08-dp-optimizations.ipynb)
- Burst Balloons / Minimum Cost to Merge Stones (interval DP)
- Find the Shortest Superstring / Partition to K Equal Sum Subsets (bitmask DP)
- Binary Tree Cameras / House Robber III (tree DP)
- Count Numbers with Unique Digits / Numbers At Most N Given Digit Set (digit DP)
- Best Time to Buy and Sell Stock with Cooldown (state-machine DP)
- Frog Jump / Largest Sum of Averages (D&C DP, Knuth, convex hull trick)

### Tree algorithms — [tree algorithms](2-algorithms/09-tree-algorithms.ipynb) · [advanced tree decompositions](2-algorithms/10-advanced-tree-decompositions.ipynb)
- Lowest Common Ancestor of a Binary Tree (and LCA via binary lifting)
- Diameter of Binary Tree / Tree Diameter
- Sum of Distances in Tree (rerooting)
- Path Sum III (path counting)
- Count Pairs of Nodes within distance K (centroid decomposition)
- Path Queries with point updates (heavy-light decomposition)

### Graphs & graph algorithms — [graphs](1-data-structures/09-graphs.ipynb) · [graph algorithms](2-algorithms/11-graph-algorithms.ipynb) · [advanced graph algorithms](2-algorithms/12-advanced-graph-algorithms.ipynb)
- Course Schedule I / II (topological sort)
- Network Delay Time (Dijkstra)
- Cheapest Flights Within K Stops (Bellman-Ford)
- Number of Connected Components / Redundant Connection (Union-Find)
- Min Cost to Connect All Points (MST)
- Critical Connections in a Network (bridges)
- Strongly Connected Components / 2-SAT (Tarjan / Kosaraju)

### Flows & matching — [max-flow & matching](2-algorithms/13-max-flow-and-matching.ipynb)
- Maximum Flow / Minimum Cut (Dinic)
- Maximum Bipartite Matching (Hopcroft-Karp / Kuhn)
- Assignment / Campus Bikes (Hungarian, min-cost flow)
- Minimum Cost to Connect Sticks via flow
- Reconstruct Itinerary (Eulerian path, Hierholzer)
- Is Graph Bipartite?

### Strings & suffix structures — [string algorithms](2-algorithms/14-string-algorithms.ipynb) · [suffix structures](2-algorithms/15-suffix-structures.ipynb) · [suffix automaton & tree](2-algorithms/16-suffix-automaton-and-tree.ipynb)
- Implement strStr() (KMP)
- Repeated Substring Pattern (prefix function)
- Longest Palindromic Substring (Manacher)
- Longest Repeated Substring (suffix array + LCP)
- Stream of Characters (Aho-Corasick)
- Number of Distinct Substrings / Longest Common Substring (suffix automaton)

### Binary search — [searching](2-algorithms/02-searching.ipynb)
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Koko Eating Bananas (binary search on the answer)
- Median of Two Sorted Arrays
- Split Array Largest Sum

### Heaps / priority queue — [heaps](1-data-structures/04-heaps.ipynb)
- Find Median from Data Stream (two heaps)
- Task Scheduler
- Meeting Rooms II
- K Closest Points to Origin

### Bit manipulation — [bit manipulation](2-algorithms/17-bit-manipulation.ipynb)
- Single Number / Single Number II
- Number of 1 Bits
- Counting Bits
- Subsets (bitmask)
- Sum of Two Integers (no `+`)
- Maximum XOR of Two Numbers in an Array (binary trie)

### Greedy — [greedy](2-algorithms/18-greedy.ipynb)
- Jump Game / Jump Game II
- Non-overlapping Intervals (activity selection)
- Gas Station
- Task Scheduler
- Huffman / Minimum Cost to merge

### Number theory, combinatorics & advanced math — [number theory](2-algorithms/19-number-theory.ipynb) · [combinatorics](2-algorithms/20-combinatorics.ipynb) · [advanced number theory](2-algorithms/21-advanced-number-theory.ipynb) · [fft](2-algorithms/22-fft-and-polynomials.ipynb)
- Count Primes (sieve)
- Pow(x, n) / Super Pow (modular exponentiation)
- Unique Paths / Pascal's Triangle (combinations)
- Climbing Stairs with huge n (matrix exponentiation)
- Nim Game / Stone Game (Sprague-Grundy)
- Multiply / Add Strings (and FFT/NTT convolution for big-int)

### Computational geometry — [computational geometry](2-algorithms/23-computational-geometry.ipynb)
- Convex Hull / Erect the Fence
- Max Points on a Line (orientation)
- Check if Point Is Inside a Polygon (ray casting)
- Minimum Area Rectangle
- K Closest Points to Origin / closest pair

### Sqrt decomposition & offline — [sqrt decomposition & offline](2-algorithms/24-sqrt-decomposition-and-offline.ipynb)
- Range Sum Query — Mutable (sqrt decomposition vs Fenwick)
- Count of distinct elements in subarrays (Mo's algorithm)
- Range mode query
- Offline range queries sorted by right endpoint

### Randomized — [randomized algorithms](2-algorithms/25-randomized-algorithms.ipynb)
- Random Pick with Weight
- Linked List Random Node (reservoir, k=1)
- Random Pick Index (reservoir sampling)
- Shuffle an Array (Fisher-Yates)
- Implement Rand10() Using Rand7()

### Tries — [tries](1-data-structures/08-tries.ipynb)
- Implement Trie (Prefix Tree)
- Word Search II
- Design Add and Search Words
- Replace Words / Longest Word in Dictionary
- Maximum XOR of Two Numbers in an Array (binary trie)

---

## 6. Python stdlib toolkit — reach for the builtin

The C-level tool that usually beats hand-rolling, and the notebook that covers it.

| Tool | Gives you | Notebook |
|---|---|---|
| `bisect.bisect_left/right`, `insort` | binary search & sorted insert into a list (O(log n) find) | [searching](2-algorithms/02-searching.ipynb) |
| `heapq.heappush/heappop`, `heapify` | binary heap / priority queue (O(log n) push-pop, O(n) build) | [heaps](1-data-structures/04-heaps.ipynb) |
| `heapq.nsmallest/nlargest` | top-k without a full sort (O(n log k)) | [selection](2-algorithms/03-selection.ipynb) · [top-k](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| `heapq.merge` | lazy, memory-light k-way merge | [top-k & k-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| `collections.deque` | O(1) push/pop both ends; BFS queue; monotonic queue; sliding-window DP | [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb) |
| `collections.Counter` | tally / frequencies / `most_common(k)` | [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) |
| `collections.defaultdict` | auto-default on missing key (adjacency lists, grouping) | [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) |
| `collections.OrderedDict` | `move_to_end` + `popitem` → an LRU cache | [lru cache](1-data-structures/12-lru-cache.ipynb) |
| `itertools.product/combinations/permutations` | combinatorial generation without recursion | [combinatorial generation](3-patterns/07-combinatorial-generation.ipynb) |
| `itertools.accumulate` | running sums / prefix arrays (and min/max/products) | [prefix sums](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) |
| `functools.cache` / `lru_cache` | memoization → exponential recursion collapses to linear | [recursion & backtracking](2-algorithms/04-recursion-and-backtracking.ipynb) · [dp](2-algorithms/06-dynamic-programming.ipynb) |
| `functools.reduce` | fold an iterable to one value | [number theory](2-algorithms/19-number-theory.ipynb) |
| `statistics.median` / `median_low` / `mean` | order statistics & averages, readable intent | [selection](2-algorithms/03-selection.ipynb) |
| `fractions.Fraction` | exact rational arithmetic (no float error) | [computational geometry](2-algorithms/23-computational-geometry.ipynb) · [number theory](2-algorithms/19-number-theory.ipynb) |
| `math.gcd/lcm`, `comb/perm/factorial`, `isqrt` | number theory & combinatorics, exact (arbitrary-precision int) | [number theory](2-algorithms/19-number-theory.ipynb) · [combinatorics](2-algorithms/20-combinatorics.ipynb) |
| `pow(b, e, m)` / `pow(a, -1, m)` | fast modular exponentiation / modular inverse | [number theory](2-algorithms/19-number-theory.ipynb) |
| `numpy.fft` / `numpy.convolve` | C-level FFT & convolution (auto O(n log n) for large n) | [fft & polynomials](2-algorithms/22-fft-and-polynomials.ipynb) |
| `random.shuffle` / `random.sample` | unbiased Fisher-Yates shuffle / sampling | [randomized algorithms](2-algorithms/25-randomized-algorithms.ipynb) |
| `array` | packed C-typed numbers, far less memory than `list` | [arrays](1-data-structures/01-arrays.ipynb) |
| `int` bitmask + `n.bit_count()`/`bit_length()` | a small fast set; subset DP; flags; nim-sum | [bit manipulation](2-algorithms/17-bit-manipulation.ipynb) |
| `sortedcontainers.SortedList` (3rd-party) | ordered container, ~O(log n) lookup **and** insert | [trees](1-data-structures/07-trees.ipynb) · [probabilistic structures](1-data-structures/13-probabilistic-structures.ipynb) |

<sub>And the through-line ([cpython-cost-model](0-foundations/03-cpython-cost-model.ipynb)): push the loop into C — a builtin over an iterable beats a pure-Python `for`, a comprehension beats `.append` in a loop, `"".join` beats `+=`, and numpy beats them all on large numeric arrays.</sub>
