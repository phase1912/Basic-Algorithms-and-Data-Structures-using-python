from pathlib import Path

def display_tree(path: Path, indent: str = "") -> None:
    print(indent + str(path.name))

    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, indent + "    ")

if __name__ == "__main__":
    root = Path("picture")
    display_tree(root)