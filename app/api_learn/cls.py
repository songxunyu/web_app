'''
接口操作脚本
'''

from flask_restful import reqparse,Resource
#引入数据
from ..db_cls import ITEMS


#设置创建数据的格式
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='need name data')
parser.add_argument('age', type=int, required=True, help='need age data')

# 操作（put / get / delete）单一资源
class Todo(Resource):
    def put(self, item_id):
            args = parser.parse_args()
            item = {'name': args['name'], 'age': args['age']}
            ITEMS[item_id] = item
            return item, 201

    def get(self, item_id):
        return ITEMS[item_id], 200

    def delete(self, item_id):
        del ITEMS[item_id]
        return '', 204

# 操作（post / get）资源列表
class TodoList(Resource):
    def get(self):
        return ITEMS, 200

    def post(self):
        args = parser.parse_args()
        item_id = 5
        ITEMS[item_id] = {'name': args['name'], 'age': args['age']}
        return ITEMS[item_id], 201
