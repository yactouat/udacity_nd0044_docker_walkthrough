from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api')
def base_route():
    return jsonify({
        "msg": "API is up",
        "data": None
    })


if __name__ == '__main__':
    app.run()
