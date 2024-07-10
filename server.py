from flask import Flask, request, jsonify

app = Flask(__name__)

storage = []

@app.route('/post-endpoint', methods=['POST'])
def post_endpoint():
    data = request.form.to_dict()
    storage.append(data)

@app.route('/get-endpoint', methods=['GET'])
def get_endpoint():
    return jsonify(storage)

if __name__ == '__main__':
    app.run(debug=True)
