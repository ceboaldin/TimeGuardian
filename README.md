
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

## Setting Global Units for Time and Memory Measurement

The TimeGuardian package allows you to set global units for time and memory measurements. This feature enables you to customize how the execution time and memory usage are reported.

### Usage

1. **Set the Units**: Use `TimeGuardian.set_time_unit(unit)` and `TimeGuardian.set_memory_unit(unit)` to set the global units for time and memory measurement. The `unit` parameter should be a string indicating the desired unit (e.g., 'ms' for milliseconds, 's' for seconds, 'bytes' for bytes, 'KB' for kilobytes, 'MB' for megabytes).

2. **Decorate Functions**: Apply the `@TimeGuardian.measure` decorator to your functions. This decorator will use the globally set units to measure and log the execution time and memory usage.

### Example

```python
from decorators import TimeGuardian

# Set the units for time and memory measurements
TimeGuardian.set_time_unit('ms')  # Set time unit to milliseconds
TimeGuardian.set_memory_unit('MB')  # Set memory unit to megabytes

@TimeGuardian.measure(elapsed=True, memory=True, name="Sample Function")
def sample_function():
    # Function implementation
    ...

# Call the decorated function
sample_function()
```

In this example, `sample_function` is measured and logged in milliseconds for time and megabytes for memory usage.

## Contributing

Contributions to TimeGuardian are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
