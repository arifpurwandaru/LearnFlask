from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Walang pacul',
        'item': {
            'itemName': 'Soft drink',
            'price': 1.2
        }
    }
]

@app.route('/')
def kenyas():
    return "Hello W"

@app.route('/store')
def sontor():
    return jsonify({'store':stores})

@app.route('/store', methods=['POST'])
def simpanStore():
    request_data =request.get_json()
    print(request_data['store'][0]['item']['itemName'])

    new_entry={
        'name': request_data['store'][0]['name'],
        'item': request_data['store'][0]['item']
    }
    stores.append(new_entry)
    return jsonify({'store':stores})

app.run(port=4000, host='192.168.1.9', debug=True)