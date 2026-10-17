# Stage 5: Loops

Repeat work, traverse sequences, search for values, and build running results.

## Concepts in this stage

`while`, `for`, counters, lists and tuples, `range()`, `break`, `continue`, `pass`, and accumulators.

## Read and run in this order

| Order | File | What I am practicing | Try or observe |
| --- | --- | --- | --- |
| 1 | [loops.py](loops.py) | Repeat a greeting with a while loop. | Predict how many lines print and why the counter changes. |
| 2 | [prac14.py](prac14.py) | Count upward and downward with while. | The script prints numbered greetings from 1 to 100, then 100 to 1. |
| 3 | [prac15.py](prac15.py) | Build a multiplication table with while. | Enter `7` to print its first ten multiples. |
| 4 | [prac16.py](prac16.py) | Traverse a list with indexing and while. | The list is `[1, 2, 4, 16, 25, 36, 49]`; inspect each actual value. |
| 5 | [prac17.py](prac17.py) | Search a tuple and stop at the first match. | Enter `25` for a match at index 4. Earlier nonmatches each print a message. |
| 6 | [forloop.py](forloop.py) | Traverse a tuple with for. | Compare direct iteration with the indexed while version. |
| 7 | [prac18.py](prac18.py) | Search a list with for. | The current search finds 36 at index 5; it continues iterating afterward. |
| 8 | [range.py](range.py) | Explore range(stop), range(start, stop), and step. | Predict each sequence, remembering that stop is excluded. |
| 9 | [range2.py](range2.py) | Generate even and odd numbers using a step. | Compare the starting values and the step of 2. |
| 10 | [prac19.py](prac19.py) | Count backward with range. | The output runs from 100 down to 1. |
| 11 | [prac20.py](prac20.py) | Build a multiplication table with for. | Enter `7` and compare with `prac15.py`. |
| 12 | [break_continue.py](break_continue.py) | Skip odd numbers with continue. | The current example prints even numbers from 2 through 14; `break` appears in `prac17.py`. |
| 13 | [pass.py](pass.py) | Use pass as a placeholder statement. | The loop has no action; a name prints after it. |
| 14 | [prac21.py](prac21.py) | Sum integers from 1 through n with while. | Enter `5` for 15, or `0` for 0. Use nonnegative integers. |
| 15 | [prac22.py](prac22.py) | Calculate a factorial with for. | Enter `5` for 120, or `0` for 1. Negative inputs need validation. |

## Run an example

From the repository root:

```powershell
python lessons/05-loops/loops.py
```

Run each file separately. Enter values when a prompt appears. Predict the output, run it, and then change one value to understand the result.

## Reflection prompts

- What did the program do, and which line caused that behavior?
- What changed when I used another input or value?
- What question or improvement should I record in my [journal](../../docs/LEARNING_JOURNAL.md)?

[Previous: Collections](../04-collections/README.md) · [Learning path](../../README.md) · [Next steps](../../docs/ROADMAP.md)
