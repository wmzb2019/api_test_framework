from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "test001" and password == "123456":

        return jsonify({
            "code": 0,
            "msg": "success",
            "token": "abc123456"
        })

    return jsonify({
        "code": 1001,
        "msg": "username or password error"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)