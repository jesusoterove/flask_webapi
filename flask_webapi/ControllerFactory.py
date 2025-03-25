from pydoc import locate

class ControllerFactory:
    def __init__(self, controller_path: str = 'app.controllers'):
        self.controller_path = controller_path

    def create_controller(self, controller_name: str):
        module_path = f"{self.controller_path.rstrip('.')}.{controller_name}"
        module = locate(module_path)
        class_name = f"{controller_name}Controller"
        controller_class = getattr(module, class_name)
        return controller_class()
