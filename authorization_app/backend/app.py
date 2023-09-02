from flask import Flask, request, jsonify
import os

app = Flask(__name__)

users = {
    "foo": "saikyounoP@ssw0rd"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
        return jsonify(authorized=True, message="Logged in successfully!")
    else:
        return jsonify(authorized=False, message="Login failed!"), 401

if __name__ == "__main__":
    debug_mode = os.environ.get('FLASK_DEBUG') == '1'
    app.run(host="0.0.0.0", port=5000, debug=True)
