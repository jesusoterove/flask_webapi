import os
from pydoc import locate
from importlib import import_module, util
from flask import Blueprint, Flask, jsonify, current_app
from .ControllerFactory import ControllerFactory
from .ControllerActionHandler import ControllerActionHandler

class WebApi:
    def __init__(self, app: Flask = None, controllers_path: str = 'app.controllers'):
        self.controllers_path = controllers_path
        self.controller_factory = ControllerFactory(controllers_path)
        if not app is None:
            self.init_app(app)

    def init_app(self, app):
        app.extensions['mvc'] = {
            'action_handler': self.action_handler(),
            'app': self
        }
        self.app = app
        self._load_controllers()
        app.register_error_handler(404, self._not_found)
        app.register_error_handler(500, self._internal_server_error)
        self.app = None

    def action_handler(self):
        return ControllerActionHandler(self.controller_factory).create_handler
    
    def register_routes(self, router: Blueprint, url_prefix: str = ''):
        self.app.register_blueprint(router, url_prefix=url_prefix)

    def _load_controllers(self):
        print("Loading controllers...")
        # Determine the full path based on the current file path
        root_path = os.getcwd() # ent_app.root_path
        controllers_full_path = os.path.join(root_path, self.controllers_path.replace('.', os.sep))
        for root, _, files in os.walk(controllers_full_path):
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    module_name = os.path.splitext(file)[0]
                    module_path = os.path.relpath(root, root_path).replace(os.sep, '.')
                    full_module_name = f"{module_path}.{module_name}"
                    print(f"Loading module...module_name: {module_name}, module_path: {module_path}, full_module_name: {full_module_name}")
                    module = locate(full_module_name)
                    if hasattr(module, 'register'):
                        module.register(self)

    # def _load_controller(self, module_name: str):
    #     module = import_module(module_name)
    #     if hasattr(module, 'register'):
    #         module.register(self)

    def _not_found(self, error):
        print(error)
        return jsonify({"error": "Not Found"}), 404

    def _internal_server_error(self, error):
        print(error)
        return jsonify({"error": "Internal Server Error"}), 500