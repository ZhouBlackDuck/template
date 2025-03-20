import re

from jsonargparse.typing import extend_base_type


def validation_wrapper(func, msg):
    def validate(_, v):
        if not func(v):
            raise ValueError(msg.format(v))

    return validate


FileMode = extend_base_type('FileMode', str,
                            validation_wrapper(lambda x: re.match(r'^[rwxabt+]+$', x) is not None,
                                               'Invalid file mode {}'))

__all__ = [
    'FileMode'
]
