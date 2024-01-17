
# TimeGuardian

TimeGuardian is a Python package designed for measuring and logging the execution time and memory usage of functions. This package is particularly useful for performance monitoring and optimization in Python applications.

## Features

- Decorators for timing functions and logging memory usage.
- Customizable logging for execution time and memory usage with rich formatting.
- Conditional logging based on execution time and memory usage thresholds.

## Installation

Install TimeGuardian directly from pip:

```bash
pip install timeguardian
```

Or, install from the source code:

```bash
cd path/to/TimeGuardian
pip install .
```

## Usage

Import `TimeGuardian` from the `timeguardian` package and use it as a decorator on your functions to measure their execution time and memory usage.

### Basic Usage

```python
from timeguardian import TimeGuardian

# To measure execution time and/or memory usage
@TimeGuardian.measure
def my_function():
    # function implementation

# Custom name logging
@TimeGuardian.measure(name="CustomName")
def another_function():
    # function implementation


# Custom logging with name, time and memory
@TimeGuardian.measure(name="CustomName", elapsed=True, memory=True) #(elapsed in ms, memory in bytes)
def another_function():
    # function implementation
```

### Advanced Usage

Monitor performance with conditional logging:

```python
from timeguardian import TimeGuardian

# Monitor and log only if execution time or memory usage exceeds the specified limits (time in ms, memory in bytes)
@TimeGuardian.monitor(elapsed=200, memory=1024)
def monitored_function():
    # function implementation
```

## Contributing

Contributions to TimeGuardian are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
