"""Import flask objects."""
from flask import Flask, jsonify, request


# define the app using Flask
app = Flask(__name__)

animals = [{'name': 'Dogs'}, {'name': 'Cats'}, {'name': 'Birds'}]

@app.route('/', methods=['GET'])
def homePage():
    """Let's test."""
    return jsonify({'message': 'Welcome to the animal API!'})

@app.route('/animals', methods=['GET'])
def returnAll():
    """Fetch all."""
    return jsonify({'animals': animals}), 200

@app.route('/animals/<string:name>', methods=['GET'])
def returnOne(name):
    """Get one."""
    animal = [animal for animal in animals if animal['name'] == name]
    return jsonify({'animal': animal[0]}), 200

@app.route('/animals', methods=['POST'])
def addOne():
    """Add one animal."""
    an = {'name': request.json['name']}
    animals.append(an)
    return jsonify({'animals': animals}), 201

@app.route('/animals/<string:name>', methods=['PUT'])
def editOne(name):
    """Update one animal."""
    animal = [animal for animal in animals if animal['name'] == name]
    animal[0]['name'] = request.json['name']
    return jsonify({'animal': animal[0]}), 201

@app.route('/animals/<string:name>', methods=['DELETE'])
def deleteOne(name):
    """Delete one animal."""
    animal = [animal for animal in animals if animal['name'] == name]
    animals.remove(animal[0])
    return jsonify({'animals': animals}), 200

if __name__ == '__main__':
    app.run(debug=True)
