# Exam board notes
The lessons in this repository are deliberately independent of any exam board: everything in them is plain Python, and it's all useful whichever course you're taking. But each exam board assesses programming in its own way, and some of them use their own _pseudocode_ in exam questions. These pages summarise the differences, how each board's pseudocode compares with Python, and which lessons cover each board's content.

> [!WARNING]
> Exam boards update their specifications and guidance from time to time. I checked everything in these notes against each board's published documents in October 2026 (each page lists its sources at the bottom), but you should always check the latest version of your own board's specification, and ask your teacher if you're unsure.

## Exam boards
| Board                                   | Qualifications                                                      |
|-----------------------------------------|---------------------------------------------------------------------|
| [AQA](aqa.md)                           | GCSE (8525), A Level (7517)                                         |
| [OCR](ocr.md)                           | GCSE (J277), A Level (H446)                                         |
| [Pearson Edexcel](pearson-edexcel.md)   | GCSE (1CP2), International GCSE (4CP0), International A Level        |
| [Eduqas](eduqas.md)                     | GCSE, A Level                                                       |
| [Cambridge International](cambridge.md) | AS & A Level (9618)                                                 |
| [IB](ib.md)                             | Diploma Programme (SL and HL)                                       |

## How is programming assessed?
### GCSE and International GCSE
| Course                                    | Programming exam                                | Format                                 | Language                                                    |
|-------------------------------------------|-------------------------------------------------|----------------------------------------|-------------------------------------------------------------|
| [AQA GCSE](aqa.md#gcse-8525)              | Paper 1: 2 hours, 90 marks, 50%                 | Written                                | Chosen when you're entered: C#, Python or VB.NET            |
| [OCR GCSE](ocr.md#gcse-j277)              | Paper 2: 1 hour 30 minutes, 80 marks, 50%       | Written                                | OCR Exam Reference Language, or "a high-level language"     |
| [Pearson Edexcel GCSE](pearson-edexcel.md#gcse-1cp2) | Paper 2: 2 hours, 75 marks, 50%      | On-screen, using an IDE                | Python 3                                                    |
| [Pearson Edexcel International GCSE](pearson-edexcel.md#international-gcse-4cp0) | Paper 2: 3 hours, 80 marks, 50% | Part written, part on-screen | Python, C# or Java                                 |
| [Eduqas GCSE](eduqas.md#gcse)             | Component 2: 2 hours, 80 marks, 50%             | On-screen, plus a word processor       | Python 3                                                    |

### A Level, International A Level and IB
| Course                                    | Programming assessment                                          | Format                                 | Language                                                    |
|-------------------------------------------|-----------------------------------------------------------------|----------------------------------------|-------------------------------------------------------------|
| [AQA A Level](aqa.md#a-level-7517)        | Paper 1: 2 hours 30 minutes, 40%, using a pre-released skeleton program; plus a project (20%) | On-screen | Chosen by your school: C#, Java, Python or VB.NET |
| [OCR A Level](ocr.md#a-level-h446)        | Paper 2: 2 hours 30 minutes, 140 marks, 40%; plus a project (20%) | Written                              | Questions use OCR's pseudocode; project in Python, a C-family language, Java or Visual Basic |
| [Pearson Edexcel International A Level](pearson-edexcel.md#international-a-level-from-2026) | Units 2 and 4: 3 hours, 80 marks, 25% each | On-screen, using an IDE | Python 3                                  |
| [Eduqas A Level](eduqas.md#a-level)       | Component 1: 2 hours 45 minutes, 40%; plus a project (20%)      | Written                                | Not specified in the specification                          |
| [Cambridge International A Level](cambridge.md#as--a-level-9618) | Paper 2: 2 hours, 75 marks; Paper 4: 2 hours 30 minutes, 75 marks (25% each) | Paper 2 written, Paper 4 on a computer | Cambridge pseudocode (Paper 2); Python, Java or VB.NET (Paper 4) |
| [IB Diploma](ib.md) (first exams 2027)    | Paper 2: 1 hour 15 minutes and 50 marks (SL, 35%), or 2 hours and 80 marks (HL, 40%); plus an internal assessment | Written | Python or Java (your school chooses) |

## Exam technique
### Written exams
In a written exam, you'll write code with a pen, without an IDE to spot your mistakes or auto-complete things for you. You'll also be asked to read and _trace_ code (work out what it does, step by step, often using a trace table, as in [Lesson 8](../lessons/08-exceptions)). Some things to practise:
- **Write code by hand**, under timed conditions. It feels very different to typing!
- **Indentation still matters.** Make it obvious which lines are inside each loop, `if` statement or function. Some students draw faint vertical lines to keep their indentation straight.
- **Small syntax slips are usually forgiven**, but the logic must be right. OCR's GCSE specification, for example, says that it will "avoid penalising [students] for minor errors in syntax".
- **Learn to read your board's pseudocode**: exam questions often present code in it, even if you answer in Python. Each board's page compares its pseudocode with Python.

### On-screen exams
In an on-screen exam, you'll write, run and test real code on a computer, without access to the internet. Some things to bear in mind:
- **Practise in the IDE you'll use in the exam.** It may well be IDLE (which comes with Python) or Thonny (see [Lesson 0](../lessons/00-getting-started)) rather than VS Code, so make sure you're comfortable with it, and know how to run your code, use the debugger and read error messages in it.
- **Don't rely on third-party packages** like `numpy` or `matplotlib` ([Lesson 14](../lessons/14-packages)) unless your board says they're available.
- **Read the pre-release material** carefully, if your board has any (e.g. AQA's A Level skeleton program, or Eduqas's GCSE scenario).

## Which lessons do I need?
Everyone should work through [Lessons 0 to 10](../README.md#fundamentals), which cover the programming skills that all of these courses have in common: variables, selection, loops, lists and 2D lists, functions, strings, validation, exceptions and debugging, files, and searching and sorting algorithms. After that:
- **GCSE students:** the GCSE programming exams focus on the fundamentals, so Lessons 11 onwards are mostly extension material. They're well worth doing if you're thinking of taking Computer Science further, though! Eduqas students should also do [Lesson 13](../lessons/13-dictionaries-and-sets).
- **A Level and IB students:** classes and objects ([Lessons 11](../lessons/11-classes-and-objects) and [12](../lessons/12-inheritance-and-encapsulation)), recursion, stacks and queues ([Lesson 16](../lessons/16-recursion-stacks-and-queues)) and the [abstract data types](../README.md#abstract-data-types) lessons are all important. Each board's page has a table showing exactly which lessons cover which parts of its specification, and what isn't covered yet.

---
[Contents](../README.md)
