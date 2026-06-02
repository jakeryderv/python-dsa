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
```

> An `algorithms/` folder will follow later (sorting, searching, recursion/DP, graph traversals).

## Notebooks

| Topic | Status | Covers |
|---|:---:|---|
| [arrays](data-structures/arrays.ipynb) | ✅ | `list`, `tuple`, `array`, `numpy`, `deque`; dynamic-array growth strategy |
| [strings](data-structures/strings.ipynb) | ✅ | `str`, PEP 393 char-width, interning, the `+=` trap, `bytes`/`bytearray` |
| [dict & set](data-structures/dictionaries-and-sets.ipynb) | ✅ | hash tables, open addressing, compact-dict layout, resizing, hashing |
| [heaps](data-structures/heaps.ipynb) | ✅ | `heapq` binary heap, sift up/down, `heapify` is O(n) |
| [linked lists](data-structures/linked-lists.ipynb) | ✅ | singly/doubly from scratch; why CPython avoids them; `deque`/`OrderedDict` |
| [stacks & queues](data-structures/stacks-and-queues.ipynb) | ✅ | LIFO/FIFO; the `list`-as-queue O(n²) trap; `deque(maxlen)`; `queue` module |
| trees | 📋 | BST, traversals, `bisect` on sorted lists, tries |
| graphs | 📋 | adjacency list vs matrix, BFS/DFS |

## Running

Uses [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run jupyter lab                     # interactive editing

# execute a notebook in place (refresh its saved outputs):
uv run jupyter nbconvert --to notebook --execute --inplace data-structures/<name>.ipynb
```

## House style

- Every nontrivial claim gets a **runnable demo that proves it** (`sys.getsizeof`, `id`, timing).
- Each notebook ends with a **when-to-use table** and a **Big-O cheat-sheet**.
- Start new topics from `_template.ipynb` to keep the structure consistent.
