def slice_me(family: list, start: int, end: int) -> list:
    """Return a slice of the 2D family while printing its shape before and
    after."""
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    sliced = family[start:end]
    print(f"My new shape is : ({len(sliced)}, {len(sliced[0])})")
    print(sliced)
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
