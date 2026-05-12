# Python Subprocesses: Running External Programs

## Table of Contents

1. [Understanding the Fundamentals](#understanding-the-fundamentals)
2. [Synchronous Execution: subprocess.run()](#synchronous-execution-subprocessrun)
3. [Asynchronous Execution: subprocess.Popen()](#asynchronous-execution-subprocesspopen)
4. [Exception Handling in Subprocesses](#exception-handling-in-subprocesses)
5. [Signal Handling (Ctrl+C and Process Control)](#signal-handling-ctrlc-and-process-control)
6. [Choosing the Right Approach](#choosing-the-right-approach)
7. [Complete Code Examples](#complete-code-examples)

---

## Understanding the Fundamentals

### What Are Subprocesses?

A **subprocess** is an external program that your Python script launches and controls. Think of it as delegating work to another program while your Python code continues to supervise.

**Examples of external programs**:

- System commands: `git`, `ls`, `ping`, `curl`
- Other programming languages: `node script.js`, `ruby app.rb`
- Custom executables: Your own compiled programs

### Internal vs External Execution

- **Internal**: Python code running within your interpreter

  ```python
  result = my_function()  # Runs inside Python
  ```

- **External**: Separate operating system processes
  ```python
  import subprocess
  subprocess.run(["git", "status"])  # Runs outside Python
  ```

### Why Use Subprocesses?

You use subprocesses when you need to:

- ✅ Run system commands (`git`, `docker`, `npm`)
- ✅ Execute programs written in other languages
- ✅ Use command-line tools that don't have Python equivalents
- ✅ Integrate with existing shell scripts or workflows
- ✅ Leverage OS-specific utilities

### Setup

The `subprocess` module is part of Python's standard library:

```python
import subprocess
import sys  # Often needed for getting current Python executable
from pathlib import Path  # For working with file paths
```

### The Two Main Approaches

Python offers two ways to run subprocesses:

| Feature           | `subprocess.run()`        | `subprocess.Popen()`                    |
| ----------------- | ------------------------- | --------------------------------------- |
| **Type**          | Synchronous (blocking)    | Asynchronous (non-blocking)             |
| **Complexity**    | Simple                    | Advanced                                |
| **Wait behavior** | Waits for completion      | Continues immediately                   |
| **Use case**      | 95% of tasks              | Background tasks, real-time interaction |
| **Return value**  | `CompletedProcess` object | `Popen` object (running process)        |

**Rule of thumb**: Start with `run()`. Only use `Popen()` when you need fine-grained control.

---

## Synchronous Execution: subprocess.run()

### The Basics

`subprocess.run()` executes a command and waits for it to finish. It's the simplest and most common way to run external programs.

**Minimal example**:

```python
import subprocess

# Run a command and wait for it to finish
subprocess.run(["python", "--version"])
```

### Command Format: Always Use Lists

**✅ Correct** (list of arguments):

```python
subprocess.run(["git", "commit", "-m", "Update README"])
```

**❌ Dangerous** (string with `shell=True`):

```python
subprocess.run("git commit -m 'Update README'", shell=True)  # Avoid!
```

**Why lists are safer**:

- Prevents shell injection vulnerabilities
- Handles spaces and special characters correctly
- More explicit and readable
- No need to worry about shell quoting rules

**Only use `shell=True` when**:

- You need shell-specific features (pipes `|`, wildcards `*`, redirects `>`)
- Running Windows built-in commands (`dir`, `cd`, `type`)
- Using shell variables or expansions
- Even then, prefer alternatives when possible

### Return Values: The CompletedProcess Object

`subprocess.run()` returns a `CompletedProcess` object with these attributes:

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "--version"], # *: instead of ["python (or python3)", "--version"], we use [sys.executable, "--version"]
    capture_output=True,
    text=True
)

# CompletedProcess attributes
print(f"Command: {result.args}")           # The command that was run
print(f"Exit code: {result.returncode}")   # 0 = success, non-zero = error
print(f"Output: {result.stdout}")          # Standard output (captured)
print(f"Errors: {result.stderr}")          # Standard error (captured)
```

**Type information**:

```python
from subprocess import CompletedProcess, run

# When text=True (returns strings)
result: CompletedProcess[str] = run(
    ["echo", "hello"],
    capture_output=True,
    text=True
)

# When text=False (returns bytes)
result: CompletedProcess[bytes] = run(
    ["echo", "hello"],
    capture_output=True
)
```

### Capturing Output

By default, output goes directly to your terminal. To capture it:

```python
import subprocess
import sys

# Without capturing (output goes to terminal)
subprocess.run([sys.executable, "--version"])

# With capturing (store output in result object)
result = subprocess.run(
    [sys.executable, "--version"],
    capture_output=True,  # Captures both stdout and stderr
    text=True             # Returns strings instead of bytes
)

print(f"Return code: {result.returncode}")
print(f"Output: {result.stdout}")
```

**Alternative to `capture_output`** (for older Python versions or more control):

```python
result = subprocess.run(
    [sys.executable, "--version"],
    stdout=subprocess.PIPE,  # Capture stdout
    stderr=subprocess.PIPE,  # Capture stderr
    text=True
)
```

### Text vs Bytes: Understanding Output Types

#### Text Mode (Recommended for most cases)

```python
result: CompletedProcess[str] = run(
    [sys.executable, "--version"],
    capture_output=True,
    text=True,           # Output as strings
    encoding="utf-8"     # Explicit encoding (good practice)
)

print(type(result.stdout))  # <class 'str'>
print(result.stdout)        # "Python 3.14.0\n"
```

**Use text mode when**:

- Working with human-readable text
- Parsing command output (logs, version strings, etc.)
- You need string methods (`.split()`, `.strip()`, `.startswith()`)
- Output encoding is known (UTF-8 for most cases)

#### Binary Mode (Default)

```python
result: CompletedProcess[bytes] = run(
    [sys.executable, "--version"],
    capture_output=True
    # text=False is the default
)

print(type(result.stdout))  # <class 'bytes'>
print(result.stdout)        # b'Python 3.14.0\r\n'

# Decode manually if needed
text_output = result.stdout.decode('utf-8')
```

**Use binary mode when**:

- Handling binary files (images, executables, archives)
- Unknown or mixed encodings
- Exact byte-level operations matter
- Working with non-text data

### Essential Parameters Reference

```python
import subprocess

result = subprocess.run(
    ["command", "arg1", "arg2"],  # Command as list

    # Output handling
    capture_output=True,     # Capture stdout and stderr (Python 3.7+)
    text=True,               # Return strings instead of bytes
    encoding="utf-8",        # Explicit encoding for text mode

    # Error handling
    check=True,              # Raise CalledProcessError on non-zero exit
    timeout=10,              # Kill process after 10 seconds

    # Input/output redirection
    stdin=subprocess.PIPE,   # Send input to process
    stdout=subprocess.PIPE,  # Capture standard output
    stderr=subprocess.PIPE,  # Capture error output
    # stderr=subprocess.STDOUT,  # Redirect stderr to stdout

    # Working directory
    cwd="/path/to/dir",      # Run command in specific directory

    # Environment variables
    env={"PATH": "/custom/path"},  # Custom environment (replaces existing)
    # env={**os.environ, "KEY": "value"},  # Merge with existing env

    # Shell and platform
    shell=False,             # Don't use shell (safer, default)
)
```

### Error Handling: Two Approaches

#### Approach 1: Manual Exit Code Checking

Use when non-zero exits are expected or you want custom handling:

```python
import subprocess

result = subprocess.run(
    ["git", "status"],
    capture_output=True,
    text=True
    # check=False (default)
)

if result.returncode == 0:
    print("Success!")
    print(result.stdout)
else:
    print(f"Failed with code {result.returncode}")
    print(f"Error: {result.stderr}")

# You can check for specific exit codes
if result.returncode == 1:
    print("Command returned 1 (expected in this case)")
elif result.returncode == 127:
    print("Command not found")
```

**When to use**:

- Commands that may legitimately fail
- You need different behavior for different exit codes
- Building robust pipelines that handle errors gracefully
- Testing or validation scripts

#### Approach 2: Exception-Based (Fail-Fast)

Use when failures should stop execution:

```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True,
        check=True  # Raises CalledProcessError on non-zero exit
    )
    print("Success!")
    print(result.stdout)

except subprocess.CalledProcessError as e:
    print(f"Command failed: {e.cmd}")
    print(f"Exit code: {e.returncode}")
    print(f"Output: {e.stdout}")
    print(f"Error: {e.stderr}")
```

**When to use**:

- Failures should stop your script
- You want automatic error propagation
- Building deployment/build scripts
- Critical operations that must succeed

### Sending Input to Commands

Some commands expect input (like prompts or piped data). Use the `input` parameter:

```python
import subprocess

# Send input to a command
result = subprocess.run(
    ["python", "-c", "name = input('Your name: '); print(f'Hello, {name}!')"],
    input="Alice\n",  # Simulates typing "Alice" and pressing Enter
    capture_output=True,
    text=True
)

print(result.stdout)  # Output: Your name: Hello, Alice!
```

**Multi-line input**:

```python
import subprocess

# Send multiple lines of input
commands = "line 1\nline 2\nline 3\n"

result = subprocess.run(
    ["command-that-expects-input"],
    input=commands,
    capture_output=True,
    text=True
)
```

### Working Directory and Environment

#### Changing Working Directory

```python
import subprocess
from pathlib import Path

# Run command in specific directory
result = subprocess.run(
    ["git", "status"],
    cwd="/path/to/repo",  # Or use Path object
    capture_output=True,
    text=True
)

# Using pathlib
repo_path = Path.home() / "projects" / "myapp"
result = subprocess.run(
    ["git", "log", "-1"],
    cwd=repo_path,
    capture_output=True,
    text=True
)
```

#### Custom Environment Variables

```python
import subprocess
import os

# Replace entire environment
custom_env = {
    "PATH": "/usr/local/bin:/usr/bin",
    "CUSTOM_VAR": "value"
}
result = subprocess.run(
    ["command"],
    env=custom_env,  # Only these variables available
    capture_output=True,
    text=True
)

# Extend existing environment
extended_env = {
    **os.environ,        # Include all current environment variables
    "CUSTOM_VAR": "value"  # Add or override specific variable
}
result = subprocess.run(
    ["command"],
    env=extended_env,
    capture_output=True,
    text=True
)
```

### Cross-Platform Considerations

#### Platform-Specific Commands

```python
import subprocess
import platform

if platform.system() == "Windows":
    # Windows built-ins require shell=True
    result = subprocess.run(
        ["dir"],
        shell=True,
        capture_output=True,
        text=True
    )
else:
    # Unix/Linux/macOS
    result = subprocess.run(
        ["ls", "-la"],
        capture_output=True,
        text=True
    )
```

#### Executable Finding

```python
import subprocess
import sys
from shutil import which

# Get current Python executable (cross-platform)
python_exe = sys.executable

# Find an executable in PATH
git_exe = which("git")
if git_exe:
    subprocess.run([git_exe, "status"])
else:
    print("Git not found in PATH")
```

### Common Patterns

#### Pattern 1: Run and Check Success

```python
import subprocess

result = subprocess.run(
    ["git", "diff", "--quiet"],
    capture_output=True
)

if result.returncode == 0:
    print("No changes")
else:
    print("Repository has changes")
```

#### Pattern 2: Get Command Output

```python
import subprocess

result = subprocess.run(
    ["git", "rev-parse", "HEAD"],
    capture_output=True,
    text=True,
    check=True
)

commit_hash = result.stdout.strip()
print(f"Current commit: {commit_hash}")
```

#### Pattern 3: Run Multiple Commands Sequentially

```python
import subprocess

commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", "Auto commit"],
    ["git", "push", "origin", "main"]
]

for cmd in commands:
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ {' '.join(cmd)}")
    except subprocess.CalledProcessError as e:
        print(f"✗ {' '.join(cmd)} failed: {e.stderr}")
        break  # Stop on first failure
```

#### Pattern 4: Capture and Parse Output

```python
import subprocess

# Get list of Git branches
result = subprocess.run(
    ["git", "branch"],
    capture_output=True,
    text=True,
    check=True
)

branches = [
    line.strip().replace("* ", "")
    for line in result.stdout.split("\n")
    if line.strip()
]

print(f"Branches: {branches}")
```

---

## Asynchronous Execution: subprocess.Popen()

### The Concept: Non-Blocking Execution

While `subprocess.run()` waits for the command to finish, `Popen()` starts the command and immediately returns control to your Python code.

**Analogy**:

- `run()`: Call a restaurant and stay on the line until food arrives
- `Popen()`: Call a restaurant, hang up, and they deliver when ready

### Basic Usage

```python
import subprocess
from time import sleep

# Start a long-running process
process = subprocess.Popen(
    ["ping", "-c", "4", "127.0.0.1"],  # Unix
    # ["ping", "-n", "4", "127.0.0.1"],  # Windows
    stdout=subprocess.PIPE,
    text=True
)

print("Process started. Python continues running...")

# Do other work while process runs
for i in range(3):
    print(f"Python working... {i + 1}")
    sleep(0.5)

# Wait for process to finish
exit_code = process.wait()
print(f"Process finished with exit code: {exit_code}")
```

### Popen Object: Methods and Attributes

```python
import subprocess

process = subprocess.Popen(["command", "arg"])

# Control methods
exit_code = process.wait()        # Wait for process to finish, return exit code
exit_code = process.wait(timeout=5)  # Wait up to 5 seconds
status = process.poll()           # Check if finished (non-blocking), returns exitcode or None
process.terminate()               # Send SIGTERM (graceful shutdown)
process.kill()                    # Send SIGKILL (force kill)
stdout, stderr = process.communicate()  # Send input, wait, get output
stdout, stderr = process.communicate(input="data", timeout=10)

# Attributes
print(process.pid)        # Process ID
print(process.returncode) # Exit code (None if still running)
print(process.args)       # Command that was run
print(process.stdout)     # Standard output file object (if stdout=PIPE)
print(process.stderr)     # Standard error file object (if stderr=PIPE)
print(process.stdin)      # Standard input file object (if stdin=PIPE)
```

### Communicating with Processes

The `.communicate()` method is the **safe** way to interact with process I/O:

```python
import subprocess
import sys

# Start a Python script that expects input
script = """
import sys
name = input("What's your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you are {age} years old!")
"""

process = subprocess.Popen(
    [sys.executable, "-c", script],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Send input and get output (waits for completion)
input_data = "Alice\n30\n"
stdout, stderr = process.communicate(input=input_data)

print(f"Output: {stdout}")
print(f"Errors: {stderr}")
print(f"Exit code: {process.returncode}")
```

**Why `communicate()` is important**:

- **Prevents deadlocks**: When buffers fill up, process blocks
- **Handles both I/O**: Reads stdout and stderr simultaneously
- **Proper cleanup**: Closes streams correctly
- **Timeout support**: Can set time limit

**What NOT to do** (can cause deadlocks):

```python
# ❌ Dangerous - can deadlock if output buffer fills
process = subprocess.Popen(["command"], stdout=subprocess.PIPE)
output = process.stdout.read()  # May block forever
process.wait()

# ✅ Safe - use communicate instead
process = subprocess.Popen(["command"], stdout=subprocess.PIPE, text=True)
output, _ = process.communicate()
```

### Real-Time Output Processing

For long-running processes, read output line-by-line as it happens:

```python
import subprocess
import sys

# A script that prints slowly
slow_script = """
import time
for i in range(5):
    print(f"Processing item {i}...", flush=True)
    time.sleep(0.5)
print("Done!")
"""

process = subprocess.Popen(
    [sys.executable, "-c", slow_script],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Read line by line in real-time
print("Reading output in real-time:")
while True:
    line = process.stdout.readline()
    if not line:  # Empty string means EOF
        break
    print(f"  {line.strip()}")

# Wait for process to finish
process.wait()
print(f"Process completed with exit code: {process.returncode}")
```

**Important**: The process must use `flush=True` in its print statements, or set `bufsize=0` or `bufsize=1` in `Popen()` for line-buffered output.

### Checking Process Status (Non-Blocking)

```python
import subprocess
from time import sleep

process = subprocess.Popen(
    ["python", "long_running_script.py"],
    stdout=subprocess.PIPE
)

# Check if still running without blocking
while True:
    status = process.poll()

    if status is None:
        # Still running
        print("Still running...")
        sleep(1)
    else:
        # Finished
        print(f"Finished with exit code: {status}")
        break
```

### Running Background Processes

```python
import subprocess
from time import sleep

# Start a server in the background
server = subprocess.Popen(
    ["python", "-m", "http.server", "8000"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

print(f"Server started with PID: {server.pid}")

# Do your work
sleep(5)

# Stop the server
print("Stopping server...")
server.terminate()

try:
    server.wait(timeout=5)
    print("Server stopped gracefully")
except subprocess.TimeoutExpired:
    print("Server didn't stop, killing...")
    server.kill()
    server.wait()
```

### Advanced: Parallel Process Execution

```python
import subprocess
from typing import List, Tuple

def run_parallel_commands(commands: List[List[str]]) -> List[Tuple[List[str], int]]:
    """Run multiple commands in parallel and return results."""
    # Start all processes
    processes = []
    for cmd in commands:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        processes.append((cmd, proc))

    # Wait for all to complete
    results = []
    for cmd, proc in processes:
        exit_code = proc.wait()
        results.append((cmd, exit_code))

    return results

# Usage
if __name__ == "__main__":
    commands = [
        ["python", "script1.py"],
        ["python", "script2.py"],
        ["python", "script3.py"]
    ]

    results = run_parallel_commands(commands)

    for cmd, exit_code in results:
        status = "✓" if exit_code == 0 else "✗"
        print(f"{status} {' '.join(cmd)}: exit code {exit_code}")
```

### Streaming Output to File

```python
import subprocess

# Redirect output to file
with open("output.log", "w") as log_file:
    process = subprocess.Popen(
        ["python", "script.py"],
        stdout=log_file,
        stderr=subprocess.STDOUT,  # Redirect stderr to stdout (to same file)
        text=True
    )

    exit_code = process.wait()
    print(f"Process finished, output saved to output.log")
```

---

## Exception Handling in Subprocesses

### Exception Hierarchy

Understanding the exception hierarchy helps you catch the right errors:

```
Exception
├── OSError (base class for OS errors)
│   ├── FileNotFoundError (executable not found)
│   ├── PermissionError (file exists but can't execute)
│   └── ... (other OS errors)
└── subprocess.SubprocessError (base class for subprocess errors)
    ├── CalledProcessError (non-zero exit when check=True)
    └── TimeoutExpired (process exceeded timeout)
```

### Complete Exception Reference

| Exception                       | When It Occurs                           | Available Attributes                    |
| ------------------------------- | ---------------------------------------- | --------------------------------------- |
| `FileNotFoundError`             | Executable not found in PATH             | `filename`, `errno`                     |
| `PermissionError`               | File exists but lacks execute permission | `filename`, `errno`                     |
| `subprocess.CalledProcessError` | Non-zero exit code when `check=True`     | `returncode`, `cmd`, `stdout`, `stderr` |
| `subprocess.TimeoutExpired`     | Process exceeds `timeout` seconds        | `timeout`, `cmd`, `stdout`, `stderr`    |
| `OSError`                       | General OS-level errors                  | `errno`, `strerror`                     |
| `ValueError`                    | Invalid parameter values                 | Standard exception                      |
| `TypeError`                     | Invalid parameter types                  | Standard exception                      |

### Comprehensive Exception Handling Example

```python
import subprocess
from pathlib import Path

def run_command_safely(cmd: list[str], **kwargs) -> subprocess.CompletedProcess | None:
    """
    Run a command with comprehensive error handling.
    Returns CompletedProcess on success, None on failure.
    """
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            timeout=kwargs.get('timeout', 30),
            **kwargs
        )
        return result

    except FileNotFoundError as e:
        # Command executable not found
        print(f"❌ Command not found: {cmd[0]}")
        print(f"   Is it installed and in your PATH?")
        print(f"   Error: {e}")
        return None

    except PermissionError as e:
        # File exists but can't execute it
        print(f"❌ Permission denied: {cmd[0]}")
        print(f"   Check file permissions")
        print(f"   Error: {e}")
        return None

    except subprocess.TimeoutExpired as e:
        # Process exceeded timeout
        print(f"❌ Command timed out after {e.timeout} seconds")
        print(f"   Command: {' '.join(cmd)}")
        if e.stdout:
            print(f"   Partial output: {e.stdout[:100]}...")
        return None

    except subprocess.CalledProcessError as e:
        # Non-zero exit code (when check=True)
        print(f"❌ Command failed with exit code {e.returncode}")
        print(f"   Command: {' '.join(cmd)}")
        if e.stdout:
            print(f"   Output: {e.stdout}")
        if e.stderr:
            print(f"   Error: {e.stderr}")
        return None

    except OSError as e:
        # Other OS-level errors
        print(f"❌ OS error occurred")
        print(f"   Command: {' '.join(cmd)}")
        print(f"   Error: {e}")
        return None

# Usage
if __name__ == "__main__":
    # Test with various error conditions

    # Success case
    result = run_command_safely(["python", "--version"])
    if result:
        print(f"✓ Success: {result.stdout}")

    # FileNotFoundError
    result = run_command_safely(["nonexistent-command"])

    # CalledProcessError
    result = run_command_safely(["python", "-c", "import sys; sys.exit(1)"])

    # TimeoutExpired
    result = run_command_safely(
        ["python", "-c", "import time; time.sleep(10)"],
        timeout=1
    )
```

### Handling Errors in subprocess.run() vs subprocess.Popen()

#### subprocess.run() Error Handling

```python
import subprocess

# Pattern 1: Manual check (check=False, default)
result = subprocess.run(
    ["git", "status"],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print(f"Error: {result.stderr}")
else:
    print(f"Success: {result.stdout}")

# Pattern 2: Exception-based (check=True)
try:
    result = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True,
        check=True  # Raises exception on failure
    )
    print(f"Success: {result.stdout}")
except subprocess.CalledProcessError as e:
    print(f"Error (code {e.returncode}): {e.stderr}")
```

#### subprocess.Popen() Error Handling

```python
import subprocess

# Popen doesn't raise on non-zero exit by default
process = subprocess.Popen(
    ["git", "status"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

try:
    stdout, stderr = process.communicate(timeout=10)

    if process.returncode != 0:
        print(f"Process failed with code {process.returncode}")
        print(f"Error: {stderr}")
    else:
        print(f"Success: {stdout}")

except subprocess.TimeoutExpired:
    process.kill()
    stdout, stderr = process.communicate()
    print(f"Process timed out and was killed")
except Exception as e:
    print(f"Unexpected error: {e}")
    process.kill()
```

### CalledProcessError Details

When `check=True`, failed commands raise `CalledProcessError`:

```python
import subprocess

try:
    result = subprocess.run(
        ["python", "-c", "import sys; sys.exit(42)"],
        capture_output=True,
        text=True,
        check=True
    )
except subprocess.CalledProcessError as e:
    # All information about the failure
    print(f"Command: {e.cmd}")              # ['python', '-c', ...]
    print(f"Exit code: {e.returncode}")     # 42
    print(f"Stdout: {e.stdout}")            # Captured output
    print(f"Stderr: {e.stderr}")            # Captured errors

    # You can re-raise or handle
    # raise  # Re-raise if you want to propagate
```

### TimeoutExpired Details

When a process exceeds the timeout:

```python
import subprocess

try:
    result = subprocess.run(
        ["python", "-c", "import time; time.sleep(10)"],
        capture_output=True,
        text=True,
        timeout=2  # Will timeout after 2 seconds
    )
except subprocess.TimeoutExpired as e:
    # Access partial results
    print(f"Command: {e.cmd}")
    print(f"Timeout: {e.timeout} seconds")
    print(f"Partial stdout: {e.stdout}")  # May be partial
    print(f"Partial stderr: {e.stderr}")  # May be partial

    # The process was killed automatically
```

### Best Practices for Exception Handling

1. **Always set a timeout**: Prevents hanging indefinitely
2. **Order exceptions from specific to general**: Catch `FileNotFoundError` before `OSError`
3. **Capture output even when expecting errors**: Use `capture_output=True` always
4. **Log failures appropriately**: Include command, exit code, and errors
5. **Clean up on errors**: Kill processes, close files
6. **Consider retries**: For transient failures (network, etc.)
7. **Use context managers**: For file-based I/O redirection

---

## Signal Handling (Ctrl+C and Process Control)

### Understanding Process Signals

Signals are notifications sent by the operating system to processes:

| Signal  | Keyboard         | Meaning                  | Can be caught?     |
| ------- | ---------------- | ------------------------ | ------------------ |
| SIGINT  | Ctrl+C           | Interrupt (request stop) | ✅ Yes             |
| SIGTERM | (programmatic)   | Terminate (request exit) | ✅ Yes             |
| SIGKILL | (programmatic)   | Force kill               | ❌ No              |
| SIGHUP  | (terminal close) | Hangup                   | ✅ Yes (Unix only) |

**Windows differences**:

- SIGTERM not supported (use CTRL_C_EVENT or CTRL_BREAK_EVENT)
- SIGKILL equivalent is TerminateProcess
- Limited signal support overall

### Handling Ctrl+C in Parent Process

```python
import subprocess
from time import sleep
import signal
import sys

def signal_handler(sig, frame):
    """Handle Ctrl+C in parent process."""
    print("\n\nParent received Ctrl+C, cleaning up...")
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

print("Parent process running (Press Ctrl+C to stop)...")

try:
    while True:
        sleep(1)
        print("Working...")
except KeyboardInterrupt:
    print("\nCaught KeyboardInterrupt, exiting...")
```

### Gracefully Stopping Subprocesses

```python
import subprocess
from time import sleep
import signal

# Start a long-running subprocess
process = subprocess.Popen(
    ["python", "-c", """
import time
import signal

def handler(sig, frame):
    print("Child received signal, cleaning up...")
    exit(0)

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

for i in range(100):
    print(f"Working... {i}")
    time.sleep(1)
"""],
    stdout=subprocess.PIPE,
    text=True
)

print(f"Started process {process.pid}")

try:
    # Wait for process
    process.wait()
except KeyboardInterrupt:
    print("\nParent received Ctrl+C, stopping child process...")

    # Graceful shutdown sequence
    process.terminate()  # Send SIGTERM

    try:
        process.wait(timeout=5)  # Wait up to 5 seconds
        print("Child process terminated gracefully")
    except subprocess.TimeoutExpired:
        print("Child didn't stop, force killing...")
        process.kill()  # Send SIGKILL
        process.wait()
        print("Child process killed")
```

### Process Control Methods

```python
import subprocess
from time import sleep

process = subprocess.Popen(["long-running-command"])

# Check if process is still running
if process.poll() is None:
    print("Process is still running")

# Graceful termination (SIGTERM on Unix, similar on Windows)
process.terminate()
sleep(2)

# Check if it terminated
if process.poll() is None:
    print("Process didn't terminate, killing...")
    process.kill()  # Force kill (SIGKILL)

# Always wait to clean up zombie processes
process.wait()
print("Process cleaned up")
```

### Cross-Platform Signal Handling

```python
import subprocess
import platform
import signal
import sys
from time import sleep

def stop_process_gracefully(process: subprocess.Popen, timeout: int = 5) -> bool:
    """
    Stop a process gracefully, with fallback to force kill.
    Returns True if stopped gracefully, False if had to kill.
    """
    if process.poll() is not None:
        return True  # Already stopped

    # Try graceful termination
    if platform.system() == "Windows":
        # Windows doesn't have SIGTERM
        process.send_signal(signal.CTRL_C_EVENT)
    else:
        process.terminate()  # SIGTERM

    try:
        process.wait(timeout=timeout)
        return True  # Stopped gracefully
    except subprocess.TimeoutExpired:
        # Force kill
        process.kill()
        process.wait()
        return False  # Had to force kill

# Usage
process = subprocess.Popen(["long-running-command"])

try:
    process.wait()
except KeyboardInterrupt:
    if stop_process_gracefully(process):
        print("Process stopped gracefully")
    else:
        print("Process had to be force killed")
```

### Handling Multiple Subprocesses

```python
import subprocess
from time import sleep
import signal
import sys

processes: list[subprocess.Popen] = []

def cleanup_all_processes(signum=None, frame=None):
    """Cleanup all child processes."""
    print("\nStopping all child processes...")

    for i, proc in enumerate(processes):
        if proc.poll() is None:  # Still running
            print(f"  Stopping process {i} (PID {proc.pid})...")
            proc.terminate()

    # Wait for all to finish
    for i, proc in enumerate(processes):
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print(f"  Process {i} didn't stop, killing...")
            proc.kill()
            proc.wait()

    print("All processes stopped")
    sys.exit(0)

# Register cleanup on Ctrl+C
signal.signal(signal.SIGINT, cleanup_all_processes)
signal.signal(signal.SIGTERM, cleanup_all_processes)

# Start multiple processes
for i in range(3):
    proc = subprocess.Popen(
        ["python", "-c", f"import time; [print(f'Worker {i}: {{j}}') or time.sleep(1) for j in range(100)]"]
    )
    processes.append(proc)
    print(f"Started worker {i} (PID {proc.pid})")

# Wait for all
for proc in processes:
    proc.wait()
```

### Process Groups (Unix/Linux)

On Unix systems, you can create process groups for better signal handling:

```python
import subprocess
import os
import signal
from time import sleep

# Start process in new process group
process = subprocess.Popen(
    ["bash", "-c", "sleep 100"],
    preexec_fn=os.setsid  # Create new session (Unix only)
)

print(f"Process {process.pid} started in new process group")

try:
    sleep(5)
except KeyboardInterrupt:
    print("\nTerminating process group...")
    # Kill entire process group
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    process.wait()
```

### Timeout Patterns

```python
import subprocess

# Pattern 1: Global timeout
try:
    result = subprocess.run(
        ["long-command"],
        timeout=10,  # Total timeout
        capture_output=True
    )
except subprocess.TimeoutExpired as e:
    print(f"Command timed out after {e.timeout} seconds")

# Pattern 2: Popen with timeout
process = subprocess.Popen(["long-command"])

try:
    exit_code = process.wait(timeout=10)
except subprocess.TimeoutExpired:
    print("Process timed out, terminating...")
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()

# Pattern 3: Communicate with timeout
process = subprocess.Popen(
    ["command"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

try:
    stdout, stderr = process.communicate(input="data", timeout=10)
except subprocess.TimeoutExpired:
    process.kill()
    stdout, stderr = process.communicate()
```

### Signal Handling Best Practices

| Scenario                  | Recommended Approach                                                          |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Single subprocess**     | Use `try/except KeyboardInterrupt`, call `.terminate()` then `.wait(timeout)` |
| **Multiple subprocesses** | Register signal handler, iterate and terminate all                            |
| **Long-running daemons**  | Use process groups (Unix) or job objects (Windows)                            |
| **Critical operations**   | Implement cleanup in signal handlers                                          |
| **Cross-platform**        | Check `platform.system()` and use appropriate signals                         |
| **Production**            | Always set timeouts, handle both SIGINT and SIGTERM                           |

---

## Choosing the Right Approach

### Decision Tree

```
Do you need to...
│
├─→ Just run a command and get the result?
│   └─→ Use subprocess.run()
│       - Simple, synchronous
│       - 95% of use cases
│       - Automatic cleanup
│
├─→ Run a command in the background?
│   └─→ Use subprocess.Popen()
│       - Start server/daemon
│       - Continue Python execution
│       - Manual process management
│
├─→ Interact with a running process?
│   └─→ Use subprocess.Popen()
│       - Send input over time
│       - Read output in real-time
│       - Use .communicate() for safety
│
└─→ Monitor long-running process?
    └─→ Use subprocess.Popen()
        - Check status with .poll()
        - Display progress updates
        - Handle timeout/termination
```

### subprocess.run() Use Cases

**✅ When to use `run()`**:

- Running git commands (`git status`, `git commit`)
- Checking installed versions (`python --version`, `node --version`)
- Build scripts (`npm install`, `make build`)
- System administration (`systemctl status`, `docker ps`)
- Any command where you need the result before continuing
- Simple automation scripts
- CI/CD pipelines

**Example scenarios**:

```python
import subprocess

# Check if service is running
result = subprocess.run(
    ["systemctl", "is-active", "nginx"],
    capture_output=True,
    text=True
)

if result.stdout.strip() == "active":
    print("✓ Nginx is running")
else:
    print("✗ Nginx is not running")

# Run tests and check results
result = subprocess.run(
    ["pytest", "tests/"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("All tests passed!")
else:
    print("Tests failed!")
    print(result.stdout)
```

### subprocess.Popen() Use Cases

**✅ When to use `Popen()`**:

- Starting long-running servers or daemons
- Real-time output processing (progress bars, streaming logs)
- Interactive CLI programs (expecting user input over time)
- Running multiple commands in parallel
- Need to terminate/control process dynamically
- Process monitoring and health checks

**Example scenarios**:

```python
import subprocess
from time import sleep

# Start development server
dev_server = subprocess.Popen(
    ["npm", "run", "dev"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

print(f"Dev server started (PID: {dev_server.pid})")

# Stream the output
for line in dev_server.stdout:
    print(f"[Server] {line.strip()}")
    if "Server started on" in line:
        break

# Do your work...
print("Running tests...")
sleep(10)

# Stop the server when done
print("Stopping server...")
dev_server.terminate()
dev_server.wait(timeout=5)
```

### Performance Considerations

| Factor       | subprocess.run()             | subprocess.Popen()        |
| ------------ | ---------------------------- | ------------------------- |
| **Overhead** | Low (single call)            | Higher (more control)     |
| **Memory**   | Efficient (auto cleanup)     | Manual management needed  |
| **CPU**      | Blocks during execution      | Non-blocking              |
| **Use when** | I/O not performance critical | Need concurrent execution |

### Common Mistakes to Avoid

| Mistake                                   | Why It's Wrong                  | Correct Approach                         |
| ----------------------------------------- | ------------------------------- | ---------------------------------------- |
| Using `shell=True` unnecessarily          | Security risk (shell injection) | Use list of arguments                    |
| Not capturing output                      | Can't debug or process results  | Set `capture_output=True`                |
| Not setting timeout                       | Scripts hang indefinitely       | Always set `timeout` parameter           |
| Using `subprocess.call()`                 | Deprecated, less features       | Use `subprocess.run()`                   |
| Reading stdout/stderr directly from Popen | Can cause deadlocks             | Use `.communicate()`                     |
| Not handling exceptions                   | Script crashes unexpectedly     | Wrap in try/except                       |
| Forgetting to wait/join                   | Process becomes zombie          | Call `.wait()`                           |
| Mixing text and binary modes              | Encoding errors                 | Be explicit: `text=True` or handle bytes |
| Not checking return codes                 | Silent failures                 | Check `returncode` or use `check=True`   |

---

## Complete Code Examples

### Example 1: Git Workflow Automation

```python
import subprocess
from typing import Optional
from pathlib import Path

class GitRepo:
    """Manage Git repository operations with error handling."""

    def __init__(self, repo_path: Path):
        self.repo_path = repo_path

    def run_git(self, args: list[str], timeout: int = 30) -> Optional[subprocess.CompletedProcess]:
        """Run a git command with comprehensive error handling."""
        try:
            result = subprocess.run(
                ["git"] + args,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=True,
                timeout=timeout
            )
            return result

        except FileNotFoundError:
            print("❌ Git not installed or not in PATH")
            return None

        except subprocess.TimeoutExpired:
            print(f"❌ Git command timed out after {timeout}s")
            return None

        except subprocess.CalledProcessError as e:
            print(f"❌ Git command failed (exit code {e.returncode})")
            print(f"   Error: {e.stderr}")
            return None

    def status(self) -> Optional[str]:
        """Get repository status."""
        result = self.run_git(["status", "--short"])
        return result.stdout if result else None

    def add_all(self) -> bool:
        """Stage all changes."""
        result = self.run_git(["add", "."])
        return result is not None

    def commit(self, message: str) -> bool:
        """Create a commit."""
        result = self.run_git(["commit", "-m", message])
        return result is not None

    def push(self, remote: str = "origin", branch: str = "main") -> bool:
        """Push to remote."""
        result = self.run_git(["push", remote, branch])
        return result is not None

    def auto_commit_and_push(self, message: str) -> bool:
        """Complete workflow: add, commit, push."""
        print("Checking status...")
        status = self.status()
        if not status:
            return False

        if not status.strip():
            print("No changes to commit")
            return True

        print(f"Changes detected:\n{status}")

        if not self.add_all():
            return False
        print("✓ Changes staged")

        if not self.commit(message):
            return False
        print("✓ Commit created")

        if not self.push():
            return False
        print("✓ Pushed to remote")

        return True

# Usage
if __name__ == "__main__":
    repo = GitRepo(Path.cwd())
    success = repo.auto_commit_and_push("Auto-commit: Update documentation")

    if success:
        print("\n✅ All operations completed successfully")
    else:
        print("\n❌ Some operations failed")
```

### Example 2: Development Environment Checker

```python
import subprocess
from typing import Optional
from dataclasses import dataclass

@dataclass
class ToolInfo:
    """Information about an installed tool."""
    name: str
    version: str
    installed: bool

def check_tool_version(command: list[str], timeout: int = 5) -> Optional[str]:
    """Check if a tool is installed and return its version."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None

    except FileNotFoundError:
        return None
    except subprocess.TimeoutExpired:
        return None
    except Exception:
        return None

def check_development_environment() -> dict[str, ToolInfo]:
    """Verify all required tools are installed."""
    tools = {
        "Python": ["python", "--version"],
        "Node.js": ["node", "--version"],
        "Git": ["git", "--version"],
        "Docker": ["docker", "--version"],
        "npm": ["npm", "--version"],
        "pip": ["pip", "--version"]
    }

    results = {}

    print("Development Environment Check")
    print("=" * 50)

    for tool_name, command in tools.items():
        version = check_tool_version(command)

        if version:
            results[tool_name] = ToolInfo(tool_name, version, True)
            print(f"✓ {tool_name:12} {version}")
        else:
            results[tool_name] = ToolInfo(tool_name, "N/A", False)
            print(f"✗ {tool_name:12} NOT FOUND")

    print("=" * 50)

    installed_count = sum(1 for tool in results.values() if tool.installed)
    total_count = len(results)

    if installed_count == total_count:
        print(f"✅ All tools installed ({installed_count}/{total_count})")
    else:
        print(f"⚠️  Some tools missing ({installed_count}/{total_count})")

    return results

# Usage
if __name__ == "__main__":
    results = check_development_environment()

    # Check specific requirements
    if not results["Python"].installed:
        print("\n❌ Python is required but not installed")
        exit(1)

    if not results["Git"].installed:
        print("\n⚠️  Git is recommended but not installed")
```

### Example 3: Real-Time Log Monitoring

```python
import subprocess
from datetime import datetime
from time import sleep
import signal
import sys

class LogMonitor:
    """Monitor a log file or command output in real-time."""

    def __init__(self, command: list[str]):
        self.command = command
        self.process: Optional[subprocess.Popen] = None
        self.running = False

    def start(self):
        """Start monitoring."""
        self.running = True

        try:
            self.process = subprocess.Popen(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1  # Line buffered
            )

            print(f"Monitoring started (PID {self.process.pid})")
            print("Press Ctrl+C to stop\n")

            # Read output line by line
            while self.running:
                line = self.process.stdout.readline()

                if not line:
                    # EOF reached
                    break

                self._process_line(line.rstrip())

        except KeyboardInterrupt:
            print("\n\nStopping monitor...")
            self.stop()

        except Exception as e:
            print(f"Error: {e}")
            self.stop()

    def _process_line(self, line: str):
        """Process a single log line."""
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Highlight errors and warnings
        if "ERROR" in line.upper():
            print(f"[{timestamp}] 🔴 {line}")
        elif "WARN" in line.upper():
            print(f"[{timestamp}] 🟡 {line}")
        else:
            print(f"[{timestamp}] {line}")

    def stop(self):
        """Stop monitoring gracefully."""
        self.running = False

        if self.process and self.process.poll() is None:
            self.process.terminate()

            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()

        print("Monitor stopped")

# Usage
if __name__ == "__main__":
    # Monitor system logs (example)
    # monitor = LogMonitor(["tail", "-f", "/var/log/syslog"])

    # Monitor Python script output
    monitor = LogMonitor([
        "python", "-c", """
import time
import random

messages = ["INFO: Processing item", "WARN: Slow response", "ERROR: Connection failed"]

for i in range(100):
    msg = random.choice(messages)
    print(f"{msg} {i}")
    time.sleep(0.5)
"""
    ])

    monitor.start()
```

### Example 4: Parallel Command Execution with Progress

```python
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict
from time import perf_counter
from dataclasses import dataclass

@dataclass
class CommandResult:
    """Result of a command execution."""
    command: List[str]
    exit_code: int
    stdout: str
    stderr: str
    duration: float
    success: bool

def run_command(cmd: List[str], timeout: int = 30) -> CommandResult:
    """Run a single command and return detailed results."""
    start_time = perf_counter()

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        duration = perf_counter() - start_time

        return CommandResult(
            command=cmd,
            exit_code=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
            duration=duration,
            success=result.returncode == 0
        )

    except subprocess.TimeoutExpired:
        duration = perf_counter() - start_time
        return CommandResult(
            command=cmd,
            exit_code=-1,
            stdout="",
            stderr=f"Timeout after {timeout}s",
            duration=duration,
            success=False
        )

    except Exception as e:
        duration = perf_counter() - start_time
        return CommandResult(
            command=cmd,
            exit_code=-2,
            stdout="",
            stderr=str(e),
            duration=duration,
            success=False
        )

def run_commands_parallel(
    commands: List[List[str]],
    max_workers: int = 4
) -> List[CommandResult]:
    """Run multiple commands in parallel with progress tracking."""
    results = []
    total = len(commands)
    completed = 0

    print(f"Running {total} commands with {max_workers} workers...\n")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all commands
        futures = {
            executor.submit(run_command, cmd): cmd
            for cmd in commands
        }

        # Process as they complete
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            completed += 1

            # Display progress
            status = "✓" if result.success else "✗"
            cmd_str = " ".join(result.command[:3])  # First 3 parts
            print(f"[{completed}/{total}] {status} {cmd_str} ({result.duration:.2f}s)")

    return results

# Usage
if __name__ == "__main__":
    # Example: Run multiple test suites in parallel
    commands = [
        ["pytest", "tests/unit/"],
        ["pytest", "tests/integration/"],
        ["flake8", "src/"],
        ["mypy", "src/"],
        ["black", "--check", "src/"],
        ["isort", "--check", "src/"]
    ]

    start_time = perf_counter()
    results = run_commands_parallel(commands, max_workers=4)
    total_time = perf_counter() - start_time

    # Summary
    print("\n" + "=" * 60)
    print("Summary:")
    print("=" * 60)

    successful = sum(1 for r in results if r.success)
    failed = len(results) - successful

    print(f"Total commands: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total time: {total_time:.2f}s")

    if failed > 0:
        print("\nFailed commands:")
        for result in results:
            if not result.success:
                cmd_str = " ".join(result.command)
                print(f"  ✗ {cmd_str}")
                print(f"    Error: {result.stderr[:100]}")
```

---

## Key Takeaways

### The Big Picture

1. **`subprocess` connects Python to the OS**:
   - Run any command-line program
   - Capture and process output
   - Build automation workflows
   - Integrate with external tools

2. **Two tools for different needs**:
   - `run()`: Simple, synchronous, covers 95% of cases
   - `Popen()`: Advanced, asynchronous, fine-grained control

3. **Safety and reliability**:
   - Always use list format for commands (prevents injection)
   - Set timeouts to prevent hanging
   - Handle exceptions properly (5+ exception types to consider)
   - Manage signals for graceful shutdown

4. **Return types matter**:
   - `CompletedProcess[str]`: When `text=True`
   - `CompletedProcess[bytes]`: When `text=False`
   - Access via `.returncode`, `.stdout`, `.stderr`, `.args`

### Exception Handling Summary

```
Exception Hierarchy:
├── FileNotFoundError (command not found)
├── PermissionError (can't execute)
├── subprocess.CalledProcessError (non-zero exit with check=True)
├── subprocess.TimeoutExpired (timeout exceeded)
└── OSError (other OS errors)
```

**Always handle**: `FileNotFoundError`, `CalledProcessError`, `TimeoutExpired`

### Signal Handling Summary

```
Process Control Sequence:
1. process.terminate()      # SIGTERM (graceful)
2. process.wait(timeout=5)  # Wait for shutdown
3. process.kill()           # SIGKILL (force) if still running
4. process.wait()           # Clean up zombie
```

**Always**: Set timeouts, handle KeyboardInterrupt, clean up processes

### Quick Reference

**Basic subprocess.run()**:

```python
import subprocess

result = subprocess.run(
    ["command", "arg1", "arg2"],
    capture_output=True,
    text=True,
    encoding="utf-8",
    check=True,
    timeout=30
)
```

**Basic subprocess.Popen()**:

```python
import subprocess

process = subprocess.Popen(
    ["command", "arg1"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Do work while process runs
stdout, stderr = process.communicate(timeout=30)
```

**Error handling pattern**:

```python
try:
    result = subprocess.run([...], check=True, timeout=30)
except FileNotFoundError:
    # Handle missing command
except subprocess.CalledProcessError as e:
    # Handle failed command
except subprocess.TimeoutExpired:
    # Handle timeout
```

### Best Practices Checklist

- ✅ Use list format for commands: `["cmd", "arg"]`
- ✅ Set `capture_output=True` to get output
- ✅ Set `text=True` for string output
- ✅ Set `encoding="utf-8"` explicitly
- ✅ Always set `timeout` parameter
- ✅ Use `check=True` or handle return codes
- ✅ Wrap in try/except for comprehensive error handling
- ✅ Handle `KeyboardInterrupt` for Ctrl+C support
- ✅ Use `.communicate()` instead of reading streams directly
- ✅ Call `.wait()` to prevent zombie processes
- ❌ Avoid `shell=True` unless absolutely necessary
- ❌ Don't use deprecated `subprocess.call()` or `subprocess.check_output()`

### Remember

- Start with `subprocess.run()` for almost everything
- Only use `Popen()` when you need background processes or real-time interaction
- Always handle errors — external programs fail in many ways
- Always handle signals — users need to stop your program
- Security matters: validate/sanitize any user input used in commands
- Test edge cases: missing commands, timeouts, different exit codes

---

**Related Topics**: Learn about Python's threading and multiprocessing for running Python code concurrently, and `asyncio` for asynchronous I/O.
