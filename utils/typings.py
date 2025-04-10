def validation_wrapper(func, msg):
    def validate(_, v):
        if not func(v):
            raise ValueError(msg.format(v))

    return validate
