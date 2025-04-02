from jsonargparse.typing import extend_base_type


def validation_wrapper(func, msg):
    def validate(_, v):
        if not func(v):
            raise ValueError(msg.format(v))

    return validate


FileMode = extend_base_type('FileMode', str,
                            validation_wrapper(
                                lambda x: x in ["r",
                                                "U",
                                                "rt", "tr",
                                                "r+", "+r",
                                                "rU", "Ur",
                                                "rt+", "r+t", "+rt", "tr+", "t+r", "+tr",
                                                "rtU", "rUt", "Urt", "trU", "tUr", "Utr",
                                                "w",
                                                "w+", "+w",
                                                "wt", "tw",
                                                "wt+", "w+t", "+wt", "tw+", "t+w", "+tw",
                                                "a",
                                                "a+", "+a",
                                                "at", "ta",
                                                "at+", "a+t", "+at", "ta+", "t+a", "+ta",
                                                "x",
                                                "xt", "tx",
                                                "x+", "+x",
                                                "xt+", "x+t", "+xt", "tx+", "t+x", "+tx"],
                                'Invalid file mode {}'))

__all__ = [
    'FileMode'
]
