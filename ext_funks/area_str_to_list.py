def area_str_to_list(str_area: str) -> list[int]:
    result = [0, 0, 0, 0]
    if len(str_area) > 1:
        result = list(map(lambda i: int(i), str_area[1:-1].split(",")))
        if len(result) != 4:
            result = [0, 0, 0, 0]
    return result
