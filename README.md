
# TimeGuardian

TimeGuardian is a Python package designed for measuring and logging the execution time of functions. This package is especially useful for performance monitoring and optimization in Python applications.

## Features

- Easy-to-use decorators for timing functions.
- Integrated logging with rich formatting.
- Conditional logging based on execution time.

## Installation

You can install TimeGuardian directly from pip:

```bash
pip install timeguardian
```

Alternatively, if you have downloaded the source code, you can install it using:

```bash
cd path/to/TimeGuardian
pip install timeguardian
```

## Usage

Import `TimeGuardian` from the `timeguardian` package and use it as a decorator on your functions to measure their execution time.

### Basic Usage

```python
from timeguardian import TimeGuardian

@TimeGuardian.measure
def my_function():
    # function implementation
```

<br>
Terminal output:<br>
<img
  src="docs/images/Screenshot1.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 400px">

### Advanced Usage

You can also provide a custom name for logging the execution time:

```python
from timeguardian import TimeGuardian

@TimeGuardian.measure(name="CustomFunctionName")
def another_function():
    # function implementation
```

Additionally, you can set a time limit for logging. Execution times will only be logged if they exceed this limit:

```python
from timeguardian import TimeGuardian

@TimeGuardian.measure(logTimeLimit=200)
def limited_function():
    # function implementation
```

<br>
Terminal output:<br>
<img
  src="docs/images/Screenshot2.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 400px">

## Contributing

Contributions to TimeGuardian are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

