def triangle_area(base, height):
    result = None
    try:
        result = base * height / 2
    except Exception as ex:
        pass

    return result


def rectangle_area(width, height):
    result = None

    try:
        result = width*height
    except Exception as ex:
        pass

    return result
