def show_args(*args):
    """
    *args
    """
    print(args)


def show_args2(**kwargs):
    """
    **kwargs
    """
    print(kwargs)


def show_args3(*args, **kwargs):
    """
    *args, **kwargs
    """
    print(args, kwargs)


if __name__ == "__main__":
    show_args(1, 3, 5)

    show_args2(sample="test", sample2=333, sample3=True)

    show_args3(3, 5, "aaa", sample=3)
