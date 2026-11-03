import pandas as pd
import os


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file and return a pandas DataFrame.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("The file doesnt exist")
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file format is not .csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None

# def main():
#     """
#     Main function to load a CSV file and print its contents.
#     """
#     dataset = load_csv("life_expectancy_years.csv")
#     if dataset is not None:
#         print("\nTEST 1\nPrinting the first row from the dataset\n")
#         print(dataset.head(1))
#         print("\nTEST 2\nFull dataset\n")
#         print(dataset)

#     baddataset = load_csv("wrongfile.png")
#     if baddataset is None:
#         print("Failed to load the bad dataset.")

# if __name__ == "__main__":
#     main()
