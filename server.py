from flask import Flask, request, jsonify

app = Flask(__name__)

storage = {}

@app.route('/post-endpoint', methods=['POST'])
def post_endpoint():
    data = request.json
    if data['action'] == "addHouse":
        if data['address'] == "":
            return "Address cannot be empty"
        if data['address'] == "No addresses in storage":
            return "Address cannot be 'No addresses in storage'"
        if data['address'] in storage:
            return "Address already exists"
        storage[data['address']] = []
        return "House successfully added"
    
    elif data['action'] == "removeHouse":
        if data['address'] not in storage:
            return "Address does not exist"
        del storage[data['address']]
        return "House successfully removed"
  
    elif data['action'] == "addPerson":
        if data['address'] not in storage:
            return "Address does not exist"
        if data['person'] in storage[data['address']]:
            return "Person already exists"
        storage[data['address']].append(data['person'])
        return "Person successfully added"
    
    elif data['action'] == "removePerson":
        if data['address'] not in storage:
            return "Address does not exist"
        if data['person'] not in storage[data['address']]:
            return "Person does not exist"
        storage[data['address']].remove(data['person'])
        return "Person successfully removed"

@app.route('/get-endpoint', methods=['GET'])
def get_endpoint():
    lst = request.args.get('list')
    address = request.args.get('address')
    if lst == "True":
        if len(storage) == 0:
            return "No addresses in storage"
        return jsonify(list(storage.keys()))
    elif address not in storage:
        return "Address does not exist"
    if not storage[address]:
        return "No people in this address"
    return jsonify(storage[address])

if __name__ == '__main__':
    app.run(debug=True)
