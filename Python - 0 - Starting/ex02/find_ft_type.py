def all_thing_is_obj(object: any) -> int:
    type_of_object = type(object)
    A = None

    match object:
        case list():
            A = f'List : {type_of_object}'
        case tuple():
            A = f'Tuple : {type_of_object}'
        case set():
            A = f'Set : {type_of_object}'
        case dict():
            A = f'Dict : {type_of_object}'
        case str():
            A = f'{object} is in the kitchen : {type_of_object}'
        case _:
            A = "Type not found"
    if A is not None:
        print(A)
    return 42


def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")
    print(all_thing_is_obj(10))

if __name__ == "__main__":
    main()
