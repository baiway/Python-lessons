# Task 3 solution
```python
>>> a = 9001
>>> type(a)
<class 'int'>
>>> b = "3"
>>> type(b)
<class 'str'>
>>> c = False
>>> type(c)
<class 'bool'>
>>> d = 2.718281828
>>> type(d)
<class 'float'>
>>> e = "apple"
>>> type(e)
<class 'str'>
>>> f = 10 / 2
>>> type(f)
<class 'float'>
```

Note that:
- `b` is a string, not an integer, because it's surrounded by quotation marks.
- `f` is a float, not an integer, even though $10 \div 2 = 5$ is a whole number. In Python, `/` _always_ gives a float. If you want an integer, use `//`.
