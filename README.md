# Learning Python from Scratch

My Python learning journey, one small program at a time.

I'm Siam, and this repository brings together my early Python practice: greetings, variables, strings, decisions, collections, and loops. Each stage includes the scripts I worked on, an order to read them in, and small experiments to try next.

These are learning exercises with rough edges to revisit. The original Python contents and filenames are preserved, including an empty operator-practice placeholder.

## Start here

1. Open [Stage 1: Foundations](lessons/01-foundations/README.md).
2. Read each stage's README and run its examples in the listed order.
3. Change an input or value, predict the result, and compare it with the output.
4. Record what happened in the [learning journal](docs/LEARNING_JOURNAL.md).

## My learning path

| Stage | Focus | Files | Guide |
| --- | --- | ---: | --- |
| 1 | Foundations | 7 | [Foundations](lessons/01-foundations/README.md) |
| 2 | Strings | 5 | [Strings](lessons/02-strings/README.md) |
| 3 | Decisions | 8 | [Decisions](lessons/03-decisions/README.md) |
| 4 | Collections | 10 | [Collections](lessons/04-collections/README.md) |
| 5 | Loops | 15 | [Loops](lessons/05-loops/README.md) |

There are **45 original Python files**: 44 contain code and `operators.py` is an empty placeholder. Stage order follows prerequisites; it does not claim exact dates or completion of every topic.

## Run an example

Use Python 3. There are no third-party dependencies to install.

From the repository folder:

```powershell
python --version
python lessons/01-foundations/helloworld.py
python lessons/03-decisions/prac5.py
```

For the second exercise, enter `49` when prompted to check a multiple of seven. Run one script at a time. Files using `input()` wait for keyboard input, and a few scripts intentionally have no output. In Windows, `py` can replace `python` if that is your configured launcher.

## Repository layout

```text
lessons/
  01-foundations/    First output, types, arithmetic, and input
  02-strings/        Text, indexing, slices, and methods
  03-decisions/      Conditions, comparisons, and divisibility
  04-collections/    Dictionaries, nested data, and sets
  05-loops/          Repetition, search, ranges, sums, and factorials
docs/
  FILE_INDEX.md         Where each original file lives
  LEARNING_JOURNAL.md   Evidence from my practice and future entries
  ROADMAP.md            Topics and improvements to work on next
```

## Journey notes

- [Learning journal](docs/LEARNING_JOURNAL.md): what the existing exercises show and mistakes to revisit.
- [Roadmap](docs/ROADMAP.md): future practice, from functions to small projects.
- [File index](docs/FILE_INDEX.md): find an exercise by its original filename.

The repository was organized on **17 October 2026**. Original exercise dates are unknown. The missing practice numbers 8 and 9 have no files in this collection; they are not marked complete.

## Keep the journey going

Add each new exercise to the relevant stage, or create a new numbered stage when starting a new topic. Update the index and add a dated journal entry with the problem, what you tried, what happened, and what to revisit.

After a practice session, save the changes with a message that describes the work:

```powershell
git add lessons docs
git commit -m "Practice functions with a temperature converter"
git push
```

Use a commit message that matches the changes actually made.
