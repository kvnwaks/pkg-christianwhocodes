# Python Path Operations: Working with Files and Directories Using pathlib

## Table of Contents

1. [Understanding the Fundamentals](#understanding-the-fundamentals)
2. [Creating and Manipulating Paths](#creating-and-manipulating-paths)
3. [Path Properties and Attributes](#path-properties-and-attributes)
4. [Navigating the File System](#navigating-the-file-system)
5. [File and Directory Operations](#file-and-directory-operations)
6. [Pattern Matching and Searching](#pattern-matching-and-searching)
7. [Cross-Platform Path Handling](#cross-platform-path-handling)
8. [Complete Code Examples](#complete-code-examples)

---

## Understanding the Fundamentals

### What is pathlib?

`pathlib` is Python's modern, object-oriented approach to file system paths. It provides:

- **Clean syntax**: Intuitive, chainable operations
- **Cross-platform**: Works on Windows, macOS, Linux
- **Type safety**: Path objects instead of strings
- **Rich functionality**: Built-in file operations

**Before pathlib (string-based)**:

```python
import os

# Clunky string manipulation
path = os.path.join('folder', 'subfolder', 'file.txt')
directory = os.path.dirname(path)
filename = os.path.basename(path)

# Awkward existence checks
if os.path.exists(path) and os.path.isfile(path):
    with open(path, 'r') as f:
        content = f.read()
```

**With pathlib (object-oriented)**:

```python
from pathlib import Path

# Clean, intuitive syntax
path = Path('folder') / 'subfolder' / 'file.txt'
directory = path.parent
filename = path.name

# Elegant existence checks and operations
if path.exists() and path.is_file():
    content = path.read_text()
```

### Why Use pathlib?

**Advantages**:

1. ✅ **Readable**: Code reads like natural language
2. ✅ **Safe**: Automatic handling of separators (`/` vs `\`)
3. ✅ **Convenient**: Built-in methods for common operations
4. ✅ **Modern**: Introduced in Python 3.4, standard since 3.6
5. ✅ **Chainable**: Combine operations smoothly

**Use pathlib when**:

- Working with file paths
- Navigating directories
- Checking file properties
- Building cross-platform applications
- Writing modern Python code

**Use os.path when**:

- Legacy code compatibility
- Need specific os.path features
- Working with older Python versions

### The Path Object

```python
from pathlib import Path

# Create a Path object
path = Path('folder/file.txt')

# Path objects are immutable
print(type(path))  # <class 'pathlib.PosixPath'> or WindowsPath

# Convert to string when needed
path_string = str(path)

# Most operations return new Path objects
new_path = path.with_suffix('.md')  # New object
print(path)      # folder/file.txt (unchanged)
print(new_path)  # folder/file.md (new)
```

### Path Types

```python
from pathlib import Path, PurePath, PosixPath, WindowsPath
from pathlib import PurePosixPath, PureWindowsPath

# Path (concrete path for current OS)
path = Path('file.txt')  # PosixPath on Unix, WindowsPath on Windows

# PurePath (path manipulation without filesystem access)
pure = PurePath('folder/file.txt')  # Works on any OS

# Platform-specific concrete paths (require matching OS)
posix_path = PosixPath('folder/file.txt')    # Unix-style, only on Unix
windows_path = WindowsPath('folder\\file.txt')  # Windows-style, only on Windows

# Platform-specific pure paths (work on any OS)
pure_posix = PurePosixPath('folder/file.txt')      # Unix-style, works anywhere
pure_windows = PureWindowsPath('folder\\file.txt')  # Windows-style, works anywhere
```

**Hierarchy**:

```
PurePath (abstract base)
├── PurePosixPath (Unix path manipulation, no filesystem)
└── PureWindowsPath (Windows path manipulation, no filesystem)

Path (concrete, requires matching OS)
├── PosixPath (Unix paths, Unix OS only)
└── WindowsPath (Windows paths, Windows OS only)
```

**When to use each**:

- `Path`: Default choice for file operations (90% of use cases)
- `PurePath`: Path manipulation without touching filesystem
- `PurePosixPath`: Manipulate Unix paths on any OS (e.g., processing logs)
- `PureWindowsPath`: Manipulate Windows paths on any OS (e.g., parsing configs)
- `PosixPath`/`WindowsPath`: Platform-specific file operations (rarely needed)

**Key difference between Pure and Concrete**:

```python
# PurePath: Path manipulation only (no filesystem access)
pure = PurePosixPath('/home/user/file.txt')
# Can manipulate: pure.name, pure.parent, pure.with_suffix()
# Cannot do: pure.exists(), pure.read_text(), pure.mkdir()

# Path: Full filesystem operations
concrete = Path('/home/user/file.txt')
# Can do everything: .name, .exists(), .read_text(), etc.
```

---

## Creating and Manipulating Paths

### Creating Path Objects

```python
from pathlib import Path

# From string
path = Path('folder/file.txt')

# From multiple parts
path = Path('folder', 'subfolder', 'file.txt')

# Using / operator (recommended)
path = Path('folder') / 'subfolder' / 'file.txt'

# Current directory
current = Path('.')
current_absolute = Path.cwd()

# Home directory
home = Path.home()  # /home/username or C:\Users\username

# Absolute path
absolute = Path('/usr/local/bin')

# Relative path
relative = Path('../parent_folder/file.txt')
```

### Path Construction

```python
from pathlib import Path

# Building paths with / operator
base = Path('projects')
project = base / 'myapp'
source = project / 'src'
main_file = source / 'main.py'

print(main_file)  # projects/myapp/src/main.py

# Combining with strings
path = Path('folder') / 'subfolder' / 'file.txt'

# From parts
parts = ['folder', 'subfolder', 'file.txt']
path = Path(*parts)

# Joining multiple paths
path1 = Path('folder')
path2 = Path('subfolder/file.txt')
combined = path1 / path2
print(combined)  # folder/subfolder/file.txt
```

### Path Modification

#### Changing File Names

```python
from pathlib import Path

path = Path('folder/document.txt')

# Change filename (keep directory)
new_path = path.with_name('report.txt')
print(new_path)  # folder/report.txt

# Change extension
new_path = path.with_suffix('.md')
print(new_path)  # folder/document.md

# Change stem (filename without extension)
new_path = path.with_stem('article')  # Python 3.9+
print(new_path)  # folder/article.txt

# Remove extension
new_path = path.with_suffix('')
print(new_path)  # folder/document
```

#### Working with Directories

```python
from pathlib import Path

path = Path('projects/myapp/src/main.py')

# Get parent directory
parent = path.parent
print(parent)  # projects/myapp/src

# Get multiple levels up
grandparent = path.parent.parent
print(grandparent)  # projects/myapp

# Get all parents
for p in path.parents:
    print(p)
# Output:
# projects/myapp/src
# projects/myapp
# projects
# .
```

### Absolute and Relative Paths

```python
from pathlib import Path

# Get absolute path
relative = Path('folder/file.txt')
absolute = relative.resolve()
print(absolute)  # /home/user/current_dir/folder/file.txt

# Get absolute without resolving symlinks
absolute = relative.absolute()

# Make path relative to another
base = Path('/home/user/projects')
full = Path('/home/user/projects/myapp/src/main.py')
relative = full.relative_to(base)
print(relative)  # myapp/src/main.py

# Check if path is absolute
print(Path('/home/user').is_absolute())    # True
print(Path('folder/file').is_absolute())   # False

# Check if path is relative to another
base = Path('/home/user')
path = Path('/home/user/documents/file.txt')
print(path.is_relative_to(base))  # True (Python 3.9+)
```

### Path Normalization

```python
from pathlib import Path

# Resolve removes . and ..
path = Path('folder/../another/./file.txt')
normalized = path.resolve()
print(normalized)  # /absolute/path/another/file.txt

# Remove redundant separators
path = Path('folder//subfolder///file.txt')
print(path)  # folder/subfolder/file.txt (automatically normalized)

# Resolve symlinks
symlink = Path('shortcut.txt')  # Points to real_file.txt
real_path = symlink.resolve()
print(real_path)  # /path/to/real_file.txt
```

---

## Path Properties and Attributes

### Path Components

```python
from pathlib import Path

path = Path('/home/user/documents/report.txt')

# Full path
print(path)  # /home/user/documents/report.txt

# Individual components
print(path.name)       # report.txt (filename with extension)
print(path.stem)       # report (filename without extension)
print(path.suffix)     # .txt (file extension)
print(path.suffixes)   # ['.txt'] (all extensions, for .tar.gz etc.)
print(path.parent)     # /home/user/documents (directory)

# Path parts as tuple
print(path.parts)      # ('/', 'home', 'user', 'documents', 'report.txt')

# Root and anchor
print(path.root)       # / (root directory)
print(path.anchor)     # / (anchor, includes drive on Windows)

# Drive (Windows only)
win_path = Path('C:/Users/user/file.txt')
print(win_path.drive)  # C: (on Windows)
```

**Component breakdown**:

```python
path = Path('/home/user/documents/report.backup.txt')

print(f"Full path: {path}")
print(f"Name: {path.name}")           # report.backup.txt
print(f"Stem: {path.stem}")           # report.backup
print(f"Suffix: {path.suffix}")       # .txt
print(f"Suffixes: {path.suffixes}")   # ['.backup', '.txt']
print(f"Parent: {path.parent}")       # /home/user/documents
```

### Multiple Extensions

```python
from pathlib import Path

# Handling multiple extensions (e.g., .tar.gz)
path = Path('archive.tar.gz')

print(path.suffix)    # .gz (last extension)
print(path.suffixes)  # ['.tar', '.gz'] (all extensions)
print(path.stem)      # archive.tar (name without last extension)

# Remove all extensions
name_only = Path(path.stem).stem
print(name_only)      # archive

# Change all extensions
new_path = Path(name_only).with_suffix('.zip')
print(new_path)       # archive.zip
```

### File Information

```python
from pathlib import Path

path = Path('document.txt')

if path.exists():
    # File metadata
    stats = path.stat()

    print(f"Size: {stats.st_size} bytes")
    print(f"Created: {stats.st_ctime}")
    print(f"Modified: {stats.st_mtime}")
    print(f"Accessed: {stats.st_atime}")
    print(f"Permissions: {oct(stats.st_mode)}")

    # Formatted file size
    size_mb = stats.st_size / (1024 * 1024)
    print(f"Size: {size_mb:.2f} MB")

    # Timestamps as datetime
    from datetime import datetime
    modified = datetime.fromtimestamp(stats.st_mtime)
    print(f"Last modified: {modified}")
```

### File Type Checking

```python
from pathlib import Path

path = Path('some_path')

# Check if exists
print(path.exists())    # True if file or directory exists

# Check type
print(path.is_file())      # True if regular file
print(path.is_dir())       # True if directory
print(path.is_symlink())   # True if symbolic link
print(path.is_socket())    # True if socket
print(path.is_fifo())      # True if FIFO (named pipe)
print(path.is_block_device())   # True if block device
print(path.is_char_device())    # True if character device

# Check if mount point
print(path.is_mount())     # True if mount point

# Check if reserved (Windows)
print(path.is_reserved())  # True if reserved name (Windows: CON, PRN, etc.)
```

### Permissions and Ownership

```python
from pathlib import Path
import stat

path = Path('file.txt')

if path.exists():
    stats = path.stat()
    mode = stats.st_mode

    # Check permissions
    is_readable = mode & stat.S_IRUSR
    is_writable = mode & stat.S_IWUSR
    is_executable = mode & stat.S_IXUSR

    print(f"Readable: {bool(is_readable)}")
    print(f"Writable: {bool(is_writable)}")
    print(f"Executable: {bool(is_executable)}")

    # Get owner (Unix only)
    print(f"Owner UID: {stats.st_uid}")
    print(f"Group GID: {stats.st_gid}")

    # Change permissions (Unix)
    path.chmod(0o644)  # rw-r--r--

    # Change owner (Unix, requires privileges)
    import os
    os.chown(path, uid=1000, gid=1000)
```

---

## Navigating the File System

### Current and Home Directories

```python
from pathlib import Path

# Current working directory
cwd = Path.cwd()
print(f"Current directory: {cwd}")

# Change working directory (use os.chdir)
import os
os.chdir('/tmp')
print(f"New directory: {Path.cwd()}")

# Home directory
home = Path.home()
print(f"Home directory: {home}")

# Common paths
downloads = home / 'Downloads'
documents = home / 'Documents'
desktop = home / 'Desktop'
```

### Expanding User Paths

The `expanduser()` method expands `~` and `~user` to absolute paths:

```python
from pathlib import Path

# Expand ~ to current user's home
path = Path('~/documents/file.txt')
expanded = path.expanduser()
print(expanded)  # /home/username/documents/file.txt (Unix)
                 # C:\Users\username\documents\file.txt (Windows)

# Expand ~username to specific user's home (Unix only)
other_user = Path('~alice/documents/file.txt')
expanded = other_user.expanduser()
print(expanded)  # /home/alice/documents/file.txt

# Works with relative paths containing ~
path = Path('~/projects/../documents/file.txt')
expanded = path.expanduser()
print(expanded)  # /home/username/projects/../documents/file.txt

# Combine with resolve() to get clean absolute path
clean = path.expanduser().resolve()
print(clean)  # /home/username/documents/file.txt

# If path doesn't contain ~, returns unchanged
regular = Path('/absolute/path/file.txt')
print(regular.expanduser())  # /absolute/path/file.txt (unchanged)
```

**Common usage patterns**:

```python
from pathlib import Path

# Reading config from user's home
config_path = Path('~/.config/myapp/settings.json').expanduser()
if config_path.exists():
    config = config_path.read_text()

# Creating files in user's home
log_file = Path('~/logs/app.log').expanduser()
log_file.parent.mkdir(parents=True, exist_ok=True)
log_file.write_text('Log entry\n')

# Cross-platform user data directory
if sys.platform == 'win32':
    data_dir = Path('~/AppData/Local/MyApp').expanduser()
else:
    data_dir = Path('~/.local/share/myapp').expanduser()

data_dir.mkdir(parents=True, exist_ok=True)
```

**Important notes**:

- `expanduser()` only expands `~`, it does not resolve symbolic links or `..`
- Use `.expanduser().resolve()` to get a fully resolved path
- On Windows, `~` expands to the user profile directory
- `~username` syntax only works on Unix-like systems
- Returns a new Path object (original is unchanged)

### Listing Directory Contents

```python
from pathlib import Path

# List all items in directory
directory = Path('.')

# Using iterdir() - returns generator
for item in directory.iterdir():
    print(item)

# Convert to list
items = list(directory.iterdir())
print(f"Found {len(items)} items")

# Filter by type
files = [f for f in directory.iterdir() if f.is_file()]
dirs = [d for d in directory.iterdir() if d.is_dir()]

print(f"Files: {len(files)}")
print(f"Directories: {len(dirs)}")

# Sort by modification time
sorted_files = sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)
print("Most recently modified:")
for f in sorted_files[:5]:
    print(f"  {f.name}")
```

### Recursive Traversal

```python
from pathlib import Path

directory = Path('.')

# Recursively find all files
all_files = list(directory.rglob('*'))
print(f"Total items: {len(all_files)}")

# Only files (not directories)
files_only = [f for f in directory.rglob('*') if f.is_file()]
print(f"Total files: {len(files_only)}")

# Find specific file types
python_files = list(directory.rglob('*.py'))
text_files = list(directory.rglob('*.txt'))

print(f"Python files: {len(python_files)}")
print(f"Text files: {len(text_files)}")

# Find in subdirectories only (not current)
for py_file in directory.rglob('*/*.py'):
    print(py_file)
```

### Walking Directory Trees

```python
from pathlib import Path

def walk_directory(directory):
    """Walk directory tree and categorize files."""
    stats = {
        'directories': 0,
        'files': 0,
        'total_size': 0,
        'extensions': {}
    }

    for path in Path(directory).rglob('*'):
        if path.is_dir():
            stats['directories'] += 1
        elif path.is_file():
            stats['files'] += 1
            stats['total_size'] += path.stat().st_size

            # Count by extension
            ext = path.suffix.lower()
            stats['extensions'][ext] = stats['extensions'].get(ext, 0) + 1

    return stats

# Usage
stats = walk_directory('.')
print(f"Directories: {stats['directories']}")
print(f"Files: {stats['files']}")
print(f"Total size: {stats['total_size'] / (1024**2):.2f} MB")
print("\nFiles by extension:")
for ext, count in sorted(stats['extensions'].items(), key=lambda x: x[1], reverse=True):
    ext_name = ext if ext else '(no extension)'
    print(f"  {ext_name}: {count}")
```

### Finding Specific Files

```python
from pathlib import Path

def find_files(directory, pattern='*', max_depth=None):
    """Find files matching pattern up to max_depth."""
    directory = Path(directory)
    found = []

    def search(path, depth=0):
        if max_depth and depth > max_depth:
            return

        try:
            for item in path.iterdir():
                if item.is_file() and item.match(pattern):
                    found.append(item)
                elif item.is_dir():
                    search(item, depth + 1)
        except PermissionError:
            pass  # Skip directories we can't access

    search(directory)
    return found

# Find all Python files in current directory (depth 0)
py_files = find_files('.', '*.py', max_depth=0)

# Find all config files recursively
config_files = find_files('.', '*.conf')

# Find all README files (case-insensitive)
readmes = [f for f in find_files('.') if f.name.lower().startswith('readme')]
```

---

## File and Directory Operations

### Creating Directories

```python
from pathlib import Path

# Create single directory
directory = Path('new_folder')
directory.mkdir()

# Create directory with parents
nested = Path('parent/child/grandchild')
nested.mkdir(parents=True)  # Creates all intermediate directories

# Don't fail if exists
directory.mkdir(exist_ok=True)

# Create with specific permissions (Unix)
directory.mkdir(mode=0o755)  # rwxr-xr-x

# Create multiple directories
directories = ['logs', 'data', 'config']
for dir_name in directories:
    Path(dir_name).mkdir(exist_ok=True)
```

### Reading Files

```python
from pathlib import Path

path = Path('document.txt')

# Read text file
text = path.read_text(encoding='utf-8')
print(text)

# Read binary file
binary_data = path.read_bytes()
print(f"Size: {len(binary_data)} bytes")

# Read lines
lines = path.read_text(encoding='utf-8').splitlines()
for line in lines:
    print(line)

# Read with explicit encoding and error handling
try:
    content = path.read_text(encoding='utf-8', errors='strict')
except FileNotFoundError:
    print("File not found")
except UnicodeDecodeError:
    print("Encoding error")
```

### Writing Files

```python
from pathlib import Path

path = Path('output.txt')

# Write text file
path.write_text('Hello, World!\n', encoding='utf-8')

# Write binary file
path.write_bytes(b'\x89PNG\r\n\x1a\n')

# Append to file (using open)
with path.open('a', encoding='utf-8') as f:
    f.write('Appended line\n')

# Write multiple lines
lines = ['Line 1', 'Line 2', 'Line 3']
path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

# Create parent directories if needed
nested_file = Path('parent/child/file.txt')
nested_file.parent.mkdir(parents=True, exist_ok=True)
nested_file.write_text('Content', encoding='utf-8')
```

### Opening Files

```python
from pathlib import Path

path = Path('data.txt')

# Open for reading
with path.open('r', encoding='utf-8') as f:
    content = f.read()

# Open for writing
with path.open('w', encoding='utf-8') as f:
    f.write('New content\n')

# Open for appending
with path.open('a', encoding='utf-8') as f:
    f.write('Appended content\n')

# Open binary
with path.open('rb') as f:
    data = f.read()

# Multiple files
input_path = Path('input.txt')
output_path = Path('output.txt')

with input_path.open('r') as infile, output_path.open('w') as outfile:
    for line in infile:
        outfile.write(line.upper())
```

### Copying and Moving

```python
from pathlib import Path
import shutil

source = Path('source.txt')
destination = Path('destination.txt')

# Copy file (requires shutil)
shutil.copy2(source, destination)

# Copy to directory
dest_dir = Path('backup')
dest_dir.mkdir(exist_ok=True)
shutil.copy2(source, dest_dir)

# Move/rename file
source.rename(destination)

# Move to different directory
dest_path = Path('folder') / source.name
source.rename(dest_path)

# Replace existing file (Python 3.8+)
source.replace(destination)  # Overwrites destination
```

### Deleting Files and Directories

```python
from pathlib import Path
import shutil

# Delete file
file_path = Path('file.txt')
if file_path.exists():
    file_path.unlink()  # Delete file

# Delete file, ignore if doesn't exist (Python 3.8+)
file_path.unlink(missing_ok=True)

# Delete empty directory
dir_path = Path('empty_folder')
if dir_path.exists() and dir_path.is_dir():
    dir_path.rmdir()  # Only works if empty

# Delete directory tree (requires shutil)
dir_path = Path('folder_with_contents')
if dir_path.exists():
    shutil.rmtree(dir_path)  # ⚠️ Deletes everything!

# Safe deletion with confirmation
def safe_delete(path):
    """Delete with confirmation."""
    path = Path(path)
    if not path.exists():
        print(f"Path doesn't exist: {path}")
        return

    response = input(f"Delete {path}? (y/n): ")
    if response.lower() == 'y':
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)
        print(f"Deleted: {path}")
    else:
        print("Cancelled")
```

### Symbolic Links

```python
from pathlib import Path

# Create symbolic link
target = Path('original_file.txt')
link = Path('link_to_file.txt')

link.symlink_to(target)

# Check if symbolic link
print(link.is_symlink())  # True

# Read link target
if link.is_symlink():
    target = link.readlink()  # Python 3.9+
    print(f"Link points to: {target}")

# Resolve link to actual path
actual_path = link.resolve()
print(f"Actual file: {actual_path}")

# Delete symbolic link
link.unlink()  # Deletes link, not target
```

### Temporary Files and Directories

```python
from pathlib import Path
import tempfile

# Create temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    tmp_path = Path(tmpdir)

    # Use temporary directory
    temp_file = tmp_path / 'temp.txt'
    temp_file.write_text('Temporary data')

    print(f"Temp file: {temp_file}")
    print(f"Exists: {temp_file.exists()}")
# Directory and contents automatically deleted here

# Create temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
    tmp_path = Path(tmp.name)
    tmp.write('Temporary content')

print(f"Temp file: {tmp_path}")
print(f"Exists: {tmp_path.exists()}")

# Clean up manually
tmp_path.unlink()
```

---

## Pattern Matching and Searching

### glob() - Non-Recursive Patterns

```python
from pathlib import Path

directory = Path('.')

# Find all Python files in current directory
py_files = list(directory.glob('*.py'))

# Find files with specific pattern
test_files = list(directory.glob('test_*.py'))

# Find multiple patterns
patterns = ['*.py', '*.txt', '*.md']
all_files = []
for pattern in patterns:
    all_files.extend(directory.glob(pattern))

# Case-insensitive matching (depends on OS)
readme_files = list(directory.glob('[Rr][Ee][Aa][Dd][Mm][Ee]*'))
```

### rglob() - Recursive Patterns

```python
from pathlib import Path

directory = Path('.')

# Find all Python files recursively
all_py = list(directory.rglob('*.py'))

# Find all __init__.py files
init_files = list(directory.rglob('__init__.py'))

# Find files in any subdirectory named 'tests'
test_files = list(directory.rglob('tests/*.py'))

# Find all files (not directories)
all_files = [f for f in directory.rglob('*') if f.is_file()]

# Find hidden files (Unix)
hidden_files = list(directory.rglob('.*'))
```

### match() - Pattern Matching

```python
from pathlib import Path

path = Path('folder/subfolder/test_file.py')

# Match pattern
print(path.match('*.py'))              # True
print(path.match('test_*.py'))         # True
print(path.match('*/test_*.py'))       # True
print(path.match('**/test_*.py'))      # True (matches at any level)
print(path.match('folder/*/test_*.py')) # True

# Case sensitivity
print(path.match('*.PY'))  # False (case-sensitive on Unix)

# Match suffix
print(path.match('*.py'))   # True
print(path.match('*.txt'))  # False
```

### Pattern Examples

```python
from pathlib import Path

directory = Path('.')

# All text files
txt_files = directory.glob('*.txt')

# All files starting with 'data'
data_files = directory.glob('data*')

# All files with numeric names
numbered_files = directory.glob('[0-9]*.txt')

# Files with single character names
single_char = directory.glob('?.txt')

# Python files in 'src' subdirectories
src_python = directory.rglob('src/*.py')

# All __pycache__ directories
pycache_dirs = [d for d in directory.rglob('__pycache__') if d.is_dir()]

# All files except hidden ones
visible_files = [f for f in directory.rglob('*')
                 if f.is_file() and not f.name.startswith('.')]
```

### Advanced Filtering

```python
from pathlib import Path
import fnmatch

def find_files_advanced(directory, patterns=None, exclude_patterns=None,
                       min_size=None, max_size=None):
    """Advanced file finding with multiple filters."""
    directory = Path(directory)
    found = []

    for path in directory.rglob('*'):
        if not path.is_file():
            continue

        # Pattern matching
        if patterns:
            if not any(path.match(p) for p in patterns):
                continue

        # Exclude patterns
        if exclude_patterns:
            if any(path.match(p) for p in exclude_patterns):
                continue

        # Size filtering
        size = path.stat().st_size
        if min_size and size < min_size:
            continue
        if max_size and size > max_size:
            continue

        found.append(path)

    return found

# Usage examples
# Find Python files larger than 1KB
large_py = find_files_advanced('.', patterns=['*.py'], min_size=1024)

# Find text files but exclude tests
non_test_txt = find_files_advanced('.',
                                   patterns=['*.txt'],
                                   exclude_patterns=['test_*.txt', '**/tests/*'])

# Find small config files
small_configs = find_files_advanced('.',
                                   patterns=['*.conf', '*.ini', '*.cfg'],
                                   max_size=10240)  # 10KB
```

---

## Cross-Platform Path Handling

### Path Separators

```python
from pathlib import Path
import os

# pathlib automatically uses correct separator
path = Path('folder') / 'subfolder' / 'file.txt'
print(path)  # folder/subfolder/file.txt (Unix)
             # folder\subfolder\file.txt (Windows)

# Get platform separator
print(os.sep)  # '/' on Unix, '\\' on Windows

# Path parts (always consistent)
print(path.parts)  # ('folder', 'subfolder', 'file.txt')

# String conversion uses platform separator
path_str = str(path)
print(path_str)  # Uses platform-specific separator
```

### Converting Between Formats

```python
from pathlib import Path, PureWindowsPath, PurePosixPath

# Convert Windows path to Unix format
win_path = PureWindowsPath('C:\\Users\\user\\documents\\file.txt')
posix_path = PurePosixPath(*win_path.parts[1:])  # Skip drive
print(posix_path)  # Users/user/documents/file.txt

# Convert Unix path to Windows format
unix_path = PurePosixPath('/home/user/documents/file.txt')
win_path = PureWindowsPath(*unix_path.parts[1:])  # Skip root
print(win_path)  # home\user\documents\file.txt

# Use forward slashes (works on all platforms)
path = Path('folder/subfolder/file.txt')
print(path)  # Works on Unix and Windows
```

### Working with PurePosixPath and PureWindowsPath

Pure path classes allow you to manipulate paths for different operating systems without requiring that OS:

```python
from pathlib import PurePosixPath, PureWindowsPath

# Manipulate Unix paths on any OS (even Windows)
posix = PurePosixPath('/usr/local/bin/python3')
print(posix.parts)        # ('/', 'usr', 'local', 'bin', 'python3')
print(posix.parent)       # /usr/local/bin
print(posix.name)         # python3
print(posix.suffix)       # (no suffix)

# Manipulate Windows paths on any OS (even Unix)
windows = PureWindowsPath('C:\\Program Files\\Python\\python.exe')
print(windows.parts)      # ('C:\\', 'Program Files', 'Python', 'python.exe')
print(windows.drive)      # C:
print(windows.parent)     # C:\Program Files\Python
print(windows.name)       # python.exe
print(windows.suffix)     # .exe

# Path construction works the same
unix_config = PurePosixPath('/etc') / 'nginx' / 'nginx.conf'
print(unix_config)        # /etc/nginx/nginx.conf

win_config = PureWindowsPath('C:\\Windows') / 'System32' / 'drivers'
print(win_config)         # C:\Windows\System32\drivers

# Comparison and matching
unix_path = PurePosixPath('/home/user/file.txt')
print(unix_path.match('*.txt'))           # True
print(unix_path.match('/home/*/file.txt')) # True

win_path = PureWindowsPath('C:\\Users\\Alice\\file.txt')
print(win_path.match('*.txt'))            # True
print(win_path.match('C:\\Users\\*\\*'))  # True
```

**Practical use cases for Pure paths**:

```python
from pathlib import PurePosixPath, PureWindowsPath

# 1. Parsing log files with Unix paths (on any OS)
def parse_unix_log_path(log_line):
    """Extract and analyze Unix path from log, regardless of current OS."""
    # Example log: "ERROR: Failed to read /var/log/app/error.log"
    path_str = log_line.split()[-1]
    path = PurePosixPath(path_str)

    return {
        'directory': str(path.parent),
        'filename': path.name,
        'extension': path.suffix,
        'is_var_log': path.parts[1:3] == ('var', 'log') if len(path.parts) > 2 else False
    }

log = "ERROR: Failed to read /var/log/app/error.log"
info = parse_unix_log_path(log)
print(info)
# {'directory': '/var/log/app', 'filename': 'error.log',
#  'extension': '.log', 'is_var_log': True}

# 2. Processing Windows registry paths (on any OS)
def analyze_registry_path(reg_path_str):
    """Analyze Windows registry path structure."""
    path = PureWindowsPath(reg_path_str)

    # Registry paths use backslashes like file paths
    parts = path.parts
    hive = parts[0] if parts else None
    subkeys = parts[1:] if len(parts) > 1 else []

    return {
        'hive': hive,
        'depth': len(subkeys),
        'leaf_key': path.name
    }

reg_path = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion'
info = analyze_registry_path(reg_path)
print(info)
# {'hive': 'HKEY_LOCAL_MACHINE', 'depth': 4, 'leaf_key': 'CurrentVersion'}

# 3. Building cross-platform configuration
def create_config_path(base, *parts, platform='posix'):
    """Create configuration path for specific platform."""
    if platform == 'posix':
        return str(PurePosixPath(base).joinpath(*parts))
    else:
        return str(PureWindowsPath(base).joinpath(*parts))

# Generate both Unix and Windows config paths
unix_conf = create_config_path('/etc', 'myapp', 'config.ini', platform='posix')
win_conf = create_config_path('C:\\ProgramData', 'MyApp', 'config.ini', platform='windows')

print(f"Unix config: {unix_conf}")      # /etc/myapp/config.ini
print(f"Windows config: {win_conf}")    # C:\ProgramData\MyApp\config.ini

# 4. Validating path patterns across platforms
def validate_install_path(path_str, platform='posix'):
    """Validate installation path follows conventions."""
    if platform == 'posix':
        path = PurePosixPath(path_str)
        # Unix: should be under /usr/local or /opt
        valid_prefixes = [PurePosixPath('/usr/local'), PurePosixPath('/opt')]
        return any(
            path.parts[:len(prefix.parts)] == prefix.parts
            for prefix in valid_prefixes
        )
    else:
        path = PureWindowsPath(path_str)
        # Windows: should be under Program Files
        valid_prefixes = [
            PureWindowsPath('C:\\Program Files'),
            PureWindowsPath('C:\\Program Files (x86)')
        ]
        return any(
            str(path).startswith(str(prefix))
            for prefix in valid_prefixes
        )

print(validate_install_path('/usr/local/bin/myapp', 'posix'))       # True
print(validate_install_path('/home/user/myapp', 'posix'))            # False
print(validate_install_path('C:\\Program Files\\MyApp', 'windows'))  # True
print(validate_install_path('C:\\Users\\MyApp', 'windows'))          # False

# 5. Path normalization for different systems
def normalize_path(path_str, target_platform='posix'):
    """Normalize path to target platform format."""
    # Try to detect source platform
    if '\\' in path_str and ':' in path_str:
        # Looks like Windows path
        parts = PureWindowsPath(path_str).parts
        # Remove drive if present
        if parts and ':' in parts[0]:
            parts = parts[1:]
    else:
        # Assume Unix path
        parts = PurePosixPath(path_str).parts
        # Remove root if present
        if parts and parts[0] == '/':
            parts = parts[1:]

    # Construct in target format
    if target_platform == 'posix':
        return '/' + str(PurePosixPath(*parts))
    else:
        return str(PureWindowsPath('C:\\', *parts))

# Convert between formats
win_path = 'C:\\Users\\Alice\\Documents\\file.txt'
unix_path = normalize_path(win_path, 'posix')
print(unix_path)  # /Users/Alice/Documents/file.txt

unix_path = '/home/alice/documents/file.txt'
win_path = normalize_path(unix_path, 'windows')
print(win_path)  # C:\home\alice\documents\file.txt
```

**Key differences between Pure and Concrete paths**:

```python
from pathlib import Path, PurePosixPath

# Pure paths: No filesystem operations
pure = PurePosixPath('/tmp/file.txt')
print(pure.name)          # ✅ Works: 'file.txt'
print(pure.parent)        # ✅ Works: /tmp
print(pure.suffix)        # ✅ Works: '.txt'
# print(pure.exists())    # ❌ AttributeError: no filesystem access
# print(pure.read_text()) # ❌ AttributeError: no filesystem access

# Concrete paths: Full filesystem operations
concrete = Path('/tmp/file.txt')
print(concrete.name)      # ✅ Works: 'file.txt'
print(concrete.exists())  # ✅ Works: True/False
print(concrete.stat())    # ✅ Works: file metadata
```

**When to use Pure paths**:

- ✅ Parsing paths from logs, configs, or databases
- ✅ Manipulating paths for different OSes than you're running on
- ✅ Building path strings for documentation or code generation
- ✅ Testing path logic without filesystem access
- ✅ Processing remote paths (from SSH, FTP logs, etc.)
- ✅ Working with paths that don't exist yet

**When to use Concrete paths (regular Path)**:

- ✅ Any actual file operations (read, write, check existence)
- ✅ Working with local filesystem
- ✅ Need to resolve symlinks or relative paths
- ✅ Need file metadata (size, timestamps, permissions)

### Platform-Specific Paths

```python
from pathlib import Path, PureWindowsPath, PurePosixPath
import sys

# Detect platform
if sys.platform == 'win32':
    print("Running on Windows")
    # Windows-specific code
elif sys.platform == 'darwin':
    print("Running on macOS")
    # macOS-specific code
elif sys.platform.startswith('linux'):
    print("Running on Linux")
    # Linux-specific code

# Get home directory (platform-agnostic)
home = Path.home()
print(f"Home: {home}")

# Common user directories
if sys.platform == 'win32':
    documents = home / 'Documents'
    downloads = home / 'Downloads'
    appdata = Path(os.environ['APPDATA'])
else:
    documents = home / 'Documents'
    downloads = home / 'Downloads'
    config = home / '.config'
```

### Handling Absolute Paths

```python
from pathlib import Path

# Absolute paths on different platforms
if sys.platform == 'win32':
    # Windows: C:\path\to\file
    abs_path = Path('C:/Users/user/file.txt')
else:
    # Unix: /path/to/file
    abs_path = Path('/home/user/file.txt')

# Convert relative to absolute
relative = Path('folder/file.txt')
absolute = relative.resolve()
print(absolute)

# Check if absolute
print(Path('/home/user').is_absolute())    # True (Unix)
print(Path('C:/Users').is_absolute())      # True (Windows)
print(Path('folder/file').is_absolute())   # False
```

### Safe Path Construction

```python
from pathlib import Path

def safe_join(*parts):
    """Safely join path parts, preventing directory traversal."""
    base = Path(parts[0])
    for part in parts[1:]:
        # Remove leading slashes and parent references
        part = str(part).lstrip('/\\')
        if '..' in Path(part).parts:
            raise ValueError(f"Invalid path component: {part}")
        base = base / part
    return base

# Safe usage
try:
    path = safe_join('/base', 'folder', 'file.txt')
    print(path)  # /base/folder/file.txt

    # This will raise an error
    path = safe_join('/base', '../etc/passwd')
except ValueError as e:
    print(f"Error: {e}")
```

### Platform-Specific Path Validation

```python
from pathlib import Path, PureWindowsPath
import string

def is_valid_filename(filename, platform='current'):
    """Check if filename is valid for platform."""
    if platform == 'current':
        platform = sys.platform

    # Windows reserved names
    if 'win' in platform:
        reserved = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3',
                   'COM4', 'LPT1', 'LPT2', 'LPT3'}
        if filename.upper() in reserved:
            return False

        # Windows forbidden characters
        forbidden = '<>:"|?*'
        if any(char in filename for char in forbidden):
            return False

    # Unix: only NULL and / are forbidden
    else:
        if '\0' in filename or '/' in filename:
            return False

    return True

# Test filenames
filenames = ['document.txt', 'CON', 'file:name', 'valid_file_123']
for name in filenames:
    valid = is_valid_filename(name)
    print(f"{name}: {'Valid' if valid else 'Invalid'}")
```

---

## Complete Code Examples

### Example 1: File Organizer

```python
#!/usr/bin/env python3
"""
Organize files by extension into subdirectories.
"""

from pathlib import Path
import shutil
from collections import defaultdict

def organize_files(directory, dry_run=True):
    """
    Organize files in directory by extension.

    Args:
        directory: Directory to organize
        dry_run: If True, only show what would be done
    """
    directory = Path(directory)

    if not directory.is_dir():
        print(f"Error: Not a directory: {directory}")
        return

    # Group files by extension
    files_by_ext = defaultdict(list)

    for file_path in directory.iterdir():
        if file_path.is_file():
            ext = file_path.suffix.lower()
            if not ext:
                ext = 'no_extension'
            files_by_ext[ext].append(file_path)

    # Report what will be done
    print(f"Found {sum(len(files) for files in files_by_ext.values())} files")
    print(f"Extensions: {len(files_by_ext)}\n")

    for ext, files in sorted(files_by_ext.items()):
        print(f"{ext}: {len(files)} files")

    if dry_run:
        print("\nDry run - no changes made")
        print("Run with dry_run=False to organize files")
        return

    # Create directories and move files
    print("\nOrganizing files...")

    for ext, files in files_by_ext.items():
        # Create subdirectory for extension
        ext_dir = directory / ext.lstrip('.')
        ext_dir.mkdir(exist_ok=True)

        # Move files
        for file_path in files:
            dest_path = ext_dir / file_path.name

            # Handle name conflicts
            if dest_path.exists():
                stem = dest_path.stem
                suffix = dest_path.suffix
                counter = 1
                while dest_path.exists():
                    dest_path = ext_dir / f"{stem}_{counter}{suffix}"
                    counter += 1

            shutil.move(str(file_path), str(dest_path))
            print(f"Moved: {file_path.name} -> {ext_dir.name}/")

    print(f"\nOrganization complete!")

def main():
    # Organize current directory
    organize_files('.', dry_run=True)

    # To actually move files:
    # organize_files('.', dry_run=False)

if __name__ == '__main__':
    main()
```

### Example 2: Duplicate File Finder

```python
#!/usr/bin/env python3
"""
Find duplicate files based on content hash.
"""

from pathlib import Path
import hashlib
from collections import defaultdict

def hash_file(file_path, block_size=65536):
    """Calculate MD5 hash of file."""
    hasher = hashlib.md5()

    with open(file_path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)

    return hasher.hexdigest()

def find_duplicates(directory, min_size=0):
    """
    Find duplicate files in directory.

    Args:
        directory: Directory to search
        min_size: Minimum file size to consider (bytes)

    Returns:
        Dictionary mapping hash to list of duplicate files
    """
    directory = Path(directory)

    # First pass: group by size (cheap check)
    files_by_size = defaultdict(list)

    print("Scanning files...")
    for file_path in directory.rglob('*'):
        if file_path.is_file():
            size = file_path.stat().st_size
            if size >= min_size:
                files_by_size[size].append(file_path)

    # Second pass: hash files with same size
    files_by_hash = defaultdict(list)
    total_files = sum(len(files) for files in files_by_size.values()
                     if len(files) > 1)
    processed = 0

    print(f"Hashing {total_files} potential duplicates...")

    for size, files in files_by_size.items():
        if len(files) > 1:  # Only hash if multiple files have same size
            for file_path in files:
                try:
                    file_hash = hash_file(file_path)
                    files_by_hash[file_hash].append(file_path)
                    processed += 1
                    if processed % 10 == 0:
                        print(f"Progress: {processed}/{total_files}", end='\r')
                except Exception as e:
                    print(f"\nError hashing {file_path}: {e}")

    print()  # New line after progress

    # Filter to only duplicates
    duplicates = {h: files for h, files in files_by_hash.items()
                 if len(files) > 1}

    return duplicates

def report_duplicates(duplicates):
    """Generate duplicate files report."""
    if not duplicates:
        print("No duplicates found!")
        return

    total_duplicates = sum(len(files) - 1 for files in duplicates.values())
    total_wasted = sum(
        files[0].stat().st_size * (len(files) - 1)
        for files in duplicates.values()
    )

    print(f"\nFound {len(duplicates)} sets of duplicates")
    print(f"Total duplicate files: {total_duplicates}")
    print(f"Wasted space: {total_wasted / (1024**2):.2f} MB\n")

    for i, (file_hash, files) in enumerate(duplicates.items(), 1):
        size = files[0].stat().st_size
        print(f"Duplicate set {i} (size: {size / 1024:.2f} KB):")
        for file_path in files:
            print(f"  {file_path}")
        print()

def main():
    directory = '.'
    min_size = 1024  # Ignore files smaller than 1KB

    duplicates = find_duplicates(directory, min_size)
    report_duplicates(duplicates)

if __name__ == '__main__':
    main()
```

### Example 3: Project Structure Generator

```python
#!/usr/bin/env python3
"""
Generate project directory structure from template.
"""

from pathlib import Path
from datetime import datetime

def create_project_structure(project_name, project_type='python'):
    """
    Create project directory structure.

    Args:
        project_name: Name of the project
        project_type: Type of project ('python', 'web', 'data')
    """
    base_dir = Path(project_name)

    # Check if project already exists
    if base_dir.exists():
        print(f"Error: Directory '{project_name}' already exists")
        return False

    # Define structures for different project types
    structures = {
        'python': {
            'dirs': [
                'src',
                'tests',
                'docs',
                'data',
                'scripts',
            ],
            'files': {
                'README.md': f"# {project_name}\n\nProject description here.\n",
                '.gitignore': "__pycache__/\n*.pyc\n.env\nvenv/\n*.egg-info/\n",
                'requirements.txt': "# Add dependencies here\n",
                'setup.py': f"from setuptools import setup, find_packages\n\nsetup(\n    name='{project_name}',\n    version='0.1.0',\n    packages=find_packages(),\n)\n",
                'src/__init__.py': f'"""\\n{project_name} package.\\n"""\n',
                'tests/__init__.py': '',
                'tests/test_basic.py': 'def test_placeholder():\n    assert True\n',
            }
        },
        'web': {
            'dirs': [
                'static/css',
                'static/js',
                'static/images',
                'templates',
                'app',
                'tests',
            ],
            'files': {
                'README.md': f"# {project_name}\n\nWeb application.\n",
                '.gitignore': "__pycache__/\n*.pyc\n.env\nnode_modules/\n",
                'app/__init__.py': '',
                'app/routes.py': "# Define routes here\n",
                'templates/index.html': "<!DOCTYPE html>\n<html>\n<head>\n    <title>{}</title>\n</head>\n<body>\n    <h1>Welcome</h1>\n</body>\n</html>\n".format(project_name),
            }
        },
        'data': {
            'dirs': [
                'data/raw',
                'data/processed',
                'notebooks',
                'src',
                'reports/figures',
            ],
            'files': {
                'README.md': f"# {project_name}\n\nData science project.\n",
                '.gitignore': "*.pyc\n__pycache__/\n.ipynb_checkpoints/\ndata/raw/*\n!data/raw/.gitkeep\n",
                'requirements.txt': "pandas\nnumpy\nmatplotlib\njupyter\n",
                'data/raw/.gitkeep': '',
                'notebooks/01_exploration.ipynb': '',
            }
        }
    }

    if project_type not in structures:
        print(f"Error: Unknown project type '{project_type}'")
        print(f"Available types: {', '.join(structures.keys())}")
        return False

    structure = structures[project_type]

    try:
        # Create base directory
        base_dir.mkdir()
        print(f"Created project: {project_name}/")

        # Create subdirectories
        for dir_path in structure['dirs']:
            full_path = base_dir / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"  Created: {dir_path}/")

        # Create files
        for file_path, content in structure['files'].items():
            full_path = base_dir / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding='utf-8')
            print(f"  Created: {file_path}")

        print(f"\n✓ Project '{project_name}' created successfully!")
        print(f"\nNext steps:")
        print(f"  cd {project_name}")
        if project_type == 'python':
            print("  python -m venv venv")
            print("  source venv/bin/activate  # or venv\\Scripts\\activate on Windows")
            print("  pip install -r requirements.txt")

        return True

    except Exception as e:
        print(f"Error creating project: {e}")
        # Clean up partial creation
        if base_dir.exists():
            import shutil
            shutil.rmtree(base_dir)
        return False

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python create_project.py <project_name> [type]")
        print("Types: python (default), web, data")
        sys.exit(1)

    project_name = sys.argv[1]
    project_type = sys.argv[2] if len(sys.argv) > 2 else 'python'

    create_project_structure(project_name, project_type)

if __name__ == '__main__':
    main()
```

---

## Key Takeaways

### The Big Picture

1. **pathlib is the modern standard**:
   - Object-oriented, intuitive
   - Cross-platform by design
   - Rich functionality
   - Better than string manipulation

2. **Path objects are immutable**:
   - Operations return new paths
   - Safe for concurrent use
   - Predictable behavior
   - No accidental modifications

3. **Integration with file operations**:
   - Direct file reading/writing
   - Built-in methods for common tasks
   - Seamless with `open()`
   - Works with `shutil` operations

4. **Cross-platform by default**:
   - Automatic path separator handling
   - Platform-agnostic code
   - Consistent API across systems
   - Easy platform detection

### Quick Reference

**Creating paths**:

```python
from pathlib import Path

path = Path('folder') / 'file.txt'
absolute = Path.cwd() / 'file.txt'
home = Path.home() / 'documents'
```

**Path properties**:

```python
path = Path('folder/document.txt')
print(path.name)      # document.txt
print(path.stem)      # document
print(path.suffix)    # .txt
print(path.parent)    # folder
```

**File operations**:

```python
# Read
text = path.read_text(encoding='utf-8')
data = path.read_bytes()

# Write
path.write_text('content', encoding='utf-8')
path.write_bytes(b'data')

# Check
if path.exists() and path.is_file():
    print("File exists")
```

**Directory operations**:

```python
# List
for item in Path('.').iterdir():
    print(item)

# Find
for py_file in Path('.').rglob('*.py'):
    print(py_file)

# Create
Path('new_dir').mkdir(parents=True, exist_ok=True)
```

### Best Practices Checklist

- ✅ Use `Path` objects instead of strings for file paths
- ✅ Use `/` operator to join paths
- ✅ Use `.rglob()` for recursive searches
- ✅ Specify `encoding='utf-8'` explicitly
- ✅ Use `.exists()` and `.is_file()` for safety
- ✅ Use `parents=True, exist_ok=True` when creating directories
- ✅ Convert to string only when necessary (`str(path)`)
- ✅ Handle exceptions (file not found, permission errors)
- ✅ Use `.resolve()` to get absolute paths
- ✅ Use `.relative_to()` for relative paths
- ❌ Don't manually construct paths with string concatenation
- ❌ Don't use string methods on paths (use Path methods)
- ❌ Don't assume specific path separators

### Common Patterns

**Safe file reading**:

```python
from pathlib import Path

path = Path('file.txt')
if path.exists() and path.is_file():
    content = path.read_text(encoding='utf-8')
```

**Directory traversal**:

```python
for py_file in Path('.').rglob('*.py'):
    if py_file.is_file():
        print(py_file)
```

**Creating nested structure**:

```python
file_path = Path('parent/child/file.txt')
file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.write_text('content')
```

### Remember

- pathlib is part of the standard library (Python 3.4+)
- Path objects work with most file-related functions
- Always use context managers for file operations
- Cross-platform code is the default, not an afterthought
- Combine with `shutil` for advanced operations
- Use `.resolve()` to eliminate `.` and `..`
- Pattern matching with `glob()` and `rglob()` is powerful
- Test on different platforms if writing portable code

---

**Related Topics**: Review file operations (reading, writing, copying) and learn about `os` module for lower-level operations and `glob` for pattern-based file finding.
