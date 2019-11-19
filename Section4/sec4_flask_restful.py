from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'Walang_Pacul2019' # or app.secret_key= 'Walang_Pacul2019'
jwt = JWT(app, authenticate, identity)  # /auth

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        data = request.get_json()
        if next(filter(lambda x: x['name'] == data['name'], items), None):
            return {'message': "An Item with name '{}' already exist.".format(name)}, 400
        item = {'name': data['name'], 'price': data['price']}
        items.append(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(host='172.19.16.66', port=4000)
