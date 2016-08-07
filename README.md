# A simple Python profiler
Work in progress

Uses Python's [cProfile](https://docs.python.org/2/library/profile.html).

## Usage
Download zip of this project this install with pip, 
`pip install this_project.zip`.

Decorate the function to be profiled and supply a directory of the
output of the profiler to be saved to.

```python
from simpler_profiler import profile


@profile('/data/tmp/my_profiling_results')
def function_being_profiled(x, y):
    return x + y 

```

Run the following command supplying the same path that was given as an
 arg to the `profile` decorator,
```bash
print_profile_stats /data/tmp/my_profiling_results
```

## To do
* Creating a file every time that the function is called is inefficient.
* What would happen to profiled functions being called recursively?