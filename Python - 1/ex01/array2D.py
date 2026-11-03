def slice_me(family: list, start: int, end: int) -> list:
    """Return a slice of the 2D family while printing its shape before and
    after.
    """
    if not family or not isinstance(family, list):
        raise ValueError("family must be a non-empty 2D list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists")
    if not family[0]:
        raise ValueError("each row must contain at least one value")

    rows, cols = len(family), len(family[0])
    print(f"My shape is : ({rows}, {cols})")

    sliced = family[start:end]
    new_rows = len(sliced)
    new_cols = len(sliced[0]) if sliced and sliced[0] else 0
    print(f"My new shape is : ({new_rows}, {new_cols})")
    return sliced


# def main():
#     family = [[1.80, 78.4],
#               [2.15, 102.7],
#               [2.10, 98.5],
#               [1.88, 75.2]]
#     slice_me(family, 0, 2)
#     slice_me(family, 1, -2)


# if __name__ == "__main__":
#     main()
