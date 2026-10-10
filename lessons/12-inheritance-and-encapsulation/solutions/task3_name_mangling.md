# Task 3 solution
```
anyone can see me
please don't look at me
you can't see me... or can you?
you can't see me... or can you?
Traceback (most recent call last):
  ...
AttributeError: 'Secretive' object has no attribute '__private'
```

- `s.public` is a normal, public attribute, so we can access it.
- `s._protected` _works_, even though the underscore tells us we shouldn't use it from outside the class. Python doesn't enforce single underscores at all.
- `s.reveal()` works, because `reveal` is inside the class, so it can use `self.__private`.
- `s._Secretive__private` works, because inside the class, Python renamed `__private` to `_Secretive__private`. This is name mangling.
- `s.__private` raises an `AttributeError`, because outside the class, Python doesn't do the renaming, and there's no attribute called `__private`. This is as close as Python gets to private attributes!
