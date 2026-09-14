import pandas as pd


def inspect(path_or_url):
    # 1. Load CSV dataset
    df = pd.read_csv(path_or_url)

    # 2. Print shape
    print("=== Shape ===")
    print(df.shape)
    print()

    # 3. Print data types
    print("=== Data Types ===")
    print(df.dtypes)
    print()

    # 4. Print missing values
    print("=== Missing Values ===")
    print(df.isnull().sum())
    print()

    # 5. Print missing percentages
    print("=== Missing Percentages ===")
    print((df.isnull().mean() * 100).round(2))
    print()

    # 6. Print numeric summary
    print("=== Numeric Summary ===")
    print(df.select_dtypes(include="number").describe())


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python inspect.py <path_or_url>")
    else:
        inspect(sys.argv[1])