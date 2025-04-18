from typing import Callable

from pydantic import validate_call


@validate_call
def validation_wrapper(func: Callable, msg: str):
    def validate(_, v):
        if not func(v):
            raise ValueError(msg.format(v))

    return validate
