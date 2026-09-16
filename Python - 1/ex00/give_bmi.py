def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """The give_bmi() function returns a list of BMI values calculated from the
    given height and weight lists """
    bmi = []
    for h, w in zip(height, weight):
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """The apply_limit() function returns a list of boolean values indicating
    whether each BMI value in the given list is greater than the specified
    limit """
    return [b > limit for b in bmi]


# def main():
#     from give_bmi import give_bmi, apply_limit
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))


# if __name__ == "__main__":
#     main()
