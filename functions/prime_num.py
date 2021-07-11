def verify_positive(func):
    def verify(*args):
        if not all([x > 0 for x in args]):
            raise ValueError("The number should be positive!")
        return func(*args)
    return verify


def verify_types(*args):
    expected = args

    def decorator(func):
        def verify(*args):
            actual_types = [type(x) for x in args]
            for position in range(0, len(expected)):
                if expected[position] != actual_types[position]:
                    raise TypeError("Invalid type!")

            return func(*args)
        return verify
    return decorator


@verify_positive
@verify_types(int)
def dividers(x):
    return [i for i in range(2, x) if x % i == 0]


@verify_types(int)
def prime_num(x):
    if x == 1:
        return False
    return not dividers(x)
