from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student-details', methods=['GET'])
def get_details():
    return jsonify({
        "name": "Shalini",
        "roll": "2023bcs00229",
        "register": "bcs229"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)