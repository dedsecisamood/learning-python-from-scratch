# My Python learning journal

I am Siam, and this repository collects my early Python notes and practice scripts. I am organizing my work so I can follow the ideas step by step and return to examples when I need them.

The stages below describe what is present in my files. They are a suggested study order, not a claim about when I wrote each exercise or which topics I have mastered.

## 2026-10-17 — Organizing my learning journey

I collected my existing Python scripts into five lesson folders and added documentation for finding and running them. The original scripts and filenames are preserved, including rough edges and incomplete work.

**The original exercise dates are unknown.** This date records the repository organization, not the dates I learned or completed these topics.

### Stage 1 — Foundations

My [foundation examples](../lessons/01-foundations/) start with printing, assigning variables, basic types, keyboard input, arithmetic, and calculating an average. Files such as `helloworld.py`, `datatype.py`, `input.py`, `excersice1.py`, `variable2prac.py`, and `prac1.py` provide the starting material.

`operators.py` is an empty placeholder. In `datatype.py`, the variables are defined, but the `print(type(...))` calls are commented out, so running it produces no output. These files represent work to revisit, not completed demonstrations of every concept.

### Stage 2 — Strings

My [string examples](../lessons/02-strings/) cover concatenation, length, indexing, slicing, negative indices, and methods such as `endswith`, `capitalize`, `replace`, `find`, and `count`. The exercises include extracting pieces of my name and counting dollar signs in `prac2.py`.

### Stage 3 — Decisions

My [decision examples](../lessons/03-decisions/) use `if`, `elif`, and `else` for age and traffic-light examples, grade thresholds, even and odd numbers, divisibility, and comparing numbers. `prac6.py` includes separate branches for divisibility by both 3 and 7, by either number alone, or by neither.

The grade example has no bounds check for marks. The greatest-number exercises choose a single position when values tie; they do not explain that multiple inputs can share the greatest value.

### Stage 4 — Collections

My [collection examples](../lessons/04-collections/) introduce dictionaries, nested dictionaries, dictionary methods, sets, union, intersection, and duplicate removal. `prac12.py` builds a subject-to-marks dictionary from input. `prac13.py` compares `9` and `9.0` and shows that a set keeps only one of those equal values.

In `prac_10.py`, the adjacent string literals for the `table` entry become one string automatically. This is valid Python, but I should revisit the representation if I want separate definitions. In `prac11.py`, the subject string `"Python "` includes a trailing space.

### Stage 5 — Loops

My [loop examples](../lessons/05-loops/) cover `while`, `for`, `range`, counters, `continue`, `break`, and `pass`. Practice scripts include multiplication tables, list and tuple traversal, searches, a running total, and factorial. `prac15.py` and `prac20.py` offer a useful comparison: the same multiplication-table task with two different loop types.

`prac17.py` stops at the first match and prints a message for every preceding mismatch; it has no overall summary when the requested number is absent. `prac21.py` returns `0` for negative input, and `prac22.py` returns `1` for negative input. Those exercises need a defined input domain and validation before I treat them as general-purpose calculations.

## Notes I want to revisit

These are observations from the current source, not fixes already completed:

- `variable2prac.py` calculates `a - b`, while its output label says `a+b`.
- `operators.py` needs actual operator examples; `datatype.py` needs its output enabled if I want to inspect the types.
- `gradesystem.py` needs an explicit allowed marks range.
- `prac4.py` and `prac7.py` need an explicit decision about tied greatest values.
- `prac_10.py` needs a review of how the definitions should be stored.
- `prac17.py` needs a clear final result when a search fails.
- `prac21.py` and `prac22.py` need nonnegative input handling; scripts that call `int()` or `float()` also need a plan for invalid text.
- Several examples use names such as `str`, `list`, `dict`, and `sum`, which hide Python built-ins. More descriptive names would make later revisions easier to read.

The practice-number sequence skips `prac8.py` and `prac9.py`; those files were not present in the original collection. I have not added invented exercises to fill the gap.

## Template for my next entry

Copy this template when I have a real study session to record. Use the actual date and only record what I did or observed.

```text
## YYYY-MM-DD — Topic

Files I worked on:
What I tried:
Input and output I observed:
What I changed or understood from that example:
What is still unclear:
My next step:
```

My [roadmap](ROADMAP.md) lists possible next steps. Its unchecked items are plans, not completed work.
