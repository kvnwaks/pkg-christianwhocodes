# Python Concurrency: Threads and Processes

## Table of Contents

1. [Understanding the Fundamentals](#understanding-the-fundamentals)
2. [Python's Threading: Concurrent Execution](#pythons-threading-concurrent-execution)
3. [Python's Multiprocessing: Parallel Execution](#pythons-multiprocessing-parallel-execution)
4. [Exception Handling in Concurrent Code](#exception-handling-in-concurrent-code)
5. [Signal Handling (Ctrl+C and Interrupts)](#signal-handling-ctrlc-and-interrupts)
6. [Choosing the Right Approach](#choosing-the-right-approach)
7. [Complete Code Examples](#complete-code-examples)

---

## Understanding the Fundamentals

### What Are We Trying to Solve?

Normal Python code runs **sequentially** — one instruction at a time. When one function sleeps for 1 second, your entire program freezes for that second. When we have multiple tasks that could run simultaneously, this is inefficient.

Python offers two main approaches to run multiple tasks:

- **Threading**: Multiple tasks sharing the same memory space
- **Multiprocessing**: Multiple independent Python processes

### Memory vs Storage: The Foundation

Before diving into threads and processes, understand how your computer manages data:

- **Storage (Disk)**: Permanent files saved on your hard drive (like filing cabinets)
- **Memory (RAM)**: Active workspace where running programs operate (like your desk surface)

**Key Point**: Multiple processes can read the same **files** on disk, but they cannot share the same **memory** (RAM). This is enforced by your operating system for security and stability.

### Threads vs Processes: Core Differences

Think of it this way:

- **Process**: A completely separate program with its own isolated memory
- **Thread**: A lightweight execution path within a process that shares memory with other threads

```
Single Process
├── Thread 1 ──┐
├── Thread 2 ──┤──→ All threads share the same memory space
└── Thread 3 ──┘──→ Can access the same variables
```

```
Multiple Processes
├── Process 1 (isolated memory) ──→ Cannot access Process 2's variables
└── Process 2 (isolated memory) ──→ Cannot access Process 1's variables
```

### The Python GIL (Global Interpreter Lock)

Python has a unique constraint called the **GIL** that affects how threads work:

- **What it does**: Prevents multiple threads from executing Python bytecode simultaneously
- **Why it exists**: Simplifies memory management and protects Python's internal state
- **Impact**: Python threads can't fully utilize multiple CPU cores for CPU-intensive tasks

**Analogy**:

- **Threading with GIL**: One chef rapidly switching between multiple dishes on a single stove
- **Multiprocessing**: Multiple chefs each with their own stove, working truly in parallel

### Quick Comparison

| Feature                | Threading                           | Multiprocessing                      |
| ---------------------- | ----------------------------------- | ------------------------------------ |
| **Memory**             | Shared between threads              | Isolated per process                 |
| **Data sharing**       | Easy (same variables)               | Complex (need special mechanisms)    |
| **True parallelism**   | No (GIL limited)                    | Yes (separate Python instances)      |
| **Best for**           | I/O-bound tasks (waiting)           | CPU-bound tasks (computing)          |
| **Overhead**           | Lightweight                         | Heavier (full process copy)          |
| **Output behavior**    | Organized                           | Can be interleaved/messy             |
| **Exception handling** | In thread (can't propagate to main) | In process (can't propagate to main) |

### When to Use What: Quick Decision Guide

**Use Threading when your task involves WAITING:**

- ✅ Network requests (API calls, web scraping)
- ✅ File I/O (reading/writing files)
- ✅ Database queries
- ✅ User interface responsiveness

**Use Multiprocessing when your task involves COMPUTING:**

- ✅ Heavy mathematical calculations
- ✅ Image/video processing
- ✅ Data analysis (NumPy, Pandas operations)
- ✅ Machine learning training
- ✅ Encryption/compression

---

## Python's Threading: Concurrent Execution

### Setup

Threading is part of Python's standard library:

```python
from threading import Thread
from time import sleep
```

### The Problem: Sequential Slowness

Here's a function that simulates a slow operation:

```python
from time import sleep

def long_square(num: int) -> int:
    sleep(1)  # Simulates waiting (network delay, file I/O, etc.)
    return num ** 2
```

Running this 5 times sequentially takes **5 seconds**:

```python
results = [long_square(n) for n in range(5)]  # Takes 5 seconds
```

### The Solution: Running Tasks Concurrently

#### Basic Threading Pattern

```python
from threading import Thread
from time import sleep

def long_square(num: int) -> int:
    sleep(1)
    return num ** 2

# Create thread objects
t1 = Thread(target=long_square, args=(1,))
t2 = Thread(target=long_square, args=(2,))

# Start both threads (they run concurrently)
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

# Total time: ~1 second instead of 2!
```

**Key Thread Methods**:

- `start()`: Begins thread execution in the background
- `join()`: Blocks the main program until the thread finishes
- `is_alive()`: Returns True if thread is still running
- `name`: Get or set the thread's name for debugging

### The Return Value Challenge

**Problem**: Threads don't have a built-in way to return values.

```python
result = t1.start()  # ❌ This doesn't work!
```

**Solution**: Use a **shared mutable object** that all threads can modify.

```python
from threading import Thread
from time import sleep

def long_square(num: int, results: dict[int, int]) -> None:
    sleep(1)
    results[num] = num ** 2  # Store result in shared dictionary


# Shared data structure
results: dict[int, int] = {}

# Create and run thread
t1 = Thread(target=long_square, args=(1, results))
t1.start()
t1.join()

print(results)  # Output: {1: 1}
```

**Why this works**: Threads share the same memory space, so they can all read and write to the same `results` dictionary.

### Scaling Up: The List Pattern

Instead of creating individual variables (`t1`, `t2`, `t3`...), use a list:

```python
from threading import Thread
from time import sleep

def long_square(num: int, results: dict[int, int]) -> None:
    sleep(1)
    results[num] = num ** 2


results: dict[int, int] = {}
threads: list[Thread] = []

# Create all threads
for n in range(100):
    t = Thread(target=long_square, args=(n, results))
    threads.append(t)

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Computed {len(results)} squares in ~1 second!")
# 100 operations complete in ~1 second (instead of 100 seconds)
```

### Thread Synchronization: Locks

When multiple threads modify shared data, you may need synchronization to prevent race conditions:

```python
from threading import Thread, Lock
from time import sleep

counter = 0
lock = Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Only one thread can execute this block at a time
            counter += 1

threads = [Thread(target=increment) for _ in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter: {counter}")  # Will be 1,000,000 (correct)
# Without lock, result would be unpredictable due to race conditions
```

### Threading Best Practices

1. **Always join your threads**: Otherwise your program may exit before threads finish
2. **Use shared containers**: Dictionaries, lists, or objects for return values
3. **Separate start and join loops**: Start all threads first, then join them all
4. **Use locks for shared mutable state**: Prevent race conditions
5. **Keep it simple**: Threading is best for I/O-bound tasks with simple coordination
6. **Name your threads**: Use `Thread(name="worker-1", ...)` for easier debugging

---

## Python's Multiprocessing: Parallel Execution

### Setup and Library Choice

You have two options for multiprocessing in Python:

```python
# Option 1: Standard library (has restrictions)
from multiprocessing import Process

# Option 2: Third-party library (more flexible)
# Install with: pip install multiprocess
from multiprocess import Process
```

**Why `multiprocess` exists and when to use it:**

| Feature                | `multiprocessing` (stdlib) | `multiprocess` (third-party)          |
| ---------------------- | -------------------------- | ------------------------------------- |
| **Installation**       | Built-in                   | `pip install multiprocess`            |
| **API**                | Standard                   | Identical to stdlib                   |
| **Jupyter/IPython**    | Often fails                | Works reliably                        |
| **Interactive shells** | Restricted                 | No restrictions                       |
| **Pickleability**      | Strict requirements        | More forgiving                        |
| **Function location**  | Must be module-level       | Can be anywhere                       |
| **Use when**           | Production scripts         | Development, notebooks, complex cases |

**Common `multiprocessing` limitations:**

1. Functions must be defined at module level (not inside other functions)
2. Lambda functions cannot be pickled
3. Fails in `__main__` without proper guards
4. Issues in Jupyter notebooks and REPL

**Recommendation**: Start with `multiprocessing` for simple scripts. Switch to `multiprocess` if you encounter pickle errors or work in notebooks.

```python
# This fails with multiprocessing in notebooks:
from multiprocessing import Process

def outer():
    def worker(x):  # ❌ Nested function
        return x * 2

    p = Process(target=worker, args=(5,))
    p.start()

# This works with multiprocess:
from multiprocess import Process

def outer():
    def worker(x):  # ✓ Works fine
        return x * 2

    p = Process(target=worker, args=(5,))
    p.start()
```

### The Concept: True Parallelism

Multiprocessing creates completely separate Python interpreter instances. Each process:

- Has its own memory space
- Runs on its own CPU core
- Is not limited by the GIL
- Can execute Python code in true parallel

### Basic Implementation

```python
from multiprocessing import Process
from time import sleep

def long_square(num: int) -> None:
    sleep(1)
    print(f"{num} squared is {num ** 2}")

if __name__ == "__main__":  # Required for multiprocessing
    p1 = Process(target=long_square, args=(1,))
    p1.start()
    p1.join()
```

**Note**: The `if __name__ == "__main__":` guard is critical:

- **Why**: Prevents recursive process spawning when module is imported
- **When required**: Always on Windows, good practice on all platforms
- **What happens without it**: Infinite process creation, system crash

### The Critical Difference: Memory Isolation

**This is where processes diverge from threads:**

```python
from multiprocessing import Process
from time import sleep

def long_square(num: int, results: dict[int, int]) -> None:
    sleep(1)
    results[num] = num ** 2


# ❌ This DOES NOT work with processes
results: dict[int, int] = {}

if __name__ == "__main__":
    p = Process(target=long_square, args=(1, results))
    p.start()
    p.join()

    print(results)  # Output: {} — EMPTY!
```

**Why?** When you pass `results` to a process, Python sends a **copy** of that dictionary to the new process. The process modifies its own copy, not your original.

### Handling Process Results

Since processes can't easily share variables, you have several options:

#### Option 1: Print Directly (Simplest)

```python
from multiprocessing import Process
from time import sleep

def long_square(num: int) -> None:
    sleep(1)
    print(f"{num} squared = {num ** 2}")

if __name__ == "__main__":
    processes: list[Process] = []

    for n in range(10):
        p = Process(target=long_square, args=(n,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
```

**Note**: Output from multiple processes may be interleaved (messy) because multiple processes are printing to the same terminal simultaneously.

#### Option 2: Write to Files

```python
from multiprocessing import Process
from time import sleep

def long_square(num: int, filename: str) -> None:
    sleep(1)
    result = num ** 2

    with open(filename, 'a') as f:
        f.write(f"{num},{result}\n")

if __name__ == "__main__":
    # Each process writes to the same file
    for n in range(10):
        p = Process(target=long_square, args=(n, "results.csv"))
        p.start()
```

#### Option 3: Use Multiprocessing Queue (Recommended)

```python
from multiprocessing import Process, Queue
from time import sleep

def long_square(num: int, queue: Queue) -> None:
    sleep(1)
    queue.put((num, num ** 2))

if __name__ == "__main__":
    queue: Queue = Queue()
    processes: list[Process] = []

    # Start processes
    for n in range(10):
        p = Process(target=long_square, args=(n, queue))
        p.start()
        processes.append(p)

    # Wait for completion
    for p in processes:
        p.join()

    # Collect results
    results = {}
    while not queue.empty():
        num, squared = queue.get()
        results[num] = squared

    print(results)
```

#### Option 4: Use Manager (For Complex Shared Data)

```python
from multiprocessing import Process, Manager
from time import sleep

def long_square(num: int, results: dict) -> None:
    """Note: results is now a managed dict, not a regular dict"""
    sleep(1)
    results[num] = num ** 2

if __name__ == "__main__":
    with Manager() as manager:
        # Create a shared dictionary managed by the Manager
        results = manager.dict()
        processes: list[Process] = []

        for n in range(10):
            p = Process(target=long_square, args=(n, results))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        # Convert to regular dict for normal use
        print(dict(results))
```

### Process vs Thread Output Behavior

**Threading** (output is organized):

```
1 squared = 1
2 squared = 4
3 squared = 9
```

**Multiprocessing** (output can be interleaved):

```
1 squared = 13 squared
2 squared = 49
squared = 4
```

This happens because multiple processes are writing to the same output stream at the exact same time.

### Process Methods and Attributes

```python
from multiprocessing import Process

def worker(x):
    return x * 2

if __name__ == "__main__":
    p = Process(target=worker, args=(5,))

    # Control methods
    p.start()           # Start the process
    p.join()            # Wait for process to finish
    p.join(timeout=5)   # Wait up to 5 seconds
    p.terminate()       # Send SIGTERM (graceful shutdown)
    p.kill()            # Send SIGKILL (force kill)

    # Attributes
    print(p.pid)        # Process ID
    print(p.exitcode)   # Exit code (None if still running)
    print(p.is_alive()) # True if process is running
    print(p.name)       # Process name
```

### Multiprocessing Best Practices

1. **Always use `if __name__ == "__main__":`**: Prevents recursive process spawning
2. **Expect messy output**: Multiple processes printing simultaneously get interleaved
3. **Plan for data collection**: Use Queue, Manager, files, or simply print results
4. **Monitor CPU usage**: Make sure you're actually using multiple cores
5. **Consider overhead**: Only worth it for CPU-intensive tasks
6. **Be aware of pickling**: Functions and data must be serializable
7. **Close resources**: Explicitly terminate or join all processes

---

## Exception Handling in Concurrent Code

### The Challenge: Exceptions Don't Propagate

When an exception occurs in a thread or process, it **does not** automatically propagate to the main program:

```python
from threading import Thread

def failing_worker():
    raise ValueError("Something went wrong!")

# This will NOT crash your program
t = Thread(target=failing_worker)
t.start()
t.join()

print("Main program continues...")  # This still runs!
```

**Why?** Threads and processes run independently. An exception in a child thread/process stays in that thread/process.

### Solution 1: Wrapper Function with Exception Storage (Threading)

```python
from threading import Thread
from typing import Optional

def worker_with_exception_handling(
    func,
    args: tuple,
    results: dict,
    exceptions: dict,
    thread_id: int
) -> None:
    """Wrapper that catches and stores exceptions."""
    try:
        results[thread_id] = func(*args)
    except Exception as e:
        exceptions[thread_id] = e


def risky_operation(x: int) -> int:
    if x < 0:
        raise ValueError(f"Negative value: {x}")
    return x ** 2


# Usage
results = {}
exceptions = {}
threads = []

for i, num in enumerate([-1, 2, -3, 4]):
    t = Thread(
        target=worker_with_exception_handling,
        args=(risky_operation, (num,), results, exceptions, i)
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Check for exceptions
if exceptions:
    print(f"Errors occurred in {len(exceptions)} threads:")
    for thread_id, exc in exceptions.items():
        print(f"  Thread {thread_id}: {exc}")
else:
    print(f"All threads completed successfully: {results}")
```

### Solution 2: Using Concurrent.futures (Modern Approach)

The `concurrent.futures` module provides a cleaner way to handle exceptions:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

def risky_operation(x: int) -> int:
    sleep(0.1)
    if x < 0:
        raise ValueError(f"Negative value: {x}")
    return x ** 2


# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit all tasks
    futures = {executor.submit(risky_operation, x): x for x in [-1, 2, -3, 4, 5]}

    # Process results as they complete
    for future in as_completed(futures):
        input_value = futures[future]
        try:
            result = future.result()  # This will raise if the task raised
            print(f"✓ {input_value} -> {result}")
        except ValueError as e:
            print(f"✗ {input_value} -> Error: {e}")
```

Output:

```
✓ 2 -> 4
✗ -1 -> Error: Negative value: -1
✗ -3 -> Error: Negative value: -3
✓ 4 -> 16
✓ 5 -> 25
```

### Solution 3: Process Pool with Error Handling

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
from time import sleep

def cpu_intensive_task(x: int) -> int:
    sleep(0.1)
    if x == 0:
        raise ZeroDivisionError("Cannot process zero")
    return 100 // x


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        inputs = [10, 5, 0, 2, 0, 4]
        futures = {executor.submit(cpu_intensive_task, x): x for x in inputs}

        for future in as_completed(futures):
            input_value = futures[future]
            try:
                result = future.result()
                print(f"✓ {input_value} -> {result}")
            except ZeroDivisionError as e:
                print(f"✗ {input_value} -> Error: {e}")
            except Exception as e:
                print(f"✗ {input_value} -> Unexpected error: {e}")
```

### Exception Types in Concurrent Code

| Exception                             | When It Occurs                   | Module               |
| ------------------------------------- | -------------------------------- | -------------------- |
| `threading.ThreadError`               | Thread-specific errors           | `threading`          |
| `RuntimeError`                        | Thread operations in wrong state | Built-in             |
| `multiprocessing.ProcessError`        | Base class for process errors    | `multiprocessing`    |
| `multiprocessing.BufferTooShort`      | Received message too short       | `multiprocessing`    |
| `multiprocessing.AuthenticationError` | Authentication failed            | `multiprocessing`    |
| `multiprocessing.TimeoutError`        | Operation timed out              | `multiprocessing`    |
| `concurrent.futures.CancelledError`   | Future was cancelled             | `concurrent.futures` |
| `concurrent.futures.TimeoutError`     | Future timed out                 | `concurrent.futures` |

### Best Practices for Exception Handling

1. **Always wrap worker functions**: Use try/except in thread/process targets
2. **Store exceptions for later**: Use shared dictionaries or futures
3. **Use concurrent.futures when possible**: Built-in exception propagation
4. **Log exceptions in workers**: Print or log errors before they're lost
5. **Validate inputs early**: Check before spawning threads/processes
6. **Test error paths**: Ensure your exception handling actually works

---

## Signal Handling (Ctrl+C and Interrupts)

### Understanding Signals

Signals are notifications sent by the operating system to processes. The most common:

- **SIGINT** (Ctrl+C): Interrupt signal, requests graceful shutdown
- **SIGTERM**: Termination signal, requests process to exit
- **SIGKILL**: Force kill (cannot be caught or ignored)

### The Problem: Default Signal Behavior

By default, when you press Ctrl+C:

- **Main program**: Receives `KeyboardInterrupt` exception
- **Threads**: Continue running (not interrupted)
- **Processes**: Each receives its own SIGINT

### Handling Ctrl+C in Threading

#### Basic Pattern: Graceful Shutdown

```python
from threading import Thread, Event
from time import sleep

# Shared stop signal
stop_event = Event()

def worker(worker_id: int):
    """Worker that checks for stop signal."""
    while not stop_event.is_set():
        print(f"Worker {worker_id} working...")
        sleep(1)
    print(f"Worker {worker_id} stopping gracefully")

threads = []
for i in range(3):
    t = Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

try:
    # Main thread waits
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    print("\nCtrl+C received. Stopping workers...")
    stop_event.set()  # Signal all threads to stop

    for t in threads:
        t.join()

    print("All workers stopped cleanly")
```

#### Using Daemon Threads (Quick Exit)

```python
from threading import Thread
from time import sleep

def worker():
    while True:
        print("Working...")
        sleep(1)

# Daemon threads exit when main program exits
t = Thread(target=worker, daemon=True)
t.start()

try:
    sleep(5)
except KeyboardInterrupt:
    print("\nExiting...")
    # No need to join daemon threads - they die automatically
```

**Note**: Daemon threads are killed immediately when the main program exits. Use regular threads with proper shutdown for important work.

### Handling Ctrl+C in Multiprocessing

#### Pattern 1: Process Termination

```python
from multiprocessing import Process
from time import sleep
import signal
import sys

def worker(worker_id: int):
    """Worker that handles its own SIGINT."""
    def signal_handler(sig, frame):
        print(f"\nWorker {worker_id} received Ctrl+C, exiting...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print(f"Worker {worker_id} working...")
        sleep(1)

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = Process(target=worker, args=(i,))
        p.start()
        processes.append(p)

    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("\nMain process received Ctrl+C")
        for p in processes:
            p.terminate()  # Send SIGTERM
            p.join(timeout=5)  # Wait up to 5 seconds

            if p.is_alive():
                p.kill()  # Force kill if still running

        print("All processes terminated")
```

#### Pattern 2: Using Queue for Shutdown Signal

```python
from multiprocessing import Process, Queue
from time import sleep

def worker(worker_id: int, shutdown_queue: Queue):
    """Worker that checks queue for shutdown message."""
    while True:
        if not shutdown_queue.empty():
            msg = shutdown_queue.get()
            if msg == "STOP":
                print(f"Worker {worker_id} shutting down")
                break

        print(f"Worker {worker_id} working...")
        sleep(1)

if __name__ == "__main__":
    shutdown_queue = Queue()
    processes = []

    for i in range(3):
        p = Process(target=worker, args=(i, shutdown_queue))
        p.start()
        processes.append(p)

    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nSending shutdown signal to workers...")
        for _ in processes:
            shutdown_queue.put("STOP")

        for p in processes:
            p.join(timeout=5)

        print("All workers stopped")
```

### Handling Signals in Subprocesses

```python
import subprocess
from time import sleep
import signal

# Start a long-running subprocess
process = subprocess.Popen(
    ["python", "-c", "import time; [time.sleep(1) or print('tick') for _ in range(100)]"],
    stdout=subprocess.PIPE
)

try:
    # Wait for process
    process.wait()
except KeyboardInterrupt:
    print("\nCtrl+C received. Terminating subprocess...")

    # Graceful termination
    process.terminate()  # Send SIGTERM

    try:
        process.wait(timeout=5)  # Wait up to 5 seconds
    except subprocess.TimeoutExpired:
        print("Process didn't terminate, killing...")
        process.kill()  # Force kill
        process.wait()

    print("Subprocess terminated")
```

### Signal Handling Best Practices

| Scenario               | Recommended Approach                                                |
| ---------------------- | ------------------------------------------------------------------- |
| **Threading**          | Use `Event()` for shutdown signaling                                |
| **Quick exit threads** | Use `daemon=True`                                                   |
| **Multiprocessing**    | Use `Queue` or `Manager` for communication                          |
| **Subprocess**         | Call `.terminate()` then `.wait(timeout)`, then `.kill()` if needed |
| **Production code**    | Always handle `KeyboardInterrupt`                                   |
| **Critical work**      | Implement proper cleanup in signal handlers                         |

### Cross-Platform Signal Handling

```python
import signal
import sys
from threading import Thread, Event
from time import sleep

stop_event = Event()

def signal_handler(sig, frame):
    """Handle both SIGINT and SIGTERM."""
    print(f"\nReceived signal {sig}. Shutting down...")
    stop_event.set()

# Register handlers for common signals
signal.signal(signal.SIGINT, signal_handler)   # Ctrl+C
signal.signal(signal.SIGTERM, signal_handler)  # Termination signal

# On Unix, you can also handle SIGHUP (hangup)
if sys.platform != "win32":
    signal.signal(signal.SIGHUP, signal_handler)

def worker():
    while not stop_event.is_set():
        print("Working...")
        sleep(1)
    print("Worker exiting")

t = Thread(target=worker)
t.start()

# Wait for signal
stop_event.wait()
t.join()
print("Cleanup complete")
```

### Common Pitfalls

1. **Not joining threads/processes**: They become zombies
2. **Using `os._exit()` in threads**: Kills entire program
3. **Ignoring daemon threads**: May lose data
4. **Not setting timeouts on join**: Program hangs forever
5. **Killing processes without cleanup**: May corrupt files/data

---

## Choosing the Right Approach

### Decision Tree

```
Does your task spend most of its time...
│
├─→ WAITING (I/O-bound)?
│   └─→ Use THREADING
│       Examples: API calls, file operations, database queries
│       Libraries: threading, concurrent.futures.ThreadPoolExecutor
│
└─→ COMPUTING (CPU-bound)?
    └─→ Use MULTIPROCESSING
        Examples: Math calculations, image processing, data analysis
        Libraries: multiprocessing/multiprocess, concurrent.futures.ProcessPoolExecutor
```

### Real-World Scenarios

#### Scenario 1: Web Scraping 100 URLs

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
import random

def scrape_url(url: str) -> dict:
    """Simulate scraping a URL."""
    sleep(random.uniform(0.1, 0.5))  # Simulates network delay
    return {"url": url, "title": f"Page {url}", "status": 200}

urls = [f"https://example.com/page{i}" for i in range(100)]

# ✅ Use ThreadPoolExecutor - we're waiting for network responses
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(scrape_url, url): url for url in urls}

    results = []
    for future in as_completed(futures):
        try:
            result = future.result()
            results.append(result)
            print(f"✓ Scraped {result['url']}")
        except Exception as e:
            url = futures[future]
            print(f"✗ Failed {url}: {e}")

print(f"\nScraped {len(results)} URLs")
```

#### Scenario 2: Processing 100 Images

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

def process_image(filepath: str) -> str:
    """Simulate CPU-intensive image processing."""
    # Simulate heavy computation
    result = sum(i * i for i in range(1000000))

    return f"Processed {filepath}"

if __name__ == "__main__":
    image_files = [f"image_{i}.jpg" for i in range(100)]

    # ✅ Use ProcessPoolExecutor - CPU-intensive processing
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(process_image, f): f for f in image_files}

        for future in as_completed(futures):
            try:
                result = future.result()
                print(f"✓ {result}")
            except Exception as e:
                filepath = futures[future]
                print(f"✗ Failed {filepath}: {e}")
```

#### Scenario 3: Hybrid Approach (I/O + CPU)

Sometimes you need both! Use processes for CPU work, threads for I/O within each process:

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import sleep

def fetch_data_batch(urls: list[str]) -> list[dict]:
    """Fetch multiple URLs using threading (I/O-bound)."""
    def fetch(url):
        sleep(0.1)  # Simulate network
        return {"url": url, "data": f"content from {url}"}

    with ThreadPoolExecutor(max_workers=10) as executor:
        return list(executor.map(fetch, urls))

def process_batch(batch_id: int, urls: list[str]) -> dict:
    """Process a batch: fetch (I/O) then compute (CPU)."""
    # I/O phase: fetch all URLs in this batch using threads
    data = fetch_data_batch(urls)

    # CPU phase: heavy processing
    processed = sum(len(item["data"]) for item in data)

    return {"batch": batch_id, "processed": processed}

if __name__ == "__main__":
    all_urls = [f"https://api.example.com/{i}" for i in range(100)]

    # Split into 4 batches
    batch_size = 25
    batches = [
        (i, all_urls[i * batch_size:(i + 1) * batch_size])
        for i in range(4)
    ]

    # Process batches in parallel using processes
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(process_batch, batch_id, urls): batch_id
            for batch_id, urls in batches
        }

        for future in as_completed(futures):
            result = future.result()
            print(f"Batch {result['batch']}: {result['processed']} items")
```

### Common Mistakes to Avoid

| Mistake                                 | Why It's Wrong                                | Correct Approach                                    |
| --------------------------------------- | --------------------------------------------- | --------------------------------------------------- |
| Using multiprocessing for API calls     | Overhead outweighs benefits, GIL not a factor | Use threading or async                              |
| Using threading for heavy math          | GIL prevents parallelism                      | Use multiprocessing                                 |
| Not joining threads/processes           | Program may exit early, zombie processes      | Always join or use daemon                           |
| Expecting shared variables in processes | Processes get copies, not references          | Use Queue, Manager, or files                        |
| Forgetting `if __name__ == "__main__":` | Recursive spawning on Windows                 | Always include for multiprocessing                  |
| Not handling exceptions                 | Silent failures, hard to debug                | Wrap workers, use concurrent.futures                |
| Ignoring Ctrl+C                         | Program can't be stopped cleanly              | Handle KeyboardInterrupt                            |
| Creating too many threads/processes     | Resource exhaustion                           | Use pools (ThreadPoolExecutor, ProcessPoolExecutor) |

---

## Complete Code Examples

### Example 1: Robust Web Scraper with Threading

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Event
from time import sleep
import signal

# Global stop signal
stop_event = Event()

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully."""
    print("\n\nShutdown signal received. Finishing current tasks...")
    stop_event.set()

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

def fetch_url(url: str) -> dict:
    """Fetch a URL with interruption support."""
    if stop_event.is_set():
        return {"url": url, "status": "cancelled"}

    try:
        sleep(0.5)  # Simulate network request

        if stop_event.is_set():
            return {"url": url, "status": "cancelled"}

        return {"url": url, "status": "success", "data": f"Content from {url}"}

    except Exception as e:
        return {"url": url, "status": "error", "error": str(e)}

def main():
    urls = [f"https://example.com/page{i}" for i in range(100)]
    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all tasks
        futures = {executor.submit(fetch_url, url): url for url in urls}

        # Process as they complete
        for future in as_completed(futures):
            if stop_event.is_set():
                # Cancel remaining futures
                for f in futures:
                    f.cancel()
                break

            try:
                result = future.result(timeout=1)
                results.append(result)

                if result["status"] == "success":
                    print(f"✓ {result['url']}")
                elif result["status"] == "cancelled":
                    print(f"⊘ {result['url']} (cancelled)")
                else:
                    print(f"✗ {result['url']}: {result.get('error', 'unknown error')}")

            except Exception as e:
                url = futures[future]
                print(f"✗ {url}: {e}")

    print(f"\n{'='*50}")
    print(f"Completed: {len([r for r in results if r['status'] == 'success'])}")
    print(f"Failed: {len([r for r in results if r['status'] == 'error'])}")
    print(f"Cancelled: {len([r for r in results if r['status'] == 'cancelled'])}")

if __name__ == "__main__":
    main()
```

### Example 2: CPU-Intensive Parallel Processing

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count
from time import perf_counter

def fibonacci(n: int) -> int:
    """Compute Fibonacci number (CPU-intensive)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def process_number(n: int) -> tuple[int, int, float]:
    """Process a number and return timing info."""
    start = perf_counter()
    result = fibonacci(n)
    elapsed = perf_counter() - start
    return n, result, elapsed

if __name__ == "__main__":
    # Numbers to process
    numbers = [30, 31, 32, 33, 34, 35]

    print(f"Processing on {cpu_count()} CPU cores\n")

    # Sequential (for comparison)
    print("Sequential processing:")
    start = perf_counter()
    for n in numbers:
        _, result, _ = process_number(n)
        print(f"  fib({n}) = {result:,}")
    seq_time = perf_counter() - start
    print(f"Sequential time: {seq_time:.2f}s\n")

    # Parallel processing
    print("Parallel processing:")
    start = perf_counter()

    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        futures = {executor.submit(process_number, n): n for n in numbers}

        for future in as_completed(futures):
            try:
                n, result, task_time = future.result()
                print(f"  fib({n}) = {result:,} ({task_time:.2f}s)")
            except Exception as e:
                n = futures[future]
                print(f"  fib({n}) failed: {e}")

    par_time = perf_counter() - start
    print(f"Parallel time: {par_time:.2f}s")
    print(f"Speedup: {seq_time/par_time:.2f}x")
```

### Example 3: Worker Pool with Queue

```python
from threading import Thread, Event
from queue import Queue, Empty
from time import sleep
import signal

class WorkerPool:
    """Thread pool that processes tasks from a queue."""

    def __init__(self, num_workers: int = 4):
        self.task_queue: Queue = Queue()
        self.result_queue: Queue = Queue()
        self.stop_event = Event()
        self.workers: list[Thread] = []

        # Create worker threads
        for i in range(num_workers):
            worker = Thread(target=self._worker, args=(i,), daemon=False)
            worker.start()
            self.workers.append(worker)

    def _worker(self, worker_id: int):
        """Worker thread that processes tasks."""
        print(f"Worker {worker_id} started")

        while not self.stop_event.is_set():
            try:
                # Get task with timeout to allow checking stop_event
                task = self.task_queue.get(timeout=0.1)
            except Empty:
                continue

            try:
                # Process task
                result = self._process_task(task)
                self.result_queue.put(("success", task, result))
            except Exception as e:
                self.result_queue.put(("error", task, str(e)))
            finally:
                self.task_queue.task_done()

        print(f"Worker {worker_id} stopped")

    def _process_task(self, task: dict) -> dict:
        """Process a single task (simulated work)."""
        sleep(0.5)  # Simulate I/O operation
        return {
            "task_id": task["id"],
            "result": task["value"] ** 2,
            "processed": True
        }

    def add_task(self, task: dict):
        """Add a task to the queue."""
        self.task_queue.put(task)

    def get_result(self, timeout: float = None) -> tuple:
        """Get a result from the queue."""
        return self.result_queue.get(timeout=timeout)

    def shutdown(self, wait: bool = True):
        """Shutdown the worker pool."""
        print("\nShutting down worker pool...")
        self.stop_event.set()

        if wait:
            # Wait for queue to be empty
            self.task_queue.join()

            # Wait for all workers to finish
            for worker in self.workers:
                worker.join()

        print("Worker pool shutdown complete")

# Usage example
if __name__ == "__main__":
    pool = WorkerPool(num_workers=4)

    # Handle Ctrl+C
    def signal_handler(sig, frame):
        pool.shutdown()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    # Add tasks
    print("Adding tasks...")
    for i in range(20):
        pool.add_task({"id": i, "value": i})

    # Collect results
    print("Processing tasks...\n")
    completed = 0
    try:
        while completed < 20:
            status, task, result = pool.get_result(timeout=5)

            if status == "success":
                print(f"✓ Task {task['id']}: {result}")
            else:
                print(f"✗ Task {task['id']}: {result}")

            completed += 1

    except KeyboardInterrupt:
        print("\nInterrupted by user")

    finally:
        pool.shutdown()
```

### Example 4: Multiprocessing with Shared State

```python
from multiprocessing import Process, Manager, Event
from time import sleep
import signal

def worker(worker_id: int, shared_dict: dict, stop_event: Event):
    """Worker that updates shared state."""
    # Register signal handler for this process
    def signal_handler(sig, frame):
        print(f"Worker {worker_id} received signal, exiting...")
        stop_event.set()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    counter = 0
    while not stop_event.is_set():
        # Update shared state
        shared_dict[f"worker_{worker_id}"] = counter
        print(f"Worker {worker_id}: count = {counter}")

        counter += 1
        sleep(1)

    print(f"Worker {worker_id} finished with count = {counter}")

if __name__ == "__main__":
    # Create manager for shared state
    with Manager() as manager:
        shared_dict = manager.dict()
        stop_event = manager.Event()

        # Create processes
        processes = []
        for i in range(3):
            p = Process(target=worker, args=(i, shared_dict, stop_event))
            p.start()
            processes.append(p)

        try:
            # Monitor shared state
            while not stop_event.is_set():
                sleep(2)
                print(f"\nShared state: {dict(shared_dict)}\n")

        except KeyboardInterrupt:
            print("\n\nMain process received Ctrl+C")
            print("Signaling workers to stop...")
            stop_event.set()

        finally:
            # Wait for all processes with timeout
            for p in processes:
                p.join(timeout=5)

                if p.is_alive():
                    print(f"Process {p.pid} didn't stop, terminating...")
                    p.terminate()
                    p.join()

            print("\nFinal state:", dict(shared_dict))
            print("All processes stopped")
```

---

## Key Takeaways

### The Big Picture

1. **Memory is the dividing line**:
   - Threads share memory → easy communication, but GIL limits CPU usage
   - Processes have isolated memory → complex communication, but true parallelism

2. **The GIL determines performance**:
   - Threads are limited by GIL for CPU tasks → use for I/O
   - Processes bypass GIL, use multiple cores → use for CPU tasks

3. **Exceptions don't propagate automatically**:
   - Must explicitly handle and store exceptions in workers
   - Use `concurrent.futures` for automatic exception handling

4. **Signals need special handling**:
   - Threads: Use `Event()` for graceful shutdown
   - Processes: Each process receives signals independently
   - Subprocesses: Use `.terminate()` then `.kill()` if needed

### Library Choice Guide

| Task                            | Library Choice                           | Why                             |
| ------------------------------- | ---------------------------------------- | ------------------------------- |
| Simple I/O tasks                | `threading.Thread`                       | Built-in, straightforward       |
| Complex I/O with error handling | `concurrent.futures.ThreadPoolExecutor`  | Automatic exception propagation |
| Simple CPU tasks                | `multiprocessing.Process`                | Built-in, works in scripts      |
| CPU tasks in notebooks          | `multiprocess.Process`                   | No import restrictions          |
| Complex CPU with error handling | `concurrent.futures.ProcessPoolExecutor` | Automatic exception propagation |

### Quick Reference Patterns

**Threading with Error Handling**:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(func, arg): arg for arg in items}

    for future in as_completed(futures):
        try:
            result = future.result()
            # Process result
        except Exception as e:
            # Handle exception
            pass
```

**Multiprocessing with Error Handling**:

```python
from concurrent.futures import ProcessPoolExecutor, as_completed

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(func, arg): arg for arg in items}

        for future in as_completed(futures):
            try:
                result = future.result()
                # Process result
            except Exception as e:
                # Handle exception
                pass
```

**Signal Handling Pattern**:

```python
from threading import Event
import signal

stop_event = Event()

def signal_handler(sig, frame):
    stop_event.set()

signal.signal(signal.SIGINT, signal_handler)

# In worker:
while not stop_event.is_set():
    # Do work
    pass
```

### Remember

- Start with `concurrent.futures` for most cases — it's the modern, clean API
- Use `threading.Thread` directly only for simple cases
- Use `multiprocessing.Process` for CPU-bound work in production scripts
- Use `multiprocess.Process` if working in notebooks or encountering pickle errors
- Always handle exceptions — they won't propagate automatically
- Always handle signals — users need to be able to stop your program
- Always use `if __name__ == "__main__":` with multiprocessing
- Measure performance — don't assume parallelism helps without testing

---

**Related Topics**: Learn about `subprocess` to run external programs, and `asyncio` for asynchronous I/O without threads.
