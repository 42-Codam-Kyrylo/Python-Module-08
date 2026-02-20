from typing import TypedDict
import sys

try:
    import pandas as pd
    import numpy as np
    import requests
    import matplotlib
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print(f"Missing module: {e}\n")
    print("Install dependencies with pip:")
    print("pip install -r requirements.txt\n")
    print("Or Poetry: poetry install")
    sys.exit(1)


class Post(TypedDict):
    userId: int
    id: int
    title: str
    body: str


def fetch_data() -> list[Post]:
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts", timeout=10
        )
        response.raise_for_status()
        return response.json()
    except Exception as err:
        print(f"Error occurred during data retrieval: {err}")
        sys.exit(1)


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    print(f"[OK] pandas ({pd.__version__}) Data manipulation ready")
    print(f"[OK] requests ({requests.__version__})  Network access ready")
    print(f"[OK] matplotlib ({matplotlib.__version__}) Visualization ready\n")

    print("Analyzing Matrix data...")
    data = fetch_data()
    dataframe = pd.DataFrame(data)

    dataframe["title_length"] = dataframe["title"].apply(len)
    print(f"Processing {len(dataframe)} data points...")

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    dataframe["title_length"].hist(bins=20, color="green")
    plt.title("Distribution of Matrix Message Lengths")
    plt.xlabel("Length")
    plt.ylabel("Frequency")

    plt.savefig("matrix_analysis.png")

    signal = np.random.rand(100)
    plt.figure(figsize=(10, 4))
    plt.plot(signal, color="lime")
    plt.title("Matrix Signal Strength (NumPy)")
    plt.savefig("matrix_signal.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png and matrix_signal.png")


if __name__ == "__main__":
    main()
