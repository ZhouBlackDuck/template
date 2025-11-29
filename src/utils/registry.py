from functools import partial

REGISTRY = {
    "model": {},
    "data": {}
}


def register(category):
    assert category in REGISTRY, f"Unknown resource: {category}"

    def wrapper(cls):
        name = cls.__name__
        REGISTRY[category][name] = cls
        return cls

    return wrapper


def get(category, name):
    assert category in REGISTRY, f"Unknown resource: {category}"
    assert name in REGISTRY[category], f"Unknown {category}: {name}"
    return REGISTRY[category][name]


model = register("model")
data = register("data")
get_model = partial(get, "model")
get_data = partial(get, "data")

__all__ = [
    "model",
    "data",
    "get_model",
    "get_data"
]
