from argparse import ArgumentParser
import subprocess
from pathlib import Path


def convert(path: str | Path, recurse: bool = False) -> None:
    """
    Converts Jupyter notebooks (.ipynb) to Markdown (.md).
    
    Args:
        path (str | Path): The file or directory to process.
        recurse (bool): If True, searches subdirectories recursively for notebooks.
    """
    p = Path(path)
    if not p.exists():
        print(f"Path not found: {path}")
        return

    if p.is_file():
        # If a single file was provided, ensure it's a notebook
        if p.suffix == '.ipynb':
            files = [p]
        else:
            print(f"Not a notebook file: {p}")
            return
    else:
        # If a directory was provided, use glob to find matching notebooks
        pattern = "**/*.ipynb" if recurse else "*.ipynb"
        files = list(p.glob(pattern))

    if not files:
        print(f"No notebook files found in {p}")
        return

    # Iterate through all located notebooks and execute the conversion
    for f in files:
        print(f"Converting {f}...")
        subprocess.run(["uv", "run", "jupyter", "nbconvert", "--to", "markdown", str(f)], check=False)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("path", help="File or directory to convert")
    parser.add_argument("--recurse", action="store_true", help="Recurse into subdirectories")
    args = parser.parse_args()

    convert(args.path, args.recurse)
