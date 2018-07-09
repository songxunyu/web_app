from flask_restful import Api
from .cls import TodoList,Todo
from . import api_learn
api = Api(api_learn)

#接口路由
api.add_resource(TodoList, '/items')
api.add_resource(Todo, '/items/<item_id>')

