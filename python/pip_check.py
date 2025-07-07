import sys
import subprocess


def get_installed_libs():
    """
    Getting the installed libs from pip list to use at future
    """
    result = subprocess.run(
        ["pip", "list", "--format=freeze"], capture_output=True, text=True
    )
    return [line.split("==")[0] for line in result.stdout.strip().split("\n")]


def main():
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    libs = get_installed_libs()
    print("\n".join(lib for lib in libs if lib.startswith(prefix)))


if __name__ == "__main__":
    main()
