def _validate_numeric_list(values: list[int | float], name: str) \
     -> list[int | float]:
    """Validate a list of numeric values."""
    if not isinstance(values, list):
        raise TypeError(f"{name} must be a list")
    if not values:
        raise ValueError(f"{name} must not be empty")
    for value in values:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"All values in {name} must be int or float")
    return values


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Return BMI values computed from matching height and weight lists."""
    height = _validate_numeric_list(height, "height")
    weight = _validate_numeric_list(weight, "weight")
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same size")

    bmi = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("height values must be strictly positive")
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans indicating if each BMI is above the limit."""
    bmi = _validate_numeric_list(bmi, "bmi")
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("limit must be an int")
    return [value > limit for value in bmi]


# def main():
#     from give_bmi import give_bmi, apply_limit
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))


# if __name__ == "__main__":
#     main()
