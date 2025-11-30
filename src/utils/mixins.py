class OptimizerMixin:
    def __init__(self):
        self.optimizer = None

    def prepare_optimizer(self, conf):
        raise NotImplementedError("Must implement this method")

    def set_optimizer(self, conf):
        self.optimizer = self.prepare_optimizer(conf)
