from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.get('/')
def home():
    return {'message': 'Welcome to the Store API!'}

@app.get('/store')
def get_stores():
    return {'stores': stores}

@app.post('/store')
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return stores, 201
@app.post('/store/<string:name>/item')
def enter_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return store, 201
    return {'message': 'Store not found'}, 404

@app.get('/store/<string:name>')
def get_particular_store(name):
    for store in stores:
        if store['name'] == name:
            return store
    return {'message': 'Store not found'}, 404