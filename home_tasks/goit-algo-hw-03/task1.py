from pathlib import Path
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files based on their extensions.")
    parser.add_argument("source", help="Path to the source directory.")
    parser.add_argument("destination", nargs="?", default="dist", help="Path to the destination directory (default: 'dist').")
    return parser.parse_args()

def ensure_directory_exists(path: Path):
    try:
        path.mkdir(exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {path}: {e}")
        raise

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def copy_files(source, dest):
    try:
        path_source = Path(source)

        if not path_source.exists():
            raise Exception(f"path: {path_source} not exists")

        for i in path_source.iterdir():
            if i.is_dir():
                copy_files(i, dest)
            else:
                new_file_path = Path(dest / Path(i.suffix.replace(".", "")))

                ensure_directory_exists(new_file_path)

                new_file = Path(new_file_path / Path(i.name))

                try:
                    new_file.write_bytes(i.read_bytes())
                    print(f"Copied: {i} -> {new_file}")
                except IOError as e:
                    print(f"Error copying file {i} to {new_file}: {e}")
    except Exception as e:
        print(f"Error processing directory {source}: {e}")
        raise

def main():
    try:
        args = parse_arguments()
        source_dir = args.source
        destination_dir = args.destination

        ensure_directory_exists(Path(destination_dir))

        copy_files(source_dir, destination_dir)
        print(f"Files successfully copied to: {destination_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()