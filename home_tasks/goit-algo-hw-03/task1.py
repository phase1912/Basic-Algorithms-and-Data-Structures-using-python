from pathlib import Path


def main():
    try:
        copy_files("Source", "Destination")
    except Exception as e:
        print(e)

    print("done")

def copy_files(source, dest="dist"):
    path_source = Path(source)

    if not path_source.exists():
        raise Exception(f"path: {path_source} not exists")

    for i in path_source.iterdir():
        if i.is_dir():
            copy_files(i, dest)
        else:
            new_file_path = Path(dest / Path(i.suffix.replace(".", "")))

            if not Path(dest).exists():
                Path(dest).mkdir()

            if not new_file_path.exists():
                new_file_path.mkdir()

            new_file = Path(new_file_path / Path(i.name))

            new_file.write_bytes(i.read_bytes())


if __name__ == "__main__":
    main()