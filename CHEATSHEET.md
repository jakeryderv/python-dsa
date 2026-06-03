# DSA Cheat-Sheet — The Whole Series at a Glance

A single navigable reference and study plan for the **39-notebook** Python DSA series (with a CPython-internals angle). It rolls up the per-notebook *"When to use what"* and *"Complexity cheat-sheet"* cells into one place: a decision guide for *"I have problem X, what do I reach for?"*, master complexity tables, a pattern quick-reference, a study plan of canonical practice problems, and a Python stdlib toolkit.

Every complexity below is taken straight from the per-notebook tables — each row links back to its source notebook, so use this to skim and jump in. Notation throughout: `n` = element count, `V`/`E` = vertices/edges, `m` = pattern length, `L` = key length, `k` = a small bound (top-k, prefix matches), `W` = numeric capacity. Entries are **worst case** unless marked *avg* / *amortized*.

**The meta-rule (from [cpython-cost-model](0-foundations/03-cpython-cost-model.ipynb)):** pick the algorithm *class* with [big-o](0-foundations/01-big-o.ipynb) first, then shrink the constant with the cost model. The less time your data spends as per-element Python objects in an interpreted loop, the faster you go.

---

## Series map

| Tier | Notebooks |
|---|---|
| **0 — Foundations** | [big-o](0-foundations/01-big-o.ipynb) · [python-idioms](0-foundations/02-python-idioms-for-dsa.ipynb) · [cpython-cost-model](0-foundations/03-cpython-cost-model.ipynb) |
| **1 — Data structures** | [arrays](1-data-structures/01-arrays.ipynb) · [strings](1-data-structures/02-strings.ipynb) · [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) · [heaps](1-data-structures/04-heaps.ipynb) · [linked lists](1-data-structures/05-linked-lists.ipynb) · [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb) · [trees](1-data-structures/07-trees.ipynb) · [tries](1-data-structures/08-tries.ipynb) · [graphs](1-data-structures/09-graphs.ipynb) · [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) · [lru cache](1-data-structures/11-lru-cache.ipynb) · [probabilistic structures](1-data-structures/12-probabilistic-structures.ipynb) |
| **2 — Algorithms** | [sorting](2-algorithms/01-sorting.ipynb) · [searching](2-algorithms/02-searching.ipynb) · [selection](2-algorithms/03-selection.ipynb) · [recursion & backtracking](2-algorithms/04-recursion-and-backtracking.ipynb) · [dynamic programming](2-algorithms/05-dynamic-programming.ipynb) · [graph algorithms](2-algorithms/06-graph-algorithms.ipynb) · [advanced graph algorithms](2-algorithms/07-advanced-graph-algorithms.ipynb) · [string algorithms](2-algorithms/08-string-algorithms.ipynb) · [suffix structures](2-algorithms/09-suffix-structures.ipynb) · [bit manipulation](2-algorithms/10-bit-manipulation.ipynb) · [greedy](2-algorithms/11-greedy.ipynb) · [number theory](2-algorithms/12-number-theory.ipynb) · [computational geometry](2-algorithms/13-computational-geometry.ipynb) |
| **3 — Patterns** | [two pointers](3-patterns/01-two-pointers.ipynb) · [sliding window](3-patterns/02-sliding-window.ipynb) · [prefix sums & diff arrays](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) · [monotonic stack/queue](3-patterns/04-monotonic-stack-and-queue.ipynb) · [top-k & k-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb) · [cyclic sort](3-patterns/06-cyclic-sort.ipynb) · [combinatorial generation](3-patterns/07-combinatorial-generation.ipynb) · [coordinate compression](3-patterns/08-coordinate-compression.ipynb) · [meet in the middle](3-patterns/09-meet-in-the-middle.ipynb) · [sweep line](3-patterns/10-sweep-line.ipynb) · [grid & matrix traversal](3-patterns/11-grid-and-matrix-traversal.ipynb) |

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
| Bounded LRU cache of function results | `functools.lru_cache` / `OrderedDict` | [lru cache](1-data-structures/11-lru-cache.ipynb) |

### Priorities, order statistics, ranges

| I want… | Reach for | Notebook |
|---|---|---|
| Repeatedly pull the min/max while inserting | `heapq` on a `list` (O(log n) push/pop) | [heaps](1-data-structures/04-heaps.ipynb) |
| A priority queue (Dijkstra, scheduling) | `heapq` with `(priority, count, item)` tuples | [heaps](1-data-structures/04-heaps.ipynb) |
| **k-th smallest / median (single rank)** | quickselect (O(n) avg); `statistics.median` for clarity | [selection](2-algorithms/03-selection.ipynb) |
| **The k smallest/largest items, k ≪ n** | `heapq.nsmallest` / `nlargest` (O(n log k)) | [selection](2-algorithms/03-selection.ipynb) · [top-k](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| Worst-case O(n) selection guarantee | median-of-medians (BFPRT) | [selection](2-algorithms/03-selection.ipynb) |
| Merge k sorted lists/streams lazily | `heapq.merge` (frontier heap, O(N log k)) | [top-k & k-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| **Many range-sum queries, static array** | prefix sums (O(1) query) | [prefix sums](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) |
| Many range-updates, read once | difference array (O(1) per update) | [prefix sums](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) |
| **Point update + range sum, interleaved** | Fenwick / BIT (O(log n) both) | [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) |
| Point update + range min/max/gcd | segment tree (any associative op) | [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) |
| **Range update + range query** | segment tree **+ lazy propagation** | [fenwick & segment trees](1-data-structures/10-fenwick-and-segment-trees.ipynb) |

### Searching & sorting

| I want… | Reach for | Notebook |
|---|---|---|
| Sort anything | `sorted()` / `list.sort()` (Timsort, stable, O(n log n)) | [sorting](2-algorithms/01-sorting.ipynb) |
| Sort bounded-range integers, fastest | counting / radix sort (O(n), beats the comparison floor) | [sorting](2-algorithms/01-sorting.ipynb) |
| Find / count in sorted data | `bisect` (O(log n)) | [searching](2-algorithms/02-searching.ipynb) |
| Boundary of a monotonic condition | binary search **on the answer** | [searching](2-algorithms/02-searching.ipynb) |
| Keep a list sorted as you insert | `bisect.insort` (O(log n) find, O(n) shift) | [sorting](2-algorithms/01-sorting.ipynb) |

### Strings & substring search

| I want… | Reach for | Notebook |
|---|---|---|
| Just `pattern in text` in Python | built-in `in` / `.find` (C `fastsearch`) | [string algorithms](2-algorithms/08-string-algorithms.ipynb) |
| **One pattern, understood from scratch** | KMP (O(n+m), prefix function) | [string algorithms](2-algorithms/08-string-algorithms.ipynb) |
| Rolling hash / fingerprinting / 2D | Rabin-Karp | [string algorithms](2-algorithms/08-string-algorithms.ipynb) |
| **Many substring queries on a fixed text** | suffix array (+ LCP for repeats) | [suffix structures](2-algorithms/09-suffix-structures.ipynb) |
| **Many patterns, one scan** | Aho-Corasick (O(\|T\| + matches)) | [suffix structures](2-algorithms/09-suffix-structures.ipynb) |
| Build a big string from pieces | `list` + `"".join` (never the `+=` cliff) | [strings](1-data-structures/02-strings.ipynb) |
| A mutable byte buffer | `bytearray` | [strings](1-data-structures/02-strings.ipynb) |

### Graphs & shortest paths

| Shortest path with… | Use | Cost | Notebook |
|---|---|:---:|---|
| **No weights** | BFS | O(V+E) | [graphs](1-data-structures/09-graphs.ipynb) |
| **Non-negative weights** | Dijkstra (`heapq`) | O((V+E) log V) | [graph algorithms](2-algorithms/06-graph-algorithms.ipynb) |
| **Negative weights** | Bellman-Ford | O(V·E) | [graph algorithms](2-algorithms/06-graph-algorithms.ipynb) |
| **All pairs** | Floyd-Warshall | O(V³) | [graph algorithms](2-algorithms/06-graph-algorithms.ipynb) |
| **One goal + a heuristic** | A\* | O((V+E) log V), fewer nodes | [graph algorithms](2-algorithms/06-graph-algorithms.ipynb) |

| Graph goal | Use | Notebook |
|---|---|---|
| Order tasks with dependencies | topological sort (Kahn / DFS) | [graphs](1-data-structures/09-graphs.ipynb) |
| "Same component?" / incremental connectivity | Union-Find (~O(1) amortized) | [graph algorithms](2-algorithms/06-graph-algorithms.ipynb) |
| Minimum spanning tree | Kruskal (sparse) / Prim (dense) | [graph algorithms](2-algorithms/06-graph-algorithms.ipynb) |
| SCC / 2-SAT / cycle in a digraph | Kosaraju or Tarjan | [advanced graph algorithms](2-algorithms/07-advanced-graph-algorithms.ipynb) |
| Single points of failure (links/routers) | bridges / articulation points | [advanced graph algorithms](2-algorithms/07-advanced-graph-algorithms.ipynb) |
| Throughput / min cut | Edmonds-Karp max-flow | [advanced graph algorithms](2-algorithms/07-advanced-graph-algorithms.ipynb) |
| Largest set of disjoint pairings | Kuhn bipartite matching | [advanced graph algorithms](2-algorithms/07-advanced-graph-algorithms.ipynb) |

### "Is this input actually too slow?" & scale tricks

| Situation | Reach for | Notebook |
|---|---|---|
| **"Is this big input actually O(n²)?"** | the cost model — measure, hoist lookups, drop to C/numpy | [cpython-cost-model](0-foundations/03-cpython-cost-model.ipynb) |
| Web-scale "have I seen this?" with rare false-yes OK | Bloom filter | [probabilistic structures](1-data-structures/12-probabilistic-structures.ipynb) |
| Distinct count over a huge stream | HyperLogLog | [probabilistic structures](1-data-structures/12-probabilistic-structures.ipynb) |
| Approximate heavy-hitters / top-K | count-min sketch | [probabilistic structures](1-data-structures/12-probabilistic-structures.ipynb) |
| Values up to 10⁹ but only k distinct | coordinate compression → index by value | [coordinate compression](3-patterns/08-coordinate-compression.ipynb) |
| Exponential search, n ≈ 30–45 | meet in the middle (2ⁿ → 2·2^(n/2)) | [meet in the middle](3-patterns/09-meet-in-the-middle.ipynb) |
| Overlapping subproblems + optimal substructure | dynamic programming | [dynamic programming](2-algorithms/05-dynamic-programming.ipynb) |
| Locally-best choice + provable greedy property | greedy (sort + one pass) | [greedy](2-algorithms/11-greedy.ipynb) |
| A small fixed universe needing raw speed | `int` bitmask as a set | [bit manipulation](2-algorithms/10-bit-manipulation.ipynb) |

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
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(log n + k) | — |
| BST (degenerate) | O(n) | O(n) | O(n) | O(n) | O(n) | — |
| Sorted list + `bisect` | O(log n) | O(n)† | O(n) | O(1) at ends | O(log n + k) | O(n log n) |
| Trie | O(L) | O(L) | O(L) | — | prefix O(L+k) | — |
| Prefix sum (static) | — | O(n) rebuild | — | — | O(1) | O(n) |
| Fenwick tree | — | O(log n) | — | — | O(log n) | O(n log n) |
| Segment tree | — | O(log n) | — | — | O(log n) | O(n) |
| Segment tree + lazy | — | O(log n) range | — | — | O(log n) | O(n) |

<sub>† O(log n) to find the spot, O(n) to shift. L = key length, k = matches.</sub>

### Probabilistic structures ([probabilistic structures](1-data-structures/12-probabilistic-structures.ipynb))

| Structure | Space | add | query | Error direction |
|---|:---:|:---:|:---:|---|
| Bloom filter | m bits (~1.44·log₂(1/p)·n) | O(k) | O(k) | false positives only; **no false negatives** |
| Skip list | O(n) (~2 ptrs/node) | O(log n) exp | O(log n) exp | **exact** (randomized balance) |
| Count-min sketch | w·d counters | O(d) | O(d) | overestimates only; **never undercounts** |
| HyperLogLog | M registers (~M bytes) | O(1) | O(M) | ±1.04/√M relative |

### LRU cache ([lru cache](1-data-structures/11-lru-cache.ipynb))

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

<sub>k = value range, d = digits, b = radix base.</sub>

### Searching & selection ([searching](2-algorithms/02-searching.ipynb), [selection](2-algorithms/03-selection.ipynb))

| Method | Best | Average | Worst | Space | Precondition |
|---|:---:|:---:|:---:|:---:|---|
| Linear search (`in`, `.index`) | — | O(n) | O(n) | O(1) | none |
| Binary search / `bisect` | — | O(log n) | O(log n) | O(1) | sorted |
| Hash lookup (`set`/`dict`) | — | O(1) avg | O(n) | — | hashable keys |
| Binary search on the answer | — | O(log R · P) | O(log R · P) | — | monotonic predicate |
| `min` / `max` | O(n) | O(n) | O(n) | O(1) | — |
| Quickselect (random pivot) | O(n) | O(n) | O(n²) | O(1) | — |
| Median-of-medians (BFPRT) | O(n) | O(n) | O(n) | O(n) | — |
| `heapq.nsmallest`/`nlargest(k)` | O(n) | O(n log k) | O(n log k) | O(k) | — |
| `sorted(xs)[k]` | O(n) | O(n log n) | O(n log n) | O(n) | — |

<sub>R = range size, P = predicate cost.</sub>

### Dynamic programming ([dynamic programming](2-algorithms/05-dynamic-programming.ipynb))

| Problem | State | Time | Space (naive → rolled) |
|---|---|:---:|:---:|
| Fibonacci | `n` | O(n) | O(n) → O(1) |
| Coin change | amount | O(amount × #coins) | O(amount) |
| Longest common subsequence | `(i, j)` | O(m·n) | O(m·n) → O(min(m,n)) |
| Edit distance | `(i, j)` | O(m·n) | O(m·n) → O(min(m,n)) |
| 0/1 knapsack | `(item, cap)` | O(n·W) | O(n·W) → O(W) |
| Longest increasing subseq. | `i` / patience | O(n²) or O(n log n) | O(n) |

<sub>W = capacity (knapsack is pseudo-polynomial — scales with the numeric W).</sub>

### Graph algorithms ([graph algorithms](2-algorithms/06-graph-algorithms.ipynb), [advanced](2-algorithms/07-advanced-graph-algorithms.ipynb))

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
| Kosaraju SCC | strongly connected components | O(V+E) | O(V+E) |
| Tarjan SCC | strongly connected components | O(V+E) | O(V) |
| Bridges / articulation | edges/vertices that disconnect | O(V+E) | O(V) |
| Edmonds-Karp | max-flow / min-cut | O(V·E²) | O(V+E) |
| Kuhn | maximum bipartite matching | O(V·E) | O(V+E) |
| Dinic (named) | max-flow, faster | O(V²·E) | O(V+E) |
| Hopcroft-Karp (named) | bipartite matching, faster | O(E·√V) | O(V+E) |

### String & suffix algorithms ([string algorithms](2-algorithms/08-string-algorithms.ipynb), [suffix structures](2-algorithms/09-suffix-structures.ipynb))

| Algorithm | Preprocess / build | Search / query | Space |
|---|:---:|:---:|:---:|
| Naive search | — | O(n·m) | O(1) |
| KMP | O(m) | O(n) | O(m) |
| Rabin-Karp | O(m) | O(n) avg, O(n·m) worst | O(1) |
| CPython `fastsearch` | O(m) | O(n) | O(1) |
| Z-array | O(n) | O(n) per `P+sep+T` | O(n) |
| Suffix array (prefix-doubling) | O(n log² n) | O(m log n) | O(n) |
| Suffix array (SA-IS, named) | O(n) | O(m log n) | O(n) |
| LCP array (Kasai) | O(n) given SA | O(1) lookup | O(n) |
| Aho-Corasick | O(M) | O(n + z) scan | O(M·Σ) |
| Suffix tree (named) | O(n) | O(m) | O(n) |

<sub>M = total pattern length, z = matches, Σ = alphabet size.</sub>

### Number theory & geometry ([number theory](2-algorithms/12-number-theory.ipynb), [computational geometry](2-algorithms/13-computational-geometry.ipynb))

| Task | Algorithm | Complexity | Builtin |
|---|---|:---:|---|
| GCD / LCM | Euclid | O(log n) | `math.gcd` / `math.lcm` |
| All primes ≤ n | sieve of Eratosthenes | O(n log log n) | — |
| Single primality | trial division / Miller-Rabin | O(√n) / prob. | — |
| base^exp mod m | binary exponentiation | O(log exp) | `pow(b, e, m)` |
| Modular inverse | extended Euclid / Fermat | O(log m) | `pow(a, -1, m)` |
| nCk, nPk, n! | — | — | `math.comb`/`perm`/`factorial` |
| Orientation of 3 points | sign of cross product | O(1) | — |
| Segment intersection (yes/no) | four-orientation rule | O(1) | — |
| Convex hull | Andrew's monotone chain | O(n log n) | — |
| Point in polygon | ray casting (even-odd) | O(n) | — |
| Polygon area | shoelace formula | O(n) | — |
| Closest pair | divide & conquer / sweep | O(n log n) | — |

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

## 5. Practice problems by pattern — the study plan

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

### Dynamic programming — [dynamic programming](2-algorithms/05-dynamic-programming.ipynb)
- Coin Change / Coin Change II
- Longest Common Subsequence
- Edit Distance
- 0/1 Knapsack (Partition Equal Subset Sum)
- Longest Increasing Subsequence
- House Robber
- Word Break
- Unique Paths

### Graphs & graph algorithms — [graphs](1-data-structures/09-graphs.ipynb) · [graph algorithms](2-algorithms/06-graph-algorithms.ipynb)
- Course Schedule I / II (topological sort)
- Network Delay Time (Dijkstra)
- Cheapest Flights Within K Stops (Bellman-Ford)
- Number of Connected Components / Redundant Connection (Union-Find)
- Min Cost to Connect All Points (MST)
- Word Ladder (BFS)

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

### Bit manipulation — [bit manipulation](2-algorithms/10-bit-manipulation.ipynb)
- Single Number / Single Number II
- Number of 1 Bits
- Counting Bits
- Subsets (bitmask)
- Sum of Two Integers (no `+`)

### Tries — [tries](1-data-structures/08-tries.ipynb)
- Implement Trie (Prefix Tree)
- Word Search II
- Design Add and Search Words
- Replace Words / Longest Word in Dictionary

---

## 6. Python stdlib toolkit — reach for the builtin

The C-level tool that usually beats hand-rolling, and the notebook that covers it.

| Tool | Gives you | Notebook |
|---|---|---|
| `bisect.bisect_left/right`, `insort` | binary search & sorted insert into a list (O(log n) find) | [searching](2-algorithms/02-searching.ipynb) |
| `heapq.heappush/heappop`, `heapify` | binary heap / priority queue (O(log n) push-pop, O(n) build) | [heaps](1-data-structures/04-heaps.ipynb) |
| `heapq.nsmallest/nlargest` | top-k without a full sort (O(n log k)) | [selection](2-algorithms/03-selection.ipynb) · [top-k](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| `heapq.merge` | lazy, memory-light k-way merge | [top-k & k-way merge](3-patterns/05-top-k-and-k-way-merge.ipynb) |
| `collections.deque` | O(1) push/pop both ends; BFS queue; monotonic queue | [stacks & queues](1-data-structures/06-stacks-and-queues.ipynb) |
| `collections.Counter` | tally / frequencies / `most_common(k)` | [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) |
| `collections.defaultdict` | auto-default on missing key (adjacency lists, grouping) | [dicts & sets](1-data-structures/03-dictionaries-and-sets.ipynb) |
| `collections.OrderedDict` | `move_to_end` + `popitem` → an LRU cache | [lru cache](1-data-structures/11-lru-cache.ipynb) |
| `itertools.product/combinations/permutations` | combinatorial generation without recursion | [combinatorial generation](3-patterns/07-combinatorial-generation.ipynb) |
| `itertools.accumulate` | running sums / prefix arrays (and min/max/products) | [prefix sums](3-patterns/03-prefix-sums-and-difference-arrays.ipynb) |
| `functools.cache` / `lru_cache` | memoization → exponential recursion collapses to linear | [recursion & backtracking](2-algorithms/04-recursion-and-backtracking.ipynb) · [dp](2-algorithms/05-dynamic-programming.ipynb) |
| `functools.reduce` | fold an iterable to one value | [number theory](2-algorithms/12-number-theory.ipynb) |
| `math.gcd/lcm`, `comb/perm/factorial`, `isqrt` | number theory & combinatorics, exact (arbitrary-precision int) | [number theory](2-algorithms/12-number-theory.ipynb) |
| `pow(b, e, m)` / `pow(a, -1, m)` | fast modular exponentiation / modular inverse | [number theory](2-algorithms/12-number-theory.ipynb) |
| `array` | packed C-typed numbers, far less memory than `list` | [arrays](1-data-structures/01-arrays.ipynb) |
| `int` bitmask + `n.bit_count()`/`bit_length()` | a small fast set; subset DP; flags | [bit manipulation](2-algorithms/10-bit-manipulation.ipynb) |
| `sortedcontainers.SortedList` (3rd-party) | ordered container, ~O(log n) lookup **and** insert | [trees](1-data-structures/07-trees.ipynb) · [probabilistic structures](1-data-structures/12-probabilistic-structures.ipynb) |

<sub>And the through-line ([cpython-cost-model](0-foundations/03-cpython-cost-model.ipynb)): push the loop into C — a builtin over an iterable beats a pure-Python `for`, a comprehension beats `.append` in a loop, `"".join` beats `+=`, and numpy beats them all on large numeric arrays.</sub>
