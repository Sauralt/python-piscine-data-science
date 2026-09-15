def NULL_not_found(object: any) -> int:
    type_of_object = type(object)
    A = None

    match object:
        case bool() if object is False:
            A = f'Fake: {object} {type_of_object}'
        case None:
            A = f'Nothing: {object} {type_of_object}'
        case float() if object != object:
            A = f'Cheese: {object} {type_of_object}'
        case int() if object == 0:
            A = f'Zero: {object} {type_of_object}'
        case str() if not object:
            A = f'Empty: {object} {type_of_object}'
        case _:
            A = "Type not found"
    if A is not None:
        print(A)
    return 1


# def main():
#     Nothing = None
#     Garlic = float("NaN")
#     Zero = 0
#     Empty = ''
#     Fake = False

#     print('\33[1m' + 'Mandatory tests:\n' + '\33[0m')
#     NULL_not_found(Nothing)
#     NULL_not_found(Garlic)
#     NULL_not_found(Zero)
#     NULL_not_found(Empty)
#     NULL_not_found(Fake)
#     print(NULL_not_found("Brian"))


# if __name__ == "__main__":
#     main()
