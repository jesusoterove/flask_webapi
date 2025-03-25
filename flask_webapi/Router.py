from flask import Blueprint
from .WebApi import MvcApp

class Router:
    def __init__(self, app: MvcApp, controller_path:str):
        self.controller_name = controller_path.split('.')[-1]
        self.blueprint = Blueprint(f'{self.controller_name}Controller', controller_path)
        self.handler_factory = app.action_handler()
        self.app = app

    def route(self, rule: str, method: str, **options):
        handler = self.handler_factory(self.controller_name, method)
        handler.__name__ = f"{self.controller_name}_{method}"
        self.blueprint.route(rule, **options)(handler)

    def register(self, url_prefix: str):
        self.app.register_routes(self.blueprint, url_prefix=url_prefix)
