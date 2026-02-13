import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_dir_structure(path: Path, prefix=""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}")
                print_dir_structure(item, prefix + "    ")  
            else:
                print(f"{prefix}{Fore.MAGENTA}{item.name}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}Permission denied: {path}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <directory_path>")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Error: Path does not exist -> {dir_path}")
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"{Fore.RED}Error: Path is not a directory -> {dir_path}")
        sys.exit(1)

    print(f"{Fore.CYAN}Directory structure of: {dir_path}")
    print_dir_structure(dir_path)

if __name__ == "__main__":
    main()
