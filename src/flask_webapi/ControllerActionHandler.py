import inspect
from .ControllerFactory import ControllerFactory

class ControllerActionHandler:
    def __init__(self, controller_factory: ControllerFactory):
        self.controller_factory = controller_factory

    def create_handler(self, controller_name, method_name):
        def handler(*args, **kwargs):
            controller = self.controller_factory.create_controller(controller_name)
            method = getattr(controller, method_name)
            # Get the method's signature
            sig = inspect.signature(method)
            # Filter kwargs to only include known arguments
            filtered_kwargs = {k: v for k, v in kwargs.items() if k in sig.parameters}
            return method(**filtered_kwargs)

        return handler
