# Python File Operations: Reading, Writing, and Managing Files

## Table of Contents

1. [Understanding the Fundamentals](#understanding-the-fundamentals)
2. [Opening and Closing Files](#opening-and-closing-files)
3. [Reading Files](#reading-files)
4. [Writing Files](#writing-files)
5. [File Modes and Binary Operations](#file-modes-and-binary-operations)
6. [File Management with shutil](#file-management-with-shutil)
7. [Error Handling and Best Practices](#error-handling-and-best-practices)
8. [Complete Code Examples](#complete-code-examples)

---

## Understanding the Fundamentals

### What Are Files?

A **file** is a named collection of data stored on disk. Files can contain:

- **Text**: Human-readable characters (`.txt`, `.py`, `.csv`, `.json`)
- **Binary**: Raw bytes (`.jpg`, `.pdf`, `.zip`, `.exe`)

### File Operations Overview

Python provides several ways to work with files:

| Operation  | Description             | Common Use Cases                         |
| ---------- | ----------------------- | ---------------------------------------- |
| **Read**   | Get data from a file    | Load configuration, parse logs, read CSV |
| **Write**  | Put data into a file    | Save results, create reports, log events |
| **Append** | Add data to end of file | Append to logs, add records              |
| **Copy**   | Duplicate a file        | Backup files, create templates           |
| **Move**   | Relocate a file         | Organize files, rename                   |
| **Delete** | Remove a file           | Clean up temporary files                 |

### The File Object

When you open a file, Python creates a **file object** that provides methods to interact with the file:

```python
# Open a file
file = open('example.txt', 'r')

# File object attributes
print(file.name)      # 'example.txt'
print(file.mode)      # 'r'
print(file.closed)    # False

# Close the file
file.close()
print(file.closed)    # True
```

### Text vs Binary Files

**Text files**:

- Contain human-readable characters
- Use encoding (usually UTF-8)
- Line endings vary by OS (`\n` on Unix, `\r\n` on Windows)
- Examples: `.txt`, `.py`, `.csv`, `.json`, `.html`

**Binary files**:

- Contain raw bytes
- No encoding/decoding
- Exact byte-for-byte representation
- Examples: `.jpg`, `.pdf`, `.zip`, `.mp3`, `.exe`

```python
# Text file
with open('text.txt', 'r') as f:
    content = f.read()  # Returns string

# Binary file
with open('image.jpg', 'rb') as f:
    content = f.read()  # Returns bytes
```

### File Paths

Files are accessed via paths:

```python
# Relative path (relative to current directory)
file = open('data.txt', 'r')
file = open('folder/data.txt', 'r')

# Absolute path (full path from root)
file = open('/home/user/documents/data.txt', 'r')
file = open('C:/Users/user/documents/data.txt', 'r')  # Windows
```

**Note**: Use `pathlib` (covered in the next guide) for better path handling.

---

## Opening and Closing Files

### The open() Function

The `open()` function is the primary way to work with files:

```python
file = open(filename, mode, encoding=None, errors=None, newline=None)
```

**Basic usage**:

```python
# Open for reading
file = open('data.txt', 'r')

# Open for writing
file = open('output.txt', 'w')

# Open for appending
file = open('log.txt', 'a')
```

### File Modes

| Mode   | Description      | File Must Exist?        | Overwrites? | Position |
| ------ | ---------------- | ----------------------- | ----------- | -------- |
| `'r'`  | Read only        | ✅ Yes                  | ❌ No       | Start    |
| `'w'`  | Write only       | ❌ No (creates)         | ✅ Yes      | Start    |
| `'a'`  | Append only      | ❌ No (creates)         | ❌ No       | End      |
| `'x'`  | Exclusive create | ❌ No (fails if exists) | N/A         | Start    |
| `'r+'` | Read and write   | ✅ Yes                  | ❌ No       | Start    |
| `'w+'` | Write and read   | ❌ No (creates)         | ✅ Yes      | Start    |
| `'a+'` | Append and read  | ❌ No (creates)         | ❌ No       | End      |

**Add 'b' for binary mode**:

- `'rb'`: Read binary
- `'wb'`: Write binary
- `'ab'`: Append binary
- `'rb+'`: Read/write binary

**Examples**:

```python
# Read existing file
f = open('data.txt', 'r')

# Create new file (or overwrite existing)
f = open('output.txt', 'w')

# Append to file
f = open('log.txt', 'a')

# Exclusive create (fails if exists)
try:
    f = open('new.txt', 'x')
except FileExistsError:
    print("File already exists!")

# Read and write
f = open('data.txt', 'r+')

# Binary read
f = open('image.jpg', 'rb')
```

### Closing Files: The Manual Way

**Always close files** to free system resources:

```python
file = open('data.txt', 'r')
content = file.read()
file.close()  # ⚠️ Easy to forget!

# Check if closed
print(file.closed)  # True
```

**Problem**: If an error occurs, the file might never close:

```python
file = open('data.txt', 'r')
# If something crashes here...
content = file.read()
file.close()  # ...this never runs!
```

### Context Managers: The Right Way

**Context managers** automatically close files:

```python
with open('data.txt', 'r') as file:
    content = file.read()
    # File is automatically closed after this block
    # Even if an exception occurs!

# File is already closed here
print(file.closed)  # True
```

**Why context managers are better**:

1. ✅ Automatic cleanup (always closes)
2. ✅ Works even with exceptions
3. ✅ Cleaner, more readable code
4. ✅ Prevents resource leaks

**Multiple files**:

```python
# Open multiple files
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())
# Both files closed automatically
```

### Encoding

**Text files use encoding** to convert between bytes and characters:

```python
# UTF-8 (most common, recommended)
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Latin-1 (Western European)
with open('data.txt', 'r', encoding='latin-1') as f:
    content = f.read()

# ASCII
with open('data.txt', 'r', encoding='ascii') as f:
    content = f.read()
```

**Default encoding**:

- Windows: `cp1252` or `utf-8` (Python 3.15+)
- macOS/Linux: `utf-8`

**Always specify encoding explicitly**:

```python
# ❌ Bad (platform-dependent)
with open('data.txt', 'r') as f:
    content = f.read()

# ✅ Good (explicit)
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### Error Handling for Encoding

```python
# Ignore errors (skip invalid characters)
with open('data.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace errors with �
with open('data.txt', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Strict (default, raises UnicodeDecodeError)
with open('data.txt', 'r', encoding='utf-8', errors='strict') as f:
    content = f.read()
```

---

## Reading Files

### Reading Entire File

#### read() - Entire File as String

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # Returns entire file as single string

print(content)
print(f"File size: {len(content)} characters")
```

**When to use**:

- Small files that fit in memory
- Need entire content at once
- Processing as single unit

**Warning**: Large files can consume all memory!

#### read(size) - Read N Characters

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    chunk = f.read(100)  # Read first 100 characters
    print(chunk)
```

### Reading Lines

#### readline() - One Line at a Time

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    line1 = f.readline()  # First line (includes \n)
    line2 = f.readline()  # Second line
    line3 = f.readline()  # Third line

    # Empty string when EOF reached
    line4 = f.readline()  # '' if no more lines
```

#### readlines() - All Lines as List

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # Returns list of strings

# Each line includes newline character
for line in lines:
    print(repr(line))  # 'First line\n', 'Second line\n', etc.

# Remove newlines
clean_lines = [line.rstrip('\n') for line in lines]
```

**When to use**:

- Need all lines in a list
- Small files
- Random access to lines

**Warning**: Loads entire file into memory!

#### Iterating Over Lines (Best Practice)

```python
# Memory-efficient: reads one line at a time
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip('\n'))  # Remove trailing newline
```

**Why this is best**:

- ✅ Memory-efficient (doesn't load entire file)
- ✅ Works with huge files
- ✅ Clean, Pythonic syntax
- ✅ Automatic buffering

### Reading Line by Line Examples

```python
# Count lines
with open('data.txt', 'r', encoding='utf-8') as f:
    count = sum(1 for line in f)
print(f"File has {count} lines")

# Process each line
with open('data.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.rstrip()}")

# Filter lines
with open('data.txt', 'r', encoding='utf-8') as f:
    matching_lines = [line.rstrip() for line in f if 'keyword' in line]

# Find first matching line
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('ERROR'):
            print(f"Found error: {line.rstrip()}")
            break
```

### Reading with File Position

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    # Get current position
    pos = f.tell()
    print(f"Position: {pos}")  # 0 (start)

    # Read some data
    chunk = f.read(10)
    pos = f.tell()
    print(f"Position: {pos}")  # 10

    # Seek to specific position
    f.seek(0)  # Back to start
    pos = f.tell()
    print(f"Position: {pos}")  # 0

    # Seek relative to current position
    f.seek(5, 1)  # 5 bytes forward from current

    # Seek relative to end
    f.seek(-10, 2)  # 10 bytes before end
```

**seek() parameters**:

- `seek(offset, whence)`
- `whence`: 0 (start), 1 (current), 2 (end)
- Returns new position

### Reading Binary Files

```python
# Read entire binary file
with open('image.jpg', 'rb') as f:
    data = f.read()  # Returns bytes object
    print(f"File size: {len(data)} bytes")

# Read chunks
with open('image.jpg', 'rb') as f:
    chunk_size = 1024  # 1 KB
    while True:
        chunk = f.read(chunk_size)
        if not chunk:  # Empty bytes = EOF
            break
        process_chunk(chunk)
```

### Reading CSV Files

```python
import csv

# Using csv module (recommended)
with open('data.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)  # First row
    for row in reader:
        print(row)  # List of values

# DictReader (access by column name)
with open('data.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])
```

**Note**: Use `newline=''` for CSV files to handle line endings correctly.

### Reading JSON Files

```python
import json

# Read JSON file
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # Parses JSON to Python object

print(data['key'])

# Read JSON string
with open('data.json', 'r', encoding='utf-8') as f:
    content = f.read()
    data = json.loads(content)  # Parse string
```

---

## Writing Files

### Writing Text

#### write() - Write String

```python
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')
    f.write('Second line\n')
# File automatically closed and saved
```

**Important**: `write()` does not add newlines automatically!

```python
# ❌ Creates single line
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Line 1')
    f.write('Line 2')
# Result: "Line 1Line 2"

# ✅ Correct way
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
# Result: "Line 1\nLine 2\n"
```

#### writelines() - Write List of Strings

```python
lines = ['First line\n', 'Second line\n', 'Third line\n']

with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
```

**Important**: `writelines()` also doesn't add newlines!

```python
# ❌ No newlines added
lines = ['Line 1', 'Line 2', 'Line 3']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
# Result: "Line 1Line 2Line 3"

# ✅ Add newlines yourself
lines = ['Line 1', 'Line 2', 'Line 3']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(line + '\n' for line in lines)
# Result: "Line 1\nLine 2\nLine 3\n"
```

### Print to File

```python
# Using print() with file parameter
with open('output.txt', 'w', encoding='utf-8') as f:
    print('Hello, World!', file=f)  # Automatically adds newline
    print('Second line', file=f)
    print('Multiple', 'values', 'separated', file=f)
```

**Advantages of print()**:

- ✅ Automatically adds newlines
- ✅ Converts objects to strings
- ✅ Separates multiple arguments with spaces
- ✅ Familiar syntax

### Appending to Files

```python
# 'a' mode: append to end of file
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('New log entry\n')
    # Existing content preserved, new content added at end
```

**Append vs Write**:

```python
# 'w' mode: erases existing content
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('This erases everything\n')

# 'a' mode: keeps existing content
with open('file.txt', 'a', encoding='utf-8') as f:
    f.write('This is added to the end\n')
```

### Writing CSV Files

```python
import csv

# Write rows
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Write dictionaries
data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
]

with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()  # Write column names
    writer.writerows(data)
```

### Writing JSON Files

```python
import json

data = {
    'name': 'Alice',
    'age': 30,
    'hobbies': ['reading', 'coding', 'hiking']
}

# Write JSON file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)  # indent for pretty printing

# Compact format
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, separators=(',', ':'))
```

### Writing Binary Files

```python
# Write bytes
data = b'Binary data here'

with open('output.bin', 'wb') as f:
    f.write(data)

# Write integers as bytes
with open('output.bin', 'wb') as f:
    f.write(bytes([65, 66, 67]))  # Writes 'ABC'

# Copy binary file
with open('source.jpg', 'rb') as src, open('dest.jpg', 'wb') as dst:
    dst.write(src.read())
```

### Buffering and Flushing

```python
# Writes are buffered (stored in memory temporarily)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Line 1\n')
    # Not written to disk yet!

    f.flush()  # Force write to disk now
    f.write('Line 2\n')
    # Still buffered

# File automatically flushed and closed when context exits

# Unbuffered writing
with open('output.txt', 'w', encoding='utf-8', buffering=1) as f:
    f.write('This is written immediately\n')
```

**When to flush**:

- Writing logs before a crash
- Real-time monitoring
- Coordinating with other processes
- Before long-running operations

---

## File Modes and Binary Operations

### Complete Mode Reference

| Mode  | Read | Write | Create | Truncate | Position | Binary |
| ----- | ---- | ----- | ------ | -------- | -------- | ------ |
| `r`   | ✅   | ❌    | ❌     | ❌       | Start    | ❌     |
| `rb`  | ✅   | ❌    | ❌     | ❌       | Start    | ✅     |
| `w`   | ❌   | ✅    | ✅     | ✅       | Start    | ❌     |
| `wb`  | ❌   | ✅    | ✅     | ✅       | Start    | ✅     |
| `a`   | ❌   | ✅    | ✅     | ❌       | End      | ❌     |
| `ab`  | ❌   | ✅    | ✅     | ❌       | End      | ✅     |
| `x`   | ❌   | ✅    | ✅\*   | ❌       | Start    | ❌     |
| `xb`  | ❌   | ✅    | ✅\*   | ❌       | Start    | ✅     |
| `r+`  | ✅   | ✅    | ❌     | ❌       | Start    | ❌     |
| `rb+` | ✅   | ✅    | ❌     | ❌       | Start    | ✅     |
| `w+`  | ✅   | ✅    | ✅     | ✅       | Start    | ❌     |
| `wb+` | ✅   | ✅    | ✅     | ✅       | Start    | ✅     |
| `a+`  | ✅   | ✅    | ✅     | ❌       | End      | ❌     |
| `ab+` | ✅   | ✅    | ✅     | ❌       | End      | ✅     |

\*`x` modes fail if file exists (exclusive create)

### Mode Selection Guide

```python
# Read existing file
with open('file.txt', 'r') as f:
    content = f.read()

# Create/overwrite file
with open('file.txt', 'w') as f:
    f.write('New content')

# Add to end of file
with open('file.txt', 'a') as f:
    f.write('Appended content')

# Create only if doesn't exist
try:
    with open('file.txt', 'x') as f:
        f.write('New file only')
except FileExistsError:
    print("File already exists")

# Read and write (modify in place)
with open('file.txt', 'r+') as f:
    content = f.read()
    f.seek(0)
    f.write(content.upper())
    f.truncate()  # Remove everything after current position
```

### Binary Mode Operations

```python
# Read binary file
with open('image.png', 'rb') as f:
    data = f.read()  # bytes object
    print(f"Size: {len(data)} bytes")
    print(f"First 10 bytes: {data[:10]}")

# Write binary file
with open('output.bin', 'wb') as f:
    f.write(b'\x89PNG\r\n\x1a\n')  # PNG header

# Read/write in chunks (for large files)
with open('large.bin', 'rb') as src, open('copy.bin', 'wb') as dst:
    chunk_size = 8192  # 8 KB
    while True:
        chunk = src.read(chunk_size)
        if not chunk:
            break
        dst.write(chunk)
```

### Text vs Binary Examples

```python
# Text mode: automatic encoding/decoding
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, 世界!')  # Automatically encoded to bytes

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()  # Automatically decoded from bytes
    print(type(text))  # <class 'str'>

# Binary mode: no encoding/decoding
with open('text.txt', 'rb') as f:
    data = f.read()  # Raw bytes
    print(type(data))  # <class 'bytes'>
    print(data)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c!'
```

### Line Endings

Different operating systems use different line endings:

- **Unix/Linux/macOS**: `\n` (LF)
- **Windows**: `\r\n` (CRLF)
- **Old Mac**: `\r` (CR)

```python
# Text mode handles line endings automatically
with open('file.txt', 'r') as f:
    lines = f.readlines()
    # On Windows, \r\n is converted to \n automatically

# Binary mode preserves exact bytes
with open('file.txt', 'rb') as f:
    data = f.read()
    # Line endings unchanged (\r\n stays \r\n)

# Universal newlines (default in text mode)
with open('file.txt', 'r', newline=None) as f:
    # All line endings converted to \n
    content = f.read()

# Preserve exact line endings
with open('file.txt', 'r', newline='') as f:
    # Line endings not translated
    content = f.read()
```

---

## File Management with shutil

The `shutil` module provides high-level file operations:

```python
import shutil
from pathlib import Path
```

### Copying Files

#### shutil.copy() - Copy File (Preserve Permissions)

```python
import shutil

# Copy file to destination
shutil.copy('source.txt', 'destination.txt')

# Copy to directory (keeps same filename)
shutil.copy('source.txt', 'backup_folder/')

# Returns destination path
dest = shutil.copy('source.txt', 'destination.txt')
print(f"Copied to: {dest}")
```

**What it copies**:

- ✅ File content
- ✅ Permission bits
- ❌ Metadata (timestamps, etc.)

#### shutil.copy2() - Copy File (Preserve All Metadata)

```python
import shutil

# Copy with metadata
shutil.copy2('source.txt', 'destination.txt')
```

**What it copies**:

- ✅ File content
- ✅ Permission bits
- ✅ Metadata (last access time, last modification time)
- ✅ All file attributes

**Use `copy2()` for backups** to preserve timestamps.

#### shutil.copyfile() - Copy File Content Only

```python
import shutil

# Copy only the file contents
shutil.copyfile('source.txt', 'destination.txt')
```

**What it copies**:

- ✅ File content only
- ❌ No permissions
- ❌ No metadata

**Use when**: You only care about content, not attributes.

### Copying Directories

#### shutil.copytree() - Copy Entire Directory Tree

```python
import shutil

# Copy directory and all contents
shutil.copytree('source_dir', 'destination_dir')

# Copy with options
shutil.copytree(
    'source_dir',
    'destination_dir',
    ignore=shutil.ignore_patterns('*.tmp', '.DS_Store'),  # Skip patterns
    dirs_exist_ok=False  # Fail if destination exists (default)
)

# Copy only specific files
def copy_only_py(dir, files):
    """Ignore function: return files to ignore."""
    return [f for f in files if not f.endswith('.py')]

shutil.copytree('source_dir', 'dest_dir', ignore=copy_only_py)
```

**Options**:

- `ignore`: Function or pattern to skip files
- `dirs_exist_ok`: Allow destination to exist (Python 3.8+)
- `copy_function`: Custom copy function (default: `copy2`)

**Note**: Destination directory must not exist (unless `dirs_exist_ok=True`).

### Moving and Renaming

#### shutil.move() - Move or Rename Files/Directories

```python
import shutil

# Rename file
shutil.move('old_name.txt', 'new_name.txt')

# Move to directory
shutil.move('file.txt', 'folder/')

# Move to directory with new name
shutil.move('file.txt', 'folder/new_name.txt')

# Move directory
shutil.move('old_folder', 'new_folder')

# Returns destination path
dest = shutil.move('source.txt', 'destination.txt')
```

**Behavior**:

- If destination is a directory, moves file into it
- If destination is a filename, renames/moves to that name
- Works across filesystems (copies then deletes if needed)

### Deleting Files and Directories

#### os.remove() - Delete File

```python
import os

# Delete a file
os.remove('file.txt')

# Check if exists first
if os.path.exists('file.txt'):
    os.remove('file.txt')
```

#### os.rmdir() - Delete Empty Directory

```python
import os

# Delete empty directory only
os.rmdir('empty_folder')

# Fails if directory is not empty
try:
    os.rmdir('full_folder')
except OSError as e:
    print(f"Cannot delete: {e}")
```

#### shutil.rmtree() - Delete Directory Tree

```python
import shutil

# Delete directory and all contents (⚠️ DANGEROUS!)
shutil.rmtree('folder')

# With error handling
def handle_error(func, path, exc_info):
    print(f"Error deleting {path}: {exc_info}")

shutil.rmtree('folder', onerror=handle_error)

# Ignore errors
shutil.rmtree('folder', ignore_errors=True)
```

**⚠️ WARNING**: `rmtree()` permanently deletes everything! No recycle bin!

### Disk Usage

#### shutil.disk_usage() - Get Disk Space Info

```python
import shutil

usage = shutil.disk_usage('/')

print(f"Total: {usage.total / (1024**3):.2f} GB")
print(f"Used: {usage.used / (1024**3):.2f} GB")
print(f"Free: {usage.free / (1024**3):.2f} GB")

# Check if enough space
required_space = 1024 * 1024 * 1024  # 1 GB
if usage.free > required_space:
    print("Enough space available")
```

### Archive Operations

#### Creating Archives

```python
import shutil

# Create zip archive
shutil.make_archive(
    'backup',           # Base name (without extension)
    'zip',              # Format: 'zip', 'tar', 'gztar', 'bztar', 'xztar'
    'folder_to_backup'  # Directory to archive
)
# Creates 'backup.zip'

# Create tar.gz archive
shutil.make_archive('backup', 'gztar', 'folder')
# Creates 'backup.tar.gz'

# Archive with specific output directory
shutil.make_archive(
    '/backups/backup',  # Full path
    'zip',
    root_dir='folder'
)
```

#### Extracting Archives

```python
import shutil

# Extract archive
shutil.unpack_archive('backup.zip', 'extracted_folder')

# Extract specific format
shutil.unpack_archive('backup.tar.gz', 'extracted_folder', 'gztar')

# Extract to current directory
shutil.unpack_archive('backup.zip')
```

**Supported formats**:

- `zip`: ZIP archive
- `tar`: Uncompressed TAR
- `gztar`: Gzip compressed TAR
- `bztar`: Bzip2 compressed TAR
- `xztar`: XZ compressed TAR

### Safe File Operations

```python
import shutil
import os
from pathlib import Path

def safe_copy(src, dst):
    """Copy file with safety checks."""
    src_path = Path(src)
    dst_path = Path(dst)

    # Check source exists
    if not src_path.exists():
        raise FileNotFoundError(f"Source not found: {src}")

    # Check destination doesn't exist
    if dst_path.exists():
        raise FileExistsError(f"Destination already exists: {dst}")

    # Check enough disk space
    src_size = src_path.stat().st_size
    usage = shutil.disk_usage(dst_path.parent)
    if usage.free < src_size:
        raise OSError(f"Not enough disk space")

    # Perform copy
    shutil.copy2(src, dst)

    # Verify copy
    if dst_path.stat().st_size != src_size:
        dst_path.unlink()
        raise OSError("Copy verification failed")

    return dst_path

# Usage
try:
    result = safe_copy('important.txt', 'backup.txt')
    print(f"Successfully copied to: {result}")
except Exception as e:
    print(f"Copy failed: {e}")
```

---

## Error Handling and Best Practices

### Common File Exceptions

| Exception            | When It Occurs               | How to Handle                              |
| -------------------- | ---------------------------- | ------------------------------------------ |
| `FileNotFoundError`  | File doesn't exist           | Check existence first                      |
| `PermissionError`    | No permission to access      | Check permissions, run as appropriate user |
| `IsADirectoryError`  | Expected file, got directory | Check if path is file                      |
| `NotADirectoryError` | Expected directory, got file | Check if path is directory                 |
| `FileExistsError`    | File already exists          | Use different name or overwrite            |
| `OSError`            | General OS-level error       | Check disk space, file system              |
| `UnicodeDecodeError` | Wrong encoding               | Try different encoding                     |
| `IOError`            | I/O operation failed         | Check disk, permissions                    |

### Exception Handling Patterns

#### Basic Try-Except

```python
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"Unexpected error: {e}")
```

#### Check Before Opening

```python
import os

# Check if file exists
if os.path.exists('file.txt'):
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
else:
    print("File not found")

# Check if readable
if os.access('file.txt', os.R_OK):
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
```

#### Create if Not Exists

```python
import os

# Create file if it doesn't exist
if not os.path.exists('log.txt'):
    with open('log.txt', 'w', encoding='utf-8') as f:
        f.write('')  # Create empty file

# Or use 'a' mode (creates if needed)
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('Log entry\n')
```

#### Safe Writing Pattern

```python
import os
import tempfile
import shutil

def safe_write(filename, content):
    """Write to temporary file, then move to destination."""
    # Create temporary file in same directory
    dir_name = os.path.dirname(filename)

    with tempfile.NamedTemporaryFile(
        mode='w',
        encoding='utf-8',
        dir=dir_name,
        delete=False
    ) as tmp_file:
        tmp_file.write(content)
        tmp_path = tmp_file.name

    try:
        # Atomically replace original file
        shutil.move(tmp_path, filename)
    except:
        # Clean up temporary file on error
        os.remove(tmp_path)
        raise

# Usage
safe_write('important.txt', 'Critical data')
```

### Best Practices

#### 1. Always Use Context Managers

```python
# ❌ Manual closing (error-prone)
f = open('file.txt', 'r')
content = f.read()
f.close()

# ✅ Context manager (automatic cleanup)
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

#### 2. Specify Encoding Explicitly

```python
# ❌ Platform-dependent encoding
with open('file.txt', 'r') as f:
    content = f.read()

# ✅ Explicit encoding
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

#### 3. Use Appropriate File Modes

```python
# ❌ Using 'w' when you meant to append
with open('log.txt', 'w') as f:  # Erases existing content!
    f.write('New entry\n')

# ✅ Use 'a' for appending
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('New entry\n')
```

#### 4. Handle Large Files Efficiently

```python
# ❌ Loading entire file into memory
with open('huge.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # Memory exhausted!

# ✅ Process line by line
with open('huge.txt', 'r', encoding='utf-8') as f:
    for line in f:  # Memory-efficient
        process(line)
```

#### 5. Validate Paths

```python
from pathlib import Path

def safe_read(filepath):
    """Read file with validation."""
    path = Path(filepath)

    # Check exists
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    # Check is file
    if not path.is_file():
        raise IsADirectoryError(f"Not a file: {filepath}")

    # Check readable
    if not os.access(path, os.R_OK):
        raise PermissionError(f"Cannot read: {filepath}")

    # Read file
    with path.open('r', encoding='utf-8') as f:
        return f.read()
```

#### 6. Use Temporary Files for Intermediate Results

```python
import tempfile

# Create temporary file (auto-deleted)
with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=True) as tmp:
    tmp.write('Temporary data')
    tmp.flush()

    # Process temporary file
    process(tmp.name)
# File automatically deleted here

# Create temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    # Use tmpdir for temporary files
    filepath = os.path.join(tmpdir, 'temp.txt')
    with open(filepath, 'w') as f:
        f.write('Data')
# Directory and all contents deleted here
```

---

## Complete Code Examples

### Example 1: Log File Analyzer

```python
#!/usr/bin/env python3
"""
Analyze log files and generate reports.
"""

import os
from pathlib import Path
from datetime import datetime
from collections import Counter

def analyze_log(log_file):
    """Analyze log file and return statistics."""
    stats = {
        'total_lines': 0,
        'error_count': 0,
        'warning_count': 0,
        'info_count': 0,
        'status_codes': Counter(),
        'errors': []
    }

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                stats['total_lines'] += 1
                line = line.strip()

                # Count log levels
                if 'ERROR' in line:
                    stats['error_count'] += 1
                    stats['errors'].append(line)
                elif 'WARNING' in line:
                    stats['warning_count'] += 1
                elif 'INFO' in line:
                    stats['info_count'] += 1

                # Extract status codes (if present)
                if 'status=' in line:
                    parts = line.split('status=')
                    if len(parts) > 1:
                        code = parts[1].split()[0]
                        stats['status_codes'][code] += 1

    except FileNotFoundError:
        print(f"Error: Log file not found: {log_file}")
        return None
    except PermissionError:
        print(f"Error: Permission denied: {log_file}")
        return None

    return stats

def generate_report(stats, output_file):
    """Generate analysis report."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*50 + "\n")
        f.write("Log Analysis Report\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*50 + "\n\n")

        f.write(f"Total Lines: {stats['total_lines']}\n")
        f.write(f"Errors: {stats['error_count']}\n")
        f.write(f"Warnings: {stats['warning_count']}\n")
        f.write(f"Info: {stats['info_count']}\n\n")

        if stats['status_codes']:
            f.write("Status Code Distribution:\n")
            for code, count in stats['status_codes'].most_common():
                f.write(f"  {code}: {count}\n")
            f.write("\n")

        if stats['errors']:
            f.write("Recent Errors:\n")
            for error in stats['errors'][-10:]:  # Last 10 errors
                f.write(f"  {error}\n")

def main():
    log_file = 'application.log'
    output_file = 'log_analysis.txt'

    print(f"Analyzing {log_file}...")

    stats = analyze_log(log_file)
    if stats:
        generate_report(stats, output_file)
        print(f"Report generated: {output_file}")
        print(f"Found {stats['error_count']} errors, {stats['warning_count']} warnings")

if __name__ == '__main__':
    main()
```

### Example 2: File Backup Utility

```python
#!/usr/bin/env python3
"""
Backup utility with compression and rotation.
"""

import shutil
import os
from pathlib import Path
from datetime import datetime
import sys

def create_backup(source_dir, backup_dir, keep_last=5):
    """
    Create compressed backup with rotation.

    Args:
        source_dir: Directory to backup
        backup_dir: Where to store backups
        keep_last: Number of backups to keep
    """
    source_path = Path(source_dir)
    backup_path = Path(backup_dir)

    # Validate source
    if not source_path.exists():
        print(f"Error: Source directory not found: {source_dir}")
        return False

    if not source_path.is_dir():
        print(f"Error: Source is not a directory: {source_dir}")
        return False

    # Create backup directory
    backup_path.mkdir(parents=True, exist_ok=True)

    # Generate backup filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"backup_{source_path.name}_{timestamp}"
    backup_file = backup_path / backup_name

    try:
        # Check disk space
        source_size = sum(f.stat().st_size for f in source_path.rglob('*') if f.is_file())
        usage = shutil.disk_usage(backup_path)

        # Require 2x space (for compression overhead)
        if usage.free < source_size * 2:
            print(f"Error: Not enough disk space")
            print(f"Required: {source_size * 2 / (1024**3):.2f} GB")
            print(f"Available: {usage.free / (1024**3):.2f} GB")
            return False

        # Create backup
        print(f"Creating backup: {backup_name}")
        archive_path = shutil.make_archive(
            str(backup_file),
            'gztar',
            source_path.parent,
            source_path.name
        )

        print(f"Backup created: {archive_path}")

        # Get backup size
        backup_size = Path(archive_path).stat().st_size
        print(f"Backup size: {backup_size / (1024**2):.2f} MB")
        print(f"Compression ratio: {(1 - backup_size / source_size) * 100:.1f}%")

        # Rotate old backups
        rotate_backups(backup_path, keep_last)

        return True

    except Exception as e:
        print(f"Error creating backup: {e}")
        return False

def rotate_backups(backup_dir, keep_last):
    """Delete old backups, keeping only the most recent."""
    backup_path = Path(backup_dir)

    # Find all backup files
    backups = sorted(
        backup_path.glob('backup_*.tar.gz'),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    # Delete old backups
    if len(backups) > keep_last:
        print(f"\nRotating backups (keeping last {keep_last})...")
        for old_backup in backups[keep_last:]:
            print(f"Deleting old backup: {old_backup.name}")
            old_backup.unlink()

def restore_backup(backup_file, restore_dir):
    """Restore from backup archive."""
    backup_path = Path(backup_file)
    restore_path = Path(restore_dir)

    # Validate backup file
    if not backup_path.exists():
        print(f"Error: Backup file not found: {backup_file}")
        return False

    # Create restore directory
    restore_path.mkdir(parents=True, exist_ok=True)

    try:
        print(f"Restoring backup: {backup_path.name}")
        shutil.unpack_archive(backup_path, restore_path)
        print(f"Restored to: {restore_path}")
        return True

    except Exception as e:
        print(f"Error restoring backup: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Backup:  python backup.py backup <source_dir> [backup_dir]")
        print("  Restore: python backup.py restore <backup_file> <restore_dir>")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'backup':
        source_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
        backup_dir = sys.argv[3] if len(sys.argv) > 3 else 'backups'

        success = create_backup(source_dir, backup_dir)
        sys.exit(0 if success else 1)

    elif command == 'restore':
        if len(sys.argv) < 4:
            print("Error: Restore requires <backup_file> and <restore_dir>")
            sys.exit(1)

        backup_file = sys.argv[2]
        restore_dir = sys.argv[3]

        success = restore_backup(backup_file, restore_dir)
        sys.exit(0 if success else 1)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

### Example 3: CSV Data Processor

```python
#!/usr/bin/env python3
"""
Process CSV files with filtering and transformation.
"""

import csv
import sys
from pathlib import Path
from collections import defaultdict

def read_csv(filepath):
    """Read CSV file and return rows as dictionaries."""
    rows = []

    try:
        with open(filepath, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None
    except csv.Error as e:
        print(f"Error reading CSV: {e}")
        return None

    return rows

def filter_rows(rows, column, value):
    """Filter rows where column equals value."""
    return [row for row in rows if row.get(column) == value]

def aggregate_by_column(rows, group_by, agg_column):
    """Group rows by column and sum another column."""
    groups = defaultdict(float)

    for row in rows:
        key = row.get(group_by)
        value = float(row.get(agg_column, 0))
        groups[key] += value

    return dict(groups)

def write_csv(filepath, rows, fieldnames=None):
    """Write rows to CSV file."""
    if not rows:
        print("Warning: No data to write")
        return

    # Use provided fieldnames or infer from first row
    if fieldnames is None:
        fieldnames = list(rows[0].keys())

    try:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Wrote {len(rows)} rows to {filepath}")

    except Exception as e:
        print(f"Error writing CSV: {e}")

def generate_summary(rows, output_file):
    """Generate summary report."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*50 + "\n")
        f.write("Data Summary\n")
        f.write("="*50 + "\n\n")

        f.write(f"Total Rows: {len(rows)}\n\n")

        if rows:
            f.write("Columns:\n")
            for col in rows[0].keys():
                f.write(f"  - {col}\n")

            f.write("\nSample Data (first 5 rows):\n")
            for i, row in enumerate(rows[:5], 1):
                f.write(f"\nRow {i}:\n")
                for key, value in row.items():
                    f.write(f"  {key}: {value}\n")

def main():
    input_file = 'data.csv'
    output_file = 'processed.csv'
    summary_file = 'summary.txt'

    print(f"Reading {input_file}...")
    rows = read_csv(input_file)

    if rows is None:
        sys.exit(1)

    print(f"Loaded {len(rows)} rows")

    # Example: Filter rows
    # filtered = filter_rows(rows, 'status', 'active')
    # print(f"Filtered to {len(filtered)} active rows")

    # Example: Aggregate
    # totals = aggregate_by_column(rows, 'category', 'amount')
    # print(f"Aggregated by category: {totals}")

    # Write processed data
    write_csv(output_file, rows)

    # Generate summary
    generate_summary(rows, summary_file)
    print(f"Summary written to {summary_file}")

if __name__ == '__main__':
    main()
```

---

## Key Takeaways

### The Big Picture

1. **Files are fundamental**:
   - Persistent data storage
   - Program input and output
   - Configuration and logs
   - Data exchange between programs

2. **Context managers are essential**:
   - Always use `with` statements
   - Automatic resource cleanup
   - Exception safety
   - Cleaner code

3. **Choose the right tool**:
   - Basic operations: `open()`, `read()`, `write()`
   - File management: `shutil` module
   - Path operations: `pathlib` (next guide)

4. **Handle errors gracefully**:
   - Files can fail in many ways
   - Validate inputs
   - Provide clear error messages
   - Clean up on failures

### Quick Reference

**Reading files**:

```python
# Read entire file
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Read lines
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        process(line)
```

**Writing files**:

```python
# Write/overwrite
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('content\n')

# Append
with open('file.txt', 'a', encoding='utf-8') as f:
    f.write('more content\n')
```

**File operations**:

```python
import shutil

# Copy
shutil.copy2('source.txt', 'dest.txt')

# Move/rename
shutil.move('old.txt', 'new.txt')

# Delete file
os.remove('file.txt')

# Delete directory
shutil.rmtree('folder')
```

### Best Practices Checklist

- ✅ Always use context managers (`with` statements)
- ✅ Specify encoding explicitly (`encoding='utf-8'`)
- ✅ Choose appropriate file mode (`'r'`, `'w'`, `'a'`)
- ✅ Handle exceptions (file not found, permission errors)
- ✅ Use `read()` for small files, iterate for large files
- ✅ Flush buffers for critical writes
- ✅ Use `shutil.copy2()` to preserve metadata
- ✅ Validate paths before operations
- ✅ Check disk space for large operations
- ✅ Use temporary files for intermediate results
- ❌ Never use `'w'` mode on important files without backups
- ❌ Don't load huge files entirely into memory
- ❌ Don't ignore exceptions

### Common Patterns

**Safe file reading**:

```python
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

**Safe file writing**:

```python
import tempfile
import shutil

# Write to temp file, then move
with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    tmp.write(content)
    tmp_path = tmp.name

shutil.move(tmp_path, 'final.txt')
```

**Processing large files**:

```python
with open('huge.txt', 'r', encoding='utf-8') as f:
    for line in f:  # Memory-efficient
        process(line)
```

### Remember

- Files are a critical part of most programs
- Context managers handle cleanup automatically
- Text files need encoding, binary files don't
- shutil provides high-level file operations
- Always handle errors - file operations fail often
- Test with edge cases (empty files, huge files, missing files)
- Back up before destructive operations
- Use appropriate tools for the job

---

**Related Topics**: Next, learn about `pathlib` for object-oriented path handling, and explore `os` and `glob` for advanced file system operations.
