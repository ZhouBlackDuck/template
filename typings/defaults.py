class DefaultsMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['__defaults__'] = []
        prefix = f'DEFAULT_{name.upper()}__'
        for k, v in attrs.items():
            if not k.startswith('_') and not callable(v):
                attrs['__defaults__'].append((f'{prefix}{k.upper()}', v))
        return super().__new__(cls, name, bases, attrs)
