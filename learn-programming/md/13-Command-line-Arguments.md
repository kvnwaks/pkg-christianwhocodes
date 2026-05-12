# Python Command-Line Arguments: sys.argv and argparse

## Table of Contents

1. [Understanding the Fundamentals](#understanding-the-fundamentals)
2. [sys.argv: Basic Argument Access](#sysargv-basic-argument-access)
3. [argparse: Professional Argument Parsing](#argparse-professional-argument-parsing)
4. [Type Conversion and Validation](#type-conversion-and-validation)
5. [Error Handling and User Experience](#error-handling-and-user-experience)
6. [Advanced argparse Features](#advanced-argparse-features)
7. [Complete Code Examples](#complete-code-examples)

---

## Understanding the Fundamentals

### What Are Command-Line Arguments?

**Command-line arguments** are values you pass to a program when you run it from the terminal. They allow users to control program behavior without modifying code or using interactive prompts.

**Examples**:

```bash
# Arguments provide input
python script.py input.txt output.txt

# Arguments configure behavior
python script.py --verbose --output=results.json

# Arguments combine data and options
python backup.py /home/user --compress --exclude=*.tmp
```

### Why Use Command-Line Arguments?

You use command-line arguments when you need to:

- ✅ Make scripts reusable with different inputs
- ✅ Enable automation and scripting (no user interaction needed)
- ✅ Integrate with shell scripts and pipelines
- ✅ Build professional command-line tools
- ✅ Configure program behavior without code changes
- ✅ Support batch processing and cron jobs

### The Command-Line Anatomy

When you run a command, the shell passes the arguments to Python. Here is how they map to `sys.argv`:

```bash
python script.py file.txt --verbose --output results.json --count 5
       │         │         │          │      │             │      │
       │         │         │          │      │             │      └─ sys.argv[6]: "5"
       │         │         │          │      │             │
       │         │         │          │      │             └─ sys.argv[5]: "--count"
       │         │         │          │      │
       │         │         │          │      └─ sys.argv[4]: "results.json"
       │         │         │          │
       │         │         │          └─ sys.argv[3]: "--output"
       │         │         │
       │         │         └─ sys.argv[2]: "--verbose"
       │         │
       │         └─ sys.argv[1]: "file.txt"
       │
       └─ sys.argv[0]: "script.py" (The script name)
```

**Key concepts**:

- **Positional arguments**: Order matters (e.g., `script.py` and `file.txt`)
- **Optional arguments**: Flags and options (e.g., `--verbose`, `--output`, and `--count`)
- **Argument values**: Data following option names (e.g., `results.json` after `--output`, and `5` after `--count`)

### Argument Naming Conventions

| Type                  | Example                            | Description                      |
| --------------------- | ---------------------------------- | -------------------------------- |
| **Short option**      | `-v`, `-h`, `-o`                   | Single dash, single letter       |
| **Long option**       | `--verbose`, `--help`, `--output`  | Double dash, full word           |
| **Combined short**    | `-vvv`, `-abc`                     | Multiple short options together  |
| **Option with value** | `-o file.txt`, `--output=file.txt` | Option followed by value         |
| **Flag**              | `--verbose`, `--debug`             | Boolean option (presence = True) |
| **Positional**        | `input.txt`, `output.txt`          | No prefix, order-dependent       |

### The Two Approaches in Python

Python provides two main ways to handle command-line arguments:

| Feature             | `sys.argv`              | `argparse`           |
| ------------------- | ----------------------- | -------------------- |
| **Type**            | Raw list of strings     | Full-featured parser |
| **Complexity**      | Simple                  | Moderate to advanced |
| **Use case**        | Quick scripts, 1-3 args | Professional tools   |
| **Help generation** | Manual                  | Automatic            |
| **Type conversion** | Manual                  | Built-in             |
| **Validation**      | Manual                  | Built-in             |
| **Error messages**  | Manual                  | Automatic            |
| **Subcommands**     | Manual/Complex          | Built-in support     |

**Rule of thumb**: Use `sys.argv` for tiny scripts with 1-2 simple arguments. Use `argparse` for everything else.

### Quick Comparison

**sys.argv** (raw and simple):

```python
import sys

if len(sys.argv) < 2:
    print("Usage: script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
print(f"Processing {filename}")
```

**argparse** (structured and powerful):

```python
import argparse

parser = argparse.ArgumentParser(description="Process a file")
parser.add_argument("filename", help="file to process")
args = parser.parse_args()

print(f"Processing {args.filename}")
```

Both accomplish the same task, but `argparse` provides:

- Automatic help messages (`--help`)
- Better error messages
- Type checking
- Option handling
- Documentation generation

---

## sys.argv: Basic Argument Access

### Setup and Basic Structure

`sys.argv` is a list containing all command-line arguments:

```python
import sys

# sys.argv is always available
print(sys.argv)
```

### Understanding sys.argv

```python
# script.py
import sys

print(f"Program name: {sys.argv[0]}")
print(f"All arguments: {sys.argv}")
print(f"Number of arguments: {len(sys.argv)}")
```

Running this:

```bash
$ python script.py arg1 arg2 arg3
Program name: script.py
All arguments: ['script.py', 'arg1', 'arg2', 'arg3']
Number of arguments: 4
```

**Key points**:

- `sys.argv[0]` is always the script name
- Actual arguments start at `sys.argv[1]`
- All arguments are strings (no automatic type conversion)
- Empty spaces separate arguments (quoted strings stay together)

### Argument Indexing

```python
import sys

# Direct indexing
program_name = sys.argv[0]      # Always the script name
first_arg = sys.argv[1]         # First actual argument
second_arg = sys.argv[2]        # Second actual argument

# Slicing to get all actual arguments
actual_args = sys.argv[1:]      # Everything except script name

# Number of actual arguments
num_args = len(sys.argv) - 1    # Subtract 1 for script name
```

### Basic Patterns with sys.argv

#### Pattern 1: Single Required Argument

```python
# backup.py - Takes a directory path
import sys

if len(sys.argv) != 2:
    print("Usage: python backup.py <directory>")
    sys.exit(1)

directory = sys.argv[1]
print(f"Backing up: {directory}")
```

Usage:

```bash
$ python backup.py /home/user/documents
Backing up: /home/user/documents

$ python backup.py
Usage: python backup.py <directory>
```

#### Pattern 2: Multiple Required Arguments

```python
# copy_file.py - Takes source and destination
import sys

if len(sys.argv) != 3:
    print("Usage: python copy_file.py <source> <destination>")
    print("Example: python copy_file.py input.txt output.txt")
    sys.exit(1)

source = sys.argv[1]
destination = sys.argv[2]

print(f"Copying {source} to {destination}")
```

Usage:

```bash
$ python copy_file.py input.txt output.txt
Copying input.txt to output.txt
```

#### Pattern 3: Variable Number of Arguments

```python
# sum.py - Sums all provided numbers
import sys

if len(sys.argv) < 2:
    print("Usage: python sum.py <number1> <number2> [number3] ...")
    sys.exit(1)

numbers = sys.argv[1:]  # All arguments except script name

try:
    total = sum(float(n) for n in numbers)
    print(f"Sum: {total}")
except ValueError:
    print("Error: All arguments must be numbers")
    sys.exit(1)
```

Usage:

```bash
$ python sum.py 10 20 30 40
Sum: 100.0

$ python sum.py 5.5 10.3 2.2
Sum: 18.0
```

#### Pattern 4: Optional Arguments with Defaults

```python
# greet.py - Greeting with optional name
import sys

name = sys.argv[1] if len(sys.argv) > 1 else "World"
print(f"Hello, {name}!")
```

Usage:

```bash
$ python greet.py Alice
Hello, Alice!

$ python greet.py
Hello, World!
```

### Type Conversion with sys.argv

All `sys.argv` values are strings. You must convert them manually:

```python
import sys

if len(sys.argv) != 3:
    print("Usage: python calculate.py <number1> <number2>")
    sys.exit(1)

try:
    # Convert strings to numbers
    num1 = float(sys.argv[1])
    num2 = int(sys.argv[2])

    result = num1 * num2
    print(f"Result: {result}")

except ValueError as e:
    print(f"Error: Invalid number format - {e}")
    sys.exit(1)
```

**Common conversions**:

```python
# String to integer
count = int(sys.argv[1])

# String to float
price = float(sys.argv[1])

# String to boolean (custom logic needed)
verbose = sys.argv[1].lower() in ('true', '1', 'yes', 'on')

# String to Path object
from pathlib import Path
filepath = Path(sys.argv[1])

# String remains string
filename = sys.argv[1]
```

### Handling Spaces and Special Characters

**Problem**: Spaces separate arguments

```bash
$ python script.py hello world
# sys.argv = ['script.py', 'hello', 'world']  # Two arguments
```

**Solution**: Use quotes

```bash
$ python script.py "hello world"
# sys.argv = ['script.py', 'hello world']  # One argument
```

**Example script**:

```python
# message.py
import sys

if len(sys.argv) != 2:
    print("Usage: python message.py '<message>'")
    print("Use quotes if message contains spaces")
    sys.exit(1)

message = sys.argv[1]
print(f"Message: {message}")
```

Usage:

```bash
$ python message.py "Hello, World!"
Message: Hello, World!

$ python message.py 'This is a long message'
Message: This is a long message
```

### Simple Flag Detection

```python
# run.py - Simple verbose flag
import sys

verbose = '--verbose' in sys.argv or '-v' in sys.argv

# Remove flags from arguments
args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]

if verbose:
    print(f"Verbose mode enabled")
    print(f"Arguments: {args}")

# Process remaining arguments
for arg in args:
    print(f"Processing: {arg}")
```

Usage:

```bash
$ python run.py file1.txt file2.txt --verbose
Verbose mode enabled
Arguments: ['file1.txt', 'file2.txt']
Processing: file1.txt
Processing: file2.txt
```

### Basic Option Parsing

```python
# config.py - Simple option parsing
import sys

def parse_args():
    """Parse basic options from sys.argv."""
    args = {
        'files': [],
        'verbose': False,
        'output': 'output.txt'  # Default value
    }

    i = 1  # Skip script name
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg == '--verbose' or arg == '-v':
            args['verbose'] = True

        elif arg == '--output' or arg == '-o':
            # Next argument is the output file
            if i + 1 < len(sys.argv):
                args['output'] = sys.argv[i + 1]
                i += 1  # Skip next argument
            else:
                print("Error: --output requires a value")
                sys.exit(1)

        elif not arg.startswith('-'):
            # Positional argument
            args['files'].append(arg)

        else:
            print(f"Unknown option: {arg}")
            sys.exit(1)

        i += 1

    return args

# Usage
args = parse_args()
print(f"Verbose: {args['verbose']}")
print(f"Output: {args['output']}")
print(f"Files: {args['files']}")
```

Usage:

```bash
$ python config.py file1.txt file2.txt -v --output results.txt
Verbose: True
Output: results.txt
Files: ['file1.txt', 'file2.txt']
```

### When to Use sys.argv

**✅ Use sys.argv when**:

- Script takes 1-2 simple arguments
- No options or flags needed
- Quick and dirty scripts
- Learning or prototyping
- Performance is critical (minimal overhead)

**❌ Don't use sys.argv when**:

- Multiple options or flags
- Need help messages
- Type validation required
- User-facing tools
- Complex argument logic
- Optional arguments with defaults

### sys.argv Limitations

```python
import sys

# ❌ No automatic help
# User must read code or documentation

# ❌ No type checking
number = int(sys.argv[1])  # Can crash with non-number

# ❌ Manual error messages
if len(sys.argv) < 2:
    print("Error: Missing argument")  # You write every message

# ❌ No validation
if not sys.argv[1].endswith('.txt'):
    print("Error: File must be .txt")  # Manual checks

# ❌ No default values
output = sys.argv[2] if len(sys.argv) > 2 else 'output.txt'  # Manual logic

# ❌ Complex flag parsing
if '--flag' in sys.argv:  # Fragile
    sys.argv.remove('--flag')  # Modifying sys.argv is messy
```

### sys.argv Best Practices

1. **Always check argument count**:

   ```python
   if len(sys.argv) != expected_count:
       print("Usage: ...")
       sys.exit(1)
   ```

2. **Provide usage messages**:

   ```python
   def print_usage():
       print("Usage: python script.py <arg1> <arg2>")
       print("Example: python script.py input.txt output.txt")
   ```

3. **Handle type conversion errors**:

   ```python
   try:
       value = int(sys.argv[1])
   except ValueError:
       print("Error: Argument must be a number")
       sys.exit(1)
   ```

4. **Use descriptive variable names**:

   ```python
   # ❌ Bad
   a = sys.argv[1]
   b = sys.argv[2]

   # ✅ Good
   input_file = sys.argv[1]
   output_file = sys.argv[2]
   ```

5. **Document expected arguments**:

   ```python
   """
   Script to process files.

   Usage: python script.py <input> <output>

   Arguments:
       input: Path to input file
       output: Path to output file
   """
   ```

---

## argparse: Professional Argument Parsing

### Why argparse?

`argparse` is Python's standard library for building command-line interfaces. It provides:

- Automatic help generation (`--help`)
- Type conversion and validation
- Required and optional arguments
- Default values
- Argument groups and subcommands
- Professional error messages
- Consistent user experience

### Basic Setup

```python
import argparse

# Create parser
parser = argparse.ArgumentParser(
    description="What your program does"
)

# Add arguments
parser.add_argument('name', help='argument description')

# Parse arguments
args = parser.parse_args()

# Access values
print(args.name)
```

### Creating a Parser

```python
import argparse

parser = argparse.ArgumentParser(
    prog='myprogram',                          # Program name (default: sys.argv[0])
    description='Process some files',          # What the program does
    epilog='Thanks for using %(prog)s!',       # Text after help
    formatter_class=argparse.RawDescriptionHelpFormatter,  # Help formatting
    add_help=True                              # Add --help flag (default: True)
)
```

### Positional Arguments

Positional arguments are required and order-dependent:

```python
import argparse

parser = argparse.ArgumentParser(description='Copy a file')

# Add positional arguments
parser.add_argument('source', help='source file path')
parser.add_argument('destination', help='destination file path')

args = parser.parse_args()

print(f"Copying {args.source} to {args.destination}")
```

Usage:

```bash
$ python copy.py input.txt output.txt
Copying input.txt to output.txt

$ python copy.py --help
usage: copy.py [-h] source destination

Copy a file

positional arguments:
  source       source file path
  destination  destination file path

optional arguments:
  -h, --help   show this help message and exit
```

### Optional Arguments (Flags)

Optional arguments start with `-` or `--`:

```python
import argparse

parser = argparse.ArgumentParser(description='Process files')

# Boolean flag (stores True if present)
parser.add_argument(
    '--verbose', '-v',
    action='store_true',
    help='enable verbose output'
)

# Optional argument with value
parser.add_argument(
    '--output', '-o',
    help='output file path',
    default='output.txt'
)

args = parser.parse_args()

if args.verbose:
    print("Verbose mode enabled")

print(f"Output will be saved to: {args.output}")
```

Usage:

```bash
$ python process.py --verbose --output results.txt
Verbose mode enabled
Output will be saved to: results.txt

$ python process.py -v -o results.txt
Verbose mode enabled
Output will be saved to: results.txt

$ python process.py
Output will be saved to: output.txt
```

### Argument Actions

The `action` parameter controls what happens when an argument is encountered:

```python
import argparse

parser = argparse.ArgumentParser()

# store (default): Store the argument value
parser.add_argument('--name', action='store')

# store_true: Store True if flag present, False otherwise
parser.add_argument('--verbose', action='store_true')

# store_false: Store False if flag present, True otherwise
parser.add_argument('--no-color', action='store_false', dest='color')

# store_const: Store a constant value
parser.add_argument('--debug', action='store_const', const=True, dest='debug_mode')

# append: Append value to a list (can be used multiple times)
parser.add_argument('--include', action='append', default=[])

# count: Count number of times flag appears
parser.add_argument('--verbose', '-v', action='count', default=0)

# version: Print version and exit
parser.add_argument('--version', action='version', version='%(prog)s 2.0')

args = parser.parse_args()
```

**Practical examples**:

```python
import argparse

parser = argparse.ArgumentParser()

# Count verbosity level: -v, -vv, -vvv
parser.add_argument(
    '-v', '--verbose',
    action='count',
    default=0,
    help='increase verbosity (can be repeated)'
)

# Multiple include paths
parser.add_argument(
    '--include',
    action='append',
    help='include directory (can be used multiple times)'
)

args = parser.parse_args()

# Verbosity level
if args.verbose == 0:
    print("Normal output")
elif args.verbose == 1:
    print("Verbose output")
elif args.verbose >= 2:
    print("Debug output")

# Include paths
if args.include:
    print(f"Include directories: {args.include}")
```

Usage:

```bash
$ python script.py -v
Verbose output

$ python script.py -vvv
Debug output

$ python script.py --include /usr/include --include /usr/local/include
Include directories: ['/usr/include', '/usr/local/include']
```

### Type Conversion

`argparse` can automatically convert string arguments to other types:

```python
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

# Built-in types
parser.add_argument('--count', type=int, help='number of items')
parser.add_argument('--ratio', type=float, help='ratio value')

# File objects (auto-opens files)
parser.add_argument('--input', type=argparse.FileType('r'), help='input file')
parser.add_argument('--output', type=argparse.FileType('w'), help='output file')

# Path objects
parser.add_argument('--path', type=Path, help='file path')

# Custom conversion function
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be positive")
    return ivalue

parser.add_argument('--threads', type=positive_int, help='number of threads (>0)')

args = parser.parse_args()
```

Usage:

```bash
$ python script.py --count 10 --ratio 0.5
# args.count = 10 (int)
# args.ratio = 0.5 (float)

$ python script.py --threads -5
usage: script.py [-h] [--threads THREADS]
script.py: error: argument --threads: -5 must be positive
```

### Choices (Restricted Values)

Limit argument values to a predefined set:

```python
import argparse

parser = argparse.ArgumentParser()

# String choices
parser.add_argument(
    '--format',
    choices=['json', 'xml', 'yaml'],
    default='json',
    help='output format'
)

# Numeric choices
parser.add_argument(
    '--level',
    type=int,
    choices=[1, 2, 3, 4, 5],
    help='log level'
)

# Enum choices (Python 3.8+)
from enum import Enum

class Mode(Enum):
    READ = 'read'
    WRITE = 'write'
    APPEND = 'append'

parser.add_argument(
    '--mode',
    type=Mode,
    choices=list(Mode),
    help='file mode'
)

args = parser.parse_args()
```

Usage:

```bash
$ python script.py --format csv
usage: script.py [-h] [--format {json,xml,yaml}]
script.py: error: argument --format: invalid choice: 'csv' (choose from 'json', 'xml', 'yaml')

$ python script.py --format json
# args.format = 'json'
```

### Required Arguments

Make optional arguments required:

```python
import argparse

parser = argparse.ArgumentParser()

# Optional argument that's required (contradictory, but useful)
parser.add_argument(
    '--config',
    required=True,
    help='configuration file path (required)'
)

# Truly optional argument
parser.add_argument(
    '--output',
    help='output file path'
)

args = parser.parse_args()
```

Usage:

```bash
$ python script.py
usage: script.py [-h] --config CONFIG [--output OUTPUT]
script.py: error: the following arguments are required: --config

$ python script.py --config settings.json
# Works
```

### Default Values

Provide default values for optional arguments:

```python
import argparse

parser = argparse.ArgumentParser()

# Simple default
parser.add_argument(
    '--threads',
    type=int,
    default=4,
    help='number of threads (default: %(default)s)'
)

# None as default (useful for optional files)
parser.add_argument(
    '--config',
    default=None,
    help='config file (optional)'
)

# List as default
parser.add_argument(
    '--exclude',
    action='append',
    default=[],
    help='patterns to exclude'
)

args = parser.parse_args()

# Use defaults
threads = args.threads  # 4 if not specified
config = args.config    # None if not specified
```

**Note**: Use `%(default)s` in help text to show the default value automatically.

### Mutually Exclusive Arguments

Arguments that cannot be used together:

```python
import argparse

parser = argparse.ArgumentParser()

# Create mutually exclusive group
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--encrypt', action='store_true', help='encrypt file')
group.add_argument('--decrypt', action='store_true', help='decrypt file')

args = parser.parse_args()

if args.encrypt:
    print("Encrypting...")
elif args.decrypt:
    print("Decrypting...")
```

Usage:

```bash
$ python script.py --encrypt --decrypt
usage: script.py [-h] (--encrypt | --decrypt)
script.py: error: argument --decrypt: not allowed with argument --encrypt

$ python script.py --encrypt
Encrypting...
```

### Argument Groups

Organize arguments in help output:

```python
import argparse

parser = argparse.ArgumentParser(description='Database tool')

# Input/Output group
io_group = parser.add_argument_group('input/output options')
io_group.add_argument('--input', help='input file')
io_group.add_argument('--output', help='output file')

# Database group
db_group = parser.add_argument_group('database options')
db_group.add_argument('--host', default='localhost', help='database host')
db_group.add_argument('--port', type=int, default=5432, help='database port')
db_group.add_argument('--database', required=True, help='database name')

# Logging group
log_group = parser.add_argument_group('logging options')
log_group.add_argument('--verbose', '-v', action='count', default=0)
log_group.add_argument('--log-file', help='log file path')

args = parser.parse_args()
```

The help output will be organized:

```bash
$ python script.py --help
usage: script.py [-h] [--input INPUT] [--output OUTPUT] ...

Database tool

optional arguments:
  -h, --help       show this help message and exit

input/output options:
  --input INPUT    input file
  --output OUTPUT  output file

database options:
  --host HOST      database host
  --port PORT      database port
  --database DB    database name

logging options:
  -v, --verbose    increase verbosity
  --log-file FILE  log file path
```

### Variable Number of Arguments

Accept multiple values for an argument:

```python
import argparse

parser = argparse.ArgumentParser()

# One or more values (at least one required)
parser.add_argument(
    'files',
    nargs='+',
    help='files to process (at least one)'
)

# Zero or more values
parser.add_argument(
    '--exclude',
    nargs='*',
    default=[],
    help='patterns to exclude'
)

# Exactly N values
parser.add_argument(
    '--coordinates',
    nargs=2,
    type=float,
    metavar=('X', 'Y'),
    help='coordinates (x y)'
)

# Optional single value (stores None if not provided, or a list with one element if provided)
parser.add_argument(
    '--config',
    nargs='?',
    const='default.conf',  # Value if flag present without argument
    default='default.conf',  # Value if flag not present
    help='config file'
)

args = parser.parse_args()
```

**nargs options**:

- `N` (integer): Exactly N arguments → produces a list
- `?`: 0 or 1 argument → produces a single value or None
- `*`: 0 or more arguments → produces a list
- `+`: 1 or more arguments → produces a list (at least one required)

Usage:

```bash
$ python script.py file1.txt file2.txt file3.txt --exclude *.tmp *.log
# args.files = ['file1.txt', 'file2.txt', 'file3.txt']
# args.exclude = ['*.tmp', '*.log']

$ python script.py data.csv --coordinates 10.5 20.3
# args.coordinates = [10.5, 20.3]
```

### Subcommands (Subparsers)

Create tools with multiple commands (like `git commit`, `git push`):

```python
import argparse

# Main parser
parser = argparse.ArgumentParser(prog='git-like')

# Create subcommand parser
subparsers = parser.add_subparsers(
    dest='command',
    help='available commands'
)

# 'init' command
init_parser = subparsers.add_parser('init', help='initialize repository')
init_parser.add_argument('--bare', action='store_true', help='create bare repository')

# 'commit' command
commit_parser = subparsers.add_parser('commit', help='commit changes')
commit_parser.add_argument('-m', '--message', required=True, help='commit message')
commit_parser.add_argument('--author', help='commit author')

# 'clone' command
clone_parser = subparsers.add_parser('clone', help='clone repository')
clone_parser.add_argument('url', help='repository URL')
clone_parser.add_argument('directory', nargs='?', help='target directory')

args = parser.parse_args()

# Handle commands
if args.command == 'init':
    print(f"Initializing repository (bare={args.bare})")
elif args.command == 'commit':
    print(f"Committing with message: {args.message}")
    if args.author:
        print(f"Author: {args.author}")
elif args.command == 'clone':
    print(f"Cloning {args.url}")
    if args.directory:
        print(f"Into directory: {args.directory}")
else:
    parser.print_help()
```

Usage:

```bash
$ python git-like.py --help
usage: git-like [-h] {init,commit,clone} ...

optional arguments:
  -h, --help          show this help message and exit

available commands:
  {init,commit,clone}
    init              initialize repository
    commit            commit changes
    clone             clone repository

$ python git-like.py commit -m "Initial commit" --author "Alice"
Committing with message: Initial commit
Author: Alice

$ python git-like.py clone https://github.com/user/repo.git myproject
Cloning https://github.com/user/repo.git
Into directory: myproject
```

### Custom Help Messages

Customize help output:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='myapp',
    description='Application description that appears at the top',
    epilog='''
Examples:
  %(prog)s --input data.csv --output results.json
  %(prog)s -i data.csv -o results.json --verbose

For more information, visit https://example.com/docs
    ''',
    formatter_class=argparse.RawDescriptionHelpFormatter  # Preserve formatting
)

# Custom metavar for cleaner help
parser.add_argument(
    '--input', '-i',
    metavar='FILE',
    help='input file path'
)

# Custom destination variable name
parser.add_argument(
    '--output', '-o',
    dest='output_file',
    metavar='FILE',
    help='output file path'
)

args = parser.parse_args()

# Access via custom destination
print(args.output_file)
```

### Parser Configuration

```python
import argparse

parser = argparse.ArgumentParser(
    prog='myprogram',                    # Program name in help
    description='What the program does', # Description text
    epilog='Text at bottom of help',     # Epilog text

    # Prefix characters (for non-Unix style)
    prefix_chars='-+/',  # Allows -, +, / for options

    # Allow abbreviations (default: True)
    allow_abbrev=False,  # Require full option names

    # Exit on error (default: True)
    exit_on_error=False,  # Raise exception instead of exiting

    # Formatter class
    formatter_class=argparse.RawDescriptionHelpFormatter,

    # Add help (default: True)
    add_help=True,

    # Conflict handler
    conflict_handler='resolve'  # Override conflicting options
)
```

---

## Type Conversion and Validation

### Built-in Type Converters

argparse provides automatic type conversion:

```python
import argparse

parser = argparse.ArgumentParser()

# Numeric types
parser.add_argument('--int', type=int)
parser.add_argument('--float', type=float)
parser.add_argument('--complex', type=complex)

# Boolean (careful: bool("False") is True!)
# Use action='store_true' instead for boolean flags

# File types
parser.add_argument('--input', type=argparse.FileType('r'))
parser.add_argument('--output', type=argparse.FileType('w'))
parser.add_argument('--binary', type=argparse.FileType('rb'))

args = parser.parse_args()

# Files are automatically opened
if args.input:
    content = args.input.read()
    args.input.close()  # Don't forget to close
```

### Custom Type Converters

Create functions to validate and convert arguments:

```python
import argparse
import re
from pathlib import Path

def positive_int(value):
    """Validate positive integer."""
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"{value} must be a positive integer")
        return ivalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} must be an integer")

def valid_email(value):
    """Validate email address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value):
        raise argparse.ArgumentTypeError(f"{value} is not a valid email address")
    return value

def existing_file(value):
    """Validate that file exists."""
    path = Path(value)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"File not found: {value}")
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"Not a file: {value}")
    return path

def existing_dir(value):
    """Validate that directory exists."""
    path = Path(value)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"Directory not found: {value}")
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"Not a directory: {value}")
    return path

def percentage(value):
    """Validate percentage (0-100)."""
    try:
        fvalue = float(value)
        if fvalue < 0 or fvalue > 100:
            raise argparse.ArgumentTypeError(f"{value} must be between 0 and 100")
        return fvalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} must be a number")

# Usage
parser = argparse.ArgumentParser()
parser.add_argument('--threads', type=positive_int, help='number of threads')
parser.add_argument('--email', type=valid_email, help='email address')
parser.add_argument('--input', type=existing_file, help='input file')
parser.add_argument('--workdir', type=existing_dir, help='working directory')
parser.add_argument('--threshold', type=percentage, help='threshold percentage')

args = parser.parse_args()
```

Usage:

```bash
$ python script.py --threads -5
script.py: error: argument --threads: -5 must be a positive integer

$ python script.py --email invalid-email
script.py: error: argument --email: invalid-email is not a valid email address

$ python script.py --input nonexistent.txt
script.py: error: argument --input: File not found: nonexistent.txt
```

### Range Validation

```python
import argparse

def range_limited_float(min_val, max_val):
    """Create a type function that validates a float range."""
    def type_func(value):
        try:
            fvalue = float(value)
            if fvalue < min_val or fvalue > max_val:
                raise argparse.ArgumentTypeError(
                    f"{value} must be between {min_val} and {max_val}"
                )
            return fvalue
        except ValueError:
            raise argparse.ArgumentTypeError(f"{value} must be a number")

    return type_func

parser = argparse.ArgumentParser()

# Temperature in Celsius (-273.15 to infinity)
parser.add_argument(
    '--temp',
    type=range_limited_float(-273.15, float('inf')),
    help='temperature in Celsius'
)

# Probability (0.0 to 1.0)
parser.add_argument(
    '--probability',
    type=range_limited_float(0.0, 1.0),
    help='probability value'
)

args = parser.parse_args()
```

### File Extension Validation

```python
import argparse
from pathlib import Path

def file_with_extension(extensions):
    """Create a type function that validates file extensions."""
    def type_func(value):
        path = Path(value)

        # Check if file exists
        if not path.exists():
            raise argparse.ArgumentTypeError(f"File not found: {value}")

        # Check extension
        if path.suffix.lower() not in extensions:
            raise argparse.ArgumentTypeError(
                f"File must have one of these extensions: {', '.join(extensions)}"
            )

        return path

    return type_func

parser = argparse.ArgumentParser()

parser.add_argument(
    '--image',
    type=file_with_extension(['.jpg', '.png', '.gif']),
    help='image file'
)

parser.add_argument(
    '--data',
    type=file_with_extension(['.csv', '.tsv', '.txt']),
    help='data file'
)

args = parser.parse_args()
```

### Complex Validation Logic

For validation beyond type conversion, use a custom function after parsing:

```python
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument('--input', type=Path, help='input file')
parser.add_argument('--output', type=Path, help='output file')
parser.add_argument('--overwrite', action='store_true', help='overwrite existing files')

args = parser.parse_args()

# Post-parsing validation
def validate_args(args):
    """Validate argument combinations."""
    errors = []

    # Check input file exists
    if not args.input.exists():
        errors.append(f"Input file not found: {args.input}")

    # Check output file doesn't exist (unless overwrite)
    if args.output.exists() and not args.overwrite:
        errors.append(f"Output file exists: {args.output}. Use --overwrite to replace.")

    # Check input and output are different
    if args.input.resolve() == args.output.resolve():
        errors.append("Input and output files must be different")

    # Report all errors
    if errors:
        for error in errors:
            print(f"Error: {error}")
        sys.exit(1)

validate_args(args)
```

### Type Conversion Best Practices

1. **Use built-in types when possible**: `int`, `float`, `Path`
2. **Provide clear error messages**: Explain what's wrong and what's expected
3. **Validate early**: Catch errors before processing starts
4. **Use Path objects**: Better than strings for file paths
5. **Avoid bool(value)**: It's almost always True; use `action='store_true'` instead
6. **Document valid formats**: In help text, show examples of valid input
7. **Return converted types**: Type functions should return the converted value, not the string

---

## Error Handling and User Experience

### Understanding argparse Errors

argparse automatically handles several error conditions:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--number', type=int, required=True)
parser.add_argument('--format', choices=['json', 'xml'])

# Automatic error handling:
# - Missing required arguments
# - Invalid type conversion
# - Invalid choices
# - Unknown arguments

args = parser.parse_args()
```

Error examples:

```bash
$ python script.py
usage: script.py [-h] --number NUMBER [--format {json,xml}]
script.py: error: the following arguments are required: --number

$ python script.py --number abc
script.py: error: argument --number: invalid int value: 'abc'

$ python script.py --number 5 --format csv
script.py: error: argument --format: invalid choice: 'csv' (choose from 'json', 'xml')

$ python script.py --number 5 --unknown flag
script.py: error: unrecognized arguments: --unknown flag
```

### Custom Error Messages

Override error messages for better clarity:

```python
import argparse
import sys

class CustomArgumentParser(argparse.ArgumentParser):
    """Custom parser with better error messages."""

    def error(self, message):
        """Override error method to customize messages."""
        sys.stderr.write(f'Error: {message}\n')
        self.print_help()
        sys.exit(2)

parser = CustomArgumentParser(description='Process files')
parser.add_argument('--input', required=True, help='input file')
parser.add_argument('--output', required=True, help='output file')

args = parser.parse_args()
```

### Graceful Error Handling

Handle errors gracefully in your application:

```python
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='File processor')
    parser.add_argument('--input', type=Path, required=True, help='input file')
    parser.add_argument('--output', type=Path, required=True, help='output file')
    parser.add_argument('--verbose', action='store_true', help='verbose output')

    # Parse arguments
    try:
        args = parser.parse_args()
    except SystemExit as e:
        # argparse calls sys.exit() on error
        # This catches it if you need custom cleanup
        return e.code

    # Validate arguments
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        return 1

    if args.output.exists():
        response = input(f"Output file {args.output} exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Aborted")
            return 0

    # Process files
    try:
        with args.input.open('r') as f_in, args.output.open('w') as f_out:
            # Process
            content = f_in.read()
            f_out.write(content.upper())

        if args.verbose:
            print(f"Processed {args.input} -> {args.output}")

        return 0

    except Exception as e:
        print(f"Error processing files: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
```

### User-Friendly Help Messages

Write helpful descriptions:

```python
import argparse

parser = argparse.ArgumentParser(
    description='''
    Process and transform text files with various options.

    This tool reads input files, applies transformations, and
    writes the results to output files.
    ''',
    epilog='''
Examples:
  # Basic usage
  %(prog)s --input data.txt --output results.txt

  # With transformations
  %(prog)s -i data.txt -o results.txt --uppercase --trim

  # Verbose mode
  %(prog)s -i data.txt -o results.txt -v

For more information, see the documentation at:
https://example.com/docs
    ''',
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Clear, descriptive help for each argument
parser.add_argument(
    '--input', '-i',
    type=Path,
    required=True,
    metavar='FILE',
    help='input text file to process'
)

parser.add_argument(
    '--output', '-o',
    type=Path,
    required=True,
    metavar='FILE',
    help='output file for processed results'
)

parser.add_argument(
    '--uppercase',
    action='store_true',
    help='convert all text to uppercase'
)

parser.add_argument(
    '--trim',
    action='store_true',
    help='remove leading and trailing whitespace from lines'
)

parser.add_argument(
    '--verbose', '-v',
    action='count',
    default=0,
    help='increase output verbosity (can be repeated: -v, -vv, -vvv)'
)

args = parser.parse_args()
```

### Progress Feedback

Provide feedback for long-running operations:

```python
import argparse
import sys
from pathlib import Path
from time import sleep

def process_files(files, verbose=0):
    """Process multiple files with progress feedback."""
    total = len(files)

    for i, file in enumerate(files, 1):
        if verbose > 0:
            print(f"[{i}/{total}] Processing {file}...", end='')
            sys.stdout.flush()

        # Simulate processing
        sleep(0.5)

        if verbose > 0:
            print(" done")
        elif i % 10 == 0:
            print(f"Progress: {i}/{total} files")

def main():
    parser = argparse.ArgumentParser(description='Batch file processor')
    parser.add_argument('files', nargs='+', type=Path, help='files to process')
    parser.add_argument('-v', '--verbose', action='count', default=0)

    args = parser.parse_args()

    print(f"Processing {len(args.files)} files...")
    process_files(args.files, verbose=args.verbose)
    print("Done!")

if __name__ == '__main__':
    main()
```

### Configuration File Support

Combine command-line arguments with config files:

```python
import argparse
import json
from pathlib import Path

def load_config(config_file):
    """Load configuration from JSON file."""
    try:
        with open(config_file) as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}

def main():
    parser = argparse.ArgumentParser(description='Configurable tool')

    # Config file
    parser.add_argument(
        '--config',
        type=Path,
        help='configuration file (JSON format)'
    )

    # Other arguments
    parser.add_argument('--host', help='server host')
    parser.add_argument('--port', type=int, help='server port')
    parser.add_argument('--verbose', action='store_true', help='verbose output')

    args = parser.parse_args()

    # Load config file if provided
    config = {}
    if args.config:
        config = load_config(args.config)

    # Command-line arguments override config file
    host = args.host or config.get('host', 'localhost')
    port = args.port or config.get('port', 8080)
    verbose = args.verbose or config.get('verbose', False)

    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Verbose: {verbose}")

if __name__ == '__main__':
    main()
```

---

## Advanced argparse Features

### Namespace Objects

Arguments are stored in a Namespace object:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name')
parser.add_argument('--age', type=int)

args = parser.parse_args(['--name', 'Alice', '--age', '30'])

# Access as attributes
print(args.name)  # 'Alice'
print(args.age)   # 30

# Convert to dict
args_dict = vars(args)
print(args_dict)  # {'name': 'Alice', 'age': 30}

# Create custom namespace
custom_ns = argparse.Namespace(name='Bob', age=25)
args = parser.parse_args(['--age', '30'], namespace=custom_ns)
print(args.name)  # 'Bob' (from namespace)
print(args.age)   # 30 (from command-line)
```

### Argument Abbreviation

argparse allows abbreviating long options (unless disabled):

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--version', action='store_true')

# These all work:
args = parser.parse_args(['--verbose'])
args = parser.parse_args(['--verb'])
args = parser.parse_args(['--v'])  # Ambiguous! Error.

# Disable abbreviation
parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args(['--verbose'])  # Works
args = parser.parse_args(['--verb'])     # Error: unrecognized argument
```

### Parsing Partial Arguments

Parse only known arguments, leaving unknown ones:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--known', help='known argument')

# Parse only known arguments
args, unknown = parser.parse_known_args(['--known', 'value', '--unknown', 'arg'])

print(args.known)   # 'value'
print(unknown)      # ['--unknown', 'arg']

# Useful for plugins or passing arguments to subprocesses
```

### Argument Defaults from Environment

Set defaults from environment variables:

```python
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument(
    '--api-key',
    default=os.environ.get('API_KEY'),
    help='API key (default: $API_KEY environment variable)'
)

parser.add_argument(
    '--port',
    type=int,
    default=int(os.environ.get('PORT', '8080')),
    help='server port (default: $PORT or 8080)'
)

args = parser.parse_args()
```

### ArgumentDefaultsHelpFormatter

Automatically show default values in help:

```python
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument('--threads', type=int, default=4, help='number of threads')
parser.add_argument('--timeout', type=int, default=30, help='timeout in seconds')

# Help output will show:
# --threads THREADS     number of threads (default: 4)
# --timeout TIMEOUT     timeout in seconds (default: 30)
```

### Custom Formatter Classes

```python
import argparse

# Raw description (preserves formatting)
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Raw help (preserves formatting for all text)
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter
)

# Show defaults
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

# Show metavar only once
parser = argparse.ArgumentParser(
    formatter_class=argparse.MetavarTypeHelpFormatter
)

# Custom formatter
class CustomFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        # Customize how arguments are displayed
        return super()._format_action_invocation(action)

parser = argparse.ArgumentParser(formatter_class=CustomFormatter)
```

### Parent Parsers

Share common arguments across multiple parsers:

```python
import argparse

# Parent parser with common arguments
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--verbose', '-v', action='count', default=0)
parent_parser.add_argument('--config', type=Path)

# Child parsers inherit parent arguments
parser1 = argparse.ArgumentParser(parents=[parent_parser])
parser1.add_argument('--input', required=True)

parser2 = argparse.ArgumentParser(parents=[parent_parser])
parser2.add_argument('--output', required=True)

# Both parsers have --verbose and --config
args1 = parser1.parse_args(['--input', 'file.txt', '-v'])
args2 = parser2.parse_args(['--output', 'out.txt', '--config', 'cfg.json'])
```

### Argument Dependencies

Implement complex argument dependencies:

```python
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--format', choices=['json', 'xml', 'custom'])
parser.add_argument('--custom-template', help='template for custom format')

args = parser.parse_args()

# Validate dependencies after parsing
if args.format == 'custom' and not args.custom_template:
    parser.error('--custom-template is required when --format=custom')

if args.custom_template and args.format != 'custom':
    print("Warning: --custom-template ignored (--format must be custom)")
```

### Conditional Requirements

Make arguments required based on other arguments:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mode', choices=['local', 'remote'], required=True)
parser.add_argument('--host', help='remote host')
parser.add_argument('--port', type=int, help='remote port')
parser.add_argument('--path', help='local path')

args = parser.parse_args()

# Conditional validation
if args.mode == 'remote':
    if not args.host or not args.port:
        parser.error('--mode=remote requires --host and --port')
elif args.mode == 'local':
    if not args.path:
        parser.error('--mode=local requires --path')
```

---

## Complete Code Examples

### Example 1: File Processing Tool

```python
#!/usr/bin/env python3
"""
File processing tool with comprehensive argument handling.
"""

import argparse
import sys
from pathlib import Path
from typing import List

def setup_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description='Process text files with various transformations',
        epilog='''
Examples:
  %(prog)s input.txt --output output.txt --uppercase
  %(prog)s *.txt --output-dir processed/ --trim --sort
  %(prog)s data.txt -o result.txt -v
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Input files
    parser.add_argument(
        'files',
        nargs='+',
        type=Path,
        metavar='FILE',
        help='input files to process'
    )

    # Output options (mutually exclusive)
    output_group = parser.add_mutually_exclusive_group(required=True)
    output_group.add_argument(
        '--output', '-o',
        type=Path,
        metavar='FILE',
        help='output file (for single input only)'
    )
    output_group.add_argument(
        '--output-dir',
        type=Path,
        metavar='DIR',
        help='output directory (for multiple inputs)'
    )

    # Transformation options
    transform_group = parser.add_argument_group('transformations')
    transform_group.add_argument(
        '--uppercase',
        action='store_true',
        help='convert to uppercase'
    )
    transform_group.add_argument(
        '--lowercase',
        action='store_true',
        help='convert to lowercase'
    )
    transform_group.add_argument(
        '--trim',
        action='store_true',
        help='trim whitespace from lines'
    )
    transform_group.add_argument(
        '--sort',
        action='store_true',
        help='sort lines alphabetically'
    )

    # Options
    parser.add_argument(
        '--overwrite',
        action='store_true',
        help='overwrite existing output files'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='count',
        default=0,
        help='increase verbosity (-v, -vv, -vvv)'
    )

    return parser

def validate_args(args: argparse.Namespace) -> None:
    """Validate argument combinations."""
    # Check single file with --output
    if args.output and len(args.files) > 1:
        print("Error: --output can only be used with a single input file")
        print("Use --output-dir for multiple files")
        sys.exit(1)

    # Check input files exist
    for file in args.files:
        if not file.exists():
            print(f"Error: Input file not found: {file}")
            sys.exit(1)
        if not file.is_file():
            print(f"Error: Not a file: {file}")
            sys.exit(1)

    # Check/create output directory
    if args.output_dir:
        if not args.output_dir.exists():
            if args.verbose > 0:
                print(f"Creating output directory: {args.output_dir}")
            args.output_dir.mkdir(parents=True)
        elif not args.output_dir.is_dir():
            print(f"Error: Not a directory: {args.output_dir}")
            sys.exit(1)

    # Check output file
    if args.output and args.output.exists() and not args.overwrite:
        response = input(f"Output file {args.output} exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Aborted")
            sys.exit(0)

def transform_text(text: str, args: argparse.Namespace) -> str:
    """Apply transformations to text."""
    lines = text.splitlines()

    if args.trim:
        lines = [line.strip() for line in lines]

    if args.uppercase:
        lines = [line.upper() for line in lines]
    elif args.lowercase:
        lines = [line.lower() for line in lines]

    if args.sort:
        lines.sort()

    return '\n'.join(lines)

def process_file(input_file: Path, output_file: Path, args: argparse.Namespace) -> None:
    """Process a single file."""
    if args.verbose > 0:
        print(f"Processing {input_file} -> {output_file}")

    # Read input
    try:
        text = input_file.read_text()
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return

    # Transform
    transformed = transform_text(text, args)

    # Write output
    try:
        output_file.write_text(transformed)
        if args.verbose > 1:
            print(f"  Wrote {len(transformed)} characters")
    except Exception as e:
        print(f"Error writing {output_file}: {e}")

def main() -> int:
    """Main entry point."""
    parser = setup_parser()
    args = parser.parse_args()

    # Validate arguments
    validate_args(args)

    # Process files
    total = len(args.files)
    for i, input_file in enumerate(args.files, 1):
        if args.output:
            output_file = args.output
        else:
            output_file = args.output_dir / input_file.name

        if args.verbose == 0 and total > 1 and i % 10 == 0:
            print(f"Progress: {i}/{total}")

        process_file(input_file, output_file, args)

    if args.verbose > 0:
        print(f"Processed {total} file(s)")

    return 0

if __name__ == '__main__':
    sys.exit(main())
```

### Example 2: Database CLI Tool with Subcommands

```python
#!/usr/bin/env python3
"""
Database CLI tool with multiple subcommands.
"""

import argparse
import sys
from pathlib import Path

def cmd_init(args: argparse.Namespace) -> int:
    """Initialize database."""
    print(f"Initializing database: {args.database}")
    if args.overwrite:
        print("  Overwriting existing database")
    return 0

def cmd_backup(args: argparse.Namespace) -> int:
    """Backup database."""
    print(f"Backing up {args.database} to {args.output}")
    if args.compress:
        print("  Using compression")
    return 0

def cmd_restore(args: argparse.Namespace) -> int:
    """Restore database."""
    print(f"Restoring {args.backup} to {args.database}")
    return 0

def cmd_query(args: argparse.Namespace) -> int:
    """Execute query."""
    if args.file:
        print(f"Executing query from {args.file}")
    else:
        print(f"Executing query: {args.sql}")

    if args.format:
        print(f"  Output format: {args.format}")

    return 0

def setup_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        prog='dbcli',
        description='Database command-line tool'
    )

    # Global arguments
    parser.add_argument(
        '--database',
        default='database.db',
        help='database file path (default: %(default)s)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='count',
        default=0,
        help='increase verbosity'
    )

    # Subcommands
    subparsers = parser.add_subparsers(
        dest='command',
        help='available commands',
        required=True
    )

    # init command
    init_parser = subparsers.add_parser(
        'init',
        help='initialize a new database'
    )
    init_parser.add_argument(
        '--overwrite',
        action='store_true',
        help='overwrite existing database'
    )
    init_parser.set_defaults(func=cmd_init)

    # backup command
    backup_parser = subparsers.add_parser(
        'backup',
        help='backup database'
    )
    backup_parser.add_argument(
        '--output', '-o',
        required=True,
        type=Path,
        help='backup file path'
    )
    backup_parser.add_argument(
        '--compress',
        action='store_true',
        help='compress backup'
    )
    backup_parser.set_defaults(func=cmd_backup)

    # restore command
    restore_parser = subparsers.add_parser(
        'restore',
        help='restore database from backup'
    )
    restore_parser.add_argument(
        'backup',
        type=Path,
        help='backup file to restore'
    )
    restore_parser.set_defaults(func=cmd_restore)

    # query command
    query_parser = subparsers.add_parser(
        'query',
        help='execute SQL query'
    )
    query_group = query_parser.add_mutually_exclusive_group(required=True)
    query_group.add_argument(
        '--sql',
        help='SQL query to execute'
    )
    query_group.add_argument(
        '--file', '-f',
        type=Path,
        help='SQL file to execute'
    )
    query_parser.add_argument(
        '--format',
        choices=['table', 'json', 'csv'],
        default='table',
        help='output format (default: %(default)s)'
    )
    query_parser.set_defaults(func=cmd_query)

    return parser

def main() -> int:
    """Main entry point."""
    parser = setup_parser()
    args = parser.parse_args()

    # Execute command
    return args.func(args)

if __name__ == '__main__':
    sys.exit(main())
```

### Example 3: Flexible Configuration Tool

```python
#!/usr/bin/env python3
"""
Configuration tool supporting multiple input sources.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

def load_config_file(path: Path) -> Dict[str, Any]:
    """Load configuration from JSON file."""
    try:
        with path.open() as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: Config file not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {path}: {e}")
        sys.exit(1)

def merge_configs(
    defaults: Dict[str, Any],
    file_config: Dict[str, Any],
    cli_args: argparse.Namespace
) -> Dict[str, Any]:
    """Merge configuration from multiple sources.

    Priority (highest to lowest):
    1. Command-line arguments
    2. Config file
    3. Default values
    """
    config = defaults.copy()
    config.update(file_config)

    # Override with CLI arguments (if provided)
    cli_dict = vars(cli_args)
    for key, value in cli_dict.items():
        if value is not None and key != 'config':
            config[key] = value

    return config

def setup_parser() -> argparse.ArgumentParser:
    """Create argument parser."""
    parser = argparse.ArgumentParser(
        description='Flexible configuration tool',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Config file
    parser.add_argument(
        '--config', '-c',
        type=Path,
        help='configuration file (JSON)'
    )

    # Server options
    server_group = parser.add_argument_group('server options')
    server_group.add_argument(
        '--host',
        help='server host'
    )
    server_group.add_argument(
        '--port',
        type=int,
        help='server port'
    )

    # Database options
    db_group = parser.add_argument_group('database options')
    db_group.add_argument(
        '--db-host',
        help='database host'
    )
    db_group.add_argument(
        '--db-port',
        type=int,
        help='database port'
    )
    db_group.add_argument(
        '--db-name',
        help='database name'
    )

    # Logging options
    log_group = parser.add_argument_group('logging options')
    log_group.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='logging level'
    )
    log_group.add_argument(
        '--log-file',
        type=Path,
        help='log file path'
    )

    return parser

def main() -> int:
    """Main entry point."""
    # Default configuration
    defaults = {
        'host': 'localhost',
        'port': 8080,
        'db_host': 'localhost',
        'db_port': 5432,
        'db_name': 'myapp',
        'log_level': 'INFO',
        'log_file': None
    }

    # Parse arguments
    parser = setup_parser()
    args = parser.parse_args()

    # Load config file
    file_config = {}
    if args.config:
        file_config = load_config_file(args.config)

    # Merge configurations
    config = merge_configs(defaults, file_config, args)

    # Display final configuration
    print("Final Configuration:")
    print("=" * 50)
    print(f"Server:")
    print(f"  Host: {config['host']}")
    print(f"  Port: {config['port']}")
    print(f"Database:")
    print(f"  Host: {config['db_host']}")
    print(f"  Port: {config['db_port']}")
    print(f"  Name: {config['db_name']}")
    print(f"Logging:")
    print(f"  Level: {config['log_level']}")
    print(f"  File: {config['log_file'] or '(stdout)'}")

    return 0

if __name__ == '__main__':
    sys.exit(main())
```

---

## Key Takeaways

### The Big Picture

1. **Two tools, different purposes**:
   - `sys.argv`: Raw list access for simple scripts
   - `argparse`: Professional parsing for real applications

2. **argparse provides structure**:
   - Automatic help generation
   - Type conversion and validation
   - Error messages and user feedback
   - Subcommands and complex workflows

3. **Command-line interfaces matter**:
   - Make tools reusable and scriptable
   - Enable automation without user interaction
   - Provide professional user experience
   - Integrate with pipelines and workflows

4. **Best practices apply**:
   - Validate early, provide clear errors
   - Document expected inputs
   - Support standard conventions
   - Test edge cases

### Quick Reference

**sys.argv basics**:

```python
import sys

program = sys.argv[0]        # Script name
args = sys.argv[1:]          # Actual arguments
count = len(sys.argv) - 1    # Number of arguments

# All values are strings
number = int(sys.argv[1])    # Manual conversion
```

**argparse basics**:

```python
import argparse

parser = argparse.ArgumentParser(description='...')
parser.add_argument('pos', help='positional arg')
parser.add_argument('--opt', help='optional arg')
args = parser.parse_args()

# Automatic type conversion
parser.add_argument('--num', type=int)
```

### Decision Guide

**Use sys.argv when**:

- Exactly 1-2 arguments
- No validation needed
- Quick throwaway script
- Performance critical

**Use argparse when**:

- 3+ arguments or any options
- Need help messages
- Type validation required
- User-facing tool
- Subcommands needed
- Professional quality

### Common Patterns

**Required positional arguments**:

```python
parser.add_argument('input', help='input file')
parser.add_argument('output', help='output file')
```

**Optional flags**:

```python
parser.add_argument('--verbose', '-v', action='store_true')
parser.add_argument('--debug', action='store_true')
```

**Options with values**:

```python
parser.add_argument('--output', '-o', required=True, help='output path')
parser.add_argument('--threads', type=int, default=4)
```

**Multiple values**:

```python
parser.add_argument('files', nargs='+', help='files to process')
parser.add_argument('--exclude', nargs='*', default=[])
```

**Mutually exclusive**:

```python
group = parser.add_mutually_exclusive_group()
group.add_argument('--json', action='store_true')
group.add_argument('--xml', action='store_true')
```

### Remember

- Start with `argparse` unless you have a reason not to
- Provide helpful error messages and documentation
- Validate arguments early and thoroughly
- Support standard conventions (`-h`, `--help`, `--version`)
- Use type converters for validation
- Organize complex tools with subcommands
- Test your interface with users
- Document with examples in help text

---

**Related Topics**: Learn about environment variables (`os.environ`), configuration files (JSON, YAML, TOML), and logging for complete application configuration.
