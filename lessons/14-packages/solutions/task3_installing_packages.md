# Task 3 solution
Each of these options creates a virtual environment in a folder called `.venv`, and installs `numpy` and `matplotlib` into it. Your output will look slightly different (e.g. different version numbers), but should be along the same lines.

## Option 1: `venv` and `pip`
On macOS or Linux:
```console
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install numpy matplotlib
Collecting numpy
...
Successfully installed ... matplotlib-3.10.7 numpy-2.3.4 ...
(.venv) $ python -c "import numpy; print(numpy.__version__)"
2.3.4
```

On Windows (PowerShell), the only difference is how you activate the environment:
```console
PS> python -m venv .venv
PS> .venv\Scripts\Activate.ps1
(.venv) PS> pip install numpy matplotlib
```

## Option 2: `uv pip`
```console
$ uv venv
Using CPython 3.14.0
Creating virtual environment at: .venv
$ uv pip install numpy matplotlib
Resolved 11 packages in 1.02s
Installed 11 packages in 64ms
...
$ uv run python -c "import numpy; print(numpy.__version__)"
2.3.4
```

## Option 3: a `uv` project
```console
$ uv init
Initialized project `lesson-15`
$ uv add numpy matplotlib
Using CPython 3.14.0
Creating virtual environment at: .venv
Resolved 12 packages in 1.11s
Installed 11 packages in 62ms
...
$ uv run python -c "import numpy; print(numpy.__version__)"
2.3.4
```

After this, `pyproject.toml` will contain:
```toml
dependencies = [
    "matplotlib>=3.10.7",
    "numpy>=2.3.4",
]
```

If you ever see `ModuleNotFoundError: No module named 'numpy'`, it almost always means that you're running your program with a different Python to the one you installed `numpy` into. Check that your virtual environment is activated (or use `uv run`).
