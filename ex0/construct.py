import sys
import os
import site


def check_matrix_status() -> None:
    try:
        is_in_venv: bool = sys.prefix != sys.base_prefix

        if not is_in_venv:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")

            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")

            print("To enter the construct, run:")
            print("python3 -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate # On Windows\n")
            print("Then run this program again.")
        else:
            venv_name: str = os.path.basename(sys.prefix)
            pkg_path: str = site.getsitepackages()[0]

            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {sys.prefix}\n")

            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.\n")
            print(f"Package installation path:\n{pkg_path}")

    except Exception as e:
        print(f"An error occurred while reading the Matrix: {e}")


def main() -> None:
    check_matrix_status()


if __name__ == "__main__":
    main()
