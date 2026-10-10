# Eduqas
Eduqas (part of WJEC) offers a GCSE and an A Level in Computer Science in England.

## GCSE
| Component   | What it covers                       | Format                                  | Length            | Marks | Weighting |
|-------------|--------------------------------------|-----------------------------------------|-------------------|-------|-----------|
| Component 1 | Understanding computer science       | Written                                 | 1 hour 45 minutes | 100   | 50%       |
| Component 2 | Computer programming                 | On-screen, in Python 3, plus a word processor | 2 hours     | 80    | 50%       |

- Eduqas releases a _scenario_ (a list of requirements) on 1 September of the year before the exam, which you'll work on in advance.
- In the exam itself, you're given a prototype Python program to use, evaluate and change, and you answer some questions in a word-processed document.
- Eduqas says that "only the standard Python 3 download should be used with no additional libraries installed", so you can't rely on third-party packages like `numpy` or `matplotlib` ([Lesson 14](../lessons/14-packages)).
- The specification also mentions graphical user interfaces built using Python's built-in libraries (i.e. `tkinter`), which these lessons don't cover.
- **Which lessons?** [Lessons 0 to 10](../README.md#fundamentals), plus [Lesson 13](../lessons/13-dictionaries-and-sets), because the specification asks you to use "lists, tuples and dictionaries".

## A Level
| Component   | What it covers                                                | Format     | Length            | Weighting |
|-------------|---------------------------------------------------------------|------------|-------------------|-----------|
| Component 1 | Programming and system development                            | Written    | 2 hours 45 minutes | 40%      |
| Component 2 | Computer architecture, data, communication and applications  | Written    | 2 hours 45 minutes | 40%      |
| Component 3 | A programmed solution to a problem (non-exam assessment)      | Coursework | —                 | 20%       |

### How the A Level programming content maps onto these lessons
| Topic                                                                           | Lessons                                                                 |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Arrays (up to three dimensions) and records                                     | [4](../lessons/04-lists), [5](../lessons/05-2d-lists) and [15](../lessons/15-type-hints-and-dataclasses) |
| Stacks and queues, including "using pointers and arrays"                        | [16](../lessons/16-recursion-stacks-and-queues)                         |
| Linked lists, including "using pointers and arrays"                             | [18](../lessons/18-linked-lists) (see "Linked lists in arrays")         |
| Trees                                                                           | [19](../lessons/19-binary-search-trees)                                 |
| Hash tables                                                                     | [20](../lessons/20-hash-tables-and-sets)                                |

## Sources
- [GCSE Computer Science specification](https://www.eduqas.co.uk/media/tf3bvmxe/eduqas-gcse-computer-science-specification-10-02-2020.pdf) (teaching from 2020), sections 2.2 and 3.2.
- [A Level Computer Science specification](https://www.eduqas.co.uk/media/zhpapwjj/eduqas-a-level-computer-science-spec-from-2015-e-24-01-2020.pdf) (teaching from 2015).

---
[Exam board notes](README.md) | [Contents](../README.md)
