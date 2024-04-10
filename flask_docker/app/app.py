from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
CONNECTION_STRING = "mongodb://localhost:27017"
client = MongoClient(CONNECTION_STRING)
db = client['my_db']
db = db['db']
posts = db.posts


@app.route('/create', methods=['POST'])
def create():
    data = request.json
    key = data.get('key')
    value = data.get('value')
    if key and value:
        posts.insert_one({'key': key, 'value': value})
        return jsonify({'message': 'Key created successfully'}), 201

    return jsonify({'error': 'Invalid request data'}), 400


@app.route('/update/<key>', methods=['PUT'])
def update(key):
    data = request.json
    db.posts.update_one({"key": key}, {"$set": data})
    return jsonify({"message": "Value updated successfully"}), 200


@app.route('/read/<key>', methods=['GET'])
def read(key):
    value = db.posts.find_one({"key": key})
    if value:
        value['_id'] = str(value['_id'])
        return jsonify(value), 200
    else:
        return jsonify({"message": "Value not found"}), 404


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
